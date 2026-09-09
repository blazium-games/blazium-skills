---
name: blazium-save-systems
description: >
  Persists local game state on Blazium 0.6.x with a versioned schema, user://
  slots, ConfigFile or ResourceSaver, and atomic temp-plus-rename writes.
  Use for save/load, save slots, autosave, or migrating old saves. Not
  ColdStorage VCS, lobby cloud state, or SQLite tables.
---

# Blazium save systems

Local progress that survives quit. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Save **data**, not live node paths. Stamp `version` from slot 1.

`user://` only. `ConfigFile` for settings; `JSON` + `FileAccess` or a
`Resource` + `ResourceSaver` for slots. Atomic write: temp file, flush,
keep `.bak`, then rename.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding save slots, quicksave, autosave, or a schema `version`.
- Use when a patch must load an older `user://` file.

**When not to use:** editor VCS / cstoraged → `blazium-coldstorage`.
Cloud lobby / reconnect tokens → `blazium-lobby`. Relational tables →
`blazium-sqlite`. Settings keys only with no slots → `blazium-config`.

## Workflow

1. **Inspect.** What is authoritative (hp, flags, seed) vs reconstructable.
2. **Choose.** JSON dictionary, `ConfigFile`, or a `Resource` `.tres` / `.res`.
3. **Implement.** Embed `version`. Write `path.tmp`, flush, rotate `.bak`,
   rename onto `path`. Autosave a **separate** file.
4. **Verify.** Save → quit → load. Load a previous `version`. Autowork
   `assert_eq` on fields — not a screenshot of a menu.
5. **Handoff.** Slot paths + current schema version.

## Patterns

### Capture data, not nodes

```gdscript
const SAVE_VERSION := 1
const SLOT := "user://save_0.json"

func capture_state() -> Dictionary:
	return {
		"version": SAVE_VERSION,
		"player": {"hp": player.hp, "pos": [player.position.x, player.position.y]},
		"flags": world.flags,
		"seed": world.seed,
	}
```

### Atomic write + `.bak` (Windows-safe)

```gdscript
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

On load: parse → if `version` newer than `SAVE_VERSION`, refuse → migrate
`v` to `v+1` in order → validate keys → reconstruct objects.

`ConfigFile` for options (`cfg.save("user://settings.cfg")`).
`ResourceSaver.save(res, "user://slot_0.tres")` when the slot **is** a Resource.

## Pitfalls

- **Serialized node paths** → renaming a node breaks every old save.
- **No `version` field** → the next patch cannot migrate.
- **Wrote the slot in place** → a crash truncates the only copy.
- **Autosave overwrote a manual slot** → use `user://autosave.json`.
- **Trusted a local file for online state** → lobby / JWT stay server-side.

## Resources

- https://docs.blazium.app — `FileAccess`, `DirAccess`, `ConfigFile`, `ResourceSaver`

## Related skills

- `blazium-resources` — Resource / `.tres` shape
- `blazium-sqlite` — relational tables, not slot files
- `blazium-lobby` — cloud room / reconnect token
- `blazium-coldstorage` — editor VCS, not player saves
- `blazium-config` — `.env` / ENV, not game slots
