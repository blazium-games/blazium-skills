---
name: blazium-verify
pack: infra
---

# blazium-verify

Falsifiable evidence loop. Engine baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents declare "it works" from a screenshot. This skill forces a verdict
from Autowork, remote, or MCP.

## What

Restate claim → one surface → `VERIFIED` / `NOT VERIFIED` / `INCONCLUSIVE`.

**Non-goals:** Playwright, host-only harnesses, writing the whole suite.

## How

1. Name the metric.
2. Run one published runner.
3. Quote the artifact and verdict.

## Reasoning

Distinct from `blazium-autowork` (author tests) and `blazium-ci-watch` (jobs).

## Sources

- Blazium: Autowork, remote_control `/v1`, JustAMCP

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-autowork` — adjacent
- `blazium-cli-remote` — adjacent
- `blazium-ci-watch` — adjacent
