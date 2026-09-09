---
name: blazium-httpserver
pack: modules
---

# blazium-httpserver

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

In-engine REST + SSE underpins custom backends inside the game.

## What

`HTTPServer`, `HTTPRequestContext`, `HTTPResponse`, `SSEConnection`. JSON-RPC folds here.

**Non-goals:** Socket.IO client (`blazium-socketio`). Editor `remote_control`. JustAMCP.

## How

- Module: `blazium/modules/httpserver/`
- Tests: https://github.com/blazium-games/httpserver_module_tests
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

In-game HTTP listen is not editor remote and not Socket.IO.

## Sources

- https://github.com/blazium-games/httpserver_module_tests
- `blazium/modules/httpserver/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-socketio` — Socket.IO client
- `blazium-cli-remote` — editor HTTP
- `blazium-mcp` — agent MCP
- `blazium-enet-server` — gameplay server
