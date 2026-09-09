---
name: blazium-genre-tower-defense
pack: growth
---

# blazium-genre-tower-defense

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Genre on-ramp so agents compose engine pack skills instead of inventing a tower-defense framework.

## What

Compose pinned Blazium skills: navigation, tilemap, resources, ui.

**Non-goals:** Do not fork a studio-clone skill pack.

## How

1. Compose the pinned Blazium skills (4.3.2 APIs).
2. Verify with Autowork.

## Reasoning

Compositional. Exists so the router can load a genre without 73 studio skills.

## Sources

- Pinned skills: navigation, tilemap, resources, ui

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-navigation` — pin
- `blazium-tilemap` — pin
- `blazium-resources` — pin
- `blazium-ui` — pin
