---
name: blazium-2d-movement
description: >
  Implements CharacterBody2D movement (platformer, top-down, slopes) on
  Blazium 0.6.x / Godot 4.3.2 with move_and_slide. Use when writing player or
  enemy 2D controllers. Verify with Autowork simulate().
---

# Blazium 2D movement

`CharacterBody2D` + `move_and_slide()` on **4.3.2**. Do not invent Unity
`Rigidbody2D` APIs.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when implementing player/enemy 2D motion, jumps, slopes.

**When not to use:** tile painting → `blazium-tilemap`. Collision layers only →
`blazium-physics`. InputMap setup → `blazium-input`.

## Workflow

1. **Inspect.** Body type, floor layers, InputMap actions.
2. **Implement.** Velocity in `_physics_process`; `move_and_slide()`.
3. **Verify.** Autowork `simulate(node, frames, delta, false, SIMULATE_PHYSICS)`
   or play-mode MCP. Not screenshots alone.
4. **Handoff.** Actions used + collision layers.

## Patterns

```gdscript
extends CharacterBody2D

@export var speed: float = 200.0
@export var jump_velocity: float = -400.0

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity += get_gravity() * delta
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = jump_velocity
	var dir := Input.get_axis("ui_left", "ui_right")
	velocity.x = dir * speed
	move_and_slide()
```

Copy [assets/player_body_2d.gd](assets/player_body_2d.gd). Top-down: skip
gravity; use `Input.get_vector`.

## Pitfalls

- **Moved in `_process`** → tunneling; use `_physics_process`.
- **Forgot `move_and_slide`** → velocity never applied.
- **Copied Godot 3 `move_and_slide` args** → 4.x uses velocity property.

## Resources

- JustAMCP: `physics_tools`, `input_tools`

## Related skills

- `blazium-physics` — layers / Area2D
- `blazium-input` — actions
- `blazium-tilemap` — world
- `blazium-autowork` — simulate
