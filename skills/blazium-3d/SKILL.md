---
name: blazium-3d
description: >
  Sets up Blazium 3D scenes (Node3D, Camera3D, lights, GridMap) on 4.3.2 /
  0.6.x. Use when building 3D levels or cameras. Prefer JustAMCP scene3d_tools.
---

# Blazium 3D

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. JustAMCP: `add_mesh_instance`,
`setup_lighting`, `setup_environment`, `setup_camera_3d`, `add_gridmap`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding 3D nodes, cameras, lights, or GridMap levels.

**When not to use:** WorldEnvironment volumes in depth → `blazium-environment`.
Nav bake → `blazium-navigation`. Physics bodies → `blazium-physics`.

## Workflow

1. **Inspect.** Existing Node3D tree / `blazium://scene/hierarchy`.
2. **Place** mesh, camera, light via `scene3d_tools`. GridMap for tile-based 3D.
3. **Verify.** Play mode: confirm exactly one `Camera3D` is current (play-mode
   tree or Autowork `assert_true(cam.current)`). Not a screenshot alone.
4. **Handoff.** Scene path, current camera, GridMap MeshLibrary if used.

## Patterns

One Camera3D current; lights with sensible energy. GridMap uses a MeshLibrary —
do not invent Unity Grid APIs.

```gdscript
extends Node3D

@onready var cam: Camera3D = $Camera3D

func _ready() -> void:
	cam.current = true
	cam.position = Vector3(0.0, 4.0, 8.0)
```

JustAMCP: `setup_camera_3d` then `add_mesh_instance` / `setup_lighting`. Call
`add_gridmap` only after a MeshLibrary exists.

## Pitfalls

- **No current camera** → black screen. Set `Camera3D.current` on one node.
- **Two cameras both current** → last processed wins. Keep exactly one current.
- **Copied Unity Transform API** → `position` / `rotation` / `transform` on Node3D.
- **Forgot environment** → flat look; hand off to `blazium-environment`.
- **GridMap with empty MeshLibrary** → cells paint nothing. Assign a MeshLibrary first.

## Resources

- JustAMCP: `scene3d_tools`

## Related skills

- `blazium-environment` — WorldEnvironment
- `blazium-navigation` — 3D agents
- `blazium-physics` — 3D colliders
- `blazium-autowork` — camera asserts
