---
name: blazium-behavior
pack: content
---

# blazium-behavior

GDScript behavior trees and utility scores. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Many NPCs need a priority tick or a scored choice. That is not the native GOAP planner.

## What

Blackboard, sequence, selector, leaf `tick`, 0–1 utility curves.

**Non-goals:** `BlaziumGoapAgent`, nav baking, animation trees.

## How

1. Confirm it is not GOAP.
2. Tick after physics.
3. Leaves delegate movement.
4. Autowork a forced selector branch and a score change.

## Reasoning

`blazium-goap` owns `BlaziumGoap*`. This skill owns handwritten tick trees so the router does not load the planner for a patrol selector.

## Sources

- Blazium: GDScript `Node` composition. No behavior-tree class.

## Limits

Do not invent `BlaziumBehaviorTree`. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-goap` — planner
- `blazium-navigation` — movement leaves
