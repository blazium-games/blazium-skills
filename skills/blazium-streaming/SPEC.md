---
name: blazium-streaming
pack: modules
---

# blazium-streaming

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Twitch/Kick/IRC/OBS/CrowdControl are one streamer-game job on Blazium modules.

## What

Helix + Kick REST, Twitch IRC chat, OBS WebSocket 5.x, Crowd Control effect packs.

**Non-goals:** Do not create five skills. Do not own Discord (different platform).

## How

- twitchapi (14): `TwitchAPI`, `TwitchHTTPClient`, `TwitchChatRequests`.
- kickapi (11): `KickAPI`, `KickHTTPClient`, `KickChatRequests`.
- ircclient (9): `TwitchIRCClient`, `TwitchIRCClientNode`, `TwitchMessage`.
- obsclient: `OBSClient` (WebSocket 5.x).
- crowdcontrol (5): `CrowdControl`, `CrowdControlEffect`, `CrowdControlGamePack`.
- Tokens via `blazium-config` / user:// — never res://.

## Reasoning

Shared streamer loop: auth → chat command → game effect → OBS scene.

## Sources

- twitchapi
- kickapi
- ircclient
- obsclient
- crowdcontrol

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-config` — secrets
- `blazium-discord` — not this stack
