---
name: blazium-dddbrowser
pack: modules
---

# blazium-dddbrowser

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

12 classes: 3D web-world authoring + Luau gamemode export. Unpublished until a `SKILL.md` exists.

## What

`DDDBrowserLevel`, `DDDBrowserPortal`, `DDDBrowserSpawn`, `DDDBrowserExporter`, `DDDBrowserPreviewServer`.

**Non-goals:** Do not teach general 3D (`blazium-3d`) or Luau language (`blazium-luau`).

## How

- Module: `blazium/modules/dddbrowser/`.
- Author → preview → export. Luau gamemode handoff.

## Reasoning

Unique vertical, enough surface for its own skill.

## Sources

- dddbrowser (12 classes)

## Limits

Unpublished. Do not invent APIs. Do not load a skill until a `SKILL.md` exists. Verify against installed Blazium and https://docs.blazium.app.

## Related skills

- `blazium-luau` — gamemodes
- `blazium-3d` — generic 3D
