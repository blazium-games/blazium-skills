---
name: blazium-2d-movement
pack: engine
---

# blazium-2d-movement

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Platformer/top-down controllers are the default first game. Agents mix `MOTION_MODE_GROUNDED` with top-down walkers and treat coyote as an engine flag.

## What

`CharacterBody2D` + `move_and_slide()`, `MOTION_MODE_GROUNDED` (gravity + coyote float + `floor_snap_length`) vs `MOTION_MODE_FLOATING` (`Input.get_vector`, no gravity). Starter: `assets/player_body_2d.gd`. Verify with Autowork `simulate(..., SIMULATE_PHYSICS)`.

**Non-goals:** Do not own tilemaps, physics layer setup, InputMap bindings, or genre composition.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Choose grounded vs floating and state the assumption.
3. Prefer JustAMCP `physics_tools` / `input_tools` when the editor MCP is connected.
4. Set velocity in `_physics_process`; call `move_and_slide()`.
5. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `Godot CharacterBody2D (4.3.2)`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time. Genre kits compose this pin — they do not rewrite it.

## Sources

- Blazium: Godot CharacterBody2D (4.3.2)
- Asset: skills/blazium-2d-movement/assets/player_body_2d.gd
- Docs: https://docs.blazium.app

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks. Grok `code_execution` is not a physics stepper.

## Related skills

- `blazium-physics` — adjacent
- `blazium-tilemap` — adjacent
- `blazium-input` — adjacent
- `blazium-autowork` — adjacent
- `blazium-genre-platformer` — adjacent
- `blazium-game-feel` — adjacent
