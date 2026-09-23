---
name: blazium-addons
pack: content
---

# blazium-addons

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — editors/templates
- `blazium-project-config` — autoload plugins
