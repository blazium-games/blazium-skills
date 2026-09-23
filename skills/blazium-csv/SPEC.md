---
name: blazium-csv
pack: modules
---

# blazium-csv

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

16 doc classes — largest data module after JustAMCP/Tiled. Agents will `FileAccess` + `split(",")`.

## What

`CSVTable` queries, `CSVReader`/`CSVWriter`, `CSVImporter`, DSV dialects, `CSVAsyncTask`.

**Non-goals:** Do not own TranslationServer workflows (localization uses CSV as a format).

## How

- Module: `blazium/modules/dotcsv/`.
- Import pipeline vs runtime parse. Async chunking for large files.

## Reasoning

Data layer for content and localization tables.

## Sources

- dotcsv (16 classes)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-localization` — translation CSVs
- `blazium-resources` — small typed data
