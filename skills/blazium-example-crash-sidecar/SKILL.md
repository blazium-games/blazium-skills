---
name: blazium-example-crash-sidecar
description: >
  Recreates the example crash_reporter consent UI project (lists pending
  .dmp files, uploads after confirm). Use when forking a sidecar beside
  the game. Official product install stays on blazium-crash-reporter.
---

# Blazium example crash sidecar

Reference consent UI. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

This project does **not** contain Breakpad. The engine writes
`{crash-dir}/{id}.dmp` plus `{id}.json`. The sidecar only lists those
files and uploads after the player confirms.

Source of truth: https://github.com/blazium-games/example_crash_reporter_project
Companion ingest: https://github.com/blazium-games/example_crash_reporter_server
Official install: `blazium-cli update apply --product crash_reporter`
(`blazium-crash-reporter`).

## When to use

- Use when the user wants to fork or restyle the example sidecar.
- Use when teaching the engine ↔ sidecar CLI and multipart upload.

**When not to use:** install the official binary →
`blazium-crash-reporter`. Stand up ingest / stackwalk →
`blazium-example-crash-server`. `Analytics.track` / consent flags →
`blazium-crash-analytics`.

## Workflow

1. **Inspect.** Game already has `application/crash_reporter/*`? Official
   product vs fork.
2. **Choose.** Fork this example vs `blazium-cli update apply --product
   crash_reporter`.
3. **Implement.** Blazium project, `scenes/main.tscn`, `scripts/main.gd`
   + `uploader.gd`, export beside the game.
4. **Verify.** Launch with a dummy `--crash-dir` of `.dmp` + `.json`.
   Nothing uploads until Send. `--auto-send` for CI prints
   `SIDECAR_STATUS=`.
5. **Handoff.** Binary path + endpoint. Ingest →
   `blazium-example-crash-server`. Official product →
   `blazium-crash-reporter`.

## Patterns

### CLI contract (engine already resolved identity)

```text
crash_reporter --crash-dir <dir> --report-id <id> --endpoint <url> \
  --app-id <id> --api-key <key> --contact-url <url> --privacy-url <url>
```

Also: `--auto-send` (headless: upload, print `SIDECAR_STATUS=` /
`SIDECAR_DETAIL_BEGIN` … `END`, quit). Flags fill gaps; sidecar JSON is
preferred when present. Empty `--crash-dir` defaults to
`user://crashes` via `OS.get_user_data_dir()/crashes`.

### Files on disk

| File | Role |
|------|------|
| `{id}.dmp` | Engine minidump |
| `{id}.json` | Metadata |
| `{id}.state` | Written `submitted` after HTTP 2xx |

Pending = no `.state` or state ≠ `submitted`. Discard deletes `.dmp`,
`.json`, and `.state`.

### Upload

`scripts/uploader.gd` POSTs to the full endpoint URL (example
`http://127.0.0.1:8090/v1/reports`).

- Boundary: `----BlaziumCrashBoundary`
- Parts: `metadata` (`application/json`), `dump` (`.dmp`,
  `application/octet-stream`), optional `log` (`text/plain`)
- Headers: `User-Agent: BlaziumCrashReporter/example`, optional
  `X-API-Key`
- Success: HTTP 2xx → write `{id}.state` = `submitted`

Then poll up to 5 times (1s):

- `GET {endpoint.rstrip("/")}/{report_id}` — `analysis.crash_reason`
- `GET …/{report_id}/stack` — stackwalk text

Log discovery (if include-logs): `{crash_dir}/../logs/` and
`user://logs/` for `godot.log` or `blazium.log`.

### Project layout

```text
project.blazium          # main scene res://scenes/main.tscn
scenes/main.tscn         # list, detail, endpoint, api key, Send/Discard
scripts/main.gd          # CLI parse, refresh, send/discard, --auto-send
scripts/uploader.gd      # multipart + GET poll
export_presets.cfg       # Windows → bin/crash_reporter.exe
```

UI must state that nothing uploads until confirm. Privacy link from
`--privacy-url`. `api_key` is a public client key — not a secret.

### Export beside the game

1. Export Windows or Linux (`crash_reporter.exe` / `crash_reporter`).
2. Place the binary next to the game (or a subfolder).
3. Game Project Settings:

```
application/crash_reporter/enabled = true
application/crash_reporter/upload_mode = Sidecar   # or Both
application/crash_reporter/reporter_path = <relative path>
application/crash_reporter/endpoint = http://127.0.0.1:8090/v1/reports
application/crash_reporter/app_id = mygame
application/crash_reporter/api_key = public-client-key
```

Also valid: `reporter_filename` (default `crash_reporter` /
`crash_reporter.exe`) and optional `reporter_sha256`.

## Pitfalls

- **Implemented Breakpad in the sidecar** → dumps are engine-side.
- **Skipped the confirm UI** → forbidden except `--auto-send` for CI.
- **Posted to `/v1/events`** → that is analytics, not crashes.
- **Used official product APIs here** → `blazium-crash-reporter`.

## Resources

- https://github.com/blazium-games/example_crash_reporter_project
- Ingest: https://github.com/blazium-games/example_crash_reporter_server
- Tests: https://github.com/blazium-games/crash_reporter_module_tests

## Related skills

- `blazium-crash-reporter` — official sidecar binary
- `blazium-example-crash-server` — ingest + stackwalk
- `blazium-crash-analytics` — in-engine CrashReporter
- `blazium-cli` — `update apply --product crash_reporter`
- `blazium-export` — export preset beside the game
