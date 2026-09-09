---
name: blazium-3d
pack: engine
---

# blazium-3d

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

3D scene setup is a Godot skill agents still need, pinned to 4.3.2.

## What

Node3D, Camera3D, lights, GridMap. MCP scene3d_tools.

**Non-goals:** Do not own Environment volumes (`blazium-environment`) or nav bake.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP scene3d_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP scene3d_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-environment` — adjacent
- `blazium-navigation` — adjacent
- `blazium-physics` — adjacent
