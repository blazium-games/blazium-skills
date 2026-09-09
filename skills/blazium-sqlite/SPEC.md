---
name: blazium-sqlite
pack: content
---

# blazium-sqlite

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-resources` — small data
- `blazium-csv` — tabular import
- `blazium-gdscript-templates` — SQLite template
