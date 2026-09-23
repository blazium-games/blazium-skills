---
name: blazium-playtest
pack: growth
---

# blazium-playtest

Play session notes and one regression assert. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

A session without steps and a failing assert disappears. The suite skill should not own the note format.

## What

Repro notes and a single Autowork regression.

**Non-goals:** the full suite, product claim verdicts.

## How

1. Record steps, expected, and actual.
2. Add one Autowork test.
3. Quote the run.

## Reasoning

Distinct from `blazium-autowork` (how to write tests) and `blazium-verify` (verdicts).

## Sources

- Blazium Autowork `test_*`

## Limits

Do not invent a test framework. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-autowork` — suite
- `blazium-verify` — verdicts
