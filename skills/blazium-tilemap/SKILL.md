---
name: blazium-tilemap
description: >
  Builds Blazium 0.6.x 2D tile worlds with TileMapLayer and TileSet on
  Godot 4.3.2. Use when painting cells, autotile, terrains, or JustAMCP
  tilemap_tools (tilemap_set_cell, tilemap_fill_rect, tilemap_configure_atlas,
  validate_tilemap_structure). Tiled TMX/Tileson import → blazium-tiled.
  Not a player controller.
when-to-use: >
  TileMapLayer, TileSet, paint tiles, autotile, tilemap_set_cell,
  tilemap_fill_rect, validate_tilemap_structure, 2D tile world
metadata:
  author: blazium-games
  short-description: TileMapLayer paint, atlas, and cell validation
---

# Blazium tilemap

Blazium 0.6.x uses **`TileMapLayer`** (not the old single `TileMap` as the
primary API). **Pick one pipeline:** paint cells here, or import TMX via
`blazium-tiled`. Do not mix both on the same layer blindly.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when creating TileSet / TileMapLayer or terrains.
- Use when Autowork must assert a known cell after paint.

**When not to use:** `.tmx` / Tiled JSON import → `blazium-tiled`. Player
controllers → `blazium-2d-movement`. Atlas slicing without a grid →
`blazium-sprites`. Nav bake after paint → `blazium-navigation`.

## Grok host

Read this file only. Spawn `level-designer` for layer roles and
`gameplay-programmer` for `set_cell`. Child prompts must include TileSet
path, layer names, and source_id / atlas coords. Evidence is
`validate_tilemap_structure` or Autowork `assert_eq` on a cell — not a
screenshot of the map.

## Workflow

1. **Inspect.** Existing TileSet / Tiled project assets.
2. **Choose.** Native TileMapLayer here. Tiled import → `blazium-tiled`.
3. **Implement.** JustAMCP `tilemap_set_cell`, `tilemap_fill_rect`,
   `tilemap_configure_atlas`, `validate_tilemap_structure`.
4. **Verify.** `validate_tilemap_structure`; Autowork `assert_eq` on a known
   cell after `tilemap_set_cell`. Collision/nav on the right layer.
5. **Handoff.** Layer names + TileSet path. Tiled files → `blazium-tiled`.

## Patterns

One `TileMapLayer` per collision/nav/visual role. Physics: assign
collision on TileSet physics layers (`blazium-physics`).

```gdscript
extends TileMapLayer

func paint_floor(cell: Vector2i, source_id: int, atlas: Vector2i) -> void:
	set_cell(cell, source_id, atlas)
```

JustAMCP: `tilemap_configure_atlas` then `tilemap_set_cell` / `tilemap_fill_rect`.
Assign the TileSet before any paint.

## Output contract

- TileSet path
- Layer names and roles (visual / collision / nav)
- Cells or rect painted
- `validate_tilemap_structure` or Autowork cell assert

## Pitfalls

- **Used Godot 3 `TileMap` API only** → prefer TileMapLayer on 4.3.x.
- **Imported Tiled as a screenshot** → `blazium-tiled`.
- **Painted collision on the wrong layer** → validate with physics tools.
- **TileMapLayer with no TileSet** → `set_cell` / `tilemap_set_cell` paints
  nothing. Assign the TileSet first.

## Resources

- JustAMCP: `tilemap_tools`

## Related skills

- `blazium-tiled` — TMX / Tileson import
- `blazium-2d-movement` — controllers
- `blazium-physics` — collision
- `blazium-sprites` — atlas art
- `blazium-autowork` — cell asserts
