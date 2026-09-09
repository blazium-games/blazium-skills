---
name: blazium-game-feel
pack: growth
---

# blazium-game-feel

Juice with Tween / particles / camera punch. Engine baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents either skip feedback or rewrite the mover. This skill owns short
punches only.

## What

Hit-stop, squash, screenshake, particle bursts on 4.3.2 nodes.

**Non-goals:** CharacterBody controllers, AnimationTree libraries, shaders.

## How

1. Inspect who owns camera and velocity.
2. Add a short tween; restore offset / `time_scale`.
3. Verify with Autowork property asserts.

## Reasoning

Distinct from `blazium-2d-movement` (math) and `blazium-animation` (clips).

## Sources

- Blazium: `Tween`, `Camera2D`, particles (4.3.2)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-animation` — adjacent
- `blazium-2d-movement` — adjacent
- `blazium-ui` — adjacent
