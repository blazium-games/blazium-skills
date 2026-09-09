---
name: blazium-gif
description: >
  Imports, plays, and records GIFs (GIFTexture, GIFRecorder,
  ResourceImporterGIF). Use for animated GIF assets or short captures. Not
  AtlasTexture and not JustAMCP screenshots.
---

# Blazium GIF

Import + playback + recorder — not a sprite atlas. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/gif/` — `GIFTexture`, `GIFRecorder`,
`ResourceImporterGIF`, `ResourceImporterGIFFrames`.

**No JustAMCP `gif_*` tools.** Still frames → JustAMCP screenshot.
Atlases / SpriteFrames workflows → `blazium-sprites`.

Settings: `blazium/gif/max_canvas_pixels` (16777216), `max_frames` (4096),
`capture_hotkey` (0), `capture_source` (Viewport=0, Window=1),
`capture_output_dir` (`user://`).

## When to use

- Use when importing `.gif`, playing `GIFTexture`, or recording a short clip.

**When not to use:** static AtlasTexture → `blazium-sprites`. Agent
screenshot → `blazium-mcp`. AnimationPlayer timelines →
`blazium-animation`.

## Workflow

1. **Inspect.** Existing `.gif` import mode (texture vs frames).
2. **Choose.** Playback vs record. Cap duration / `max_frames`.
3. **Implement.** Import or `GIFTexture.load_from_path`. Record:
   `start_*` → `stop` → `save` to `user://`.
4. **Verify.** Frame count / file exists. Autowork on a tiny clip.
5. **Handoff.** Path. Do not leave the recorder running.

## Patterns

### Import

- `ResourceImporterGIF` → `GIFTexture`
- `ResourceImporterGIFFrames` → `SpriteFrames`

Assign `GIFTexture` to Sprite2D / TextureRect like any Texture2D.
`resource_local_to_scene` is on by default so playback does not leak.

Playback members: `play`, `autoplay_on_load`, `loop`,
`netscape_loop_count`, `speed_scale`, `current_frame`. Helpers:
`load_from_path` / `load_from_buffer`, `save_to_path`, `bake_frames`,
`from_sprite_frames` / `to_sprite_frames`, `get_frame_count`.

### Recorder start / stop

```gdscript
var rec := GIFRecorder.new()
rec.max_frames = 48  # 0 falls back to blazium/gif/max_frames
rec.start_viewport(get_viewport())
# later
var tex: GIFTexture = rec.stop()
rec.save("user://clip.gif")
```

Also: `start_window`, `start_screen`, `add_frame`,
`GIFRecorder.record_viewport(viewport, path, duration_sec, fps)` for a
timed clip.

### Screenshot vs GIF

| Need | Tool |
|------|------|
| One still for the agent | JustAMCP screenshot |
| Short animated capture | `GIFRecorder` |
| Sprite sheet | `blazium-sprites` |

## Pitfalls

- **Recorded forever** → set `max_frames` or use `record_viewport` duration.
- **Wrote capture to `res://`** → default dir is `user://`.
- **Invented `gif_*` MCP tools** → none exist.
- **Replaced AtlasTexture with GIF for a static sheet** → sprites skill.

## Resources

- Tests: https://github.com/blazium-games/gif_module_tests

- `blazium/modules/gif/doc_classes/GIFTexture.xml`
- `GIFRecorder.xml`
- Settings: `blazium/gif/*`

## Related skills

- `blazium-sprites` — static atlases
- `blazium-mcp` — screenshots
- `blazium-project-config` — `blazium/gif/*`
- `blazium-animation` — AnimationPlayer
