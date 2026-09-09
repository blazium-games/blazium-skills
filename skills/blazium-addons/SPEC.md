---
name: blazium-addons
pack: content
---

# blazium-addons

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents need AssetLib / `addons/` / editor plugins — not a foreign package manifest.

## What

Install and author `addons/`, understand editor plugins vs engine modules.

**Non-goals:** Do not teach SCons module authoring unless the user is in the engine repo.

## How

- Project `addons/` + plugin.cfg.
- AssetLib. Distinct from `blazium-cli` editor installs.

## Reasoning

Package-management analog.

## Sources

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — editors/templates
- `blazium-project-config` — autoload plugins
