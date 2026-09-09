---
name: blazium-hub
pack: ship
---

# blazium-hub

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents confuse Hub with Services login and invent Hub install verbs.

## What

Desktop Hub UI (Projects/Editors/News/Settings/tray), `hub.json`, `hub-remote ensure` (never rotates a valid token), port **39218**, `blazium://hub`, `blazium://project/<encoded-path>`. Headless: `BlaziumHub --headless --ensure-hub-remote`. Hub shells `blazium-cli --json`; it does not install editors.

**Non-goals:** Top-level `install` / `templates` / `update apply` (`blazium-cli`). Services/lobby. Crash sidecar.

## How

- Product: https://github.com/blazium-games/blazium-hub
- Install: `blazium-cli update apply --product hub`
- Remote: `hub_remote.json`, `/v1/health` on 39218
- URI: `blazium-cli handle-uri blazium://hub`
- Autowork: `-s run_tests.gd` for mixed suffixes; AutoworkConfig before Luau dirs; `validate_all.ps1 -JUnit` → `--aw-junit=`

## Reasoning

Hub window is not the CLI install surface and not cloud identity.

## Sources

- https://github.com/blazium-games/blazium-hub

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — install / update
- `blazium-cli-remote` — running game/editor HTTP
