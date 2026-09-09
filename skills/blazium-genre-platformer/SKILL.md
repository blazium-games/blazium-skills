---
name: blazium-genre-platformer
description: >
  Composes a 2D platformer from pinned Blazium skills (movement, tilemap,
  physics, input, pixel-perfect, Autowork). Use for side-scroll jump games.
---

# Blazium genre: platformer

Thin adapter — not a platformer framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when building or tuning a side-scrolling / single-screen jump game.

**When not to use:** top-down no gravity → `blazium-2d-movement` only. 3D FPS
→ `blazium-genre-fps-shooter`. Idle numbers → `blazium-clicker`.

## Workflow

1. **Inspect.** `project.blazium` / `config_version`. Existing controller.
2. **Choose.** Pins below — no custom framework.
3. **Implement.** This adapter + **one** pin at a time (router + two max).
4. **Verify.** Autowork jump/land — not screenshots.
5. **Handoff.** Pins used. Streamer overlay → `blazium-streaming`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-2d-movement` | CharacterBody2D run/jump |
| `blazium-tilemap` | levels / Tiled |
| `blazium-physics` | colliders / one-way |
| `blazium-input` | InputMap / rebind |
| `blazium-pixel-perfect` | camera snap |
| `blazium-autowork` | tests |

Coyote/feel stays in `blazium-2d-movement`. Floor under the body; then:

```gdscript
extends AutoworkTest
func test_jump_then_lands() -> void:
	var p: CharacterBody2D = player.instantiate()
	add_child_autofree(p)
	var s := AutoworkInputSender.new()
	s.action_down("jump")
	simulate(p, 8, 1.0 / 60.0, false, SIMULATE_PHYSICS)
	assert_false(p.is_on_floor())
	s.reset_inputs()
	simulate(p, 90, 1.0 / 60.0, false, SIMULATE_PHYSICS)
	assert_true(p.is_on_floor(), "landed")
```

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used Godot 4.7-only APIs** → stay on 4.3.2.
- **Skipped Autowork** → add a jump/land test.

## Related skills

- `blazium-2d-movement`, `blazium-tilemap`, `blazium-physics`, `blazium-input`,
  `blazium-pixel-perfect`, `blazium-autowork`
