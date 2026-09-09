---
name: blazium-export-web
pack: ship
---

# blazium-export-web

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Web is where Blazium diverges: COOP/COEP, YouTube Playables, Discord Embedded Apps.

## What

Web export, headers, Playables (`YoutubePlayablesClient`), Discord embed Docker webbuild.

**Non-goals:** Do not own native Discord Social SDK.

## How

- Godot web export + COOP/COEP.
- socialexports: `YoutubePlayablesClient`, `DiscordEmbeddedAppClient`, `ReactClient`.

## Reasoning

Platform export, not UI.

## Sources

- optimize-web
- socialexports

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-discord` — embedded vs native
- `blazium-export` — generic presets
