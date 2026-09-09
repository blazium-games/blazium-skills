---
name: blazium-gif
pack: modules
---

# blazium-gif

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Import + runtime `GIFTexture` + `GIFRecorder` is easy to get wrong (memory, recording forever).

## What

`ResourceImporterGIF` / `GIFFrames`, playback, recorder start/stop. Settings `blazium/gif/*`.

**Non-goals:** Do not replace AtlasTexture (`blazium-sprites`) or MCP screenshots.

## How

- Module: `blazium/modules/gif/`.
- MCP screenshot vs GIF recorder decision.

## Reasoning

Distinct from static sprites and AnimationPlayer.

## Sources

- gif

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-sprites` — static atlases
- `blazium-mcp` — screenshots
