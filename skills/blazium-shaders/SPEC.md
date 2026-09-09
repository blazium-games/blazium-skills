---
name: blazium-shaders
pack: engine
---

# blazium-shaders

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Blazium shaders are text `.gdshader` authored with JustAMCP `shader_tools`.

## What

canvas_item + spatial, uniforms, MCP shader_tools.

**Non-goals:** Environment glow/tonemap (`blazium-environment`).

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP shader_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP shader_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-environment` — adjacent
- `blazium-3d` — adjacent
