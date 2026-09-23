---
name: blazium-steam-publish
pack: growth
---

# blazium-steam-publish

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-steam` — runtime
- `blazium-export` — builds
