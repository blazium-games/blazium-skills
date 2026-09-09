---
name: blazium-socketio
pack: modules
---

# blazium-socketio

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Socket.IO client handshake/`poll`/namespaces get lost inside the HTTPServer skill.

## What

Singleton `SocketIOClient`: `connect_to_url`, `close`, `poll`, `create_namespace`, `STATE_*`, signals `connected` / `namespace_connected`.

**Non-goals:** HTTPServer REST/SSE. A Socket.IO server. Editor remote_control.

## How

- Module: `blazium/modules/socketio/`
- Tests: https://github.com/blazium-games/socketio_module_tests
- Optional Node fixture: `external/socketio_node_server`
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

Realtime client is not in-game HTTP listen.

## Sources

- https://github.com/blazium-games/socketio_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-httpserver` — REST / SSE
