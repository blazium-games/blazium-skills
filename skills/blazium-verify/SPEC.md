---
name: blazium-verify
pack: infra
---

# blazium-verify

Falsifiable evidence loop. Engine baseline: **Blazium 0.8.x (Godot 4.8.x
fork)**. Use APIs that exist on `blazium_4.8`.

## Why

Agents declare "it works" from a screenshot or a Grok `code_execution`
session. This skill forces a verdict from Autowork, remote `--json`, or MCP.

## What

Restate claim → one surface → `VERIFIED` / `NOT VERIFIED` / `INCONCLUSIVE`.

**Non-goals:** Playwright, host-only harnesses, Grok `code_execution` as
the runner, writing the whole suite.

## How

1. Name the metric and the fail condition.
2. Run one published runner (Autowork, `blazium-cli remote --json`, JustAMCP).
3. Quote the artifact and return exactly one verdict.
4. On Grok, never treat chat Python as Autowork JSON.

## Reasoning

Distinct from `blazium-autowork` (author tests) and `blazium-ci-watch` (jobs).

## Sources

- Blazium: Autowork, remote_control `/v1`, JustAMCP

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-autowork` — adjacent
- `blazium-cli-remote` — adjacent
- `blazium-ci-watch` — adjacent
