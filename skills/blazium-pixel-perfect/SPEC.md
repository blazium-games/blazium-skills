---
name: blazium-pixel-perfect
pack: engine
---

# blazium-pixel-perfect

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Pixel games need Camera2D snap and integer viewport scale.

## What

Camera2D, viewport stretch, snap, integer scale.

**Non-goals:** Do not own tile painting.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `Camera2D / Window stretch settings`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: Camera2D / Window stretch settings

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-sprites` — adjacent
- `blazium-2d-movement` — adjacent
