---
name: blazium-export-web
pack: ship
---

# blazium-export-web

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-discord` — embedded vs native
- `blazium-export` — generic presets
