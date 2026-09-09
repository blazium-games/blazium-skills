---
name: blazium-tiled
pack: engine
---

# blazium-tiled

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

The Tiled importer is a 27-class module. Native TileMapLayer paint is a different job.

## What

`ResourceLoader.load("….tmx")` → scene with `TileMapLayer`. `TiledTileson.parse_file` → `TiledMap` / `TiledLayer` / `TiledTileset`.

**Non-goals:** JustAMCP `tilemap_set_cell` (`blazium-tilemap`).

## How

- Module: `blazium/modules/tiled_importer/`
- Tests: https://github.com/blazium-games/tiled_importer_module_tests
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

Import vs paint should not share one skill cookbook.

## Sources

- https://github.com/blazium-games/tiled_importer_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-tilemap` — native layers
