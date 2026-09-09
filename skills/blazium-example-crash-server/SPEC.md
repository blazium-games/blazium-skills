---
name: blazium-example-crash-server
pack: ship
---

# blazium-example-crash-server

Recreate the self-hosted Go crash ingest + Breakpad stackwalk. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Sidecar uploads need a `/v1/reports` sink with optional stackwalk. Official cloud and the sidecar binary are different jobs.

## What

Go server + CMake `minidump_reader` / `dump_syms`. Multipart ingest, filesystem store, Discord webhook, Docker on port 8090.

**Non-goals:** Official sidecar install (`blazium-crash-reporter`). Consent UI project (`blazium-example-crash-sidecar`). In-engine CrashReporter (`blazium-crash-analytics`). Analytics events.

## How

- Flags: `-addr` `127.0.0.1:8090`, `-data`, `-api-key` / `CRASH_API_KEY`, `-stackwalk-bin` / `CRASH_STACKWALK_BIN`, `-symbols` / `CRASH_SYMBOLS_DIR`, Discord flags / `DISCORD_WEBHOOK_URL`.
- POST `/v1/reports` multipart `dump` + `metadata` + optional `log` → 201. GET list/detail/dump/log/stack. POST `/{id}/analyze`.
- Store `crash_store/{id}/`. Max 64 MiB. Stackwalk/Discord errors do not fail ingest.
- Verify: `go test ./...` then a real multipart POST.

## Reasoning

Ingest + stackwalk is not the sidecar UI and not the official product install.

## Sources

- https://github.com/blazium-games/example_crash_reporter_server
- https://github.com/blazium-games/crash_reporter_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-example-crash-sidecar` — UI that uploads here
- `blazium-crash-reporter` — official product
- `blazium-crash-analytics` — engine singleton
