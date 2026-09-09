---
name: blazium-example-crash-server
description: >
  Recreates the self-hosted Go crash ingest from example_crash_reporter_server
  (multipart /v1/reports, Breakpad stackwalk, port 8090). Use when standing
  up a local crash sink. Not the official sidecar product and not Games MCP.
---

# Blazium example crash server

Self-hosted Go reference ingest + Breakpad stackwalk. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**. Not a hosted product. Official sidecar install
→ `blazium-crash-reporter`. Recreate the consent UI →
`blazium-example-crash-sidecar`. Cloud list → `blazium-games-mcp`.

Source of truth: https://github.com/blazium-games/example_crash_reporter_server
Companion sidecar: https://github.com/blazium-games/example_crash_reporter_project
Module tests: https://github.com/blazium-games/crash_reporter_module_tests

## When to use

- Use when the user wants a local crash ingest with stackwalk.
- Use when testing sidecar uploads against something other than
  `crash.blazium.app`.

**When not to use:** official `crash_reporter` binary →
`blazium-crash-reporter`. Fork the consent UI →
`blazium-example-crash-sidecar`. In-engine `CrashReporter` settings →
`blazium-crash-analytics`. Analytics events →
`blazium-example-analytics-server`.

## Workflow

1. **Inspect.** CMake + C++17 (MSVC on Windows). Existing Discord webhook?
2. **Choose.** Native `go run` + built `minidump_reader` vs Docker.
3. **Implement.** Go module (`internal/store`, `internal/stackwalk`,
   `internal/discord`), CMake tools, routes, symbol tree.
4. **Verify.** `go test ./...` (mocks stackwalk/Discord; no CMake). Then
   `GET /health` and a multipart POST.
5. **Handoff.** Base URL `http://127.0.0.1:8090/v1/reports`. Sidecar →
   `blazium-example-crash-sidecar`. Official product →
   `blazium-crash-reporter`.

## Patterns

### Build tools and run

```text
cmake -S . -B build -A x64
cmake --build build --config Release
go run . -addr 127.0.0.1:8090 -data ./crash_store
go run . -addr 127.0.0.1:8090 -data ./crash_store \
  -api-key public-client-key \
  -stackwalk-bin build/Release/minidump_reader.exe
go test ./...
docker compose up --build
```

Windows outputs: `build/Release/minidump_reader.exe`,
`build/Release/dump_syms.exe` (DIA SDK). Reader:

```text
minidump_reader [--symbols testdata/symbols] [--out stackwalk.txt] crash.dmp
```

Flags: `-addr` (default `127.0.0.1:8090`), `-data` (default
`crash_store`), `-api-key` or `CRASH_API_KEY`, `-stackwalk-bin` or
`CRASH_STACKWALK_BIN`, `-symbols` or `CRASH_SYMBOLS_DIR`,
`-discord-webhook` or `DISCORD_WEBHOOK_URL`, `-discord-username`
(default `Blazium Crash Reporter`), `-discord-attach-dump`,
`-discord-max-attach-mb` (default 8).

Docker: **8090:8090**, `-stackwalk-bin /minidump_reader`,
`-symbols /symbols`, volume `crash_store:/data`, read-only
`./testdata/symbols:/symbols`, healthcheck `GET /health`.

Webhook URL is a secret — do not commit `.env`.

### HTTP contract

| Method | Path | Result |
|--------|------|--------|
| GET | `/health` | `{"ok":true}` |
| POST | `/v1/reports` | 201 `{"id":"..."}` |
| GET | `/v1/reports` | `[{id, app_id, timestamp}, ...]` |
| GET | `/v1/reports/{id}` | metadata + `dump_url` / `log_url` / `stack_url` / `analysis` / `discord` |
| GET | `/v1/reports/{id}/dump` | `dump.dmp` |
| GET | `/v1/reports/{id}/log` | `log.txt` |
| GET | `/v1/reports/{id}/stack` | `stackwalk.txt` |
| POST | `/v1/reports/{id}/analyze` | `{"id":"...","ok":true}` |

POST is multipart: required `dump` (filename must end `.dmp`),
`metadata` (JSON field or file), optional `log`. Max body **64 MiB**.
Optional `X-API-Key`. CORS enabled.

Stackwalk or Discord failures **do not** fail ingest — still 201.

Store per report: `crash_store/{id}/dump.dmp`, `metadata.json`, optional
`log.txt`, `stackwalk.txt`, `analysis.json`, `discord.json`
(`skipped` / `posted` / `failed`).

```text
curl -F dump=@crash.dmp -F metadata=@crash.json \
  http://127.0.0.1:8090/v1/reports
```

### Metadata JSON

```json
{
  "id": "report-id",
  "engine_version": "...",
  "engine_hash": "...",
  "app_id": "mygame",
  "app_name": "My Game",
  "app_version": "1.2.3",
  "build_channel": "release",
  "os": "Windows",
  "arch": "x86_64",
  "timestamp": "2026-01-01T00:00:00Z"
}
```

Missing `id` falls back to the dump basename, then a timestamp. Missing
`timestamp` is filled UTC RFC3339.

### Symbols and Discord

```text
powershell -File scripts/dump_blazium_symbols.ps1 -Binary path\to\template.exe
```

Or `BLAZIUM_TEMPLATE`. Layout:
`testdata/symbols/<module_name>/<DEBUG_ID>/<module_name>.sym`. Use a
`crash_reporter=yes` template with `debug_symbols=yes`. Do not commit
`.exe`, `.pdb`, or generated `.sym`.

Discord posts an embed (crash reason, `ERROR` / `SCRIPT ERROR` lines,
crashing-thread excerpt) and attaches `stackwalk.txt` (and `log.txt`
when small). `-discord-attach-dump` attaches the minidump under the MiB
cap.

### Game / sidecar wiring

Game Project Settings (engine details → `blazium-crash-analytics`):

```
application/crash_reporter/enabled = true
application/crash_reporter/upload_mode = Sidecar   # or Both
application/crash_reporter/endpoint = http://127.0.0.1:8090/v1/reports
application/crash_reporter/app_id = mygame
application/crash_reporter/api_key = public-client-key
```

Official cloud host is `crash.blazium.app` — different from this example.

## Pitfalls

- **Failed ingest because stackwalk failed** → still 201; check
  `analysis.json` / `discord.json`.
- **Posted a non-`.dmp` dump part** → 400.
- **Taught Breakpad inside the sidecar** → stackwalk lives here.
- **Committed `DISCORD_WEBHOOK_URL`** → secret.

## Resources

- https://github.com/blazium-games/example_crash_reporter_server
- Sidecar: https://github.com/blazium-games/example_crash_reporter_project
- Tests: https://github.com/blazium-games/crash_reporter_module_tests

## Related skills

- `blazium-example-crash-sidecar` — consent UI that POSTs here
- `blazium-crash-reporter` — official sidecar product
- `blazium-crash-analytics` — in-engine CrashReporter
- `blazium-games-mcp` — cloud crash list
- `blazium-example-analytics-server` — events, not dumps
