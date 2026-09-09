---
name: blazium-services
pack: live-ops
---

# blazium-services

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

First-party login is the Blazium live-ops story.

## What

Login via Discord OAuth and Steam tickets using `LoginClient` templates. Persist JWT in `user://blazium.cfg`.

**Non-goals:** Local JWT crypto (`blazium-jwt`). Matchmaking rooms (`blazium-lobby`). Do not invent C++ class docs missing from the installed editor.

## How

- Templates: `blazium/modules/gdscript/editor/script_templates/` (`LoginClient`).
- Token storage: `user://blazium.cfg`.
- `LoginClient` / `LobbyClient` / `MasterServerClient` are templates on https://docs.blazium.app — verify against the installed nightly.
- Steam ticket exchange: hand off to `blazium-steam`. JWT sign/verify: `blazium-jwt`.

## Reasoning

Distinct from lobby rooms, JWT crypto, and Games cloud MCP.

## Sources

- `script_templates/LoginClient/`
- https://docs.blazium.app

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-jwt` — encode / decode / validate
- `blazium-lobby` — rooms after auth
- `blazium-steam` — ticket → JWT
- `blazium-discord` — OAuth / Social SDK
- `blazium-games-mcp` — cloud store, not identity
