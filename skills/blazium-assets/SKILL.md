---
name: blazium-assets
description: >
  Imports textures and meshes, sets filter and mipmaps, and records
  NinePatchRect slice margins. Use for an art import pass and naming.
  SpriteFrames flipbooks stay on blazium-sprites. Tile terrains stay on
  blazium-tilemap.
---

# Blazium assets

Import settings and slice margins. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Flipbook animations stay on `blazium-sprites`. This skill owns the file
landing in `res://`, the filter, and stretchable frames.

## When to use

- Use when importing a texture or mesh and choosing filter, mipmaps, or repeat.
- Use when a panel needs `NinePatchRect` margins instead of a scaled sprite.

**When not to use:** `SpriteFrames` → `blazium-sprites`. GIF → `blazium-gif`.
TileSet terrains → `blazium-tilemap`. Shader materials → `blazium-shaders`.

## Grok host

Read this file only. Spawn `art-director` or `technical-artist`. Child
prompts must include the source path and the filter mode. Evidence is the
import setting or an Autowork `texture != null` check.

## Workflow

1. **Inspect.** Pixel art vs smooth art. Existing import preset.
2. **Choose.** Nearest and no mipmaps for pixels. Linear plus mipmaps for
   3D or large smooth images.
3. **Implement.** Place files under `res://art/` (or the project’s art
   root). Set `NinePatchRect` `patch_margin_*` from the art’s safe border.
4. **Verify.** Texture loads. Pixel art stays crisp at integer scale
   (`blazium-pixel-perfect`). Not a screenshot alone.
5. **Handoff.** Paths, filter, and margin values.

## Patterns

Pixel textures: filter nearest, mipmaps off. Smooth or 3D: filter linear,
mipmaps on. Leave at least one pixel of padding between atlas cells so
filtering does not bleed (`blazium-sprites` owns the `AtlasTexture` region).

```gdscript
extends NinePatchRect

func _ready() -> void:
	patch_margin_left = 8
	patch_margin_top = 8
	patch_margin_right = 8
	patch_margin_bottom = 8
```

Name files by role (`ui_panel`, `hero_idle`), not by export date.

## Output contract

- Imported paths
- Filter and mipmap choice
- NinePatch margins if any
- Load evidence or `INCONCLUSIVE`

## Pitfalls

- **Linear filter on pixel art** → blur. Use nearest.
- **Scaled Sprite2D as a window frame** → `NinePatchRect`.
- **Mipmaps on a 16×16 sprite** → muddy. Turn them off.
- **Authored SpriteFrames here** → `blazium-sprites`.

## Resources

- https://docs.blazium.app — `NinePatchRect`, texture import
- JustAMCP: `asset_tools` when generating pixels

## Related skills

- `blazium-sprites` — atlases and flipbooks
- `blazium-pixel-perfect` — integer scale
- `blazium-tilemap` — grids
- `blazium-gif` — GIF module
