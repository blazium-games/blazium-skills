---
name: blazium-clicker
pack: modules
---

# blazium-clicker

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

`BlaziumBigNum` changes idle/incremental math. Agents will overflow `int`/`float`.

## What

Arbitrary-precision numbers for clicker economies. Construct, ops, serialize.

**Non-goals:** Do not use this in normal games. Do not invent a full idle framework.

## How

- Module: `blazium/modules/clickertools/` class `BlaziumBigNum`.
- Pair later with a clicker genre adapter.

## Reasoning

Small module, high genre impact.

## Sources

- clickertools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-resources` — economy data
- `blazium-sqlite` — save
