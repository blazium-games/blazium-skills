---
name: blazium-resources
description: >
  Authors Blazium Resource / .tres data (items, stats, configs) on 4.3.2.
  ScriptableObjects. CSV/SQLite are other skills.
---

# Blazium resources

`Resource` + `.tres` / `.res`. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
JustAMCP: `resource_tools` (`create_resource`, `read_resource_file`,
`edit_resource_file`).

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when defining custom Resource types or shared data assets.

**When not to use:** large tables → `blazium-csv`. SQL →
`blazium-sqlite`. Scene instances → `blazium-nodes-scenes`.

## Workflow

1. **Define** `class_name` Resource with `@export` fields.
2. **Create** `.tres` via `create_resource` or the editor.
3. **Load** with `preload` / `ResourceLoader`.
4. **Verify.** `read_resource_file` matches the exports. Autowork
   `assert_eq` on those fields after load. Not a screenshot of the inspector.
5. **Handoff.** Script path + `.tres` paths.

## Patterns

```gdscript
extends Resource
class_name ItemData

@export var id: StringName
@export var max_stack: int = 1
```

Load a unique instance when runtime mutation is required:

```gdscript
var item := load("res://data/potion.tres") as ItemData
```

JustAMCP: `create_resource` then `read_resource_file` / `edit_resource_file`.

## Pitfalls

- **Mutated a shared .tres at runtime** → duplicate if the instance must be unique.
- **Used ScriptableObject C#** → Resource + `.tres`.
- **Stored secrets in res://** → `user://` / `blazium-config`.
- **`.tres` type missing `class_name`** → load returns a bare Resource. Add
  `class_name` and re-save the asset.

## Resources

- JustAMCP: `resource_tools`

## Related skills

- `blazium-gdscript` — class_name
- `blazium-csv` — tables
- `blazium-sqlite` — DB
- `blazium-autowork` — field asserts
