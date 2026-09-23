---
name: blazium-assets
pack: content
---

# blazium-assets

Import filter, mipmaps, and nine-patch margins. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent an asset database. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`).

## Related skills

- `blazium-sprites` — flipbooks
- `blazium-pixel-perfect` — scale
