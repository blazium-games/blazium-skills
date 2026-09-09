---
name: blazium-goap
description: >
  Sets up Blazium’s native GOAP planner (BlaziumGoapAgent, goals, actions,
  world state). Use when an NPC needs planned action sequences. Not a simple
  FSM and not a behavior-tree rewrite.
---

# Blazium GOAP

Native planner. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/goap/` — `BlaziumGoapAgent`, `BlaziumGoapAction`,
`BlaziumGoapGoal`, `BlaziumGoapWorldState`, `BlaziumGoapActionPlanner`.

Movement after a plan → `blazium-navigation`. Authority in MP →
`blazium-multiplayer-core`. Do not rewrite behavior-tree tutorials.

## When to use

- Use when an actor has multiple goals/actions and needs cheapest-plan
  switching at runtime.

**When not to use:** one or two states → FSM / AnimationTree. Pathfinding
only → `blazium-navigation`. A generic “game AI” pass.

## Workflow

1. **Inspect.** Is GOAP warranted vs a state machine?
2. **Choose.** Goal/action child containers + a world state.
3. **Implement.** Attach `BlaziumGoapAgent`, set `goals_node` /
   `actions_node`, `init(actor)` (must be called manually).
4. **Verify.** `get_current_action()` changes when world state changes.
   Autowork on a mocked world state.
5. **Handoff.** Actor path. Steering → navigation.

## Patterns

### Happy path

```gdscript
var agent := BlaziumGoapAgent.new()
var actions := Node.new()
var goals := Node.new()
actions.add_child(GatherWood.new())  # extends BlaziumGoapAction
goals.add_child(GoalSurvive.new())   # extends BlaziumGoapGoal
agent.add_child(actions)
agent.add_child(goals)
agent.goals_node = agent.get_path_to(goals)
agent.actions_node = agent.get_path_to(actions)
actor.add_child(agent)
agent.init(actor)
```

Each tick the agent picks the highest-priority active goal and asks the
planner for the cheapest action path. It can switch mid-execution.

## Pitfalls

- **Forgot `init(actor)`** → planning loop never starts.
- **GOAP for a patrol-two-points enemy** → FSM is enough.
- **Implemented `_perform` as navigation math** → call into
  `blazium-navigation`.
- **Copied Unity/Unreal GOAP class names** → use `BlaziumGoap*` only.

## Resources

- Tests: https://github.com/blazium-games/goap_module_tests

- `blazium/modules/goap/doc_classes/BlaziumGoapAgent.xml`
- Asset: `assets/goap_init.gd`

## Related skills

- `blazium-navigation` — pathing
- `blazium-multiplayer-core` — authority
- `blazium-2d-movement` — CharacterBody feel
