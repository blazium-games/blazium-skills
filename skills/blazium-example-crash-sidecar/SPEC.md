---
name: blazium-example-crash-sidecar
pack: ship
---

# blazium-example-crash-sidecar

Recreate the example crash consent UI. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Teams fork the example sidecar to restyle consent. The official product install is a different path.

## What

Blazium project: CLI contract, pending `.dmp`/`.json`/`.state`, multipart upload, stack poll, `--auto-send`.

**Non-goals:** Official `blazium-cli update apply --product crash_reporter`. Breakpad / stackwalk (`blazium-example-crash-server`). In-engine CrashReporter APIs.

## How

- CLI: `--crash-dir`, `--report-id`, `--endpoint`, `--app-id`, `--api-key`, `--contact-url`, `--privacy-url`, `--auto-send`.
- Upload boundary `----BlaziumCrashBoundary`; parts `metadata`, `dump`, optional `log`.
- Poll `GET {endpoint}/{id}` and `/{id}/stack` (5 × 1s).
- Export `crash_reporter.exe` beside the game; set `reporter_path` / `upload_mode`.

## Reasoning

Forking the UI is not installing the official binary and not writing the ingest server.

## Sources

- https://github.com/blazium-games/example_crash_reporter_project
- https://github.com/blazium-games/example_crash_reporter_server

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-crash-reporter` — official product
- `blazium-example-crash-server` — ingest
- `blazium-crash-analytics` — engine singleton
