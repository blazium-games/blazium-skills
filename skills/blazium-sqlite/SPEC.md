---
name: blazium-sqlite
pack: content
---

# blazium-sqlite

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Native SQLite beats inventing JSON save files for anything relational.

## What

`SQLite`, `SQLiteDatabase`, `SQLiteQuery`, backup. GDScript SQLite script template.

**Non-goals:** Do not own Resource `.tres` catalogs or CSV import.

## How

- Module: `blazium/modules/sqlite3/` (8 classes).
- Template: SQLite under gdscript script_templates.

## Reasoning

Persistence skill. Complements resources and CSV.

## Sources

- roblox-datastores (conceptual)
- sqlite3

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-resources` — small data
- `blazium-csv` — tabular import
- `blazium-gdscript-templates` — SQLite template
