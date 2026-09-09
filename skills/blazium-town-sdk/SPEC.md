---
name: blazium-town-sdk
pack: modules
---

# blazium-town-sdk

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

TownServer MMO client (`TownSDK` singleton) is a different backend from Blazium Services lobby.

## What

Auth/admin/chat over ENet via `TownSdkClient`.

**Non-goals:** Do not conflate with LobbyClient. Note deployed-flag / unpublished caveats.

## How

- Module: `blazium/modules/town_sdk/`. Singleton `TownSDK`.
- Decision: Town vs Services lobby.

## Reasoning

Platform skill. Distinct backend.

## Sources

- town_sdk

## Limits

Unpublished. Do not invent APIs. Do not load a skill until a `SKILL.md` exists. Verify against installed Blazium and https://docs.blazium.app.

## Related skills

- `blazium-lobby` — Services rooms
- `blazium-enet-server` — generic dedicated
