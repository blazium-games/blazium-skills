"""Validate Claude / Cursor / Codex marketplace catalogs stay in sync."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAUDE = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR = ROOT / ".cursor-plugin" / "marketplace.json"
CODEX = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGINS = ROOT / "plugins"
CONTRACT = ROOT / "scripts" / "backend-contract.json"
WITHDRAWN = frozenset({"blazium-dddbrowser", "blazium-town-sdk"})
RETIRED = frozenset({"blazium-cli-hub", "blazium-justamcp"})
CURSOR_ENTRY_KEYS = frozenset({"name", "source", "description"})
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CLI_VERB = re.compile(r"blazium-cli[ \t]+([a-z][a-z0-9-]*)")
APPLY_PRODUCT = re.compile(r"update apply --product[ \t]+([a-z_]+)")
IGNORE_APPLY = frozenset({"is", "only", "for", "the", "needed"})
IGNORE_VERBS = frozenset({"verbs", "description", "spec", "skill", "and", "or", "the"})
SKILL_LINE_WARN = 500


def skill_dirname(skill_path: str) -> str:
    return Path(skill_path).name


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    claude = load_json(CLAUDE)
    cursor = load_json(CURSOR)
    codex = load_json(CODEX)

    claude_plugins = claude.get("plugins") or []
    cursor_plugins = cursor.get("plugins") or []
    codex_plugins = codex.get("plugins") or []
    claude_names = [p.get("name") for p in claude_plugins]
    cursor_names = [p.get("name") for p in cursor_plugins]
    codex_names = [p.get("name") for p in codex_plugins]

    if cursor_names != claude_names:
        errors.append(
            f"Cursor plugin names drift from Claude: {cursor_names} != {claude_names}"
        )
    if codex_names != claude_names:
        errors.append(
            f"Codex plugin names drift from Claude: {codex_names} != {claude_names}"
        )
    if len(cursor_plugins) != len(claude_plugins):
        errors.append(
            f"Cursor plugin count {len(cursor_plugins)} != Claude {len(claude_plugins)}"
        )
    if len(codex_plugins) != len(claude_plugins):
        errors.append(
            f"Codex plugin count {len(codex_plugins)} != Claude {len(claude_plugins)}"
        )

    for plugin in claude_plugins:
        name = plugin.get("name", "")
        for rel in plugin.get("skills") or []:
            dirname = skill_dirname(rel)
            if dirname in WITHDRAWN:
                errors.append(f"Claude plugin {name} lists withdrawn skill {dirname}")
            skill_md = ROOT / "skills" / dirname / "SKILL.md"
            if not skill_md.is_file():
                errors.append(f"Claude plugin {name} missing {skill_md}")

        pack = PLUGINS / name
        for rel_manifest in (
            "plugin.json",
            ".cursor-plugin/plugin.json",
            ".codex-plugin/plugin.json",
        ):
            manifest = pack / rel_manifest
            if not manifest.is_file():
                errors.append(f"pack {name} missing {rel_manifest}")

        wanted = [skill_dirname(rel) for rel in plugin.get("skills") or []]
        skills_root = pack / "skills"
        if not skills_root.is_dir():
            errors.append(f"pack {name} missing skills/ (run scripts/sync-plugin-packs.py)")
        else:
            present = {child.name for child in skills_root.iterdir()}
            for dirname in wanted:
                if dirname not in present:
                    errors.append(
                        f"pack {name} missing skills/{dirname} (run scripts/sync-plugin-packs.py)"
                    )
                    continue
                if not (skills_root / dirname / "SKILL.md").is_file():
                    errors.append(f"pack {name} skills/{dirname} has no SKILL.md")

    for entry in cursor_plugins:
        extra = set(entry) - CURSOR_ENTRY_KEYS
        if extra:
            errors.append(
                f"Cursor marketplace entry {entry.get('name')} has extra keys {sorted(extra)}"
            )

    for entry in codex_plugins:
        name = entry.get("name", "")
        policy = entry.get("policy") or {}
        if "installation" not in policy:
            errors.append(f"Codex entry {name} missing policy.installation")
        if "authentication" not in policy:
            errors.append(f"Codex entry {name} missing policy.authentication")
        if "category" not in entry:
            errors.append(f"Codex entry {name} missing category")

    wave_re = re.compile(r"Wave\s+[0-9]")
    brand_re = re.compile(r"docs/|gamedev-skills|awesome-gamedev")
    allow_docs = re.compile(r"https://docs\.blazium\.app|https://cdn\.blazium\.app")
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        if wave_re.search(text):
            errors.append(f"{skill_md.relative_to(ROOT)} contains process Wave language")
        for i, line in enumerate(text.splitlines(), 1):
            if allow_docs.search(line):
                continue
            if brand_re.search(line):
                errors.append(
                    f"{skill_md.relative_to(ROOT)}:{i} contains docs/ or gamedev-skills reference"
                )

    for name in RETIRED:
        if (ROOT / "skills" / name / "SKILL.md").is_file():
            errors.append(f"retired skill {name} still has SKILL.md")

    contract = load_json(CONTRACT) if CONTRACT.is_file() else {}
    cli_verbs = set((contract.get("cli") or {}).get("verbs") or [])
    apply_ok = set((contract.get("cli") or {}).get("update_apply_products") or [])
    denylist = list((contract.get("cli") or {}).get("denylist") or [])
    fence_re = re.compile(r"```.*?```", re.DOTALL)

    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        skill_dir = skill_md.parent
        lines = text.splitlines()
        if len(lines) > SKILL_LINE_WARN:
            print(
                f"warning: {skill_md.relative_to(ROOT)} has {len(lines)} lines "
                f"(soft cap {SKILL_LINE_WARN})",
                file=sys.stderr,
            )
        for i, line in enumerate(lines, 1):
            for href in MD_LINK.findall(line):
                target = href.split("#", 1)[0].strip()
                if not target.startswith("references/"):
                    continue
                if not (skill_dir / target).is_file():
                    errors.append(
                        f"{skill_md.relative_to(ROOT)}:{i} broken reference {target}"
                    )
        fences = "\n".join(block.group(0) for block in fence_re.finditer(text))
        for banned in denylist:
            if banned in fences:
                errors.append(
                    f"{skill_md.relative_to(ROOT)} invents denylisted verb {banned!r}"
                )
        skip_spans = []
        for banned in denylist:
            start = 0
            while True:
                idx = text.find(banned, start)
                if idx < 0:
                    break
                skip_spans.append((idx, idx + len(banned)))
                start = idx + 1
        for match in CLI_VERB.finditer(text):
            if any(a <= match.start() and match.end() <= b for a, b in skip_spans):
                continue
            verb = match.group(1)
            if verb in IGNORE_VERBS:
                continue
            if cli_verbs and verb not in cli_verbs:
                errors.append(
                    f"{skill_md.relative_to(ROOT)} invents CLI verb blazium-cli {verb}"
                )
        for match in APPLY_PRODUCT.finditer(text):
            if any(a <= match.start() and match.end() <= b for a, b in skip_spans):
                continue
            product = match.group(1)
            if product in IGNORE_APPLY:
                continue
            if apply_ok and product not in apply_ok:
                line_start = text.rfind("\n", 0, match.start()) + 1
                prev_start = text.rfind("\n", 0, max(line_start - 1, 0)) + 1
                line_end = text.find("\n", match.end())
                line = text[prev_start: line_end if line_end != -1 else None]
                if re.search(r"\bnot\b|invent|→", line, re.I):
                    continue
                errors.append(
                    f"{skill_md.relative_to(ROOT)} invents update apply --product {product}"
                )

    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        print(f"{len(errors)} marketplace validation error(s)", file=sys.stderr)
        return 1
    print(f"validated {len(claude_plugins)} plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
