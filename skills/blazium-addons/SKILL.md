---
name: blazium-addons
description: >
  Installs and authors Blazium/Godot project addons (addons/, plugin.cfg,
  EditorPlugin). Use for AssetLib plugins or writing an editor plugin. Not
  Hub editor installs and not SCons engine modules.
---

# Blazium addons

Project packages — not Unity UPM `manifest.json`. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

- **Install:** AssetLib / copy into `res://addons/<name>/`.
- **Author:** `plugin.cfg` + `@tool` script extending `EditorPlugin`.
- **Editors/templates:** `blazium-cli`, not this skill.
- **Engine C++ modules:** only if the user is in the engine repo (SCons).
  Do not teach module authoring for a game project.

Enable via Project Settings → Plugins (writes `project.godot` /
`project.blazium` plugin list). Autoloads from addons →
`blazium-project-config` / `blazium-nodes-scenes`.

## When to use

- Use when installing an AssetLib addon or writing `addons/*/plugin.cfg`.

**When not to use:** install Blazium editor / export templates →
`blazium-cli`. Official script templates → `blazium-gdscript-templates`.
New C++ module in `blazium/modules/` → stop unless they asked for engine work.

## Workflow

1. **Inspect.** Existing `addons/`. Is the need a plugin, an autoload, or
   an engine module?
2. **Choose.** Install vs author. Prefer AssetLib over vendoring random zips.
3. **Implement.** `plugin.cfg` + `@tool` `EditorPlugin` (`_enter_tree` /
   `_exit_tree`). Enable the plugin in project settings.
4. **Verify.** Plugin appears enabled; `_enter_tree` ran (editor restart if
   needed). Autowork does not load `@tool` the same way — check the editor.
5. **Handoff.** Addon path + whether it adds an autoload.

## Patterns

### plugin.cfg

```ini
[plugin]
name="MyPlugin"
description="Short what it does"
author="studio"
version="1.0.0"
script="plugin.gd"
```

Place at `res://addons/my_plugin/plugin.cfg`. Script is the official
`EditorPlugin` template (`@tool`, `_enter_tree` / `_exit_tree`).

### Install vs author vs module

| Need | Where |
|------|--------|
| Community editor plugin | AssetLib → `addons/` |
| Your editor UI / import hook | author `plugin.cfg` |
| Engine singleton / C++ | engine module — out of scope here |

## Pitfalls

- **Wrote a Unity `Packages/manifest.json`** → wrong ecosystem.
- **Dropped an addon outside `addons/`** → Project Settings will not list it.
- **Forgot `@tool`** → plugin script does not run in the editor.
- **Started a SCons module for a HUD widget** → GDScript addon instead.

## Resources

- Template: `script_templates/EditorPlugin/plugin.gd`
- Asset: `assets/plugin.cfg`

## Related skills

- `blazium-cli` — editors / export templates
- `blazium-project-config` — enable plugins / autoloads
- `blazium-gdscript-templates` — EditorPlugin starter
- `blazium-gdscript` — script language
