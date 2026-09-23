---
name: blazium-3d
pack: engine
---

# blazium-3d

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

3D scene setup is a Godot skill agents still need, pinned to 4.8.x.

## What

Node3D, Camera3D, lights, GridMap. MCP scene3d_tools.

**Non-goals:** Do not own Environment volumes (`blazium-environment`) or nav bake.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP scene3d_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP scene3d_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-environment` — adjacent
- `blazium-navigation` — adjacent
- `blazium-physics` — adjacent
