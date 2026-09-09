---
name: blazium-streaming
description: >
  Connects streamer platforms in one skill: Twitch Helix + IRC, Kick REST,
  OBS WebSocket 5.x, Crowd Control. Use for chat-command → game effect →
  OBS scene. Not Discord.
---

# Blazium streaming

One streamer loop — not five skills. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

| Job | Module / classes |
|-----|------------------|
| Twitch Helix | `twitchapi/` — `TwitchAPI` (auto-poll after `configure`) |
| Twitch chat | `ircclient/` — `TwitchIRCClient` / `TwitchIRCClientNode` |
| Kick REST | `kickapi/` — `KickAPI` |
| OBS | `obsclient/` — `OBSClient` (WebSocket 5.x; **`poll()` required**) |
| Viewer effects | `crowdcontrol/` — `CrowdControl`, `CrowdControlEffect`, `CrowdControlGamePack` |

Tokens via `blazium-config` / `user://` — **never `res://`**. Not Discord
(`blazium-discord`).

## When to use

- Use when auth → chat command → game effect → OBS scene is the job.

**When not to use:** Discord presence / Embedded Apps → `blazium-discord`.
Generic HTTP APIs → `blazium-httpserver`. Secrets plumbing only →
`blazium-config`.

## Workflow

1. **Inspect.** Which platforms. `ClassDB.class_exists("TwitchAPI")` etc.
2. **Choose.** Helix vs IRC vs Kick vs OBS vs Crowd Control — load only
   what the user asked.
3. **Implement.** Configure from `ENV.get_env` / `user://`. Never hardcode
   tokens.
4. **Verify.** One live request or a mocked Autowork signal — not a
   screenshot of OBS.
5. **Handoff.** Platforms wired. Token paths (not values).

## Patterns

### Twitch Helix + IRC

```gdscript
TwitchAPI.configure(ENV.get_env("TWITCH_CLIENT_ID", ""), ENV.get_env("TWITCH_TOKEN", ""))
TwitchAPI.get_users().get_users({"login": ["channel"]})
# chat: add TwitchIRCClientNode and connect_to_twitch(...)
```

Helix getters: `get_users`, `get_streams`, `get_chat`, `get_channels`,
`get_moderation`, `get_bits`, `get_clips`, `get_games`, `get_ads`,
`get_analytics`, `get_channel_points`. Signals: `request_completed`,
`request_failed`, `rate_limit_warning`. Helix auto-polls after `configure`.

### Kick

`KickAPI.configure(access_token)` then `get_users` / `get_channels` /
`get_chat` / `get_livestreams` / `get_moderation` / `get_oauth`.
Sub-clients emit `users_received` (watch + timeout). Live tests need
`res://secrets.json` (`access_token`) or they `pending()`. TLS:
`KickAPI.get_http_client().set_tls_options(TLSOptions.client(cert))` with
`res://ca-certificates.crt` on MbedTLS.

### Generic IRC (`IRCClientNode`)

Twitch chat stays on `TwitchIRCClient` / `TwitchIRCClientNode`. Generic
IRC (from `irc_module_tests`):

```gdscript
var irc := IRCClientNode.new()
irc.connect_to_server("irc.libera.chat", 6697, true, nick, "user", "realname")
# poll the client; then:
irc.join_channel("#channel")
irc.send_privmsg("#channel", "hello")
```

Also: `part_channel`, `send_notice`, `send_action`, `set_topic`,
`set_nick`, `disconnect_from_server`, `is_irc_connected()`,
`get_client()`, `set_debug_enabled()`. Client: `poll()`, `voice_user()`,
`kick_user()`. Signals: `joined`, `privmsg`, `notice`, `topic_changed`,
`mode_changed`, `nick_changed`, `kicked`, `parted`. Live suite needs
`IRC_LIVE_TESTS=1` (TLS 6697; debug tests use 6667).

### OBS scene switch

```gdscript
OBSClient.connect_to_obs("ws://127.0.0.1:4455", password)
# _process: OBSClient.poll()
OBSClient.set_current_program_scene("Gameplay")
```

Default port **4455**. Also: `get_scene_list`, `start_stream` / `stop_stream`,
`start_record` / `stop_record`, `get_version(callback)`,
`subscribe_to_events(OBS_EVENT_SUBSCRIPTION_ALL, cb)`,
`broadcast_custom_event()`, `unsubscribe_from_events()`, signal
`connected`. Live: `OBS_LIVE_TESTS=1`. Without OBS, tests `pending()`.

### Crowd Control pack

```gdscript
CrowdControl.set_credentials(application_id, secret)
# _process: CrowdControl.poll()   # required
CrowdControl.request_authentication_http()   # or request_authentication_websocket()
# signals: authentication_url_ready, authenticated
CrowdControl.connect_to_crowdcontrol("wss://pubsub.crowdcontrol.live/")
CrowdControl.start_game_session(game_id)
CrowdControl.respond_to_effect_instant(req_id, CrowdControl.STATUS_SUCCESS, "ok")
CrowdControl.respond_to_effect_timed(req_id, CrowdControl.STATUS_TIMED_BEGIN, 60000, "started")
CrowdControl.stop_game_session()
CrowdControl.close()
```

Also: `set_auth_token`, `get_auth_token`, `get_refresh_token`,
`is_authenticated()`, `is_websocket_connected()`,
`get_game_session_id()`. Pack types: `CrowdControlGamePackMeta`,
`CrowdControlEffectParameter`, `CrowdControlEffect`,
`CrowdControlGamePack`. Live tests use `user://` token caches; missing
secrets → `pending()`. Tokens never in `res://`.

## Pitfalls

- **Stored OAuth in `res://`** → export leaks tokens.
- **Forgot OBS/CrowdControl `poll()`** → handshake never finishes.
- **Assumed Twitch IRC is generic IRC** → `IRCClientNode` is the generic
  client; Twitch helpers are separate.
- **Split this into five skills** → one streamer job.
- **Used Discord Social SDK here** → wrong platform.

## Resources

- Tests: https://github.com/blazium-games/twitchapi_module_tests
- Tests: https://github.com/blazium-games/kickapi_module_tests
- Tests: https://github.com/blazium-games/irc_module_tests
- Tests: https://github.com/blazium-games/obsclient_module_tests
- Tests: https://github.com/blazium-games/crowdcontrol_module_tests

- `blazium/modules/twitchapi/doc_classes/TwitchAPI.xml`
- `blazium/modules/obsclient/doc_classes/OBSClient.xml`
- `blazium/modules/crowdcontrol/doc_classes/CrowdControl.xml`

## Related skills

- `blazium-config` — secrets
- `blazium-discord` — not this stack
- `blazium-httpserver` — local overlays
