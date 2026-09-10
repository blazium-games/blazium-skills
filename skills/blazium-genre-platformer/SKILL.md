---
name: blazium-genre-platformer
description: >
  Composes a 2D side-scroll or single-screen jump game from pinned Blazium
  0.6.x skills. Use when the request is platformer, Mario-like, Metroidvania
  start, coyote jump, one-way platforms, or "make a jump game". Load this
  adapter plus one pin at a time. Not a platformer framework and not top-down.
when-to-use: >
  platformer, side-scroll jump, coyote time, one-way platforms, Metroidvania
  start, CharacterBody2D jump game
metadata:
  author: blazium-games
  short-description: Compose a 2D platformer from movement, tilemap, physics pins
---

# Blazium genre: platformer

Thin adapter — not a platformer framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when building or tuning a side-scrolling or single-screen jump game.
- Use when the user says platformer, coyote jump, one-way floors, or
  Metroidvania *start* (movement + rooms), not a full ability-gate engine.

**When not to use:** top-down no gravity → `blazium-2d-movement` only. 3D
FPS → `blazium-genre-fps-shooter`. Idle numbers → `blazium-clicker`. Juice
only → `blazium-game-feel`.

## Grok host

On Grok, keep context small: read this file, then **one** pin `SKILL.md`.
Spawn `gameplay-programmer` for CharacterBody code and `qa-tester` for the
jump/land Autowork. Child prompts must include scene path, action names, and
the 4.3.2 pin. Do not dump the catalog.

Prefer project files over memory. Evidence is Autowork, not a screenshot.

## Workflow

1. **Inspect.** `project.blazium` / `config_version`. Existing controller,
   TileMapLayer, InputMap `jump` / `move_*`.
2. **Choose.** Pins below — no custom framework. Order: input → movement →
   physics floors → tilemap → pixel camera → Autowork.
3. **Implement.** This adapter + **one** pin at a time (router + two max).
4. **Verify.** Autowork jump/land with `SIMULATE_PHYSICS` — not screenshots.
5. **Handoff.** Pins used, scene path, action names. Streamer overlay →
   `blazium-streaming`. Feel → `blazium-game-feel` after the mover works.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-2d-movement` | CharacterBody2D run/jump / coyote |
| `blazium-tilemap` | levels / Tiled |
| `blazium-physics` | colliders / one-way |
| `blazium-input` | InputMap / rebind |
| `blazium-pixel-perfect` | camera snap |
| `blazium-autowork` | tests |

### Scene sketch (4.3.2)

`Node2D` → `CharacterBody2D` (script) + `CollisionShape2D` + `AnimatedSprite2D`
or `Sprite2D`; `TileMapLayer` for solids; `Camera2D` current. Floor collision
under the body before any jump feel.

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

## Output contract

- Scene path(s) touched
- InputMap actions (`jump`, `move_left`, `move_right`)
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used Godot 4.7-only APIs** → stay on 4.3.2 CharacterBody2D / TileMapLayer.
- **Skipped Autowork** → add a jump/land test before juice.
- **Tuned squash before the body lands** → mover first, `blazium-game-feel` second.

## Related skills

- `blazium-2d-movement`, `blazium-tilemap`, `blazium-physics`, `blazium-input`,
  `blazium-pixel-perfect`, `blazium-autowork`, `blazium-game-feel`
