---
name: blazium-playtest
description: >
  Writes a playtest note with repro steps and one Autowork regression assert
  for the failure found in a session. Use after someone plays the build.
  Authoring the whole suite stays on blazium-autowork. Claim verdicts stay
  on blazium-verify.
---

# Blazium playtest

Session notes that become one regression. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

Do not invent a second test runner. The assert is Autowork
(`blazium-autowork`). A pass/fail claim about the product is
`blazium-verify`.

## When to use

- Use when a play session found a bug and you need repro steps plus a
  regression assert.
- Use when listing what the session did not cover.

**When not to use:** writing the suite → `blazium-autowork`. Proving a
claim → `blazium-verify`. Designing the level → `blazium-level-design`.

## Grok host

Read this file only. Spawn `qa-tester` or `qa-lead`. Child prompts must
include build identity, steps, and the assert path. Evidence is the note
plus the Autowork result or `INCONCLUSIVE`.

## Workflow

1. **Inspect.** Build, scene, and what the player tried.
2. **Choose.** One failure to lock. Park the rest as follow-ups.
3. **Implement.** Write steps that another person can repeat. Add one
   Autowork `test_*` that fails before the fix and passes after.
4. **Verify.** Run that test. Quote the result. Do not treat a screenshot
   of the session as the regression.
5. **Handoff.** Note path, test path, and the fixer.

## Patterns

Note fields: build, scene, input steps, expected, actual, severity.
One regression per note. If the failure is not assertable yet, say
`INCONCLUSIVE` and keep the steps.

## Output contract

- Session scene and build
- Repro steps
- Autowork test path and result, or `INCONCLUSIVE`
- Follow-ups not covered

## Pitfalls

- **Replaced Autowork with a new harness** → `blazium-autowork`.
- **Passed the build from a screenshot** → quote the test or say inconclusive.
- **Bundled five bugs in one assert** → one failure, one test.
- **Skipped expected vs actual** → the fixer cannot tell what broke.

## Resources

- `blazium-autowork` for the assert syntax

## Related skills

- `blazium-autowork` — test authoring
- `blazium-verify` — claim verdicts
- `blazium-level-design` — layout intent
