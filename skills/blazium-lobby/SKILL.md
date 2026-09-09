---
name: blazium-lobby
description: >
  Implements Blazium matchmaking rooms (LobbyClient / ScriptedLobbyClient,
  reconnect tokens). Use after a JWT from blazium-services when creating,
  joining, leaving, or reconnecting to rooms. Not raw @rpc or WebRTC transport.
---

# Blazium Lobby

Session layer after JWT — not transport. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Nightly caveat:** `LoginClient` / `LobbyClient` / `MasterServerClient` are
script templates and https://docs.blazium.app — not C++/xml class docs in the installed editor. Copy
only template methods. Do not invent APIs. Verify against the installed nightly.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

JustAMCP prompt `blazium_multiplayer_architect` can plan netcode; stay on this
skill for rooms. After a room exists, assign peers via `blazium-enet-webrtc`
or vanilla ENet (`blazium-multiplayer-core`).

## When to use

- Use when creating, joining, leaving, or reconnecting to a Services lobby.
- Use when persisting `reconnection_token` in `user://blazium.cfg`.

**When not to use:** JWT / login → `blazium-services` first. Raw `@rpc` /
Spawner → `blazium-multiplayer-core`. `WebRTCEnetSession` internals →
`blazium-enet-webrtc`. Dedicated singleton + RCON → `blazium-enet-server`.

## Workflow

1. **Inspect.** Confirm JWT exists. Open
   `script_templates/LobbyClient/` and `ScriptedLobbyClient/`.
2. **Choose.** `LobbyClient` for standard rooms; `ScriptedLobbyClient` when
   the template’s scripted variant is required. Verify nightly class names.
3. **Implement.** Load/save `reconnection_token` under the matching
   ConfigFile section. `connect_to_server()`; handle
   `connected_to_server` / `disconnected_from_server`.
4. **Verify.** Disconnect + reconnect with the saved token. Two clients or
   play-mode MCP — not a screenshot.
5. **Handoff.** Room id / reconnect token. Name the transport skill next.

## Patterns

### Reconnect token (from official template)

```gdscript
config = ConfigFile.new()
config.load("user://blazium.cfg")
reconnection_token = config.get_value("LobbyClient", "reconnection_token", "")
disconnected_from_server.connect(_disconnected_from_server)
connected_to_server.connect(_connected_to_server)
connect_to_server()

func _connected_to_server(_peer: LobbyPeer, new_reconnection_token: String) -> void:
	config.set_value("LobbyClient", "reconnection_token", new_reconnection_token)
	config.save("user://blazium.cfg")
```

`ScriptedLobbyClient` uses section `"ScriptedLobbyClient"` instead.

Backoff on disconnect (template): cap retries, clear token on
`"Reconnect Close"`, then `connect_to_server()` again.

## Pitfalls

- **Invented LobbyClient methods** → template + nightly only.
- **Taught `@rpc` here** → hand off to `blazium-multiplayer-core`.
- **Configured `WebRTCEnetSession` here** → `blazium-enet-webrtc`.
- **Skipped JWT** → `blazium-services` first.

## Resources

- Nightly check: [references/verify-nightly.md](references/verify-nightly.md)
- Templates: `script_templates/LobbyClient/default.gd`,
  `script_templates/ScriptedLobbyClient/default.gd`
- Docs: https://docs.blazium.app (verify nightly)
- Sample game: https://github.com/blazium-games/example-game-hangman
- JustAMCP: `networking_tools`, prompt `blazium_multiplayer_architect`

## Related skills

- `blazium-services` — JWT first
- `blazium-enet-webrtc` — NAT traversal transport
- `blazium-multiplayer-core` — RPC after peers exist
- `blazium-enet-server` — dedicated server, not matchmaking
