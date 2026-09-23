---
name: blazium-release-checklist
pack: ship
---

# blazium-release-checklist

Launch and patch gates. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Export, CI, and the store page are separate skills. Shipping needs a single gate list that points at them.

## What

Preset, version, CI, store fields, patch notes.

**Non-goals:** authoring presets, reading job logs, writing the store page.

## How

1. Read each gate.
2. Hand gaps to the owner skill.
3. Report pass or gap. Do not invent a ship CLI.

## Reasoning

Distinct from `blazium-export`, `blazium-ci-watch`, and `blazium-games-publish`.

## Sources

- `export_presets.cfg`, project version, CI status, store page fields

## Limits

Do not invent publish verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-export` — presets
- `blazium-ci-watch` — CI
- `blazium-games-publish` — page
