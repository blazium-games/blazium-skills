---
name: blazium-discord
description: >
  Integrates Blazium Discord: native Social SDK (presence, OAuth, friends,
  authenticate_with_server) and DiscordEmbeddedAppClient for Embedded Apps.
  Use when adding Discord identity or activity. Not generic web export.
---

# Blazium Discord

Two surfaces. Do not mix them. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Nightly caveat:** `LoginClient` OAuth helpers are templates +
https://docs.blazium.app — not C++/xml class docs in the installed editor.
Native `Discord` and `DiscordEmbeddedAppClient` **are** in installed Blazium.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

| Surface | Module | When |
|---------|--------|------|
| Native Social SDK | `discord_module` (`Discord`, `DiscordAuthResult`) | Desktop presence, OAuth, friends, activity invites |
| Embedded / Playables host | `socialexports` (`DiscordEmbeddedAppClient`, `ReactClient`) | Game hosted on `*.discordsays.com` via `blazium-export-web` |

## When to use

- Use when adding rich presence, Discord OAuth, friends, or activity invites.
- Use when the game runs as a Discord Embedded App.

**When not to use:** JWT persistence → `blazium-services`. Services lobby rooms
→ `blazium-lobby` (activity invites are Discord-side). Generic web export →
`blazium-export-web`.

## Workflow

1. **Inspect.** Native desktop vs Embedded iframe. `Discord.is_available()`.
2. **Choose.** Presence-only vs full OAuth. Embedded vs native (table above).
3. **Implement.** Native: `initialize_presence_only(client_id)` or
   `initialize(client_id)` + `run_callbacks()` each frame. Exchange token with
   `authenticate_with_server(url, access_token, client_id)`. Embedded: wait
   `is_ready`, then `authorize` / `authenticate` on
   `DiscordEmbeddedAppClient`.
4. **Verify.** Presence updates in the Discord client, or Embedded iframe
   auth. Play-mode — not a screenshot alone.
5. **Handoff.** JWT → `blazium-services`. Embedded host/Docker webbuild →
   `blazium-export-web`.

## Patterns

### Presence-only vs OAuth

```gdscript
# Auth-less RPC presence
Discord.initialize_presence_only(client_id)

# Full social layer (friends, invites, server auth)
Discord.initialize(client_id)
# pump every frame (or rely on the engine frame hook)
Discord.run_callbacks()

var auth: DiscordAuthResult = Discord.authenticate_with_server(
	auth_url, access_token, client_id)
```

OAuth-only APIs (`accept_activity_invite`, friend requests) require
`AUTH_READY`.

### Embedded vs native

- **Native:** desktop editor/export with Partner SDK `.dll`/`.so` present.
- **Embedded / Playables:** `DiscordEmbeddedAppClient` + web / Playables
  export on `*.discordsays.com`. Template:
  `script_templates/DiscordEmbeddedAppClient/`. Host pipeline is
  `blazium-export-web` — do not treat native Social SDK as the iframe host.

## Pitfalls

- **Skipped `run_callbacks()`** → OAuth/presence stalls (unless frame hook).
- **Used Embedded client in a desktop-only build** → wrong surface.
- **Invented LoginClient Discord methods** → template + nightly only.

## Resources

- Tests: https://github.com/blazium-games/discord_module_tests

- Native: `blazium/modules/discord_module/doc_classes/Discord.xml`
- Embedded: `blazium/modules/socialexports/doc_classes/DiscordEmbeddedAppClient.xml`
- Template: `script_templates/DiscordEmbeddedAppClient/default.gd`

## Related skills

- `blazium-services` — OAuth token → JWT
- `blazium-lobby` — Services rooms vs Discord activity invites
- `blazium-export-web` — Embedded Apps host
