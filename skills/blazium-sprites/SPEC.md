---
name: blazium-sprites
pack: engine
---

# blazium-sprites

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

AtlasTexture and SpriteFrames are the 2D art path. Not GIF (`blazium-gif`).

## What

AtlasTexture, SpriteFrames, pixel atlas packing. Not GIF (`blazium-gif`).

**Non-goals:** Do not own TileSet terrains.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `core 2D + JustAMCP asset_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: core 2D + JustAMCP asset_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-tilemap` — adjacent
- `blazium-animation` — adjacent
- `blazium-gif` — adjacent
- `blazium-pixel-perfect` — adjacent
