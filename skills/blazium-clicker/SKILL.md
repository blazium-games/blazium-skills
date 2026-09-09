---
name: blazium-clicker
description: >
  Uses BlaziumBigNum for idle/incremental economies that overflow int/float.
  Use for construct, ops, and serialize of huge numbers. Not a full idle
  framework and not for normal games.
---

# Blazium clicker (BigNum)

Arbitrary-precision numbers — not an idle genre kit. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/clickertools/` — class `BlaziumBigNum` (RefCounted).

Idle/incremental loops also load a `blazium-genre-*` adapter if the user
named a genre. This skill is numbers only.

## When to use

- Use when currency / damage would overflow `int` or lose `float` precision.

**When not to use:** normal scores, HP, timers → `int` / `float`. Economy
tables → `blazium-resources` / `blazium-csv`. Saves → `blazium-sqlite`
(store `as_string()`).

## Workflow

1. **Inspect.** Will the value exceed ~1e15 or need integer exactness?
2. **Choose.** `BlaziumBigNum` vs built-in numbers.
3. **Implement.** `from_string` / `from_float` / ops / `as_string`.
4. **Verify.** Autowork: `from_string("1e20").add(...)` round-trips.
5. **Handoff.** Serialized strings. Genre loop → .

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

## Pitfalls

- **Used int for 1e40 cookies** → overflow.
- **Built a whole idle game in this skill** → numbers only.
- **Compared with `==` on wrappers** → `is_equal_to` / `compare_to`.
- **Saved as float** → `as_string()` into sqlite / resources.

## Resources

- Tests: https://github.com/blazium-games/clickertools_module_tests

- `blazium/modules/clickertools/doc_classes/BlaziumBigNum.xml`
- Tests: github.com/blazium-games/clickertools_module_tests

## Related skills

- `blazium-resources` — economy data
- `blazium-sqlite` — save
- `blazium-csv` — balance tables
