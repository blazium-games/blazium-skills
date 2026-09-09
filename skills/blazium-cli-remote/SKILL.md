---
name: blazium-cli-remote
description: >
  Controls a running Blazium editor or game via blazium-cli remote (HTTP /v1
  remote_control, default port 6508). Use for status, exec, eval, logs,
  debugger, snapshot, instance discovery, doctor, and Autowork from CI.
  Do not use for editor JustAMCP (blazium-mcp), res://mcp game tools
  (blazium-game-mcp), or cloud Games MCP (blazium-games-mcp).
---

# Blazium CLI remote

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Engine: `blazium/modules/remote_control/`  
CLI: `blazium-cli/remote/`  
Default port: **6508** (game MCP stays **6507**)

Command catalog: [references/verbs.md](references/verbs.md).

## When to use

- Use when the editor is already running and you need HTTP automation.
- Use when CI must `exec`, `eval`, `snapshot`, or `autowork run` without JustAMCP.
- Use when diagnosing instance ports (`doctor`, `instances`).

**When not to use:** authoring Autowork tests → `blazium-autowork`. Editor MCP
catalog → `blazium-mcp`. In-game REST you ship to players →
`blazium-httpserver`. Do not eval untrusted code when `allow_eval` is off.

## Workflow

1. **Inspect.** `blazium/remote_control/server_enabled`, `server_port`,
   `allow_eval`, `token`, `bind_address`. Prefer loopback.
2. **Auth.** Token in settings or `BLAZIUM_REMOTE_TOKEN`.
3. **Discover.** `--discover` scans **6500–6520**. `doctor` scans **6500–6599**.
4. **Act.** Prefer `status` / `exec` / `autowork` over `eval`. Use `--json`.
   Select with `--discover`, `--instance`, `--token` / `BLAZIUM_REMOTE_TOKEN`.
   Never hang on a prompt.
5. **Handoff.** Report instance URL, command, and evidence.

## Patterns

```bash
blazium-cli remote status --json
blazium-cli remote --discover status --json
blazium-cli remote doctor
blazium-cli remote errors
blazium-cli remote debugger stack
blazium-cli remote debugger clear
blazium-cli remote exec snapshot_editor
blazium-cli remote snapshot editor
blazium-cli remote snapshot scene -o play.png
blazium-cli remote enable --path . --project-port 6508 --allow-eval
blazium-cli remote config set enable-mcp-on-load true
blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait --wait-timeout 10m --json
```

`exec` takes `[args...]` or `--json-args '{}'`. Same agent rules as
`blazium-cli`: flags first, incremental `--help`, `--json`, no invented verbs.

Default Autowork dir if unset: `res://test` if it exists, else `res://`.
`include_subdirs` defaults **false**. Hub remote stays **39218**.

Leave `allow_eval` false unless the user needs it. Prefer `exec` of known
commands. Never bind `0.0.0.0` unless the user wants LAN exposure.

## Pitfalls

- **Treated this as MCP** → `/v1` HTTP, not `POST /mcp`.
- **Nothing listening on 6508** → remote disabled, or the project still uses 6507.
- **`--aw-*` on the editor** → starts Autowork, not remote_control; enable the setting.
- **Autowork `include_subdirs` false** → default; pass `--include-subdirs`.

## Resources

- Tests: https://github.com/blazium-games/remote_control_module_tests
- [references/verbs.md](references/verbs.md)

## Related skills

- `blazium-mcp` — MCP when the editor is the target
- `blazium-autowork` — write the tests this CLI runs
- `blazium-game-mcp` — game MCP on 6507
- `blazium-ci-export` — GHA export / Autowork jobs
