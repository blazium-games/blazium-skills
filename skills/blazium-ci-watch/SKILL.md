---
name: blazium-ci-watch
description: >
  Watches Blazium export/CI, reads the first failing job, and hands off to
  blazium-ci-export or Autowork. Use when GitHub Actions or a local export
  job failed. One failure at a time. Use gh only when the repo is on GitHub.
---

# Blazium CI watch

First failing job, then a focused fix. Baseline: **Blazium 0.6.x (Godot
4.3.2 fork)**. Host-neutral: Claude, Cursor, and Codex use the same steps.

Fix **one** actionable failure, then re-check. Do not refactor the matrix.

## When to use

- Use when a game repo’s export, Autowork, or deploy workflow failed.
- Use after a ship push when the user asked to watch CI.

**When not to use:** local export presets → `blazium-export`. Authoring the
workflow from scratch → `blazium-ci-export`. Proving a gameplay claim →
`blazium-verify`. Engine SCons `ci_cd` unless the user is on the engine.

## Workflow

1. **Detect.** GitHub remote → `gh`. Otherwise read the local export /
   Autowork log the user pointed at.
2. **Inspect.** First failing job name, command, and excerpt.
   GitHub: `gh run list` / `gh run view <id> --log-failed` (or
   `gh pr checks` when a PR exists).
3. **Classify.** Setup/install → `blazium-cli`. Preset mismatch →
   `blazium-export` / `blazium-ci-export`. `test_*` fail →
   `blazium-autowork`.
4. **Fix smallest.** One file or one flag.
5. **Re-check.** Same job. Stop when green or when the next failure is new.
6. **Handoff.** Job name, excerpt, files touched.

## Patterns

```text
# GitHub present
gh run list --limit 5
gh run view <id> --log-failed

# Local Autowork (no gh)
blazium --headless --path "$PROJECT" --aw-dir=res://tests/gdscript
# or
blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait --json
```

Official actions stay `setup-blazium-engine`, `setup-blazium-cli`,
`export-blazium-game`, `deploy-blazium-game`. Do not invent action names.

## Pitfalls

- **Fixed three jobs at once** → one failure per pass.
- **Assumed every repo has `gh`** → local logs are valid evidence.
- **Touched engine `ci_cd`** → game workflows only unless asked.
- **Invented `blazium-cli hub install`** → not a verb.

## Related skills

- `blazium-ci-export` — workflow files
- `blazium-autowork` — failing `test_*`
- `blazium-cli` — install / templates in CI
- `blazium-export` — local presets
- `blazium-verify` — gameplay evidence, not jobs
