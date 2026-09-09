---
name: blazium-goap
pack: content
---

# blazium-goap

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Native GOAP planner is more specific than the generic `game-ai` discipline.

## What

`BlaziumGoapAgent`, `BlaziumGoapActionPlanner`, actions/goals.

**Non-goals:** Do not invent a behavior-tree API.

## How

- Module: `blazium/modules/goap/` (5 classes).
- Pair with `blazium-navigation` for movement.

## Reasoning

Engine module skill, not a genre AI framework.

## Sources

- disciplines/game-ai
- goap

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-navigation` — pathing
- `blazium-multiplayer-core` — authority
