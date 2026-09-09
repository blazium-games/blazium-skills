---
name: blazium-rcon
description: >
  Runs Source and BattlEye RCON (RCONServer / RCONClient / RCONPacket) with
  required poll(). Use for dedicated-server admin. Not ENet gameplay packets
  and not HTTP/SSE admin.
---

# Blazium RCON

Source / BattlEye admin channel. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**.

Module: `blazium/modules/rcon/` — `RCONServer`, `RCONClient`, `RCONPacket`.

Dedicated gameplay packets → `blazium-enet-server`. HTTP admin →
`blazium-httpserver`.

RCON is editor + `dedicated_server` on Windows/Linux. Check
`ClassDB.class_exists("RCONServer")`.

Both sides **must `poll()`**.

## When to use

- Use when adding Source or BattlEye RCON admin to a dedicated server.

**When not to use:** `ENetServer` / `ENetClient` packets →
`blazium-enet-server`. In-game `@rpc` → `blazium-multiplayer-core`.

## Workflow

1. **Inspect.** `ClassDB.class_exists("RCONServer")`. Port free?
2. **Choose.** `PROTOCOL_SOURCE` (27015-style) or `PROTOCOL_BATTLEYE`.
3. **Implement.** `start_server` + `poll` every frame. Client:
   `connect_to_server` + `poll`.
4. **Verify.** Autowork localhost as in `rcon_module_tests`.
5. **Handoff.** Bind + protocol. Gameplay ENet stays on `blazium-enet-server`.

## Patterns

### Source

```gdscript
var server := RCONServer.new()
var client := RCONClient.new()
server.server_started.connect(func(): pass)
server.command_received.connect(func(client_id, command, request_id):
	server.send_response(client_id, request_id, "Response received: " + command)
)
server.start_server(27015, "testpass", RCONServer.PROTOCOL_SOURCE)
client.connect_to_server("127.0.0.1", 27015, "testpass", RCONClient.PROTOCOL_SOURCE)
# _process:
server.poll()
client.poll()
client.send_command("test_command hello")
```

Signals: `server_started`, `command_received` (server);
`connected`, `authenticated`, `command_response` (client).
`server.is_running()`. Stop: `stop_server` / `disconnect_from_server`.

### BattlEye

Same API with port **2302** and `PROTOCOL_BATTLEYE` /
`RCONClient.PROTOCOL_BATTLEYE`. Tests use `send_command("say welcome")`.

Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd` in
https://github.com/blazium-games/rcon_module_tests

## Pitfalls

- **Forgot `poll()`** → start/auth/commands never finish.
- **Assumed RCON in every export template** → check `ClassDB` +
  `dedicated_server`.
- **Taught ENet packets here** → `blazium-enet-server`.

## Resources

- Tests: https://github.com/blazium-games/rcon_module_tests
- `blazium/modules/rcon/doc_classes/RCONServer.xml`

## Related skills

- `blazium-enet-server` — dedicated ENet singletons
- `blazium-httpserver` — HTTP admin
- `blazium-export` — dedicated_server templates
