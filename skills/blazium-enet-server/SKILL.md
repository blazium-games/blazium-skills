---
name: blazium-enet-server
description: >
  Runs Blazium’s threaded ENetServer / ENetClient singletons. Use for
  dedicated servers and Variant packets. RCON admin → blazium-rcon. Not
  SceneMultiplayer RPC and not lobby matchmaking.
---

# Blazium ENet Server

Threaded dedicated-server singletons. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. RCON → `blazium-rcon`.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/enet_server/` (`ENetServer`, `ENetServerPeer`,
`ENetClient`, `ENetPacketUtils`).

Vanilla `ENetMultiplayerPeer` + `@rpc` stays on `blazium-multiplayer-core`.
Do not rewrite those docs here.

## When to use

- Use when you need a background-thread ENet singleton, Variant packets, or
  auth hooks instead of SceneMultiplayer.
**When not to use:** Source/BattlEye RCON → `blazium-rcon`. In-game `@rpc`
/ Spawner / Synchronizer → `blazium-multiplayer-core`. Matchmaking rooms →
`blazium-lobby`. HTTP/SSE admin → `blazium-httpserver`. Full export
pipeline → `blazium-export`.

## Workflow

1. **Inspect.** Dedicated vs listen-server. `ClassDB.class_exists("ENetServer")`.
2. **Choose.** `ENetServer`/`ENetClient` singletons vs `ENetMultiplayerPeer`.
   Prefer SceneMultiplayer when you want Godot RPC/replication.
3. **Implement.** `ENetServer.create_server(port, max_peers, max_channels)`.
   Client: `ENetClient.connect_to_server(address, port, channels)`.
4. **Verify.** Headless dedicated + one client, or Autowork with localhost
   (`enetserver_module_tests`). Two processes beat a screenshot.
5. **Handoff.** Ports, auth mode. RCON → `blazium-rcon`. Scene RPC →
   multiplayer-core.

## Patterns

### Server / client happy path

```gdscript
ENetServer.peer_authenticated.connect(_on_auth)
ENetServer.packet_received.connect(_on_packet)
ENetServer.create_server(7777, 32, 2)

func _on_auth(peer: ENetServerPeer) -> void:
	ENetServer.send_packet(peer.peer_id, {"type": "welcome"}, 0, true)
```

```gdscript
ENetClient.connected_to_server.connect(_on_connected)
ENetClient.connect_to_server("127.0.0.1", 7777, 2)
ENetClient.send_packet({"type": "login", "username": "P1"}, 0, true)
```

### When vs SceneMultiplayer

| Need | Use |
|------|-----|
| `@rpc`, MultiplayerSpawner/Synchronizer | `blazium-multiplayer-core` |
| Threaded Variant packets, custom auth | `ENetServer` / `ENetClient` |
| Browser NAT / DataChannels | `blazium-enet-webrtc` |

Headless dedicated: export with `dedicated_server` (`blazium-export` owns templates).

## Pitfalls

- **Used ENetServer for lobby rooms** → `blazium-lobby`.
- **Expected `@rpc` on ENetServer packets** → different stack; use
  SceneMultiplayer or map packets yourself.
- **Taught RCON here** → `blazium-rcon`.

## Resources

- `blazium/modules/enet_server/doc_classes/ENetServer.xml`
- Tests: https://github.com/blazium-games/enetserver_module_tests
- JustAMCP: `networking_tools`
- Asset: `assets/enet_server_boot.gd`

## Related skills

- `blazium-rcon` — Source / BattlEye admin
- `blazium-multiplayer-core` — in-game RPC
- `blazium-lobby` — player sessions
- `blazium-enet-webrtc` — NAT / relay
- `blazium-httpserver` — HTTP admin
