---
name: blazium-rcon
pack: live-ops
---

# blazium-rcon

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

RCON admin is a distinct poll/protocol surface from ENet gameplay packets.

## What

`RCONServer.start_server` / `RCONClient.connect_to_server` with `PROTOCOL_SOURCE` or `PROTOCOL_BATTLEYE`. Both sides `poll()`. `command_received` → `send_response`.

**Non-goals:** `ENetServer` packets (`blazium-enet-server`). HTTP/SSE (`blazium-httpserver`).

## How

- Module: `blazium/modules/rcon/`
- Tests: https://github.com/blazium-games/rcon_module_tests
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

Dedicated-server admin should not hide behind the ENet singleton skill.

## Sources

- https://github.com/blazium-games/rcon_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-enet-server` — gameplay ENet
- `blazium-httpserver` — HTTP admin
