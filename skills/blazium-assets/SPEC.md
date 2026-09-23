---
name: blazium-assets
pack: content
---

# blazium-assets

Import filter, mipmaps, and nine-patch margins. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Art fails in-game when filter and margins are wrong, even if the file exists.

## What

Texture and mesh import choices, `NinePatchRect` margins, file naming.

**Non-goals:** SpriteFrames, TileSet terrains, GIF record.

## How

1. Classify pixel vs smooth.
2. Set filter and mipmaps.
3. Record nine-patch margins.
4. Confirm the texture loads.

## Reasoning

`blazium-sprites` owns atlases and flipbooks. This skill owns the import pass.

## Sources

- Blazium: texture import, `NinePatchRect`

## Limits

Do not invent an asset database. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-sprites` — flipbooks
- `blazium-pixel-perfect` — scale
