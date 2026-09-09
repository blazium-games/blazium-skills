---
name: blazium-2d-movement
pack: engine
---

# blazium-2d-movement

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Platformer/top-down controllers are the default first game.

## What

CharacterBody2D + move_and_slide, slopes. Verify with Autowork simulate().

**Non-goals:** Do not own tilemaps or physics layer setup.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `Godot CharacterBody2D (4.3.2)`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: Godot CharacterBody2D (4.3.2)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-physics` — adjacent
- `blazium-tilemap` — adjacent
- `blazium-input` — adjacent
- `blazium-autowork` — adjacent
