---
name: blazium-export
description: >
  Exports Blazium desktop and mobile players (Win/Mac/Linux/Android) via
  presets, JustAMCP export_tools, and blazium-cli templates. Use when shipping
  a normal player or deploying to Android. Not web, retro, or wallpaper.
---

# Blazium export

Ship a normal player. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Prefer JustAMCP `export_tools` when the editor MCP is connected. Templates
come from `blazium-cli install … --templates` or `blazium-cli templates
download` — **not** `blazium-cli hub templates` and **not**
`update apply --product templates`.

Never conflate `blazium://open?path=` (OS/CLI) with JustAMCP `blazium://scene/…`.

## When to use

- Use when adding `export_presets.cfg` entries for Win/Mac/Linux/Android.
- Use when running a headless or JustAMCP export, or `deploy_to_android`.

**When not to use:** HTML5 / Playables / Discord embed → `blazium-export-web`.
PS1/PS2/N64 compilers → `blazium-toolchain`. Wallpaper / screensaver / USB /
InterDVD → `blazium-specialty-export`. GitHub Actions matrix →
`blazium-ci-export`. Missing editor → `blazium-cli` first.

## Workflow

1. **Inspect.** `export_presets.cfg`, `get_export_info`, installed templates
   (`blazium-cli templates path`). Confirm editor version matches templates.
2. **Choose.** Smallest preset set. Android needs keystore + adb device.
3. **Implement.** Prefer `list_export_presets` then `export_release` /
   `export_debug` / `export_project`. Android: `list_android_devices` →
   `deploy_to_android`.
4. **Verify.** Artifact exists and launches (or adb install succeeds). Not a
   screenshot alone.
5. **Handoff.** Paths + preset names. Bake `app_id`/`build_id` notes →
   `blazium-crash-analytics` (do not re-teach consent).

## Patterns

### Handoff table

| Target | Skill |
|--------|--------|
| Win / Mac / Linux / Android player | this skill |
| Web / COOP/COEP / Playables / Discord iframe | `blazium-export-web` |
| PS1 / PS2 / N64 / toolchain ISO | `blazium-toolchain` |
| Live wallpaper / .scr / autorun / InterDVD | `blazium-specialty-export` |
| GHA install + export + deploy | `blazium-ci-export` |

### JustAMCP export_tools

`list_export_presets`, `export_project` (`preset_index` / `preset_name`,
`debug`), `export_release`, `export_debug`, `export_custom`, `get_export_info`,
`list_android_devices`, `get_android_preset_info`, `deploy_to_android`
(`device_serial`, `skip_export`, `launch`).

### Templates (real CLI)

```text
blazium-cli install 0.6.714 --templates
blazium-cli templates list nightly
blazium-cli templates download nightly --tpz
blazium-cli templates path
```

Headless (editor binary, after templates exist): use the project's export
preset via JustAMCP or the editor `--export-release` / `--export-debug`
flags matching 4.3.2. Do not invent a `blazium export` subcommand.

## Pitfalls

- **Invented `blazium-cli hub templates`** → top-level `templates` /
  `install --templates`.
- **`update apply --product templates`** → not supported; use
  `templates download`.
- **Mismatched editor vs .tpz** → same version/channel.
- **Web or InterDVD preset here** → wrong skill.

## Resources

- JustAMCP: `export_tools`
- CLI: `blazium-cli templates --help`
- Asset: `assets/install_templates.txt`

## Related skills

- `blazium-export-web` — web / Playables / Discord embed
- `blazium-toolchain` — retro compilers
- `blazium-specialty-export` — novelty + DVD
- `blazium-ci-export` — GHA
- `blazium-cli` — install editor
- `blazium-crash-analytics` — bake ids
