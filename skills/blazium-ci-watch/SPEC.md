---
name: blazium-ci-watch
pack: ship
---

# blazium-ci-watch

Watch and triage export/CI. Engine baseline: **Blazium 0.8.x (Godot 4.8.x
fork)**. Use APIs that exist on `blazium_4.8`.

## Why

Agents either ignore CI or rewrite the whole matrix. This skill reads the
first failure.

## What

Inspect GitHub or local logs, classify, hand to ci-export / Autowork / CLI.

**Non-goals:** Playwright smoke, host-only watchers, engine SCons CI.

## How

1. Detect `gh` vs local logs.
2. Quote the first failing command.
3. Fix one cause; re-check.

## Reasoning

Distinct from `blazium-ci-export` (author workflows) and `blazium-verify`
(gameplay claims).

## Sources

- Blazium: `github_actions/`, Autowork, `blazium-cli`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-ci-export` — adjacent
- `blazium-autowork` — adjacent
- `blazium-verify` — adjacent
