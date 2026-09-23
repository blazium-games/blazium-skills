---
name: blazium-camera
description: >
  Builds follow, deadzone, look-ahead, level bounds, orbit, first-person, and
  multi-target cameras on Camera2D, Camera3D, and SpringArm3D. Use for framing
  and smoothing. Pixel snap stays on blazium-pixel-perfect. Hit-stop and punch
  stay on blazium-game-feel.
---

# Blazium camera

Framing and follow. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Use `Camera2D` / `Camera3D`. Do not hand-roll a follow rig when drag margins,
limits, and position smoothing already cover the shot.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep `blazium_4.8`-safe APIs unless the user asks to migrate.

## When to use

- Use when a 2D camera should follow, ignore small motion (deadzone), lead
  facing (look-ahead), or stop at level bounds.
- Use when a 3D camera needs orbit, first-person look, or a spring arm that
  shortens on collision.
- Use when several targets must stay in frame.

**When not to use:** pixel integer snap → `blazium-pixel-perfect`. Hit-stop,
squash, or offset punch → `blazium-game-feel`. Player velocity →
`blazium-2d-movement`.

## Workflow

1. **Inspect.** Who moves first: the body, then the camera. Existing current camera.
2. **Choose.** Built-in `Camera2D` smoothing and drag margins before a custom lerp.
   3D orbit: yaw/pitch on a rig plus `SpringArm3D` for collision.
3. **Implement.** Update the camera after physics (`CAMERA2D_PROCESS_PHYSICS`
   or `_physics_process`). Smooth with `1.0 - exp(-rate * delta)`, not a
   fixed per-frame lerp.
4. **Verify.** Move the target at a low and a high tick rate, into a corner,
   and against a wall. Autowork `assert_true` that the camera stays inside
   limits and returns near the target. Not a screenshot of the viewport.
5. **Handoff.** Camera node path, limits, and whether juice owns `offset`.

## Patterns

### 2D follow, deadzone, bounds

```gdscript
extends Camera2D

func _ready() -> void:
	make_current()
	position_smoothing_enabled = true
	position_smoothing_speed = 6.0
	drag_horizontal_enabled = true
	drag_vertical_enabled = true
	process_callback = CAMERA2D_PROCESS_PHYSICS
	limit_left = 0
	limit_top = 0
	limit_right = level_width
	limit_bottom = level_height
```

Look-ahead: ease `offset` along velocity, then hand punch/shake to
`blazium-game-feel` on the same `offset` so the two do not fight.

### Frame-rate-independent follow

```gdscript
func _follow(target: Node2D, delta: float, rate: float = 8.0) -> void:
	var t := 1.0 - exp(-rate * delta)
	global_position = global_position.lerp(target.global_position, t)
```

### 3D orbit with collision

Parent `Camera3D` under `SpringArm3D`. Yaw and pitch live on the arm.
`spring_length` is the rest distance; the arm shortens when the shape hits
world collision. Clamp pitch. First-person: zero length, look on the body.

Multi-target: average the targets, then widen `zoom` (2D) or `fov` (3D)
until the group fits, and still clamp to level limits.

## Pitfalls

- **Per-frame `lerp(..., 0.1)`** → feel changes with frame rate. Use exp smoothing.
- **Camera updated before `move_and_slide`** → one-frame jitter. Follow after physics.
- **Punch left on `offset`** → `blazium-game-feel` must restore `Vector2.ZERO`.
- **No `make_current()`** → another camera stays active.
- **Spring arm mask includes the player** → camera stuck inside the body.

## Resources

- https://docs.blazium.app — `Camera2D`, `Camera3D`, `SpringArm3D`

## Related skills

- `blazium-pixel-perfect` — integer snap
- `blazium-game-feel` — punch and hit-stop
- `blazium-2d-movement` — the body being followed
- `blazium-3d` — scene cameras
