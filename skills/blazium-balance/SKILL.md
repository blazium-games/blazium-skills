---
name: blazium-balance
description: >
  Designs economy and combat tables (costs, rewards, cooldowns) as Resources
  or CSV rows. Use when tuning numbers, drop weights, or prices. BigNum
  arithmetic stays on blazium-clicker. Idle loop composition stays on
  blazium-genre-idle. Seeded rolls stay on blazium-procedural.
---

# Blazium balance

Numbers in data, not in scattered literals. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

`blazium-clicker` owns `BlaziumBigNum` math. `blazium-genre-idle` owns the
idle loop. This skill owns the table a designer can edit.

## When to use

- Use when setting costs, rewards, cooldowns, or drop weights.
- Use when a combat exchange should be readable as rows.

**When not to use:** BigNum implementation → `blazium-clicker`. Genre scene
flow → the matching `blazium-genre-*` skill. Rolling a seed →
`blazium-procedural`.

## Grok host

Read this file only. Spawn `economy-designer`. Child prompts must include
the table path and the unit (points, seconds, weight). Evidence is the
Resource or CSV plus one Autowork read of a row.

## Workflow

1. **Inspect.** Existing Resource or CSV. What the player spends and earns.
2. **Choose.** One table. Do not retune the whole game in one pass.
3. **Implement.** `Resource` fields or a CSV (`blazium-csv`) with stable
   ids. Weights are integers. Cooldowns are seconds.
4. **Verify.** Autowork loads the row and `assert_eq` on one cost and one
   reward. Not a screenshot of a spreadsheet.
5. **Handoff.** Table path and which genre or clicker skill reads it.

## Patterns

| id | cost | reward | cooldown_s | weight |
|----|------|--------|------------|--------|
| strike | 2 | 5 | 0.4 | 10 |

Keep ids stable. Designers change numbers; programmers change columns.
Generation code reads the weight column (`blazium-procedural`).

## Output contract

- Table path and columns
- Rows changed
- Autowork assert on one cost and one reward, or `INCONCLUSIVE`
- Consumer skill

## Pitfalls

- **Prices hardcoded in the button script** → move them into the table.
- **Float weights** → integer weights so rolls stay reproducible.
- **Rewrote BlaziumBigNum** → `blazium-clicker`.
- **Rebuilt the idle scene** → `blazium-genre-idle`.

## Resources

- `blazium-resources` for `.tres` rows
- `blazium-csv` for large tables

## Related skills

- `blazium-clicker` — BigNum
- `blazium-genre-idle` — idle loop
- `blazium-procedural` — weighted rolls
- `blazium-csv` — table files
