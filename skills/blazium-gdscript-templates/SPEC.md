---
name: blazium-gdscript-templates
pack: content
---

# blazium-gdscript-templates

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Engine script templates (Lobby, Login, Discord embed, YouTube Playables, SQLite) are the fastest correct start and are easy to miss.

## What

List and apply templates under `blazium/modules/gdscript/editor/script_templates/`.

**Non-goals:** Do not re-teach each domain API — hand off.

## How

Templates: LobbyClient, ScriptedLobbyClient, LoginClient, DiscordEmbeddedAppClient, YoutubePlayablesClient, SQLite.
Same nightly-verification caveat for lobby/login classes.

## Reasoning

Could fold into gdscript; kept separate so the router can load 'start from official template' without the whole language skill.

## Sources

- gdscript/editor/script_templates/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — language
- `blazium-services` — LoginClient
- `blazium-lobby` — LobbyClient
- `blazium-discord` — embedded
- `blazium-sqlite` — SQLite
