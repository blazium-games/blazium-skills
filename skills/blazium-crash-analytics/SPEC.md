---
name: blazium-crash-analytics
pack: live-ops
---

# blazium-crash-analytics

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Agents skip consent and build IDs.

## What

Configure in-engine `Analytics` + `CrashReporter`. Bake `app_id`/`build_id`. Consent flags. Read crashes via Games MCP.

**Non-goals:** Official sidecar binary (`blazium-crash-reporter`). Recreate the Go `/v1/events` sink (`blazium-example-analytics-server`). Custom Breakpad. Do not disable consent prompts.

## How

- `blazium/modules/analytics/` class `Analytics`.
- `blazium/modules/crash_reporter/` class `CrashReporter`. Upload `crash.blazium.app`.
- CLI: `--analytics accepted|declined`.
- Headers: `X-App-Id`, `X-Build-Id`.
- Tests: https://github.com/blazium-games/analytics_module_tests
- Tests: https://github.com/blazium-games/crash_reporter_module_tests

## Reasoning

Runtime telemetry is not the sidecar product.

## Sources

- https://github.com/blazium-games/analytics_module_tests
- https://github.com/blazium-games/example_analytics_server

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-crash-reporter` — sidecar binary
- `blazium-example-analytics-server` — self-hosted ingest
- `blazium-games-mcp` — read crashes
- `blazium-export` — bake ids into templates
- `blazium-ci-export` — X-Build-Id in CI
