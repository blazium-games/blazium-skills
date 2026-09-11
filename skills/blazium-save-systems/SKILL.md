---
name: blazium-save-systems
description: >
  Persists local game state on Blazium 0.6.x with a versioned schema, user://
  slots, ConfigFile or ResourceSaver, and atomic temp-plus-rename writes.
  Use for save/load, save slots, autosave, or migrating old saves. Not
  ColdStorage VCS, lobby cloud state, or SQLite tables.
when-to-use: >
  save slots, user:// save, autosave, schema version, atomic temp-plus-rename,
  ResourceSaver slot, ConfigFile settings.cfg
metadata:
  author: blazium-games
  short-description: Versioned user:// save slots with atomic writes
---

# Blazium save systems

Local progress that survives quit. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Save **data**, not live node paths. Stamp `version` from slot 1.
`user://` only. Atomic write: temp file, flush, keep `.bak`, then rename.

## When to use

- Use when adding save slots, quicksave, autosave, or a schema `version`.

**When not to use:** editor VCS → `blazium-coldstorage`. Cloud lobby →
`blazium-lobby`. Relational tables → `blazium-sqlite`. Settings-only →
`blazium-config`.

## Grok host

Read this file only. Spawn `systems-designer` for the schema and
`gameplay-programmer` for atomic write. Child prompts must include slot
path and current `version`. Evidence is Autowork save → load `assert_eq`.

## Workflow

1. **Inspect.** Authoritative fields vs reconstructable.
2. **Choose.** JSON, `ConfigFile`, or Resource `.tres`.
3. **Implement.** Embed `version`. Write `path.tmp`, flush, rotate `.bak`, rename.
4. **Verify.** Save → load previous `version`. Autowork field asserts.
5. **Handoff.** Slot paths + schema version.

## Patterns

```gdscript
const SAVE_VERSION := 1
const SLOT := "user://save_0.json"

func save_atomic(path: String, data: Dictionary) -> void:
	var tmp := path + ".tmp"
	var f := FileAccess.open(tmp, FileAccess.WRITE)
	f.store_string(JSON.stringify(data))
	f.flush()
	f.close()
	if FileAccess.file_exists(path):
		DirAccess.rename_absolute(path, path + ".bak")
	DirAccess.rename_absolute(tmp, path)
```

## Output contract

- Slot paths (`user://…`)
- Schema `version`
- Write method
- Autowork save/load assertion

## Pitfalls

- **Serialized node paths** → old saves break.
- **No `version` field** → cannot migrate.
- **Wrote the slot in place** → crash truncates the only copy.
- **Autosave overwrote a manual slot** → `user://autosave.json`.

## Related skills

- `blazium-resources`, `blazium-sqlite`, `blazium-lobby`, `blazium-coldstorage`, `blazium-config`
