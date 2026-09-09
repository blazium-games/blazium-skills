---
name: blazium-nodes-scenes
description: >
  Designs Blazium scene trees (PackedScene instancing, autoloads, composition)
  on Godot 4.3.2 / 0.6.x. Use when creating .tscn files, spawning instances, or
  adding autoloads. Prefer JustAMCP scene_tools and node_tools. Do not use to
  connect editor MCP — that is blazium-mcp.
---

# Blazium nodes and scenes

Compose `.tscn` trees the 4.3.2 way. Prefer JustAMCP `scene_tools` /
`node_tools` (`create_scene`, `add_node`, `instance_scene`, `save_scene`,
`add_autoload`) over clicking the editor.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate. No 4.7-only nodes.

## When to use

- Use when creating or restructuring scenes, instancing `PackedScene`, autoloads.

**When not to use:** script syntax → `blazium-gdscript`. Signal architecture →
`blazium-signals-groups`. 2D movement math → `blazium-2d-movement`.

## Workflow

1. **Inspect.** Current scene via `blazium://scene/hierarchy` if MCP is up.
2. **Choose.** Composition: child nodes + instanced scenes, not giant scripts.
3. **Implement.** JustAMCP add/instance/save. Autoloads via `add_autoload`.
4. **Verify.** `scene_validate`. Play-mode `runtime_get_tree`: the
   `PackedScene` instance is a child after `add_child`. Autowork
   `assert_true` on that child. Not a screenshot of the Scene dock.
5. **Handoff.** Scene paths + autoload names.

## Patterns

Owner scene holds instances; children do one job. Autoload for true singletons
(services), not for every helper.

```gdscript
const EnemyScene := preload("res://enemies/enemy.tscn") as PackedScene

func spawn() -> void:
	var inst := EnemyScene.instantiate()
	add_child(inst)
```

JustAMCP: `create_scene` / `add_node` / `instance_scene` / `save_scene`.
Prompt: `blazium_scene_architect` / `blazium_scene_build_workflow`.

## Pitfalls

- **Instanced in `_init()`** → tree not ready; use `_ready()`.
- **`instantiate()` without `add_child`** → node exists but is not in the tree.
- **Edited `.tscn` as text incorrectly** → use MCP or editor.
- **Everything in one autoload** → compose scenes instead.
- **Missing `owner`** → `PackedScene.pack` / `save_scene` drops the node. After building, set `child.owner = root` on descendants. Do **not** recurse into instanced GLB / `.tscn` (`scene_file_path` set) — that inlines meshes and can blow the file to 100MB+.
- **Pack looked successful but nodes vanished** → count nodes before pack, `instantiate()` after, compare; gate save on a match. Use `scene_validate` when MCP is up.
- **`.gdignore` under game assets** → importer skips the directory with no error. Never put one under `res://` content the game loads.
- **Procedural mesh has no shadows** → call `ArrayMesh.generate_normals()`. `cull_mode` disabled as a “safety net” silently kills shadows — fix winding instead.
- **MultiMeshInstance3D + GLB empty after save** → the mesh is dropped on pack. Use individual instances. `material_override` on GLB-internal nodes also will not serialize (owner skipped) — use a procedural `ArrayMesh` when a custom material is needed.

## Resources

- JustAMCP: `scene_tools`, `node_tools`, `blazium://scene/current`

## Related skills

- `blazium-gdscript` — scripts on nodes
- `blazium-signals-groups` — communication
- `blazium-mcp` — tool discovery
- `blazium-autowork` — tree asserts
