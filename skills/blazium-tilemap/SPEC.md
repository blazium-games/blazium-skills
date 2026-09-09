---
name: blazium-tilemap
pack: engine
---

# blazium-tilemap

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

TileMapLayer paint and JustAMCP tilemap tools are the native path.

## What

TileMapLayer, TileSet, MCP `tilemap_tools`.

**Non-goals:** Tiled TMX / Tileson (`blazium-tiled`). 2D movement.

## How

1. Inspect project version (4.3.2 / 0.6.x).
2. Prefer JustAMCP `tilemap_set_cell` / `tilemap_fill_rect` / `validate_tilemap_structure`.
3. Verify with Autowork, not screenshots alone.

## Reasoning

Paint vs import should not share one cookbook.

## Sources

- JustAMCP `tilemap_tools`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-tiled` — TMX / Tileson
- `blazium-2d-movement` — adjacent
- `blazium-physics` — adjacent
- `blazium-sprites` — adjacent
