---
name: blazium-multiplayer-core
description: >
  Implements Godot-style ENet multiplayer (@rpc, authority,
  MultiplayerSpawner/Synchronizer) on Blazium 0.6.x. Use for peer RPC and
  replication only. Lobby, WebRTC-ENet, and ENetServer are other skills.
---

# Blazium multiplayer core

Vanilla ENet + scene replication. **Do not** teach LobbyClient,
`WebRTCEnetSession`, or `ENetServer` here.

JustAMCP: `networking_setup_multiplayer`, `networking_setup_rpc`,
`networking_setup_sync`. Prompt: `blazium_multiplayer_architect` (then stay
on this skill for ENet/RPC only).

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding `@rpc`, peer authority, spawners, or synchronizers.

**When not to use:** matchmaking → `blazium-lobby`. Browser NAT →
`blazium-enet-webrtc`. Dedicated singleton + RCON → `blazium-enet-server`.

## Workflow

1. **Inspect.** `multiplayer` peer, authority, existing RPCs.
2. **Peer.** `ENetMultiplayerPeer` host/join (4.3.2 API).
3. **Replicate.** `@rpc` + Spawner/Synchronizer — not custom streams first.
4. **Verify.** Two instances or Autowork with mocked peers if present.
5. **Handoff.** Ports + authority rules. Lobbies / WebRTC / dedicated → those skills.

## Patterns

```gdscript
@rpc("any_peer", "reliable")
func request_action() -> void:
	if not is_multiplayer_authority():
		return
```

## Pitfalls

- **Mixed lobby tokens into ENet peer setup** → `blazium-lobby`.
- **Trusted client RPCs** → validate on authority.
- **Copied Godot 3 `rpc_id` strings only** → 4.x `@rpc` annotations.

## Resources

- JustAMCP: `networking_tools`

## Related skills

- `blazium-lobby` — rooms
- `blazium-enet-webrtc` — WebRTC transport
- `blazium-enet-server` — dedicated
- `blazium-signals-groups` — local events
