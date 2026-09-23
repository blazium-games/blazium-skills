---
name: blazium-coldstorage
pack: ship
---

# blazium-coldstorage

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Editor VCS against `cstoraged` is not Git. Agents will install the Godot Git plugin and fight it.

## What

Connect `ColdStorageVCS`: host, port 1666, TLS, workspace, auto_pull. When to use vs Git.

**Non-goals:** Do not replace git in this ecosystem repo. Do not invent cstorage server ops beyond editor settings.

## How

- Module: `blazium/modules/coldstorage/`.
- Settings: `blazium/coldstorage/*`.
- Classes: `ColdStorageVCS`, `ColdStorageEditorPlugin`.

## Reasoning

Short ecosystem-ops spec. Repeated agent task when a studio uses ColdStorage.

## Sources

- blazium/modules/coldstorage/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — local tooling
- `blazium-project-config` — keys
