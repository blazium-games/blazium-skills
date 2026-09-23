---
name: blazium-steam
pack: live-ops
---

# blazium-steam

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

This is not GodotSteam. Native Steamworks plus session tickets exchanged for Blazium JWT.

## What

Achievements, stats, inventory, `authenticate_with_server` ticket → JWT.

**Non-goals:** Do not teach SteamPipe publishing (`blazium-steam-publish`). Do not use community GodotSteam APIs.

## How

- Module: `blazium/modules/steam/` class `Steam`.
- Ticket request → backend auth URL → JWT (`blazium-services`).
- Promo items / inventory as documented on the class.

## Reasoning

Identity + Steamworks runtime. Publishing is a growth pack adapter.

## Sources

- Blazium: steam module (not GodotSteam)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-services` — JWT
- `blazium-steam-publish` — depots / steamcmd
