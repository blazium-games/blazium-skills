---
name: blazium-ci-export
pack: ship
---

# blazium-ci-export

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

GitHub Actions exist (`setup-blazium-engine`, `setup-blazium-cli`, `export-blazium-game`, `deploy-blazium-game`) but no agent skill.

## What

Wire a CI matrix: install editor, export, deploy keys from Games MCP, `X-Build-Id` / crash headers, Autowork job.

**Non-goals:** Do not rewrite engine SCons CI (`ci_cd` editor_deploy) unless the user is working on the engine itself.

## How

- Actions: `github_actions/setup-blazium-engine`, `setup-blazium-cli`, `export-blazium-game`, `deploy-blazium-game`.
- Hub Autowork: `blazium-hub/.github/workflows/autowork.yml` as a pattern.
- Headless GDScript-only: `blazium --headless --aw-dir=res://tests/gdscript`. Mixed / Hub: `-s run_tests.gd`.

## Reasoning

Official GitHub Actions own game export/deploy. This skill wires them.

## Sources

- github_actions/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-export` — local export
- `blazium-games-mcp` — keys
- `blazium-autowork` — test job
- `blazium-crash-analytics` — build ids
