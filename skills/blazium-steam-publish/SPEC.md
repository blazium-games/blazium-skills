---
name: blazium-steam-publish
pack: growth
---

# blazium-steam-publish

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Shipping to Steam is not the same as Steamworks runtime JWT.

## What

SteamPipe / steamcmd depot upload after `blazium-export`.

**Non-goals:** Do not re-teach `authenticate_with_server`.

## How

Build with `blazium-export` / `blazium-ci-export`. Upload with steamcmd and `app_build_*.vdf`. App ID comes from the user.

## Reasoning

Publish vs runtime split.

## Sources

- `blazium-steam`
- `blazium-export`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-steam` — runtime
- `blazium-export` — builds
