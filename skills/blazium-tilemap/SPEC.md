---
name: blazium-tilemap
pack: engine
---

# blazium-tilemap

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

TileMapLayer paint and JustAMCP tilemap tools are the native path.

## What

TileMapLayer, TileSet, MCP `tilemap_tools`.

**Non-goals:** Tiled TMX / Tileson (`blazium-tiled`). 2D movement.

## How

1. Inspect project version (4.8.x / 0.8.x).
2. Prefer JustAMCP `tilemap_set_cell` / `tilemap_fill_rect` / `validate_tilemap_structure`.
3. Verify with Autowork, not screenshots alone.

## Reasoning

Paint vs import should not share one cookbook.

## Sources

- JustAMCP `tilemap_tools`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-tiled` — TMX / Tileson
- `blazium-2d-movement` — adjacent
- `blazium-physics` — adjacent
- `blazium-sprites` — adjacent
