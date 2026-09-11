---
name: blazium-multiplayer-core
pack: engine
---

# blazium-multiplayer-core

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Godot ENet/RPC must stay separate from lobby/WebRTC/ENetServer or agents mix stacks.

## What

`ENetMultiplayerPeer` `create_server` / `create_client`, `@rpc` annotations, authority, `MultiplayerSpawner` / `MultiplayerSynchronizer`. Vanilla webrtc/websocket peers only as notes. JustAMCP `networking_setup_multiplayer`, `networking_setup_rpc`, `networking_setup_sync`.

**Non-goals:** Do not teach LobbyClient, WebRTCEnetSession, or ENetServer here.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern (peer, then `@rpc`, then spawn/sync).
4. Verify with two instances, Autowork mocked peers, or play-mode MCP — not screenshots alone.

Engine / module path: `blazium/modules/multiplayer/ + enet`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/multiplayer/ + enet
- Docs: https://docs.blazium.app

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks. Grok `code_execution` is not multiplayer evidence.

## Related skills

- `blazium-lobby` — adjacent
- `blazium-enet-webrtc` — adjacent
- `blazium-enet-server` — adjacent
- `blazium-services` — adjacent
