---
name: blazium-example-analytics-server
description: >
  Recreates the self-hosted Go analytics ingest from example_analytics_server
  (JSONL store, POST /v1/events, port 8091). Use when standing up a local
  analytics sink for a Blazium game. Not Games MCP cloud analytics and not
  in-game HTTPServer.
---

# Blazium example analytics server

Self-hosted Go reference ingest. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Not a hosted product. Official cloud reads stay on
`blazium-games-mcp`. In-engine `Analytics` APIs stay on
`blazium-crash-analytics`.

Source of truth: https://github.com/blazium-games/example_analytics_server
(Go 1.23, single `main.go`). Live loop:
https://github.com/blazium-games/analytics_module_tests

## When to use

- Use when the user wants a local analytics server for their game.
- Use when wiring `ANALYTICS_ENDPOINT` / `application/analytics/endpoint`
  to something other than the official cloud.

**When not to use:** `Analytics.set_consent` / `track` / `flush` →
`blazium-crash-analytics`. Dashboard queries → `blazium-games-mcp`.
In-game REST → `blazium-httpserver`. Crash dumps →
`blazium-example-crash-server`.

## Workflow

1. **Inspect.** Does a sink already exist? Cloud vs self-hosted.
2. **Choose.** Local `go run` vs `docker compose`. Optional `X-API-Key`.
3. **Implement.** Scaffold the Go module, routes, JSONL store, Docker.
4. **Verify.** `go test ./...`, `GET /health`, POST one event, then
   `Analytics.flush()` from the game (or `ANALYTICS_LIVE=1` in
   `analytics_module_tests`).
5. **Handoff.** Base URL + whether a key is required. Engine settings →
   `blazium-crash-analytics`.

## Patterns

### Scaffold and run

```text
go run . -addr 127.0.0.1:8091 -data ./analytics_store
go run . -addr 127.0.0.1:8091 -data ./analytics_store -api-key public-client-key
go test ./...
docker compose up --build --wait
```

Flags: `-addr` (default `127.0.0.1:8091`), `-data` (default
`analytics_store`), `-api-key`. Empty `-api-key` falls back to
`ANALYTICS_API_KEY`. Copy `.env.example` → `.env`; do not commit `.env`.

Docker: publish **8091:8091**, listen `0.0.0.0:8091`, volume `/data`,
healthcheck `GET /health`.

### HTTP contract

| Method | Path | Result |
|--------|------|--------|
| GET | `/health` | `{"ok":true}` |
| POST | `/v1/events` | 202 `{"ok":true,"count":N}` |
| GET | `/v1/events` | `{"events":[...],"count":N}` |

POST body is one object, an array, or `{ "events": [...] }`. Empty
`app_id` is rejected. Max body **8 MiB**. CORS:
`Access-Control-Allow-Origin: *`, headers `Content-Type, X-API-Key`,
methods `GET, POST, OPTIONS`.

GET query: `app_id`, `build_id`, `anonymous`, `limit` (default 100).

Optional `X-API-Key` when a key is configured. Empty key = no auth.

Store: `analytics_store/{app_id}/{build_id}.jsonl`. Empty `build_id` →
`_none`. Reject path segments with `..`, slashes, or non-printable chars.

### Event JSON

Identity is top-level. Anonymous events **omit** `device_uid`.

```json
{
  "app_id": "my-game",
  "build_id": "1.2.0+gabcdef",
  "app_version": "1.2.0",
  "build_channel": "beta",
  "engine_version": "4.8.0.blazium",
  "session_id": "uuid",
  "anonymous": true,
  "event": "session_start",
  "timestamp": "2026-08-17T00:00:00Z",
  "properties": {}
}
```

Identified events: `"anonymous": false` plus `"device_uid"`.

```text
curl -sS http://127.0.0.1:8091/health
curl -sS -H "Content-Type: application/json" \
  -d '{"app_id":"my-game","event":"session_start","anonymous":true}' \
  http://127.0.0.1:8091/v1/events
curl -sS "http://127.0.0.1:8091/v1/events?app_id=my-game"
```

`scripts/smoke.sh` uses `ANALYTICS_SMOKE_URL` (default
`http://127.0.0.1:8091`).

### Game wiring

Hand off class details to `blazium-crash-analytics`. This skill only
sets the sink:

```
application/analytics/enabled = true
application/analytics/app_id = my-game
application/analytics/build_id
application/analytics/endpoint = http://127.0.0.1:8091/v1/events
```

Env override: `ANALYTICS_ENDPOINT`. If the server has a key, send matching
`X-API-Key` (this example does **not** use cloud `X-App-Id` /
`X-Build-Id` headers).

```gdscript
Analytics.set_consent(true)  # only after the player accepted
Analytics.track("session_start", {})
Analytics.flush()
```

## Pitfalls

- **Taught this as crash.blazium.app** → different host and headers.
- **Used in-game HTTPServer** → this is an external Go process.
- **Stored `device_uid` on anonymous events** → omit it.
- **Committed `.env` with `ANALYTICS_API_KEY`** → public client key still
  stays out of git.

## Resources

- https://github.com/blazium-games/example_analytics_server
- Tests: https://github.com/blazium-games/analytics_module_tests

## Related skills

- `blazium-crash-analytics` — in-engine Analytics / consent
- `blazium-games-mcp` — cloud analytics reads
- `blazium-httpserver` — in-game HTTP listen
- `blazium-example-crash-server` — crash ingest, not events
