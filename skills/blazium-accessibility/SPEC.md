---
name: blazium-accessibility
pack: growth
---

# blazium-accessibility

Remaps, font scale, locale-safe copy. Engine baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents ship English-only HUDs with fixed binds. This skill is the a11y pass.

## What

InputMap remaps, Theme scale, `tr()`, persist settings under `user://`.

**Non-goals:** Art bible, inventing TTS, owning InputMap from scratch.

## How

1. Inspect actions and Theme.
2. Rebind + scale + localize.
3. Verify with Autowork on `InputMap` and font size.

## Reasoning

Distinct from `blazium-input` (map setup) and `blazium-ui` (chrome).

## Sources

- Blazium: `InputMap`, `Theme`, `tr()` (4.3.2)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-input` — adjacent
- `blazium-ui` — adjacent
- `blazium-localization` — adjacent
