---
name: blazium-genre-roguelike
description: >
  Composes a run-based roguelike or proc-gen grid game from pinned Blazium
  0.6.x skills (resources, CSV, SQLite, Autowork). Use when the request is
  roguelike, permadeath, run seed, dungeon crawl, or loot tables. Not a
  roguelike framework and not a real-time platformer.
when-to-use: >
  roguelike, permadeath, run seed, dungeon crawl, proc-gen grid, loot table
metadata:
  author: blazium-games
  short-description: Compose a roguelike from resources, CSV, SQLite pins
---

# Blazium genre: roguelike

Thin adapter — not a roguelike framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Proc-gen lives in the game; this
skill pins data APIs.

## When to use

- Use when building a run-based, grid, or permadeath dungeon game.
- Use when loot, seeds, or meta-progress need tables plus a `user://` save.

**When not to use:** real-time platformer → `blazium-genre-platformer`.
Relational saves without genre → `blazium-sqlite` only. Card combat only →
`blazium-genre-card-game`.

## Grok host

Read this adapter, then one pin. Spawn `systems-designer` for tables and
`gameplay-programmer` for the walker. Child prompt must include seed column,
CSV/SQLite paths, and whether meta-progress survives death.

## Workflow

1. **Inspect.** Existing tables / seed / save path.
2. **Choose.** Pins below for data. Order: resources defs → CSV tables →
   SQLite run/meta → Autowork seed replay.
3. **Implement.** Router + this adapter + one pin at a time.
4. **Verify.** Autowork on seed replay / loot query — not screenshots.
5. **Handoff.** CSV/SQLite paths and seed field. Idle currency →
   `blazium-clicker`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-resources` | typed `.tres` defs |
| `blazium-csv` | tables / DSV |
| `blazium-sqlite` | run / meta save (`user://`) |
| `blazium-autowork` | seed / table tests |

Replay a run from a CSV seed column:

```gdscript
var table: CSVTable = CSVTable.from_file("res://data/loot.csv")
var rows: Array = table.where_equals("seed", str(run_seed))
assert_eq(rows.size(), 1, "one loot row per seed")
```

Persist the same seed in `user://` via `blazium-sqlite` (`SQLite.load_from`).
Do not parse CSV with `FileAccess` + `split(",")`.

## Output contract

- Table paths (`res://data/*.csv` / `.tres`)
- Save path (`user://…`)
- Seed field name
- Autowork assertion that replayed the seed

## Pitfalls

- **Invented FileAccess CSV** → `blazium-csv`.
- **Rewrote a studio roguelike pack** → compose pins.
- **Saved runs in `res://`** → `user://` via sqlite.
- **Seed not stored** → replay and daily runs become impossible.

## Related skills

- `blazium-resources`, `blazium-csv`, `blazium-sqlite`, `blazium-autowork`
