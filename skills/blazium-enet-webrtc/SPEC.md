---
name: blazium-enet-webrtc
pack: live-ops
---

# blazium-enet-webrtc

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

ENet over WebRTC DataChannels with signaling is Blazium-specific and optional at build time.

## What

`WebRTCEnetSession`, `SignalClient`. create_room / join. Assign `get_peer()` to MultiplayerAPI.

**Non-goals:** Do not assume the module is in default `modules_enabled.gen.h`. Do not rewrite Godot WebRTC peer docs.

## How

- Module: `blazium/modules/games_enet_webrtc/` — **custom SCons**, not default.
- Signaling URL + game_id + auth token. Relay vs native DataChannel tradeoffs.
- Related infra: blazium-signal, blazium-turn (class docs).
- Vanilla `webrtc` module folds here as a note only.

## Reasoning

Transport for lobby NAT traversal. Distinct from lobby policy and from ENetServer.

## Sources

- Blazium: games_enet_webrtc

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-lobby` — rooms
- `blazium-multiplayer-core` — RPC
- `blazium-enet-server` — dedicated server, not browser NAT
