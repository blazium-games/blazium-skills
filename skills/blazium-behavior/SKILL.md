---
name: blazium-behavior
description: >
  Implements a GDScript behavior tree (blackboard, sequence, selector, leaf
  tick) and utility scoring curves. Use when an NPC needs structured ticks or
  graded action scores. Native goal planning stays on blazium-goap.
---

# Blazium behavior

Tick-based decisions in GDScript. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

There is no built-in behavior-tree class. A tree is `Node` children with
`tick(actor, blackboard) -> int`. Status: `0` failure, `1` running, `2` success.

Native planned sequences stay on `blazium-goap` (`BlaziumGoapAgent`).

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when an enemy needs a selector (try A, else B) or a sequence (do A then B).
- Use when several actions compete by score (utility), not by a single goal plan.

**When not to use:** cheapest action path over world state → `blazium-goap`.
Path following → `blazium-navigation`. Two animation states → `blazium-animation`.

## Workflow

1. **Inspect.** Is this a tick tree, a utility pick, or a GOAP plan?
2. **Choose.** Selector for priority. Sequence for steps. Utility when every
   option has a 0–1 score.
3. **Implement.** One blackboard `Dictionary` on the actor. Tick from
   `_physics_process`. Leaves call navigation or combat; they do not bake paths.
4. **Verify.** Autowork: blackboard flag forces the selector onto the second
   leaf; utility pick changes when a consideration input changes.
5. **Handoff.** Tree script path and which leaves call `blazium-navigation`.

## Patterns

```gdscript
class_name BehaviorNode
extends Node

const FAIL := 0
const RUN := 1
const OK := 2

func tick(_actor: Node, _board: Dictionary) -> int:
	return FAIL

func tick_selector(actor: Node, board: Dictionary) -> int:
	for child in get_children():
		var status: int = child.tick(actor, board)
		if status != FAIL:
			return status
	return FAIL
```

Utility: each consideration maps an input through a curve into 0–1
(clamp, then `1.0 / (1.0 + exp(-k * (x - mid)))` for a sigmoid). Multiply
considerations. Pick the highest score. A tree leaf may call that pick.

## Pitfalls

- **Reimplemented `BlaziumGoapAgent`** → `blazium-goap`.
- **Tick in `_process` and move in `_physics_process`** → one-frame stale board.
- **Leaf builds a navmesh** → call `NavigationAgent` from `blazium-navigation`.
- **Unclamped utility scores** → one huge input always wins. Clamp to 0–1 first.

## Resources

- https://docs.blazium.app — `Node`, `Dictionary`

## Related skills

- `blazium-goap` — native planner
- `blazium-navigation` — path leaves
- `blazium-animation` — state playback
