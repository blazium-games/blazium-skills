---
name: blazium-navigation
description: >
  Bakes and queries Godot/Blazium navigation (NavigationRegion2D/3D,
  NavigationAgent) on 4.3.2. Use when pathfinding or NavMesh-style AI is
---

# Blazium navigation

Godot’s pack has no nav skill. Use `NavigationRegion2D`/`3D` +
`NavigationAgent2D`/`3D`. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
JustAMCP: `spatial_bake_navigation`, `navigation_set_layers`,
`navigation_get_info`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate. Do not invent Unity `NavMeshAgent` names.

## When to use

- Use when baking nav, moving agents along paths, or carving obstacles.

**When not to use:** raw physics movement → `blazium-physics` /
`blazium-2d-movement`. GOAP decisions → `blazium-goap`.

## Workflow

1. **Inspect.** Regions, agent radii, layer bits.
2. **Bake.** `spatial_bake_navigation` (MCP) or editor bake. Confirm with
   `navigation_get_info`.
3. **Agent.** `NavigationAgent` `target_position`; move with CharacterBody.
4. **Verify.** Autowork wait until the body is near the target, or play-mode
   until `target_position` is reached. Not a screenshot of the gizmos.
5. **Handoff.** Region type (2D/3D), layer bits, agent radius.

## Patterns

Bake after tile/mesh changes. Agent radius must fit baked geometry. Layers:
filter which regions an agent can use (`navigation_set_layers`).

```gdscript
extends CharacterBody2D

@onready var agent: NavigationAgent2D = $NavigationAgent2D

func go_to(world_point: Vector2) -> void:
	agent.target_position = world_point
```

Same pattern on `CharacterBody3D` + `NavigationAgent3D`.

## Pitfalls

- **Forgot to bake after editing tiles** → stale paths. Re-run `spatial_bake_navigation`.
- **Used Unity NavMeshComponent names** → Godot Navigation* nodes.
- **Editor `navigation` module internals** → not needed for gameplay.
- **Agent radius larger than the corridor** → no path. Match bake radius to the agent.

## Resources

- JustAMCP: `spatial_tools`

## Related skills

- `blazium-physics` — collision vs nav
- `blazium-tilemap` — 2D worlds
- `blazium-goap` — planner
- `blazium-autowork` — reach waits
