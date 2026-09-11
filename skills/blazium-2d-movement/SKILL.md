---
name: blazium-2d-movement
description: >
  Implements CharacterBody2D controllers on Blazium 0.6.x / Godot 4.3.2
  (MOTION_MODE_GROUNDED platformer with coyote float, MOTION_MODE_FLOATING
  top-down, slopes, floor_snap). Use when writing player or enemy 2D movers
  with move_and_slide. Verify with Autowork simulate(SIMULATE_PHYSICS).
  Not collision-layer setup, not a genre kit, not juice/Tween.
when-to-use: >
  CharacterBody2D, move_and_slide, coyote time, top-down mover, slope walk,
  MOTION_MODE_GROUNDED, MOTION_MODE_FLOATING, player controller 2D
metadata:
  author: blazium-games
  short-description: CharacterBody2D grounded or floating movers on 4.3.2
---

# Blazium 2D movement

`CharacterBody2D` + `move_and_slide()` on **Blazium 0.6.x (Godot 4.3.2 fork)**.
Do not invent Unity `Rigidbody2D` APIs. Do not apply Godot 4.7-only calls.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when implementing player or enemy 2D motion, jumps, slopes, or a
  top-down walker.
- Use when the body already exists and the feel bug is velocity / floor snap
  / coyote, not layers.

**When not to use:** tile painting → `blazium-tilemap`. Collision layers /
raycasts only → `blazium-physics`. InputMap setup → `blazium-input`.
Side-scroll genre composition → `blazium-genre-platformer` (this skill is
the mover pin). Camera punch / squash → `blazium-game-feel` after the body
lands.

## Grok host

Load this file plus at most one pin (`blazium-input` or `blazium-physics`).
Spawn `gameplay-programmer` for the body and `qa-tester` for Autowork.
Child prompts must include scene path, InputMap action names, and
`MOTION_MODE_GROUNDED` vs `MOTION_MODE_FLOATING`. Do not dump the catalog.

Grok `code_execution` and dock screenshots are not evidence. Quote Autowork
`simulate()` JSON or JustAMCP `physics_tools` / `input_tools`.

Copy [assets/player_body_2d.gd](assets/player_body_2d.gd) into the player
scene. Do not treat the asset as a genre kit.

## Workflow

1. **Inspect.** Body type, `motion_mode`, floor layers, InputMap actions
   (`jump`, `ui_left` / `ui_right` or `move_*`).
2. **Choose.** Grounded + gravity + coyote for jump games. Floating +
   `Input.get_vector` and no gravity for top-down. State the assumption.
3. **Implement.** Set velocity in `_physics_process`; call `move_and_slide()`.
   Set `up_direction` and `floor_snap_length` on grounded bodies.
4. **Verify.** Autowork `simulate(node, frames, delta, false, SIMULATE_PHYSICS)`
   or play-mode MCP. Not screenshots alone.
5. **Handoff.** Actions used, `motion_mode`, collision layers. Genre adapter
   or `blazium-game-feel` next — not a rewrite of this controller.

## Patterns

### Grounded (platformer)

`motion_mode = MOTION_MODE_GROUNDED`. Apply `get_gravity()` off-floor.
Coyote is a float timer, not an engine flag.

```gdscript
extends CharacterBody2D

@export var speed: float = 200.0
@export var jump_velocity: float = -400.0
@export var coyote_time: float = 0.08

var _coyote: float = 0.0

func _ready() -> void:
	motion_mode = MOTION_MODE_GROUNDED
	floor_snap_length = 8.0
	up_direction = Vector2.UP

func _physics_process(delta: float) -> void:
	if is_on_floor():
		_coyote = coyote_time
	else:
		velocity += get_gravity() * delta
		_coyote = maxf(_coyote - delta, 0.0)
	if Input.is_action_just_pressed("jump") and _coyote > 0.0:
		velocity.y = jump_velocity
		_coyote = 0.0
	var dir := Input.get_axis("ui_left", "ui_right")
	velocity.x = dir * speed
	move_and_slide()
```

Starter: [assets/player_body_2d.gd](assets/player_body_2d.gd).

### Floating (top-down)

```gdscript
func _ready() -> void:
	motion_mode = MOTION_MODE_FLOATING

func _physics_process(_delta: float) -> void:
	var dir := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	velocity = dir * speed
	move_and_slide()
```

No gravity. Do not set `up_direction` as a substitute for floating mode.

### Slopes

Keep `floor_max_angle` at the default unless the level needs steeper walks.
`floor_snap_length` stops the body from leaving the floor on slight ramps.
One-way platforms are collision-shape / layer work → `blazium-physics`.

### Autowork

```gdscript
func test_jump_then_lands() -> void:
	var p := $Player as CharacterBody2D
	simulate(p, 1, 1.0 / 60.0, false, SIMULATE_PHYSICS)
	p.velocity.y = -400.0
	simulate(p, 20, 1.0 / 60.0, false, SIMULATE_PHYSICS)
	assert_true(p.is_on_floor(), "landed")
```

`simulate` is an Autowork helper — see `blazium-autowork`. Do not invent a
Grok-side physics stepper.

## Output contract

- Scene path and script path
- `motion_mode` (`GROUNDED` or `FLOATING`)
- InputMap actions touched
- Coyote / snap values if used
- Autowork test name + pass/fail, or `INCONCLUSIVE` if headless physics was off
- Next skill (`blazium-physics`, `blazium-genre-platformer`, `blazium-game-feel`)

## Pitfalls

- **Moved in `_process`** → tunneling; use `_physics_process`.
- **Forgot `move_and_slide`** → velocity never applied.
- **Copied Godot 3 `move_and_slide` args** → 4.x uses the `velocity` property.
- **Grounded body with no `up_direction`** → `is_on_floor()` stays false.
- **Top-down still on `MOTION_MODE_GROUNDED`** → gravity pulls the walker.
- **Tuned squash before the body lands** → mover first, `blazium-game-feel` second.
- **Rewrote this into a genre framework** → compose `blazium-genre-platformer`.

## Resources

- Asset: [assets/player_body_2d.gd](assets/player_body_2d.gd)
- JustAMCP: `physics_tools`, `input_tools`
- Docs: https://docs.blazium.app (CharacterBody2D, 4.3.2-safe)

## Related skills

- `blazium-physics` — layers / Area2D / raycasts
- `blazium-input` — actions / rebind
- `blazium-tilemap` — world solids
- `blazium-genre-platformer` — compose this pin with tilemap / camera
- `blazium-game-feel` — juice after the mover works
- `blazium-autowork` — `simulate` / `SIMULATE_PHYSICS`
