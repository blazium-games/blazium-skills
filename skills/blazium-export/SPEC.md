---
name: blazium-export
pack: ship
---

# blazium-export

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Shipping players is the Godot export skill plus Blazium presets and headless CI.

## What

Export templates, presets, headless. Win/Mac/Linux/Android. Hand off web/retro/specialty.

**Non-goals:** Do not own Discord/YouTube web (`export-web`), toolchain ISOs, or wallpaper/screensaver.

## How

- JustAMCP export_tools: `export_project`, `export_release`, `deploy_to_android`.
- Godot-style export presets in the project.
- Templates via `blazium-cli templates download`.

## Reasoning

Desktop/mobile core. Web and retro are large enough to split.

## Sources

- JustAMCP export_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-export-web` — web / Playables / Discord embed
- `blazium-toolchain` — retro
- `blazium-specialty-export` — wallpaper/scr/autorun/DVD
- `blazium-ci-export` — GHA
