---
name: blazium-genre-puzzle
pack: growth
---

# blazium-genre-puzzle

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Genre on-ramp so agents compose engine pack skills instead of inventing a puzzle framework.

## What

Compose pinned Blazium skills: ui, input, tilemap, autowork.

**Non-goals:** Do not fork a studio-clone skill pack.

## How

1. Compose the pinned Blazium skills (4.8.x APIs).
2. Verify with Autowork.

## Reasoning

Compositional. Exists so the router can load a genre without 73 studio skills.

## Sources

- Pinned skills: ui, input, tilemap, autowork

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-ui` — pin
- `blazium-input` — pin
- `blazium-tilemap` — pin
- `blazium-autowork` — pin
