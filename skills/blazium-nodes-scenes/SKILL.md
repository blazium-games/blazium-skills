---
name: blazium-nodes-scenes
description: >
  Designs Blazium 0.6.x scene trees (PackedScene instancing, autoloads,
  composition) on Godot 4.3.2. Use when creating .tscn files, spawning
  instances, or adding autoloads. Prefer JustAMCP scene_tools and node_tools
  (create_scene, add_node, instance_scene, save_scene, add_autoload). Not
  editor MCP connect and not signal wiring.
when-to-use: >
  PackedScene, instantiate, add_child, create_scene, add_node, save_scene,
  add_autoload, scene tree, .tscn
metadata:
  author: blazium-games
  short-description: Scene trees, PackedScene instances, and autoloads
---

# Blazium nodes and scenes

Compose `.tscn` trees the 4.3.2 way. Prefer JustAMCP `scene_tools` /
`node_tools` (`create_scene`, `add_node`, `instance_scene`, `save_scene`,
`add_autoload`) over clicking the editor. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs. No 4.7-only nodes.

## When to use

- Use when creating or restructuring scenes, instancing `PackedScene`, autoloads.

**When not to use:** script syntax → `blazium-gdscript`. Signal architecture →
`blazium-signals-groups`. 2D movement math → `blazium-2d-movement`. Editor MCP
connect → `blazium-mcp`.

## Grok host

Read this file only. Spawn `gameplay-programmer` for instancing and
`level-designer` for tree layout. Child prompts must include scene paths and
autoload names. Evidence is `scene_validate` or Autowork `assert_true` on the
child after `add_child` — not a Scene dock screenshot.

## Workflow

1. **Inspect.** Current scene via `blazium://scene/hierarchy` if MCP is up.
2. **Choose.** Composition: child nodes + instanced scenes, not giant scripts.
3. **Implement.** JustAMCP add/instance/save. Autoloads via `add_autoload`.
4. **Verify.** `scene_validate`. Play-mode `runtime_get_tree`: the
   `PackedScene` instance is a child after `add_child`.
5. **Handoff.** Scene paths + autoload names.

## Patterns

```gdscript
const EnemyScene := preload("res://enemies/enemy.tscn") as PackedScene

func spawn() -> void:
	var inst := EnemyScene.instantiate()
	add_child(inst)
```

JustAMCP: `create_scene` / `add_node` / `instance_scene` / `save_scene`.
After building, set `child.owner = root` on descendants. Do **not** recurse
into instanced GLB / `.tscn` (`scene_file_path` set).

## Output contract

- Scene paths created or edited
- Autoload names
- `scene_validate` or Autowork child assert
- Surface used (JustAMCP or files only)

## Pitfalls

- **Instanced in `_init()`** → tree not ready; use `_ready()`.
- **`instantiate()` without `add_child`** → node exists but is not in the tree.
- **Missing `owner`** → `PackedScene.pack` / `save_scene` drops the node.
- **Recursed into instanced GLB** → inlines meshes and can blow the file.
- **`.gdignore` under game assets** → importer skips the directory.
- **Everything in one autoload** → compose scenes instead.

## Related skills

- `blazium-gdscript`, `blazium-signals-groups`, `blazium-mcp`, `blazium-autowork`
