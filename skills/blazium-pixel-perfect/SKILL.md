---
name: blazium-pixel-perfect
description: >
  Configures pixel-perfect 2D rendering on Blazium 0.6.x (Camera2D snap,
  viewport stretch canvas_items + integer scale, nearest filter). Use when
  pixel art must stay crisp, design resolution is 320x180-class, or the
  camera crawls. Not tile painting and not sprite atlas slicing.
when-to-use: >
  pixel-perfect, integer scale, Camera2D snap, canvas_items stretch,
  nearest filter, 320x180, subpixel crawl
metadata:
  author: blazium-games
  short-description: Camera2D snap, integer stretch, nearest pixel art
---

# Blazium pixel-perfect

Use Camera2D + stretch settings. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs.

## When to use

- Use when pixel art must stay crisp (integer scale, snap).
- Use when Camera2D subpixel motion causes crawl.

**When not to use:** tile painting → `blazium-tilemap`. Sprite filter only →
`blazium-sprites`. Juice / camera punch → `blazium-game-feel` after snap
works.

## Grok host

Read this file only. Spawn `rendering-programmer` for stretch + Camera2D
and `qa-tester` for the zoom assert. Child prompts must include design
resolution, stretch mode, and Camera2D path. Evidence is Autowork
`assert_eq` on `cam.zoom` — not a dock screenshot.

## Workflow

1. **Inspect.** Window size, stretch mode, Camera2D zoom.
2. **Set** viewport stretch (`canvas_items` / integer) and texture filter nearest.
3. **Camera2D:** zoom that maps world pixels 1:1; enable snap when needed.
4. **Verify.** Autowork `assert_eq(cam.zoom, Vector2.ONE)` (or the integer zoom
   you chose) in play mode. Optional JustAMCP `editor_take_screenshot` is extra.
5. **Handoff.** Design resolution + stretch mode + Camera2D zoom.

## Patterns

Design resolution (e.g. 320×180) + integer window scale. Disable texture filter
on sprites and TileSets. Subpixel camera motion causes crawl — snap or move in
pixel increments.

```gdscript
extends Camera2D

func _ready() -> void:
	zoom = Vector2.ONE  # 1:1 world pixels; pair with integer stretch
```

Project stretch: `canvas_items` mode + integer scale. Sprite filter:
`blazium-sprites`.

## Output contract

- Design resolution
- Stretch mode (`canvas_items` + integer)
- Camera2D path and zoom
- Autowork zoom assert pass/fail

## Pitfalls

- **Non-integer Camera2D zoom** → shimmer. Keep zoom on integer multiples.
- **Mipmaps on pixel textures** → blur. Disable mipmaps; use nearest.
- **Copied Unity Pixel Perfect Camera component** → use Camera2D + stretch.
- **Stretch mode `disabled` or `viewport`** → blurry or wrong letterbox. Use
  `canvas_items` + integer scale for retro 2D.

## Resources

- JustAMCP: `editor_take_screenshot`

## Related skills

- `blazium-sprites` — filter
- `blazium-2d-movement` — camera follow
- `blazium-tilemap` — tile worlds
- `blazium-autowork` — zoom asserts
