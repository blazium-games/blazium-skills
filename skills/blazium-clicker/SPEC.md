---
name: blazium-clicker
pack: modules
---

# blazium-clicker

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

`BlaziumBigNum` changes idle/incremental math. Agents will overflow `int`/`float` or invent a Python big-int runner.

## What

Arbitrary-precision numbers for clicker economies. Construct, ops, serialize.

**Non-goals:** Do not use this in normal games. Do not invent a full idle framework (`blazium-genre-idle`).

## How

- Module: `blazium/modules/clickertools/` class `BlaziumBigNum`.
- Construct: `from_string`, `from_float`, `from_mantissa_exponent`.
- Ops return a new instance — assign the result.
- Serialize with `as_string()` into `user://` saves or SQLite text columns.
- Pair the *game loop* with `blazium-genre-idle`.
- Verify Autowork round-trips. Do not treat Grok `code_execution` as BigNum.

## Reasoning

Small module, high genre impact. Distinct from the idle genre adapter so the router can load numbers without a HUD/save kit.

## Sources

- clickertools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-genre-idle` — idle loop composition
- `blazium-resources` — economy data
- `blazium-save-systems` — user:// slots
- `blazium-sqlite` — save
- `blazium-csv` — balance tables
