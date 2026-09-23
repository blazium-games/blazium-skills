---
name: blazium-balance
pack: growth
---

# blazium-balance

Economy and combat tables. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Tunable numbers belong in a Resource or CSV so a designer can change them without a controller rewrite.

## What

Costs, rewards, cooldowns, integer weights.

**Non-goals:** BigNum math, idle scene flow, RNG implementation.

## How

1. One table.
2. Stable ids.
3. Autowork one cost and one reward.

## Reasoning

Distinct from `blazium-clicker` and `blazium-genre-idle`.

## Sources

- Blazium `Resource` and CSV

## Limits

Do not invent an economy service. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`).

## Related skills

- `blazium-clicker` — BigNum
- `blazium-procedural` — rolls
