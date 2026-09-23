---
name: blazium-lobby
pack: live-ops
---

# blazium-lobby

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Agents need a room/reconnect path after JWT. LobbyClient templates own that surface.

## What

Matchmaking rooms, reconnect tokens, ScriptedLobbyClient patterns. After JWT from `blazium-services`.

**Non-goals:** Do not teach raw @rpc (multiplayer-core). Do not teach WebRTCEnetSession internals (enet-webrtc).

## How

- Templates: LobbyClient, ScriptedLobbyClient.
- Reconnect tokens in `user://blazium.cfg`.
- Same checkout caveat as services: verify classes against nightly + docs.blazium.app.
- After a room exists, assign peers via `blazium-enet-webrtc` or vanilla ENet (`blazium-multiplayer-core`).

## Reasoning

Session layer, not transport.

## Sources

- Blazium: script_templates + docs.blazium.app

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-services` — JWT first
- `blazium-enet-webrtc` — NAT traversal transport
- `blazium-multiplayer-core` — RPC after peers exist
