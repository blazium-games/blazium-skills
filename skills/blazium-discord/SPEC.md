---
name: blazium-discord
pack: live-ops
---

# blazium-discord

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Two Discord surfaces: native Social SDK and Embedded Apps. Agents mix them.

## What

`Discord` singleton: presence, OAuth, friends, activity invites/lobbies, `authenticate_with_server`. Plus `DiscordEmbeddedAppClient` in socialexports for `*.discordsays.com` + Docker webbuild.

**Non-goals:** Do not own generic web export (`blazium-export-web`).

## How

- Native: `blazium/modules/discord_module/` (`Discord`, `DiscordAuthResult`).
- Embedded: `blazium/modules/socialexports/` (`DiscordEmbeddedAppClient`, `ReactClient`).
- Presence-only vs full OAuth. Callback pumping.
- Templates: DiscordEmbeddedAppClient.

## Reasoning

One skill, two surfaces. Split later only if SKILL.md is too large.

## Sources

- Blazium: discord_module + socialexports

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-services` — OAuth → JWT
- `blazium-export-web` — Embedded Apps host
- `blazium-lobby` — activity invites vs Services lobby
