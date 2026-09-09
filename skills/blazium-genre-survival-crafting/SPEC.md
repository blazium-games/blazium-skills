---
name: blazium-genre-survival-crafting
pack: growth
---

# blazium-genre-survival-crafting

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Genre on-ramp so agents compose engine pack skills instead of inventing a survival-crafting framework.

## What

Compose pinned Blazium skills: resources, sqlite, 3d.

**Non-goals:** Do not fork a studio-clone skill pack.

## How

1. Compose the pinned Blazium skills (4.3.2 APIs).
2. Verify with Autowork.

## Reasoning

Compositional. Exists so the router can load a genre without 73 studio skills.

## Sources

- Pinned skills: resources, sqlite, 3d

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-resources` — pin
- `blazium-sqlite` — pin
- `blazium-3d` — pin
