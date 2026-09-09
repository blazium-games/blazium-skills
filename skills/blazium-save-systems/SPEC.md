---
name: blazium-save-systems
pack: growth
---

# blazium-save-systems

Versioned local save/load on `user://`. Engine baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents invent in-place writes and skip schema versions. This skill pins
atomic slots and migration.

## What

Design slots, autosave, JSON / ConfigFile / ResourceSaver, migrate on
`version`. Verify save-quit-load with Autowork.

**Non-goals:** ColdStorage, lobby cloud state, SQLite schemas.

## How

1. Inspect `project.blazium` and what state is authoritative.
2. Stamp `version`. Write temp + `.bak` + rename under `user://`.
3. Verify with Autowork, not a screenshot.

## Reasoning

Distinct from sqlite (tables), lobby (cloud), and coldstorage (VCS).

## Sources

- Blazium: `FileAccess`, `DirAccess`, `ConfigFile`, `ResourceSaver` (4.3.2)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-resources` — adjacent
- `blazium-sqlite` — adjacent
- `blazium-lobby` — adjacent
- `blazium-coldstorage` — adjacent
