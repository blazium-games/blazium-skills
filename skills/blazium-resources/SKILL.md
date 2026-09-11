---
name: blazium-resources
description: >
  Authors Blazium 0.6.x Resource / .tres data (items, stats, configs) on
  Godot 4.3.2 with class_name and @export fields. Use when defining custom
  Resource types or shared data assets. JustAMCP resource_tools
  (create_resource, read_resource_file, edit_resource_file). Not
  ScriptableObjects, CSV tables, or SQLite.
when-to-use: >
  Resource, .tres, class_name ItemData, create_resource, read_resource_file,
  shared data asset, stats resource
metadata:
  author: blazium-games
  short-description: Custom Resource types and .tres data assets
---

# Blazium resources

`Resource` + `.tres` / `.res`. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
JustAMCP: `resource_tools` (`create_resource`, `read_resource_file`,
`edit_resource_file`).

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when defining custom Resource types or shared data assets.

**When not to use:** large tables → `blazium-csv`. SQL →
`blazium-sqlite`. Scene instances → `blazium-nodes-scenes`. Slot files →
`blazium-save-systems`.

## Grok host

Read this file only. Spawn `systems-designer` for field lists and
`gameplay-programmer` for `class_name`. Child prompts must include script
path and `.tres` path. Evidence is `read_resource_file` or Autowork
`assert_eq` on exports — not an inspector screenshot.

## Workflow

1. **Define** `class_name` Resource with `@export` fields.
2. **Create** `.tres` via `create_resource` or the editor.
3. **Load** with `preload` / `ResourceLoader`.
4. **Verify.** `read_resource_file` matches the exports. Autowork
   `assert_eq` on those fields after load.
5. **Handoff.** Script path + `.tres` paths.

## Patterns

```gdscript
extends Resource
class_name ItemData

@export var id: StringName
@export var max_stack: int = 1
```

```gdscript
var item := load("res://data/potion.tres") as ItemData
```

JustAMCP: `create_resource` then `read_resource_file` / `edit_resource_file`.

## Output contract

- Resource script path and `class_name`
- `.tres` / `.res` paths
- Fields asserted
- Surface used (`resource_tools` or files only)

## Pitfalls

- **Mutated a shared .tres at runtime** → duplicate if the instance must be unique.
- **Used ScriptableObject C#** → Resource + `.tres`.
- **Stored secrets in res://** → `user://` / `blazium-config`.
- **`.tres` type missing `class_name`** → load returns a bare Resource.

## Related skills

- `blazium-gdscript`, `blazium-csv`, `blazium-sqlite`, `blazium-save-systems`, `blazium-autowork`
