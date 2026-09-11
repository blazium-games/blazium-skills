---
name: blazium-physics
description: >
  Sets up Blazium 0.6.x / Godot 4.3.2 collision layers, masks, Area2D/Area3D
  triggers, CharacterBody/RigidBody/StaticBody, and PhysicsDirectSpaceState
  ray / shape queries. Use when bodies overlap, raycasts miss, monitoring is
  off, or imported GLB collision is trimesh. Prefer JustAMCP physics_tools
  (setup_collision, setup_physics_body, validate_physics_setup). Not movement
  feel and not nav bake.
when-to-use: >
  collision_layer, collision_mask, Area2D, raycast miss, PhysicsRayQueryParameters2D,
  PhysicsDirectSpaceState2D, setup_collision, validate_physics_setup, overlap,
  one-way platform collider, ConcavePolygonShape3D
metadata:
  author: blazium-games
  short-description: Layers, masks, Areas, and space-state queries on 4.3.2
---

# Blazium physics

Layers and masks are the usual silent bug. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Do not invent Unity layers. Do not apply Godot
4.7-only calls.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding colliders, Areas, rigid bodies, one-way floors, or raycasts.
- Use when two bodies pass through each other or a ray never hits.

**When not to use:** movement feel / coyote / `move_and_slide` →
`blazium-2d-movement`. Nav bake → `blazium-navigation`. Juice / squash →
`blazium-game-feel`. Tile painting → `blazium-tilemap` (this skill only
owns the collider bits on those tiles).

## Grok host

Load this file plus at most one pin (`blazium-2d-movement` or
`blazium-3d`). Spawn `gameplay-programmer` for layer bits and `qa-tester`
for Autowork hit asserts. Child prompts must include the layer table,
scene path, and whether JustAMCP `:6506` is connected. Do not dump the
catalog.

Grok `code_execution` and dock screenshots are not evidence. Quote
JustAMCP `validate_physics_setup` / `physics_tools`, Autowork
`assert_true` on a known hit, or `INCONCLUSIVE` if headless physics was
off.

## Workflow

1. **Inspect.** Layer/mask bits on bodies, Areas, and tiles. Confirm
   `monitoring` / `monitorable` on Areas.
2. **Choose.** Separate world / character / hitbox / trigger layers.
   State the table before writing bits.
3. **Implement.** Set `collision_layer` and `collision_mask`. Prefer
   JustAMCP `setup_collision` / `setup_physics_body` when `:6506` is up.
   Raycasts go through `PhysicsDirectSpaceState2D/3D`, not a custom
   stepper.
4. **Verify.** `validate_physics_setup`. Play-mode overlap or Autowork
   `assert_true` on a known hit (layer/mask + Area). Not a screenshot of
   collision shapes.
5. **Handoff.** Layer table + query mask. Movement feel stays on
   `blazium-2d-movement`.

## Patterns

### Layer table (baseline)

Bits are 1-based in the editor, 0-based in code (`1 << (layer - 1)`).

| Layer | Bit | Owns |
|-------|-----|------|
| 1 world | 0 (`1`) | StaticBody / TileMapLayer solids |
| 2 characters | 1 (`2`) | CharacterBody / player / NPC |
| 3 hitboxes | 2 (`4`) | hurt / hit Area2D |
| 4 triggers | 3 (`8`) | pickups, doors, one-way sensors |

World mask includes characters. Character mask includes world. Hitboxes
mask the layer they are allowed to hit — never mask 0.

```gdscript
extends Area2D

func _ready() -> void:
	collision_layer = 4  # hitboxes
	collision_mask = 1   # world
	monitoring = true
	monitorable = true
```

Static world / character / hitboxes on **separate layers**.
`Area2D`/`Area3D` for triggers; bodies for blocking.

### Ray / shape query (4.3.2)

```gdscript
func first_hit(from: Vector2, to: Vector2, mask: int) -> Dictionary:
	var space := get_world_2d().direct_space_state
	var q := PhysicsRayQueryParameters2D.create(from, to, mask)
	q.collide_with_areas = true
	q.collide_with_bodies = true
	return space.intersect_ray(q)
```

3D: `PhysicsRayQueryParameters3D` + `get_world_3d().direct_space_state`.
Shape overlap: `PhysicsShapeQueryParameters2D` + `intersect_shape`.
Do not query `ConcavePolygonShape3D` (trimesh) and expect stable hits.

JustAMCP: `setup_collision` / `setup_physics_body`, then
`validate_physics_setup`.

## Output contract

- Scene path(s) and nodes touched
- Layer table (name → bit → who collides with whom)
- Query mask and `collide_with_areas` / `collide_with_bodies`
- Evidence: `validate_physics_setup` result, Autowork assert, or
  `INCONCLUSIVE`
- Next skill (`blazium-2d-movement`, `blazium-tilemap`, `blazium-3d`)

## Pitfalls

- **Same layer, mask 0** → never collides. Set mask bits to the other layer.
- **Scaled CollisionShape** → prefer shape size, not node scale.
- **Physics in `_process`** → use `_physics_process`.
- **Area monitoring off** → no overlap. Enable monitoring and a matching mask.
- **Raycast vs `ConcavePolygonShape3D`** → trimesh hits are unreliable. Use a shape query or sample height analytically.
- **Trimesh/convex on imported GLB** → `create_trimesh_shape()` / `create_convex_shape()` can drop below 1 FPS. Use a primitive Box/Sphere/Capsule from the mesh AABB.
- **Per-tick drag** → `speed *= (1 - drag)` is frame-rate dependent. Use `speed *= exp(-rate * delta)`.
- **Rewrote the mover here** → velocity / coyote belong on `blazium-2d-movement`.

## Resources

- JustAMCP: `physics_tools` (`setup_collision`, `setup_physics_body`, `validate_physics_setup`)
- Docs: https://docs.blazium.app (PhysicsDirectSpaceState2D, 4.3.2-safe)

## Related skills

- `blazium-2d-movement` — CharacterBody velocity / coyote
- `blazium-navigation` — pathfinding
- `blazium-3d` — 3D bodies in scenes
- `blazium-tilemap` — world solids
- `blazium-autowork` — hit asserts
