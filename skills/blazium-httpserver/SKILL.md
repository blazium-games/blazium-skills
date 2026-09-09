---
name: blazium-httpserver
description: >
  Ships an in-game HTTP REST + SSE server (HTTPServer singleton) and JSON-RPC.
  Use for custom backends inside the game. Socket.IO client → blazium-socketio.
  Not editor remote_control or JustAMCP.
---

# Blazium HTTPServer

In-game REST + SSE — not editor MCP. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/httpserver/` — singleton `HTTPServer`,
`HTTPRequestContext`, `HTTPResponse`, `SSEConnection`.

JSON-RPC folds here (`JSONRPC`). Socket.IO client → `blazium-socketio`.
WebSocket peers for gameplay stay `blazium-multiplayer-core`.

## When to use

- Use when the **game** should listen for HTTP/SSE (admin, overlays, local
  tools).
- Use when folding JSON-RPC into an HTTP route.

**When not to use:** Socket.IO client → `blazium-socketio`. Editor HTTP
`/v1` → `blazium-cli-remote`. Agent MCP → `blazium-mcp`. Gameplay
dedicated server → `blazium-enet-server`.

## Workflow

1. **Inspect.** Port conflict with remote_control (6508) or game MCP (6507).
   Tokens via `blazium-config`.
2. **Choose.** REST vs SSE vs JSON-RPC (Socket.IO → `blazium-socketio`).
3. **Implement.** `HTTPServer.listen` + `register_route`. Bind loopback
   unless the user asked otherwise.
4. **Verify.** `curl` / Autowork against the route. `is_listening()`.
5. **Handoff.** Port + routes. Do not claim this is JustAMCP.

## Patterns

### Hello route + SSE

```gdscript
HTTPServer.listen(8080, "127.0.0.1")
HTTPServer.register_route("GET", "/api/health", func(req, res):
	res.set_json({"ok": true})
)
HTTPServer.register_route("GET", "/api/events", func(req, res):
	res.start_sse()
)
# later: HTTPServer.send_sse_event(id, "tick", "{}")
```

`HTTPRequestContext`: `get_path_param`, `get_query_param`, `get_header`,
`parse_json_body`, `parse_form_data`. Path params: `/api/users/{id}`.

Also: `set_static_directory`, `enable_directory_listing`,
`set_cors_enabled` / `set_cors_origin`, `set_max_request_size`,
`complete_response`, `stop`, `clear_routes`.

### JSON-RPC (subsection)

`JSONRPC.new()` → `set_scope` / `process_action` / `process_string`. Wire
through an `HTTPServer` POST route. ErrorCode: `PARSE_ERROR`,
`INVALID_REQUEST`, `METHOD_NOT_FOUND`, `INVALID_PARAMS`, `INTERNAL_ERROR`.

### When-to-use table

| Need | Skill |
|------|-------|
| In-game REST / SSE / static | this skill |
| Socket.IO client | `blazium-socketio` |
| Editor `/v1` remote | `blazium-cli-remote` |
| Agent tools | `blazium-mcp` |
| Gameplay ENet | `blazium-enet-server` |
| RCON admin | `blazium-rcon` |

## Pitfalls

- **Bound `0.0.0.0` without asking** → loopback default.
- **Replaced remote_control with HTTPServer** → wrong layer.
- **Taught Socket.IO here** → `blazium-socketio`.

## Resources

- `blazium/modules/httpserver/doc_classes/HTTPServer.xml`
- Tests: https://github.com/blazium-games/httpserver_module_tests

## Related skills

- `blazium-socketio` — Socket.IO client
- `blazium-cli-remote` — editor HTTP
- `blazium-mcp` — agent MCP
- `blazium-enet-server` — gameplay server
- `blazium-rcon` — RCON admin
- `blazium-config` — ports / tokens
