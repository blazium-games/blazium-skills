---
name: blazium-crash-reporter
pack: ship
---

# blazium-crash-reporter

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents invent custom Breakpad uploaders instead of the official sidecar.

## What

Official `crash_reporter` binary: install, `--crash-reporter <path>`, `reporter_filename` / `reporter_path` / `reporter_sha256`, launch flags `--crash-dir --report-id --endpoint --app-id --build-id --contact-url --privacy-url`. Consent required.

**Non-goals:** In-engine `Analytics` / `CrashReporter` (`blazium-crash-analytics`). Recreate the example UI (`blazium-example-crash-sidecar`) or Go ingest (`blazium-example-crash-server`). Custom Breakpad. Cloud crash list.

## How

- Product: https://github.com/blazium-games/blazium_crash_reporter
- Install: `blazium-cli update apply --product crash_reporter`
- Engine writes `{id}.dmp` + `{id}.json`; sidecar presents and uploads after confirm
- Tests: https://github.com/blazium-games/crash_reporter_module_tests

## Reasoning

Sidecar binary is a product, not the in-engine singleton.

## Sources

- https://github.com/blazium-games/blazium_crash_reporter
- https://github.com/blazium-games/crash_reporter_module_tests

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — install product
- `blazium-crash-analytics` — engine singletons + consent
- `blazium-example-crash-sidecar` — fork the UI
- `blazium-example-crash-server` — self-hosted ingest
