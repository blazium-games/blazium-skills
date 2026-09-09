"""Generate Cursor/Codex plugin folders from .claude-plugin/marketplace.json."""

from __future__ import annotations

import json
import os
import shutil
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAUDE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGINS = ROOT / "plugins"
VERSION = "0.6.0"
HOMEPAGE = "https://docs.blazium.app"


PACK_DISPLAY = {
    "blazium": "Blazium",
    "blazium-infra": "Blazium Infra",
    "blazium-engine": "Blazium Engine",
    "blazium-live-ops": "Blazium Live Ops",
    "blazium-ship": "Blazium Ship",
    "blazium-content": "Blazium Content",
    "blazium-modules": "Blazium Modules",
    "blazium-growth": "Blazium Growth",
}

PACK_KEYWORD = {
    "blazium": "bundle",
    "blazium-infra": "infra",
    "blazium-engine": "engine",
    "blazium-live-ops": "live-ops",
    "blazium-ship": "ship",
    "blazium-content": "content",
    "blazium-modules": "modules",
    "blazium-growth": "growth",
}


def display_name(plugin_name: str) -> str:
    if plugin_name in PACK_DISPLAY:
        return PACK_DISPLAY[plugin_name]
    return plugin_name.replace("-", " ").title()


def pack_keyword(plugin_name: str) -> str:
    if plugin_name in PACK_KEYWORD:
        return PACK_KEYWORD[plugin_name]
    return plugin_name.removeprefix("blazium-")


def keywords_for(plugin_name: str) -> list[str]:
    return ["blazium", "godot", "gamedev", pack_keyword(plugin_name)]


def default_prompts(plugin_name: str, desc: str) -> list[str]:
    label = display_name(plugin_name)
    return [
        f"Use {label} to work on a Blazium 0.6.x (Godot 4.3.2 fork) project.",
        desc,
    ]


def openai_interface(plugin_name: str, desc: str) -> dict:
    return {
        "displayName": display_name(plugin_name),
        "shortDescription": desc,
        "longDescription": desc,
        "developerName": "blazium",
        "category": "Developer Tools",
        "capabilities": ["Read", "Write"],
        "websiteURL": HOMEPAGE,
        "defaultPrompt": default_prompts(plugin_name, desc),
    }


def skill_dirname(skill_path: str) -> str:
    return Path(skill_path).name


def _is_reparse_point(path: Path) -> bool:
    if path.is_symlink():
        return True
    if os.name != "nt" or not path.exists():
        return False
    try:
        attrs = os.lstat(path).st_file_attributes
    except AttributeError:
        return False
    return bool(attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def link_skill(src: Path, dest: Path) -> None:
    if dest.exists() or dest.is_symlink():
        if _is_reparse_point(dest):
            dest.unlink()
        elif dest.is_dir():
            shutil.rmtree(dest)
        else:
            dest.unlink()
    dest.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        os.system(f'cmd /c mklink /J "{dest}" "{src}" >nul')
        if dest.exists():
            return
    dest.symlink_to(src, target_is_directory=True)


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    catalog = json.loads(CLAUDE.read_text(encoding="utf-8"))
    owner = catalog.get("owner", {"name": "blazium"})
    cursor_plugins = []
    agents_plugins = []

    for plugin in catalog["plugins"]:
        name = plugin["name"]
        desc = plugin.get("description", "")
        skills = plugin.get("skills") or []
        pack = PLUGINS / name
        skills_root = pack / "skills"
        skills_root.mkdir(parents=True, exist_ok=True)
        interface = openai_interface(name, desc)
        tags = keywords_for(name)

        write_json(
            pack / "plugin.json",
            {
                "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                "name": name,
                "version": VERSION,
                "description": desc,
                "author": {"name": owner.get("name", "blazium")},
                "homepage": HOMEPAGE,
                "keywords": tags,
                "extensions": {"com.openai": {"interface": interface}},
            },
        )
        write_json(
            pack / ".codex-plugin" / "plugin.json",
            {"interface": interface},
        )
        write_json(
            pack / ".cursor-plugin" / "plugin.json",
            {
                "name": name,
                "displayName": display_name(name),
                "version": VERSION,
                "description": desc,
                "author": {"name": owner.get("name", "blazium")},
                "homepage": HOMEPAGE,
                "keywords": tags,
                "skills": "./skills/",
            },
        )

        wanted = set()
        for rel in skills:
            dirname = skill_dirname(rel)
            wanted.add(dirname)
            src = ROOT / "skills" / dirname
            if not src.is_dir():
                print(f"skip missing skill {src}", file=sys.stderr)
                continue
            link_skill(src, skills_root / dirname)

        for child in skills_root.iterdir():
            if child.name not in wanted:
                if child.is_dir() and not child.is_symlink():
                    shutil.rmtree(child)
                else:
                    child.unlink()

        cursor_plugins.append(
            {
                "name": name,
                "source": f"./plugins/{name}",
                "description": desc,
            }
        )
        agents_plugins.append(
            {
                "name": name,
                "source": {"source": "local", "path": f"./plugins/{name}"},
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Developer Tools",
            }
        )

    write_json(
        ROOT / ".cursor-plugin" / "marketplace.json",
        {
            "name": catalog["name"],
            "owner": owner,
            "metadata": {
                "description": catalog.get("metadata", {}).get("description", ""),
                "version": catalog.get("version", VERSION),
            },
            "plugins": cursor_plugins,
        },
    )
    write_json(
        ROOT / ".agents" / "plugins" / "marketplace.json",
        {
            "name": catalog["name"],
            "interface": {"displayName": "Blazium Skills"},
            "plugins": agents_plugins,
        },
    )
    print(f"synced {len(cursor_plugins)} plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
