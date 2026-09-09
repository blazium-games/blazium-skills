---
name: blazium-sprites
pack: engine
---

# blazium-sprites

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

AtlasTexture and SpriteFrames are the 2D art path. Not GIF (`blazium-gif`).

## What

AtlasTexture, SpriteFrames, pixel atlas packing. Not GIF (`blazium-gif`).

**Non-goals:** Do not own TileSet terrains.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `core 2D + JustAMCP asset_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: core 2D + JustAMCP asset_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-tilemap` — adjacent
- `blazium-animation` — adjacent
- `blazium-gif` — adjacent
- `blazium-pixel-perfect` — adjacent
