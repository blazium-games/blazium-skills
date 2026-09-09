---
name: blazium-genre-platformer
pack: growth
---

# blazium-genre-platformer

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Genre on-ramp so agents compose engine pack skills instead of inventing a platformer framework.

## What

Compose pinned Blazium skills: 2d-movement, tilemap, physics, input, pixel-perfect, autowork.

**Non-goals:** Do not fork a studio-clone skill pack.

## How

1. Compose the pinned Blazium skills (4.3.2 APIs).
2. Verify with Autowork.

## Reasoning

Compositional. Exists so the router can load a genre without 73 studio skills.

## Sources

- Pinned skills: 2d-movement, tilemap, physics, input, pixel-perfect, autowork

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-2d-movement` — pin
- `blazium-tilemap` — pin
- `blazium-physics` — pin
- `blazium-input` — pin
