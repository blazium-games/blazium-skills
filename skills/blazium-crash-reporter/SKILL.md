---
name: blazium-crash-reporter
description: >
  Installs and wires the official Blazium crash_reporter sidecar (consent UI
  that uploads .dmp + .json). Use for --crash-reporter path, reporter_filename,
  and sidecar CLI flags. Not in-engine Analytics and not a custom Breakpad.
---

# Blazium Crash Reporter

Official sidecar UI. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

This binary does **not** contain Breakpad. The engine writes
`{crash-dir}/{id}.dmp` plus `{id}.json`. The sidecar only presents those
files and uploads after the user confirms.

Install: `blazium-cli update apply --product crash_reporter`.

In-engine `Analytics` / `CrashReporter` consent and ids →
`blazium-crash-analytics`. Cloud list → `blazium-games-mcp`.

**Do not implement a custom Breakpad client.** Do not skip consent.

## When to use

- Use when installing the sidecar or setting `--crash-reporter <path>`.
- Use when exported games need `reporter_filename` / `reporter_path` /
  `reporter_sha256`.

**When not to use:** `Analytics.track` / `set_consent` →
`blazium-crash-analytics`. Dashboard crashes → `blazium-games-mcp`.
Recreate the Go ingest → `blazium-example-crash-server`. Fork the
consent UI → `blazium-example-crash-sidecar`.

## Workflow

1. **Inspect.** Sidecar installed? Engine `CrashReporter.get_resolved_config()`.
2. **Choose.** Editor launch flag vs exported-game neighbor binary.
3. **Implement.** Install product. Point the engine at the binary. Set
   endpoint / app_id / build_id in Project Settings for games.
4. **Verify.** Sidecar launches with a dummy report dir; nothing uploads
   until confirm. Never call `induce_crash()` from headless Autowork.
5. **Handoff.** Same `app_id` / `build_id` to `blazium-crash-analytics` and
   `blazium-games-mcp`.

## Patterns

### Engine finds the binary

- **Editor:** `blazium --crash-reporter <path>` (relative paths resolve next
  to the editor). Editor identity is SCons-baked — no engine `--app-id` /
  `--build-id`.
- **Exported games:** binary next to the executable.
  - `application/crash_reporter/reporter_filename` (default `crash_reporter`
    / `crash_reporter.exe` on Windows)
  - `application/crash_reporter/reporter_path` fallback
  - optional `application/crash_reporter/reporter_sha256` (lowercase hex)

Also set `enabled = true` and `upload_mode = Sidecar` or `Both`
(Disabled / InEngine / Sidecar / Both).

Engine APIs from `crash_reporter_module_tests`:
`is_breakpad_enabled()`, `get_crash_directory()`, `write_minidump()`,
`get_pending_reports()`. CLI `--write-minidump-and-quit` writes a dump
and exits. If Breakpad is off, file checks are skipped (not failed).
Never call `induce_crash()` from headless Autowork.

### Sidecar CLI (engine already resolved identity)

```text
crash_reporter --crash-dir <dir> --report-id <id> --endpoint <url> --app-id <id> --build-id <id> --contact-url <url> --privacy-url <url>
```

The sidecar still accepts `--app-id` / `--build-id`. Sidecar JSON fills
gaps when a flag is omitted. Example fork also supports `--auto-send`
for CI (`SIDECAR_STATUS=`).

Recreate (not the official product): `blazium-example-crash-sidecar`
(consent UI) and `blazium-example-crash-server` (ingest + stackwalk).
Module tests: `crash_reporter_module_tests`.

## Pitfalls

- **Taught Breakpad in the sidecar** → dumps are engine-side; sidecar uploads.
- **Skipped the confirm UI** → forbidden.
- **Called `induce_crash()` in headless tests** → do not.
- **Listed cloud crashes here** → `blazium-games-mcp`.

## Resources

- https://github.com/blazium-games/blazium_crash_reporter
- Tests: https://github.com/blazium-games/crash_reporter_module_tests
- Reference sidecar: https://github.com/blazium-games/example_crash_reporter_project
- Reference ingest: https://github.com/blazium-games/example_crash_reporter_server

## Related skills

- `blazium-cli` — `update apply --product crash_reporter`
- `blazium-crash-analytics` — in-engine Analytics / CrashReporter
- `blazium-example-crash-sidecar` — fork the consent UI
- `blazium-example-crash-server` — self-hosted ingest
- `blazium-games-mcp` — list / download uploads
