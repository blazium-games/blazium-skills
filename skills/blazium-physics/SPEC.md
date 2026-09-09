---
name: blazium-physics
pack: engine
---

# blazium-physics

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Wrong layers/masks are the top silent gameplay bug. Raycasts miss trimesh (`ConcavePolygonShape3D`). Imported GLB collision must stay primitive (AABB Box/Sphere/Capsule), not `create_trimesh_shape()` / `create_convex_shape()`. Damping: `speed *= exp(-rate * delta)`.

## What

RigidBody/StaticBody/Area/CharacterBody 2D+3D, raycasts. MCP physics tools.

**Non-goals:** Do not own navigation baking.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP physics_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP physics_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-navigation` — adjacent
- `blazium-2d-movement` — adjacent
- `blazium-3d` — adjacent
