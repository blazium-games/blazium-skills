---
name: blazium-gdscript-templates
description: >
  Lists and applies official Blazium GDScript script templates (LoginClient,
  LobbyClient, Discord embed, YouTube Playables, SQLite, EditorPlugin). Use
  when starting from an engine template. Hand off domain APIs to other skills.
---

# Blazium GDScript templates

Start from the official template — do not invent the first 20 lines. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Path: `blazium/modules/gdscript/editor/script_templates/`.

**Nightly caveat:** `LoginClient` / `LobbyClient` / `MasterServerClient` are
templates and https://docs.blazium.app — not C++/xml class docs in the installed editor. Do not invent
methods. Verify against the installed nightly.

Do **not** re-teach JWT, lobby rooms, Discord SDK, Playables, or SQL here —
hand off after the file exists.

## When to use

- Use when the user needs a Login/Lobby/Discord/Playables/SQLite/plugin
  starter and the official template exists.

**When not to use:** general `.gd` language work → `blazium-gdscript`.
Luau → `blazium-luau`. Already past the template → the domain skill.

## Workflow

1. **Inspect.** Which template matches? Editor “New Script” inherit list.
2. **Choose.** Smallest official file. Do not merge two templates.
3. **Implement.** Copy/apply the template via editor or JustAMCP
   `script_tools` (`create_script`). Keep `_BASE_` inheritance as the editor
   would.
4. **Verify.** Script parses (`validate_script`). Then open the domain skill.
5. **Handoff.** Name the domain skill in Related below.

## Patterns

### Inventory → handoff

| Template dir | Then load |
|--------------|-----------|
| `LoginClient` | `blazium-services` |
| `LobbyClient` / `ScriptedLobbyClient` | `blazium-lobby` |
| `DiscordEmbeddedAppClient` | `blazium-discord` + `blazium-export-web` |
| `YoutubePlayablesClient` | `blazium-export-web` |
| `SQLite` | `blazium-sqlite` (move DB to `user://` for runtime) |
| `EditorPlugin` | `blazium-addons` |
| `CharacterBody2D` / `CharacterBody3D` | `blazium-2d-movement` / `blazium-3d` |
| `Node` / `Object` / `EditorScript` / `EditorScenePostImport` / `RichTextEffect` / `VisualShaderNodeCustom` | `blazium-gdscript` |

### Apply

Prefer the editor inherit-and-template flow or JustAMCP `create_script`.
Do not rewrite Login/Lobby APIs from memory.

## Pitfalls

- **Invented LoginClient methods** → template + nightly only.
- **Stayed in this skill for lobby reconnect** → `blazium-lobby`.
- **Shipped `res://test.sqlite` from the SQLite template** → `user://`.
- **Used a Godot 4.7 template pack** → these engine files only.

## Resources

- `blazium/modules/gdscript/editor/script_templates/`
- JustAMCP: `script_tools`

## Related skills

- `blazium-gdscript` — language
- `blazium-services` — LoginClient
- `blazium-lobby` — LobbyClient
- `blazium-discord` — embedded
- `blazium-sqlite` — SQLite
- `blazium-addons` — EditorPlugin
- `blazium-export-web` — Playables / embed host
