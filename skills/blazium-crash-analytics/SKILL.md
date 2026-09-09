---
name: blazium-crash-analytics
description: >
  Configures in-engine Analytics and CrashReporter (app_id, build_id,
  consent, crash.blazium.app). Use when enabling telemetry or crash uploads.
  Sidecar binary → blazium-crash-reporter. Cloud list → blazium-games-mcp.
---

# Blazium crash analytics

Runtime telemetry + crash dumps. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Do not disable consent prompts.** Do not implement a custom Breakpad.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Singletons: `Analytics` (`blazium/modules/analytics/`), `CrashReporter`
(`blazium/modules/crash_reporter/`). Shared identity: `get_app_id()` /
`get_build_id()`. Ingest headers: `X-App-Id`, `X-Build-Id`. Upload host:
`crash.blazium.app`.

Editor identity is **SCons-baked** (`editor_app_id`, `editor_build_id`) — no
CLI/env override. Export templates may bake `template_app_id` /
`template_build_id` (export owns baking). Empty template bakes use
Project Settings.

## When to use

- Use when enabling analytics events, crash sidecars, or consent flags.
- Use when wiring `app_id` / `build_id` so Games MCP can find uploads.

**When not to use:** official sidecar binary → `blazium-crash-reporter`.
Self-hosted `/v1/events` sink → `blazium-example-analytics-server`.
Listing/downloading crashes on the dashboard → `blazium-games-mcp`. Baking
ids into export templates → `blazium-export` / `blazium-ci-export`.
Inventing a dump format → stop.

## Workflow

1. **Inspect.** `Analytics.get_resolved_config()`,
   `CrashReporter.get_resolved_config()`, current consent, upload_mode.
2. **Choose.** Consent path (CLI / env / `set_consent`). Upload mode:
   Disabled / InEngine / Sidecar / Both.
3. **Implement.** Do not skip the consent UI. Set Project Settings for
   exported games. Sidecar path / filename → `blazium-crash-reporter`.
4. **Verify.** `get_app_id` / `get_build_id` match the Games cloud game.
   Optional Autowork on `set_consent` / `track` — not a screenshot.
5. **Handoff.** Same ids to `blazium-games-mcp` (`list_game_crashes`).

## Patterns

### Consent (do not skip)

Priority: CLI `--analytics accepted|declined`, then
`BLAZIUM_ANALYTICS_CONSENT`, then Editor Settings or
`Analytics.set_consent(accepted)`.

```gdscript
Analytics.set_consent(true)  # only after the player accepted
Analytics.track("session_start", {})
Analytics.flush()
```

Anonymous mode (default) omits `device_uid`.

### Project Settings and queue

```
application/analytics/enabled
application/analytics/app_id
application/analytics/build_id
application/analytics/endpoint
application/analytics/anonymous
```

Empty endpoint = queue only. Live POST: set the endpoint or
`ANALYTICS_ENDPOINT`. `get_resolved_config()` exposes `queue_dir`; events
append `{queue_dir}/events.jsonl`. `track` increments `get_queue_size()`.
`set_anonymous(true|false)` / `is_anonymous()` / `is_enabled()`.

Anonymous JSONL events must include `os_name` and `locale`, must omit
`device_uid`, and must not include editor keys (`export_platform`,
`editor_video_driver`).

`ANALYTICS_LIVE=1` plus a running sink enables the live flush in
`analytics_module_tests` (CLI `--track-and-quit`). Recreate the sink →
`blazium-example-analytics-server`.

### Identity

`CrashReporter.get_app_id()` and `Analytics.get_app_id()` must match.
See `get_resolved_config()` / `get_upload_mode()`. Sidecar launch flags →
`blazium-crash-reporter`. Never call `induce_crash()` from headless Autowork.

## Pitfalls

- **Disabled consent to “make CI green”** → forbidden. Fail the task instead.
- **CLI override of editor app_id** → does not exist; ids are baked.
- **Read crashes from this skill** → use `blazium-games-mcp`.
- **Custom minidump uploader** → use CrashReporter + `crash.blazium.app`.
- **Wrote `device_uid` on anonymous events** → omit it.

## Resources

- `blazium/modules/analytics/doc_classes/Analytics.xml`
- `blazium/modules/crash_reporter/doc_classes/CrashReporter.xml`
- Cloud read path: `blazium-games-mcp`
- Tests: https://github.com/blazium-games/analytics_module_tests
- Tests: https://github.com/blazium-games/crash_reporter_module_tests
- Reference ingest: https://github.com/blazium-games/example_analytics_server

## Related skills

- `blazium-crash-reporter` — official sidecar binary
- `blazium-example-analytics-server` — self-hosted `/v1/events`
- `blazium-games-mcp` — list / download crashes
- `blazium-export` — bake template ids
- `blazium-ci-export` — `X-Build-Id` in CI
