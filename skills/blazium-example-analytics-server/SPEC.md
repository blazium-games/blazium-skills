---
name: blazium-example-analytics-server
pack: live-ops
---

# blazium-example-analytics-server

Recreate the self-hosted Go analytics ingest. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Games need a local `/v1/events` sink that matches the engine `Analytics` flush. Cloud MCP is a different backend.

## What

Go 1.23 server: `-addr` / `-data` / `-api-key`, JSONL store, POST/GET `/v1/events`, Docker on port 8091.

**Non-goals:** In-engine `Analytics` APIs (`blazium-crash-analytics`). Games MCP cloud reads. In-game `HTTPServer`. Crash dumps (`blazium-example-crash-server`).

## How

- Flags: `-addr` default `127.0.0.1:8091`, `-data` default `analytics_store`, `-api-key` or `ANALYTICS_API_KEY`.
- Routes: `GET /health`, `POST /v1/events` (object / array / `{events:[]}` → 202), `GET /v1/events?app_id&build_id&anonymous&limit`.
- Store: `{data}/{app_id}/{build_id}.jsonl` (`_none` if build_id empty). Max body 8 MiB. CORS. Optional `X-API-Key`.
- Verify: `go test ./...`, `scripts/smoke.sh`, then `ANALYTICS_LIVE=1` in analytics_module_tests.

## Reasoning

Recreating the ingest is a different job from configuring the engine singleton.

## Sources

- https://github.com/blazium-games/example_analytics_server
- https://github.com/blazium-games/analytics_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-crash-analytics` — engine Analytics
- `blazium-games-mcp` — cloud reads
- `blazium-example-crash-server` — crash ingest
