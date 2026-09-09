---
name: blazium-enet-server
pack: live-ops
---

# blazium-enet-server

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Blazium ships a threaded ENet server singleton. Vanilla ENet peers stay on `blazium-multiplayer-core`.

## What

`ENetServer`, `ENetServerPeer`, `ENetClient`. Headless dedicated export.

**Non-goals:** RCON (`blazium-rcon`). Vanilla `ENetMultiplayerPeer`. Lobby matchmaking.

## How

- Module: `blazium/modules/enet_server/`
- Tests: https://github.com/blazium-games/enetserver_module_tests
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

Dedicated gameplay packets are not RCON and not SceneMultiplayer RPC.

## Sources

- https://github.com/blazium-games/enetserver_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-rcon` — Source / BattlEye admin
- `blazium-multiplayer-core` — in-game RPC
- `blazium-lobby` — player sessions
- `blazium-httpserver` — HTTP admin
