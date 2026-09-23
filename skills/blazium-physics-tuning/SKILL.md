---
name: blazium-physics-tuning
description: >
  Tunes default gravity, friction, bounce, and damping on physics materials
  so motion stops feeling floaty or icy. Use when jumps hang or bodies slide.
  Collision layers, masks, and raycasts stay on blazium-physics.
---

# Blazium physics tuning

How motion feels after collision already works. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**.

Layers, masks, and queries stay on `blazium-physics`. This skill only changes
gravity, `PhysicsMaterial` friction/bounce, and body damping.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep `blazium_4.8`-safe APIs unless the user asks to migrate.

## When to use

- Use when jumps hang, landings feel icy, or bodies never settle.
- Use when a shared `PhysicsMaterial` should match a stated feel.

**When not to use:** missed overlaps or raycasts → `blazium-physics`.
Coyote time and jump velocity → `blazium-2d-movement`.

## Grok host

Read this file only after layers are correct. Spawn `engine-programmer`.
Child prompts must name the gravity setting and the material path. Evidence
is an Autowork settle or jump-height assert, not a screenshot.

## Workflow

1. **Inspect.** `physics/2d/default_gravity` or `physics/3d/default_gravity`,
   and any `PhysicsMaterial` on the body.
2. **Choose.** One change: gravity, friction, bounce, or damping.
3. **Implement.** Set the material on the body. Damping uses `linear_damp`
   / `angular_damp` (2D and 3D rigid bodies).
4. **Verify.** Autowork: after N physics frames a dropped body is near rest,
   or a jump apex matches the stated height. Not a screenshot.
5. **Handoff.** Values changed and the body or material path.

## Patterns

```gdscript
extends RigidBody2D

func _ready() -> void:
	var mat := PhysicsMaterial.new()
	mat.friction = 1.0
	mat.bounce = 0.0
	physics_material_override = mat
	linear_damp = 1.5
```

Project default gravity is `ProjectSettings` `physics/2d/default_gravity`
(3D: `physics/3d/default_gravity`). Change the project default only when
every body should share it.

Per-frame `speed *= (1.0 - drag)` is frame-rate dependent. Prefer
`speed *= exp(-rate * delta)` in the mover (`blazium-2d-movement`).

## Output contract

- Gravity value (2D or 3D) if changed
- Material path, friction, bounce
- Damping values
- Autowork settle or apex assert, or `INCONCLUSIVE`

## Pitfalls

- **Tuned masks to fix slide** → that is `blazium-physics`.
- **Bounce above 1** → energy gain. Keep bounce in 0–1 unless asked.
- **Friction 0 on a floor material** → ice. State that it is intentional.
- **Gravity edited on one body via project default** → every body changes.

## Resources

- https://docs.blazium.app — `PhysicsMaterial`, `RigidBody2D`, `RigidBody3D`

## Related skills

- `blazium-physics` — layers and queries
- `blazium-2d-movement` — jump velocity
- `blazium-3d` — 3D bodies
