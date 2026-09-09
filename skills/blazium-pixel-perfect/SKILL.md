---
name: blazium-pixel-perfect
description: >
  Configures pixel-perfect 2D rendering (Camera2D, viewport stretch, integer
  2d-pixel-perfect.
---

# Blazium pixel-perfect

Godot’s pack has no pixel-perfect skill. Use Camera2D + stretch settings.
Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when pixel art must stay crisp (integer scale, snap).

**When not to use:** tile painting → `blazium-tilemap`. Sprite filter only →
`blazium-sprites`.

## Workflow

1. **Inspect.** Window size, stretch mode, Camera2D zoom.
2. **Set** viewport stretch (`canvas_items` / integer) and texture filter nearest.
3. **Camera2D:** zoom that maps world pixels 1:1; enable snap when needed.
4. **Verify.** Autowork `assert_eq(cam.zoom, Vector2.ONE)` (or the integer zoom
   you chose) in play mode. Optional JustAMCP `editor_take_screenshot` is extra
   evidence — not the only check.
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
