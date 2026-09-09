---
name: blazium-sqlite
description: >
  Uses Blazium’s native SQLite module (SQLite node, SQLiteDatabase,
  SQLiteQuery, backup). Use for relational saves and queries. Runtime DBs
  belong in user://. Not .tres catalogs or CSV import.
---

# Blazium SQLite

Native SQLite — not a JSON save file. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/sqlite3/` (`SQLite`, `SQLiteDatabase`, `SQLiteQuery`,
`SQLiteQueryResult`, `SQLiteBackup`, `SQLiteColumnSchema`, `SQLiteAccess`,
`SQLiteBlob`). Template:
`script_templates/SQLite/default.gd`.

**Runtime DBs live in `user://`.** The official template saves
`res://test.sqlite` — editor/demo only.

## When to use

- Use when opening, querying, migrating, or backing up a relational DB.

**When not to use:** small designer data → `blazium-resources`. Tabular
import → `blazium-csv`. Starting from the official node
template only → `blazium-gdscript-templates` then return here.

## Workflow

1. **Inspect.** Existing `.sqlite` path. `ClassDB.class_exists("SQLite")`.
2. **Choose.** In-memory (`SQLiteDatabase.new()`) vs `user://game.sqlite`.
3. **Implement.** `load_from(path)` / schema via `create_table` +
   `SQLiteColumnSchema`. Queries: `create_query` / `execute_query` /
   `insert_row(s)` / `select_rows`. Backup: `backup_to` / `backup_async`.
4. **Verify.** Query result + `get_last_error_message` if failed. Autowork
   on a temp `user://` file.
5. **Handoff.** Path + schema. Template authoring → gdscript-templates.

## Patterns

### Open / query / backup

```gdscript
var db := SQLite.new()
if not db.load_from("user://game.sqlite"):
	push_error(db.get_last_error_message())
	return
var q: SQLiteQuery = db.create_query("SELECT name FROM test WHERE id = ?")
var result := q.execute([1])
db.backup_to("user://game.bak.sqlite")
db.close()
```

Template helpers: `SQLiteColumnSchema.create`, `database.create_table`,
`insert_rows`. `ResourceSaver.save(database, path)` is for the
`SQLiteDatabase` resource — still prefer `user://` at runtime.

### WAL, attach, custom functions

Proven in `sqlite3_module_tests` (close the DB in teardown):

```gdscript
db.create_query("PRAGMA journal_mode;").execute([])
db.connect("wal_updated", _on_wal)
db.wal_checkpoint()           # optional db name, e.g. "main"
db.attach_database("user://other.db", "secondary")
db.create_function("calc_complex", 3, Callable(self, "complex_godot_math"))
var bak = db.backup_async("user://game.bak.sqlite")
# bak.step(pages); bak.finish()
db.restore_async("user://game.bak.sqlite")
```

Also tested: savepoints, BLOB, JSON, aggregates, collations, sandbox
authorization, `SQLite` node forwarding. Always `close()` when done.

### Path rules

| Location | Use |
|----------|-----|
| `user://` | player saves, runtime |
| `res://` | shipped read-only / editor demo only |
| memory | tests / scratch |

## Pitfalls

- **Wrote the player DB into `res://`** → not writable on export.
- **Invented FileAccess CSV parsing for tables** → `blazium-csv`.
- **Used ConfigFile for relational data** → this module.
- **Copied Roblox DataStore APIs** → wrong stack.

## Resources

- Tests: https://github.com/blazium-games/sqlite3_module_tests

- `blazium/modules/sqlite3/doc_classes/SQLite.xml`
- Template: `script_templates/SQLite/default.gd`
- Tests: github.com/blazium-games/sqlite3_module_tests

## Related skills

- `blazium-resources` — small `.tres` data
- `blazium-gdscript-templates` — official SQLite starter
- `blazium-csv` — tabular import
