---
name: blazium-physics
pack: engine
---

# blazium-physics

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Wrong layers/masks are the top silent gameplay bug. Raycasts miss trimesh (`ConcavePolygonShape3D`). Imported GLB collision must stay primitive (AABB Box/Sphere/Capsule), not `create_trimesh_shape()` / `create_convex_shape()`. Damping: `speed *= exp(-rate * delta)`.

## What

RigidBody/StaticBody/Area/CharacterBody 2D+3D, `PhysicsDirectSpaceState2D/3D` ray and shape queries, layer table. MCP `physics_tools`: `setup_collision`, `setup_physics_body`, `validate_physics_setup`.

**Non-goals:** Do not own navigation baking, CharacterBody velocity / coyote, or tile painting.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Write the layer table first, then the smallest `blazium_4.8`-safe pattern.
4. Verify with `validate_physics_setup`, Autowork, or play-mode MCP — not screenshots alone.

Engine / module path: `JustAMCP physics_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time. Movement feel stays on `blazium-2d-movement`.

## Sources

- Blazium: JustAMCP physics_tools
- Docs: https://docs.blazium.app

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks. Grok `code_execution` is not physics evidence.

## Related skills

- `blazium-navigation` — adjacent
- `blazium-2d-movement` — adjacent
- `blazium-3d` — adjacent
- `blazium-tilemap` — adjacent
- `blazium-autowork` — adjacent
