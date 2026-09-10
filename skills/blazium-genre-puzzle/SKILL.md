---
name: blazium-genre-puzzle
description: >
  Composes a grid, match, or logic puzzle from pinned Blazium 0.6.x skills
  (UI, input, tilemap, Autowork). Use when the request is slide puzzle,
  match-3, sokoban, legal move, undo, or win-condition grid. Not a platformer
  and not a card-combat kit.
when-to-use: >
  puzzle, grid puzzle, match-3, sokoban, legal move, undo, win condition,
  TileMapLayer puzzle
metadata:
  author: blazium-games
  short-description: Compose a puzzle from UI, input, tilemap, Autowork pins
---

# Blazium genre: puzzle

Thin adapter — not a puzzle framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Puzzles are deterministic — tests
come before juice.

## When to use

- Use when the core verb is solve a grid, match, or logic level.
- Use when a legal-move function and a win check are the next change.

**When not to use:** action platforming → `blazium-genre-platformer`.
Card rules → `blazium-genre-card-game`. Level tables only → `blazium-csv`.

## Grok host

Read this adapter, then **one** pin. Spawn `gameplay-programmer` for the
board walker and `qa-tester` for Autowork legal-move/win. Child prompts
must include the board scene path, the move action names, and how a win is
asserted. Do not dump the catalog.

Evidence is Autowork on legal move + win — not a screenshot of the board.

## Workflow

1. **Inspect.** Board representation / InputMap / level format.
2. **Choose.** Pins below. Order: input verbs → tilemap/UI board → Autowork
   legal-move/win → CSV levels / locales last.
3. **Implement.** Router + this adapter + **one** pin at a time.
4. **Verify.** Autowork on legal move + win — not screenshots.
5. **Handoff.** Level tables → `blazium-csv`. Locales → `blazium-localization`.
   Feel → `blazium-game-feel` after the rule test passes.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-ui` | board Controls / HUD |
| `blazium-input` | click / drag / undo |
| `blazium-tilemap` | grid levels |
| `blazium-autowork` | rule tests |

Puzzles are deterministic — press a grid action and assert the board:

```gdscript
extends AutoworkTest
func test_slide_is_legal() -> void:
	var board := grid_scene.instantiate()
	add_child_autofree(board)
	var s := AutoworkInputSender.new()
	s.action_down("move_right")
	simulate(board, 1, 1.0 / 60.0, false, SIMULATE_PHYSICS)
	s.reset_inputs()
	assert_true(board.last_move_legal)
```

Keep win checks in the board script so Autowork can `assert_true` without a
dock screenshot.

## Output contract

- Board scene path
- InputMap / click actions
- Win / legal-move assertion names
- Autowork test name and pass/fail

## Pitfalls

- **Skipped tests on rules** → Autowork first; puzzles are deterministic.
- **Invented a Godot 4.7 TileMap API** → 4.3.2 `TileMapLayer` / Tiled pins.
- **Rewrote a studio puzzle kit** → compose pins.
- **Tuned match juice before legal-move passes** → `blazium-game-feel` second.

## Related skills

- `blazium-ui`, `blazium-input`, `blazium-tilemap`, `blazium-autowork`,
  `blazium-csv`, `blazium-localization`
