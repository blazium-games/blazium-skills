---
name: blazium-cli-remote
pack: infra
---

# blazium-cli-remote

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Headless and CI agents cannot click the editor. `blazium-cli remote` talks HTTP `/v1` on a running instance.

## What

Use `blazium-cli remote status|list|exec|eval|logs|errors|debugger|snapshot|autowork|instances|enable|doctor|config`. `--discover` scans 6500–6520; `doctor` scans 6500–6599. Auth with token / `BLAZIUM_REMOTE_TOKEN`.

**Non-goals:** Do not teach Autowork test authoring (that is `blazium-autowork`). Do not treat this as MCP. Do not eval untrusted code when `allow_eval` is off.

## How

- Engine: `blazium/modules/remote_control/`. CLI: `blazium-cli/remote/`.
- Settings: `blazium/remote_control/server_enabled`, `server_port` (6508), `allow_eval`, `token`, `bind_address`.
- Cross-ref: `HTTPServer` sibling (`blazium-httpserver`), Autowork E2E, Luau eval sandbox.
- Autowork invoke: `blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait`.
- Default Autowork dir if unset: `res://test` else `res://`. `include_subdirs` honored (default false).
- CLI `DefaultConfig` / `--project-port` / profile fallback: **6508**. Game MCP stays **6507**. Hub remote stays **39218**. Run `doctor` if ports collide.
- `enable --allow-eval`. `config set enable-mcp-on-load`. Catalog: `references/verbs.md`.

## Reasoning

Complements JustAMCP. Required for GitHub Actions and multi-instance. Invokes Autowork; does not author tests.

## Sources

- Blazium: `blazium-cli/remote/`, `blazium/modules/remote_control/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-mcp` — MCP instead of HTTP when editor is the target
- `blazium-autowork` — write tests this CLI runs
- `blazium-httpserver` — in-game HTTP, not editor remote
- `blazium-ci-export` — CI uses remote + headless
