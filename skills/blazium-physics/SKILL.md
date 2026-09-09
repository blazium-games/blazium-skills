---
name: blazium-physics
description: >
  Sets up Blazium 2D/3D physics (CharacterBody, RigidBody, Area, layers, masks,
  raycasts) on 4.3.2 / 0.6.x. Use when collision is wrong, bodies overlap, or
  raycasts miss. Prefer JustAMCP physics_tools.
---

# Blazium physics

Layers and masks are the usual silent bug. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding colliders, areas, rigid bodies, or raycasts.

**When not to use:** movement feel → `blazium-2d-movement`. Nav bake →
`blazium-navigation`.

## Workflow

1. **Inspect.** Layer/mask bits on bodies and tiles.
2. **Implement.** JustAMCP `setup_collision`, `setup_physics_body`,
   `validate_physics_setup`.
3. **Verify.** `validate_physics_setup`. Play-mode overlap or Autowork
   `assert_true` on a known hit (layer/mask + Area). Not a screenshot of
   collision shapes.
4. **Handoff.** Layer table.

## Patterns

Static world / character / hitboxes on **separate layers**.
`Area2D`/`Area3D` for triggers; bodies for blocking.
Raycasts: `PhysicsDirectSpaceState2D/3D` + collision mask.

```gdscript
extends Area2D

func _ready() -> void:
	collision_layer = 4  # hitboxes
	collision_mask = 1   # world
```

JustAMCP: `setup_collision` / `setup_physics_body`, then `validate_physics_setup`.

## Pitfalls

- **Same layer, mask 0** → never collides. Set mask bits to the other layer.
- **Scaled CollisionShape** → prefer shape size, not node scale.
- **Physics in `_process`** → use `_physics_process`.
- **Area monitoring off** → no overlap. Enable monitoring and a matching mask.
- **Raycast vs `ConcavePolygonShape3D`** → trimesh hits are unreliable. Use a shape query or sample height analytically.
- **Trimesh/convex on imported GLB** → `create_trimesh_shape()` / `create_convex_shape()` can drop below 1 FPS. Use a primitive Box/Sphere/Capsule from the mesh AABB.
- **Per-tick drag** → `speed *= (1 - drag)` is frame-rate dependent. Use `speed *= exp(-rate * delta)`.

## Resources

- JustAMCP: `physics_tools`

## Related skills

- `blazium-2d-movement` — CharacterBody
- `blazium-navigation` — pathfinding
- `blazium-3d` — 3D bodies in scenes
- `blazium-autowork` — hit asserts
