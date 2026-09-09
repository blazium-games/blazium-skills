---
name: blazium-csv
description: >
  Parses and queries Blazium CSV/DSV tables (CSVTable, CSVReader/Writer,
  CSVImporter, CSVAsyncTask). Use instead of FileAccess + split(","). Not
  TranslationServer workflows or SQLite.
---

# Blazium CSV

Native tables — not `FileAccess` + `split(",")`. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/dotcsv/` — `CSVTable`, `CSVReader`, `CSVWriter`,
`CSVImporter`, `CSVExporter`, `CSVAsyncTask`, `CSVIndex`, `CSVRowModel`,
`CSVDialect`, `CSVChunkProcessor`, `ResourceImporterCSV`.

DSV (custom delimiter): `DSVReader`, `DSVWriter`, `DSVImporter`,
`DSVExporter` — **no class named `DSV`**.

## When to use

- Use when importing, querying, writing, or async-chunking CSV/DSV files.

**When not to use:** translation CSVs as locale pipelines →
`blazium-localization` (this module is the parser). Small typed data →
`blazium-resources`. Relational saves → `blazium-sqlite`.

## Workflow

1. **Inspect.** Path, delimiter, headers. `ClassDB.class_exists("CSVTable")`.
2. **Choose.** Query (`CSVTable`) vs stream (`CSVReader`) vs import
   (`CSVImporter` / `ResourceImporterCSV`) vs large file (`CSVAsyncTask`).
3. **Implement.** `CSVTable.from_file` + `where_equals` / `filter_rows`.
   Writer: `CSVWriter.open` / `write_row` / `close`. DSV: `DSVReader.open(path, delimiter)`.
4. **Verify.** Row count + a known cell. Autowork on a fixture under
   `res://` or temp `user://`.
5. **Handoff.** Path + dialect. Locales → localization. SQL → sqlite.

## Patterns

### Query vs raw parse

```gdscript
var table: CSVTable = CSVTable.from_file("res://data/items.csv")
var rares: Array = table.where_equals("rarity", "rare")
```

Also: `from_csv(text)`, `get_rows()`, `row_count()`, `filter_rows`,
`where_in`, `sort_by`, `group_by`, `inner_join` / `left_join`,
`select_columns` / `drop_columns`, `build_index`, `apply_model`.

One-shot import: `CSVImporter.import(path)` / `import_with_dialect` /
`import_with_headers`.

Row stream: `CSVReader.open` → `read_row` / `read_rows` → `close`.

Write: `CSVWriter.open(path, append)` → `write_row` / `write_rows` → `close`.

### Async large files

```gdscript
var task: CSVAsyncTask = CSVAsyncTask.load_csv("res://data/big.csv")
task.start()
# later: task.is_done() → task.get_table()
```

Also: `load_dsv`, `save_csv` / `save_dsv`, `cancel`, `wait_to_finish`,
`get_progress`.

### Editor import

`ResourceImporterCSV` turns `res://*.csv` into an imported table resource.
Runtime parse still uses `CSVTable.from_file` / `CSVImporter`.

## Pitfalls

- **Invented FileAccess CSV splitting** → quoted commas break.
- **Called a class `DSV`** → use `DSVReader` / `DSVWriter`.
- **Owned TranslationServer here** → localization skill.
- **Used CSV as a player save** → sqlite.

## Resources

- Tests: https://github.com/blazium-games/dotcsv_module_tests

- `blazium/modules/dotcsv/doc_classes/CSVTable.xml`
- Importer: `ResourceImporterCSV.xml`

## Related skills

- `blazium-localization` — translation CSVs
- `blazium-resources` — small `.tres`
- `blazium-sqlite` — relational
