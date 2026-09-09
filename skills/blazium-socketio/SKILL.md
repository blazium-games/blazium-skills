---
name: blazium-socketio
description: >
  Connects the in-engine SocketIOClient singleton (Engine.IO 4, namespaces,
  poll()). Use for Socket.IO clients inside a Blazium game. Not HTTPServer
  REST/SSE and not a Socket.IO server.
---

# Blazium Socket.IO

In-engine **client**. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Module: `blazium/modules/socketio/` — singleton `SocketIOClient`,
`SocketIONamespace`.

REST/SSE → `blazium-httpserver`. Gameplay ENet → `blazium-enet-server` /
`blazium-multiplayer-core`.

**`poll()` every frame** or the handshake never finishes.

## When to use

- Use when the game is a Socket.IO **client** (events, namespaces).

**When not to use:** in-game HTTP listen → `blazium-httpserver`. Editor
`/v1` → `blazium-cli-remote`.

## Workflow

1. **Inspect.** `ClassDB.class_exists("SocketIOClient")`. Target URL.
2. **Choose.** Root `/` vs extra namespaces. Auth dict if the server needs it.
3. **Implement.** `connect_to_url` then `poll()`. Create namespaces before
   or after connect as the server requires.
4. **Verify.** Autowork in `socketio_module_tests` (mock TCP or Node fixture
   `external/socketio_node_server`).
5. **Handoff.** URL + namespace paths. REST stays on `blazium-httpserver`.

## Patterns

```gdscript
SocketIOClient.close()
assert_eq(SocketIOClient.get_connection_state(), SocketIOClient.STATE_DISCONNECTED)
assert_false(SocketIOClient.is_socket_connected())

var chat := SocketIOClient.create_namespace("/chat")
assert_true(SocketIOClient.has_namespace("/chat"))
assert_eq(SocketIOClient.get_namespace("/chat"), chat)

var err := SocketIOClient.connect_to_url("ws://127.0.0.1:9091")
# optional: connect_to_url(url, auth, tls_options)
assert_eq(err, OK)
assert_eq(SocketIOClient.get_connection_state(), SocketIOClient.STATE_CONNECTING)
# _process:
SocketIOClient.poll()
```

Signals: `connected(session_id)`, `namespace_connected(namespace_path)`.
Also: `get_engine_io_session_id()`, `get_connection_url()`,
`SocketIONamespace.get_namespace_path()`.

Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd` in
https://github.com/blazium-games/socketio_module_tests

## Pitfalls

- **Forgot `poll()`** → stays CONNECTING.
- **Taught this as a Socket.IO server** → client only.
- **Replaced HTTPServer routes with Socket.IO** → different skill.

## Resources

- Tests: https://github.com/blazium-games/socketio_module_tests
- `blazium/modules/socketio/doc_classes/SocketIOClient.xml`

## Related skills

- `blazium-httpserver` — REST / SSE
- `blazium-cli-remote` — editor HTTP `/v1`
- `blazium-config` — URLs / tokens
