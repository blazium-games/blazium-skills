---
name: blazium-genre-puzzle
description: >
  Composes a puzzle game from pinned Blazium skills (UI, input, tilemap,
  Autowork). Use for grid/logic/match puzzles
---

# Blazium genre: puzzle

Thin adapter — not a puzzle framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when the core verb is solve a grid, match, or logic level.

**When not to use:** action platforming → `blazium-genre-platformer`.
Card rules → `blazium-genre-card-game`.

## Workflow

1. **Inspect.** Board representation / InputMap / level format.
2. **Choose.** Pins below.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on legal move + win — not screenshots.
5. **Handoff.** Level tables → `blazium-csv`. Locales → localization.

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

## Pitfalls

- **Skipped tests on rules** → Autowork first; puzzles are deterministic.
- **Invented a Godot 4.7 TileMap API** → 4.3.2 TileMapLayer / Tiled pins.
- **Rewrote a studio puzzle kit** → compose pins.

## Related skills

- `blazium-ui`, `blazium-input`, `blazium-tilemap`, `blazium-autowork`
