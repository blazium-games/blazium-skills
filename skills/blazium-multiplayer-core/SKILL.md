---
name: blazium-multiplayer-core
description: >
  Implements Godot-style ENet multiplayer on Blazium 0.6.x / Godot 4.3.2:
  ENetMultiplayerPeer host/join, @rpc annotations, multiplayer authority,
  MultiplayerSpawner and MultiplayerSynchronizer. Use for peer RPC and
  scene replication only. Not LobbyClient, not WebRTCEnetSession, not
  ENetServer. Prefer JustAMCP networking_setup_multiplayer /
  networking_setup_rpc / networking_setup_sync.
when-to-use: >
  ENetMultiplayerPeer, @rpc, multiplayer authority, MultiplayerSpawner,
  MultiplayerSynchronizer, create_server, create_client, peer RPC,
  networking_setup_rpc
metadata:
  author: blazium-games
  short-description: ENet peer, @rpc, authority, and scene replication
---

# Blazium multiplayer core

Vanilla ENet + scene replication. **Do not** teach LobbyClient,
`WebRTCEnetSession`, or `ENetServer` here.

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not copy Godot 3
`rpc_id("name")` strings as the only RPC path. Do not apply Godot
4.7-only calls.

JustAMCP: `networking_setup_multiplayer`, `networking_setup_rpc`,
`networking_setup_sync`. Prompt: `blazium_multiplayer_architect` (then stay
on this skill for ENet/RPC only).

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding `@rpc`, peer authority, spawners, or synchronizers.
- Use when two editor/game instances must exchange ENet RPCs.

**When not to use:** matchmaking / rooms / reconnect tokens →
`blazium-lobby`. Browser NAT / `WebRTCEnetSession` → `blazium-enet-webrtc`.
Dedicated singleton + RCON → `blazium-enet-server`. JWT / login →
`blazium-services`. Local signals only → `blazium-signals-groups`.

## Grok host

Load this file plus at most one pin (`blazium-lobby` only after peers
exist, or `blazium-enet-webrtc` when the transport is WebRTC). Spawn
`network-programmer` for peer/`@rpc` and `qa-tester` for a two-peer
check. Child prompts must include listen port, authority rules, and
whether JustAMCP `:6506` is connected. Do not dump the catalog.

Grok `code_execution` and a screenshot of the Multiplayer debugger are
not evidence. Quote JustAMCP `networking_setup_*`, two-instance play-mode
MCP, Autowork with mocked peers if present, or `INCONCLUSIVE`.

## Workflow

1. **Inspect.** `multiplayer.multiplayer_peer`, existing `@rpc`, spawners.
2. **Peer.** `ENetMultiplayerPeer` `create_server` / `create_client`
   (4.3.2 API). Assign `multiplayer.multiplayer_peer`.
3. **Replicate.** `@rpc` + `MultiplayerSpawner` / `MultiplayerSynchronizer`
   — not custom streams first.
4. **Verify.** Two instances or Autowork with mocked peers if present.
5. **Handoff.** Ports + authority rules. Lobbies / WebRTC / dedicated →
   those skills.

## Patterns

### Host / join (4.3.2)

```gdscript
func host_game(port: int) -> Error:
	var peer := ENetMultiplayerPeer.new()
	var err := peer.create_server(port)
	if err != OK:
		return err
	multiplayer.multiplayer_peer = peer
	return OK

func join_game(address: String, port: int) -> Error:
	var peer := ENetMultiplayerPeer.new()
	var err := peer.create_client(address, port)
	if err != OK:
		return err
	multiplayer.multiplayer_peer = peer
	return OK
```

### Authority RPC

```gdscript
@rpc("any_peer", "reliable")
func request_action() -> void:
	if not is_multiplayer_authority():
		return
	_apply_action.rpc()

@rpc("authority", "call_local", "reliable")
func _apply_action() -> void:
	pass
```

Validate on the authority. Do not trust a client-only `@rpc` to mutate
sim state.

`MultiplayerSpawner` spawn paths must be in the spawnable list.
`MultiplayerSynchronizer` replication config lists the properties — do
not invent a custom bitstream first.

## Output contract

- Listen address / port and host vs client
- Authority rules (`is_multiplayer_authority` / `set_multiplayer_authority`)
- `@rpc` names and modes (`any_peer` / `authority`, reliable, call_local)
- Spawner / Synchronizer node paths if used
- Evidence: JustAMCP `networking_setup_*`, two-instance check, or
  `INCONCLUSIVE`
- Next skill (`blazium-lobby`, `blazium-enet-webrtc`, `blazium-enet-server`)

## Pitfalls

- **Mixed lobby tokens into ENet peer setup** → `blazium-lobby`.
- **Trusted client RPCs** → validate on authority.
- **Copied Godot 3 `rpc_id` strings only** → 4.x `@rpc` annotations.
- **Configured `WebRTCEnetSession` here** → `blazium-enet-webrtc`.
- **Opened RCON / dedicated singleton here** → `blazium-enet-server`.
- **No second instance** → report `INCONCLUSIVE`; do not claim replication works.

## Resources

- JustAMCP: `networking_tools` (`networking_setup_multiplayer`,
  `networking_setup_rpc`, `networking_setup_sync`)
- Docs: https://docs.blazium.app (MultiplayerAPI, 4.3.2-safe)

## Related skills

- `blazium-lobby` — rooms
- `blazium-enet-webrtc` — WebRTC transport
- `blazium-enet-server` — dedicated
- `blazium-signals-groups` — local events
- `blazium-services` — JWT before a hosted lobby
