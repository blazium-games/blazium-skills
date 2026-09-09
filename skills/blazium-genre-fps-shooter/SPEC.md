---
name: blazium-genre-fps-shooter
pack: growth
---

# blazium-genre-fps-shooter

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Genre on-ramp so agents compose engine pack skills instead of inventing a fps-shooter framework.

## What

Compose pinned Blazium skills: 3d, input, physics, navigation, multiplayer-core.

**Non-goals:** Do not fork a studio-clone skill pack.

## How

1. Compose the pinned Blazium skills (4.3.2 APIs).
2. Verify with Autowork.

## Reasoning

Compositional. Exists so the router can load a genre without 73 studio skills.

## Sources

- Pinned skills: 3d, input, physics, navigation, multiplayer-core

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-3d` — pin
- `blazium-input` — pin
- `blazium-physics` — pin
- `blazium-navigation` — pin
