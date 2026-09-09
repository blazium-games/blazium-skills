---
name: blazium-coldstorage
pack: ship
---

# blazium-coldstorage

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — local tooling
- `blazium-project-config` — keys
