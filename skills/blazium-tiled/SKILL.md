---
name: blazium-tiled
description: >
  Imports Tiled maps (TMX/TMJ) via tiled_importer (TiledTileson, TiledMap,
  TiledLayer, TiledTileset) and ResourceLoader. Use for .tmx/.tmj worlds.
  Not native TileMapLayer painting (blazium-tilemap).
---

# Blazium Tiled importer

Tiled → Blazium scenes / parser objects. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. **Pick one pipeline:** `.tmx` / Tileson here, or
native `TileMapLayer` paint in `blazium-tilemap`. Do not mix both on the
same layer blindly.

Module: `blazium/modules/tiled_importer/` — `TiledTileson`, `TiledMap`,
`TiledLayer`, `TiledTileset`.

Native `TileMapLayer` paint / JustAMCP `tilemap_tools` → `blazium-tilemap`.

Ignore `test_singletons.gd` in the tests repo — it is not importer coverage.

## When to use

- Use when loading `.tmx` / `.tmj` / Tiled JSON into a scene or parser object.

**When not to use:** painting cells on a `TileMapLayer` you author in
Blazium → `blazium-tilemap`. Atlas slicing without a grid →
`blazium-sprites`.

## Workflow

1. **Inspect.** Existing `.tmx` / tileset images. Importer compiled?
2. **Choose.** `ResourceLoader.load` (imported scene) vs
   `TiledTileson.parse_file` (data API).
3. **Implement.** Keep tileset image paths valid. One `TileMapLayer` per
   Tiled layer after instantiate.
4. **Verify.** Autowork in `tiled_importer_module_tests`.
5. **Handoff.** Layer names. Controllers → `blazium-2d-movement`.

## Patterns

### Import as scene

```gdscript
var scene := ResourceLoader.load("res://maps/simple_map.tmx")
var instance := scene.instantiate()
var layer: TileMapLayer = instance.get_node_or_null("simple_layer") as TileMapLayer
assert_true(layer.get_used_cells().size() > 0)
```

Infinite maps load the same way (`infinite.tmx`).

### Parse with Tileson

```gdscript
var tson := TiledTileson.new()
var map: TiledMap = tson.parse_file("res://maps/simple_map.json")
assert_eq(map.get_status(), "OK")
var size: Vector2 = map.get_size()
var tile_size: Vector2 = map.get_tile_size()
var layers: Array = map.get_layers()
var first: TiledLayer = layers[0]
print(first.get_name(), first.get_tson_type(), first.get_opacity())
var tilesets: Array = map.get_tilesets()
var ts: TiledTileset = tilesets[0]
```

`TiledMap` also: `get_hexside_length`, `is_infinite`, `get_next_layer_id`,
`get_next_object_id`, `get_orientation`, `get_render_order`,
`get_compression_level`, `get_parallax_origin`, `get_background_color`.

`TiledLayer` also: `get_size` (Vector2i), `get_parallax`, `has_repeat_x` /
`has_repeat_y`, `get_offset`.

Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd` in
https://github.com/blazium-games/tiled_importer_module_tests

## Pitfalls

- **Imported Tiled as a screenshot** → load TMX or parse JSON.
- **Mixed native paint and importer blindly** → pick one pipeline.
- **Treated `test_singletons.gd` as importer coverage** → ignore it.

## Resources

- Tests: https://github.com/blazium-games/tiled_importer_module_tests
- `blazium/modules/tiled_importer/`

## Related skills

- `blazium-tilemap` — native TileMapLayer / JustAMCP
- `blazium-physics` — collision on layers
- `blazium-2d-movement` — controllers
