---
name: blazium-sprites
description: >
  Sets up Blazium 2D sprite atlases (AtlasTexture, SpriteFrames) on 4.3.2.
  Use when slicing sprites, building SpriteFrames, or packing atlases. Not GIF
  (blazium-gif) and not TileSet terrains (blazium-tilemap).
---

# Blazium sprites

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when creating `AtlasTexture`, `SpriteFrames`, or pixel atlases.

**When not to use:** animated GIF import/record → `blazium-gif`.
Tile terrains → `blazium-tilemap`. AnimationPlayer on UI → `blazium-animation`.

## Workflow

1. **Inspect.** Source textures, filter/mip settings (pixel art: nearest).
2. **Slice.** Atlas regions or SpriteFrames animations (`animation_tools`).
3. **Assign.** Sprite2D / AnimatedSprite2D.
4. **Verify.** Autowork `assert_true(sprite.texture != null)` or
   `assert_true(anim.sprite_frames != null)` in play mode. JustAMCP
   `asset_tools` if generating pixels. Not a screenshot alone.
5. **Handoff.** Atlas / SpriteFrames paths + filter setting.

## Patterns

Pixel art: disable filter, integer scale (`blazium-pixel-perfect`).
`AnimatedSprite2D` + `SpriteFrames` for flipbooks. `AnimationPlayer` for mixed
property tracks (`blazium-animation`).

```gdscript
extends Sprite2D

func _ready() -> void:
	texture = load("res://art/hero_atlas.tres") as AtlasTexture
```

Pixel art: nearest filter on the texture (see `blazium-pixel-perfect`).
JustAMCP: `asset_tools` for pixels; SpriteFrames via `animation_tools`.

## Pitfalls

- **Linear filter on pixel art** → blurry sprites. Use nearest + integer scale.
- **Used GIFRecorder for a tileset** → wrong skill (`blazium-gif` / `blazium-tilemap`).
- **Packed without bleed** → seams; add padding between atlas cells.
- **AtlasTexture region larger than the source** → empty or clipped frames. Match region to the cell size.

## Resources

- JustAMCP: `asset_tools`, `animation_tools` (SpriteFrames)

## Related skills

- `blazium-tilemap` — grids
- `blazium-animation` — tracks
- `blazium-pixel-perfect` — camera snap
- `blazium-gif` — GIF module
- `blazium-autowork` — texture asserts
