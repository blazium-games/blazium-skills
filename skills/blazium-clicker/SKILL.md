---
name: blazium-clicker
description: >
  Uses BlaziumBigNum for idle/incremental economies that overflow int/float.
  Use for construct, ops, and serialize of huge numbers (from_string,
  as_string, add/mul). Not a full idle framework, not genre-idle composition,
  and not for normal scores or HP.
when-to-use: >
  BlaziumBigNum, from_string, as_string, overflow int/float, 1e18 cookies,
  clickertools, mantissa exponent
metadata:
  author: blazium-games
  short-description: BlaziumBigNum construct / ops / serialize for idle math
---

# Blazium clicker (BigNum)

Arbitrary-precision numbers — not an idle genre kit. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/clickertools/` — class `BlaziumBigNum` (RefCounted).

Idle/incremental *games* load `blazium-genre-idle`. This skill is numbers
only.

## When to use

- Use when currency / damage would overflow `int` or lose `float` precision.

**When not to use:** normal scores, HP, timers → `int` / `float`. Economy
tables → `blazium-resources` / `blazium-csv`. Saves → `blazium-save-systems`
or `blazium-sqlite` (store `as_string()`). Full idle loop (click, upgrade,
prestige, HUD) → `blazium-genre-idle`.

## Grok host

On Grok, keep context small: read this file for ops, then
`blazium-genre-idle` only if the user asked for a game loop. Spawn
`systems-designer` or `economy-designer` for balance, not for BigNum
wrappers. Child prompts must include the serialized string format and the
4.3.2 pin.

Verify with Autowork `from_string` / `as_string` round-trips. Grok
`code_execution` decimal math is **not** `BlaziumBigNum`.

## Workflow

1. **Inspect.** Will the value exceed ~1e15 or need integer exactness?
2. **Choose.** `BlaziumBigNum` vs built-in numbers.
3. **Implement.** `from_string` / `from_float` / ops / `as_string`.
4. **Verify.** Autowork: `from_string("1e20").add(...)` round-trips.
5. **Handoff.** Serialized strings. Genre loop → `blazium-genre-idle`.

## Patterns

### Construct / ops / serialize

```gdscript
var gold := BlaziumBigNum.from_string("1e18")
gold = gold.add(BlaziumBigNum.from_string("50"))
gold = gold.mul(BlaziumBigNum.from_float(1.1))
var save: String = gold.as_string()
```

Also: `from_mantissa_exponent`, `from_bignum`, `exp`, `sub`, `div`,
`pow_int` / `pow_float`, `root`, `sqroot`, `negate`, `abs_num`,
`compare_to`, `is_equal_to` / `is_greater_than` / `is_less_than`,
`to_pretty_string`, `to_int`, `get_mantissa` / `get_exponent`, `log10`.
Statics: `get_inf` / `get_min` / `get_max` / `get_nan`,
`set_default_max_digits`, `set_default_print_precision`.

Ops return a **new** `BlaziumBigNum` — assign the result.

## Output contract

- Values that use `BlaziumBigNum` vs `int`/`float`
- Serialize format (`as_string()` into save / resource)
- Autowork test name and pass/fail
- Next skill (`blazium-genre-idle`, `blazium-save-systems`, `blazium-csv`)

## Pitfalls

- **Used int for 1e40 cookies** → overflow.
- **Built a whole idle game in this skill** → numbers only; load
  `blazium-genre-idle`.
- **Compared with `==` on wrappers** → `is_equal_to` / `compare_to`.
- **Saved as float** → `as_string()` into sqlite / resources / save slots.
- **Grok Python int used as the economy** → `BlaziumBigNum` in GDScript.

## Resources

- Tests: https://github.com/blazium-games/clickertools_module_tests
- `blazium/modules/clickertools/doc_classes/BlaziumBigNum.xml`

## Related skills

- `blazium-genre-idle` — compose the idle loop
- `blazium-resources` — economy data
- `blazium-save-systems` — `user://` slots
- `blazium-sqlite` — relational save
- `blazium-csv` — balance tables
