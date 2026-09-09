---
name: blazium-config
pack: modules
---

# blazium-config

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents invent `OS.get_environment` / `ConfigFile` when Blazium ships `ENV` and `DotIniFile`.

## What

Load `.env` / `.ini`, bind properties, secrets vs `res://`.

**Non-goals:** Do not commit secrets. Do not replace ProjectSettings.

## How

- `blazium/modules/dotenv/` singleton `ENV`.
- `blazium/modules/dotini/` class `DotIniFile`.
- Override order and user:// vs res://.

## Reasoning

`ENV` and `DotIniFile` are Blazium modules. Agents should use them instead
of inventing `OS.get_environment` wrappers.

## Sources

- `blazium/modules/dotenv/`
- `blazium/modules/dotini/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-project-config` — ProjectSettings
- `blazium-httpserver` — env for ports/tokens
