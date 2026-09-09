---
name: blazium-nodes-scenes
pack: engine
---

# blazium-nodes-scenes

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Scene tree work is the most common agent task.

## What

PackedScene, instancing, autoloads. Prefer JustAMCP scene/node tools (~44 + 14).

**Non-goals:** Do not own signal architecture (signals-groups) or 2D movement. Do not require C# `SceneTree` scene builders.

Silent-failure pack traps: owner chain (skip instanced GLB/`.tscn`), pack-then-instantiate count, `.gdignore`, `generate_normals()`, MultiMesh + GLB / `material_override`.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP scene_tools + node_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP scene_tools + node_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-signals-groups` — adjacent
- `blazium-mcp` — adjacent
