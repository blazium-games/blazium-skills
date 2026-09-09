---
name: blazium-enet-webrtc
description: >
  Sets up Blazium ENet-over-WebRTC (WebRTCEnetSession, SignalClient) for NAT
  traversal. Not in the default editor — custom SCons, verify
  ClassDB.class_exists("WebRTCEnetSession"). Use when lobby peers need
  DataChannels or WSS relay. Not dedicated ENetServer.
---

# Blazium ENet over WebRTC

Transport for lobby NAT traversal. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Not in the default editor.** `blazium/modules/games_enet_webrtc/` uses
**custom SCons** and is **not** in default `modules_enabled.gen.h`. Verify
the installed build: if `ClassDB.class_exists("WebRTCEnetSession")` is
false, stop — do not invent a polyfill.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Add `WebRTCEnetSession` to the tree so it can poll. It returns a normal
`ENetMultiplayerPeer` via `get_peer()`. RPCs stay on `blazium-multiplayer-core`.

Vanilla `webrtc` (`WebRTCMultiplayerPeer`) is a note only — do not rewrite
Godot WebRTC peer docs here.

## When to use

- Use when peers cannot use LAN UDP and need signaling + DataChannel or relay.
- Use when assigning `get_peer()` after a Services or signal-server room.

**When not to use:** lobby policy / reconnect tokens → `blazium-lobby`.
`@rpc` / spawners → `blazium-multiplayer-core`. Dedicated threaded server +
RCON → `blazium-enet-server`. Module not compiled → say so; do not fake it.

## Workflow

1. **Inspect.** Confirm the module is in this editor. Signaling URL, `game_id`,
   auth token (JWT from `blazium-services` when required).
2. **Choose.** Native DataChannel (needs `WebRTCPeerConnection` / webrtc-native)
   vs WSS relay (`set_force_relay(true)` for tests / no native backend).
3. **Implement.** `configure` → `create_room` or `join_room` → await
   `session_ready` → `multiplayer.multiplayer_peer = session.get_peer()`.
4. **Verify.** Two instances (or `set_force_relay` in Autowork). Not a
   screenshot alone.
5. **Handoff.** Room code + peer assignment. RPC work → multiplayer-core.

## Patterns

### Configure, host, assign peer

```gdscript
var session: WebRTCEnetSession = $WebRTCEnetSession
var err: Error = session.configure(signal_url, game_id, auth_token)
if err != OK:
	push_error(err)
	return
session.session_ready.connect(func(_ip, _port, _code):
	multiplayer.multiplayer_peer = session.get_peer()
)
session.create_room("room", 8)
```

Join: `session.join_room(room_code, password, display_name)`.

`create_room(name, max_clients, password, hidden, tags)` — password,
`hidden`, and tags are proven in `games_enet_webrtc_module_tests`. Also:
`leave()`, `close()`, `seal()`, `kick(signal_id)`, `list_rooms()`,
`get_room_code()`, `get_local_fake_ip()`, `get_local_fake_port()`,
`get_local_signal_id()`, `is_in_room()`. Host `kick(self)` →
`ERR_INVALID_PARAMETER`. Non-host `kick()` / `seal()` →
`ERR_UNCONFIGURED`. Second `create_room` while in a room fails.

`SignalClient`: `configure(url, game_id, token)`, `connect_to_signal()`,
`poll()`, `is_open()`, `close()`. Session signals: `session_ready`,
`failed`, `rooms_listed`, `peer_link_up`, `peer_link_down`, `using_relay`.

Relay vs DataChannel: `set_force_relay(true)` skips ICE and sends ENet
datagrams on the signaling WebSocket. `using_relay` / `using_turn` are not
failures. ICE timeout: `set_ice_timeout_msec` (default 8000). Star
topology blocks joiner-to-joiner packets.

Signaling / TURN: blazium-signal, blazium-turn. Fake addresses live in
`10.66.0.0/16` (host `10.66.0.1`, joiners `.2` / `.3`). Live suite:
`SIGNAL_LIVE=1`, `SIGNAL_URL` default `ws://127.0.0.1:8080/v1/signal`.
Without a signal server, live checks skip (exit 0) unless `SIGNAL_LIVE=1`.

Signal HTTP (port 8080): `/healthz`, `/readyz`, `/metrics`, `/v1/ice`,
`/v1/rooms`. TURN `:3479` `/healthz`.

## Pitfalls

- **Assumed the module is in every build** → check ClassDB / SCons first.
- **Assigned `get_peer()` before `session_ready`** → peer is null.
- **Taught LobbyClient here** → `blazium-lobby`.
- **Rewrote vanilla WebRTCMultiplayerPeer** → note only; this skill is
  `WebRTCEnetSession`.

## Resources

- Tests: https://github.com/blazium-games/games_enet_webrtc_module_tests
- Tests: https://github.com/blazium-games/blazium-signal
- Tests: https://github.com/blazium-games/blazium-turn

- Module: `blazium/modules/games_enet_webrtc/`
- Classes: `WebRTCEnetSession`, `SignalClient`
- Live loop: companions `blazium-signal` / `blazium-turn`; set `SIGNAL_LIVE=1`
- JustAMCP: `networking_tools`, prompt `blazium_multiplayer_architect`
- Asset: `assets/webrtc_session.gd`

## Related skills

- `blazium-lobby` — rooms / tokens
- `blazium-multiplayer-core` — RPC after `get_peer()`
- `blazium-enet-server` — dedicated, not browser NAT
- `blazium-services` — auth token for `configure`
