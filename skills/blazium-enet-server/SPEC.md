---
name: blazium-enet-server
pack: live-ops
---

# blazium-enet-server

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-rcon` — Source / BattlEye admin
- `blazium-multiplayer-core` — in-game RPC
- `blazium-lobby` — player sessions
- `blazium-httpserver` — HTTP admin
