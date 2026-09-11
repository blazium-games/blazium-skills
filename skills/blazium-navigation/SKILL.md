---
name: blazium-navigation
description: >
  Bakes and queries Blazium 0.6.x navigation (NavigationRegion2D/3D,
  NavigationAgent2D/3D) on Godot 4.3.2. Use when pathfinding, baking nav, or
  carving obstacles. JustAMCP spatial_bake_navigation, navigation_set_layers,
  navigation_get_info. Not raw physics movement and not GOAP decisions.
when-to-use: >
  NavigationRegion2D, NavigationAgent2D, bake nav, spatial_bake_navigation,
  target_position, navmesh, pathfinding
metadata:
  author: blazium-games
  short-description: Navigation bake, agents, and path queries
---

# Blazium navigation

Use `NavigationRegion2D`/`3D` + `NavigationAgent2D`/`3D`. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**. JustAMCP: `spatial_bake_navigation`,
`navigation_set_layers`, `navigation_get_info`.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs. Do not invent Unity
`NavMeshAgent` names.

## When to use

- Use when baking nav, moving agents along paths, or carving obstacles.

**When not to use:** raw physics movement → `blazium-physics` /
`blazium-2d-movement`. GOAP decisions → `blazium-goap`.

## Grok host

Read this file only. Spawn `ai-programmer` for agents and `level-designer`
for bake. Child prompts must include region type (2D/3D), layer bits, and
agent radius. Evidence is Autowork wait until the body is near the target —
not a gizmo screenshot.

## Workflow

1. **Inspect.** Regions, agent radii, layer bits.
2. **Bake.** `spatial_bake_navigation` or editor bake. Confirm with
   `navigation_get_info`.
3. **Agent.** `NavigationAgent` `target_position`; move with CharacterBody.
4. **Verify.** Autowork wait until the body is near the target.
5. **Handoff.** Region type (2D/3D), layer bits, agent radius.

## Patterns

```gdscript
extends CharacterBody2D

@onready var agent: NavigationAgent2D = $NavigationAgent2D

func go_to(world_point: Vector2) -> void:
	agent.target_position = world_point
```

Same pattern on `CharacterBody3D` + `NavigationAgent3D`. Bake after tile/mesh
changes. Agent radius must fit baked geometry.

## Output contract

- Region type (2D/3D)
- Layer bits and agent radius
- Bake surface (`spatial_bake_navigation` or editor)
- Autowork reach wait

## Pitfalls

- **Forgot to bake after editing tiles** → stale paths.
- **Used Unity NavMeshComponent names** → Godot Navigation* nodes.
- **Agent radius larger than the corridor** → no path.

## Related skills

- `blazium-physics`, `blazium-tilemap`, `blazium-goap`, `blazium-autowork`
