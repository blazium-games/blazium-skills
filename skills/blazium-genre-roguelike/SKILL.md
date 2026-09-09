---
name: blazium-genre-roguelike
description: >
  Composes a roguelike from pinned Blazium skills (resources, CSV, SQLite,
  Autowork). Use for run-based / proc-gen grid games
---

# Blazium genre: roguelike

Thin adapter — not a roguelike framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when building a run-based, grid, or permadeath dungeon game.

**When not to use:** real-time platformer → `blazium-genre-platformer`.
Relational saves without genre → `blazium-sqlite` only.

## Workflow

1. **Inspect.** Existing tables / seed / save path.
2. **Choose.** Pins below for data.
3. **Implement.** Router + this adapter + one pin at a time.
4. **Verify.** Autowork on seed replay / loot query — not screenshots.
5. **Handoff.** CSV/SQLite paths. Idle currency → `blazium-clicker`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-resources` | typed `.tres` defs |
| `blazium-csv` | tables / DSV |
| `blazium-sqlite` | run / meta save (`user://`) |
| `blazium-autowork` | seed / table tests |

Proc-gen lives in the game; pin data APIs only.
Replay a run from a CSV seed column:

```gdscript
var table: CSVTable = CSVTable.from_file("res://data/loot.csv")
var rows: Array = table.where_equals("seed", str(run_seed))
assert_eq(rows.size(), 1, "one loot row per seed")
```

Persist the same seed in `user://` via `blazium-sqlite` (`SQLite.load_from`).
Do not parse CSV with `FileAccess` + `split(",")`.

## Pitfalls

- **Invented FileAccess CSV** → `blazium-csv`.
- **Rewrote a studio roguelike pack** → compose pins.
- **Saved runs in `res://`** → `user://` via sqlite.

## Related skills

- `blazium-resources`, `blazium-csv`, `blazium-sqlite`, `blazium-autowork`
