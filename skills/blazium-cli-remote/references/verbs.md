# blazium-cli remote verbs

HTTP `/v1` on **6508**. Not MCP. From `blazium-cli/remote/cmd.go`.

## Commands

```text
blazium-cli remote status --json
blazium-cli remote --discover status --json
blazium-cli remote --instance AB3K7M status --json
blazium-cli remote --token "$BLAZIUM_REMOTE_TOKEN" status --json
blazium-cli remote instances --json
blazium-cli remote doctor
blazium-cli remote exec <command> [args...]
blazium-cli remote exec <command> --json-args '{"key":"value"}'
blazium-cli remote list
blazium-cli remote logs
blazium-cli remote errors
blazium-cli remote debugger info|status|stack|breakpoints|error-breaks
blazium-cli remote debugger clear
blazium-cli remote debugger clear --errors --error-breaks
blazium-cli remote debugger clear --logs
blazium-cli remote snapshot editor|scene [-o FILE.png]
blazium-cli remote eval <expression>
blazium-cli remote eval-gdscript <expression>
blazium-cli remote eval-lua <expression>
blazium-cli remote enable --path . --project-port 6508 [--allow-eval]
blazium-cli remote config get|set eval-default|enable-on-open|enable-mcp-on-load
blazium-cli remote failed-run
blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait --wait-timeout 10m
blazium-cli remote autowork status
blazium-cli remote autowork results
```

Persistent select: `--host`, `--port`, `--token` (or `BLAZIUM_REMOTE_TOKEN`),
`--discover` (scan 6500–6520), `--instance <id>`, `--project <path>`.

`exec` takes positional args or `--json-args` (JSON object). Prefer named
commands from `list` over `eval`.

## `autowork run` flags

`--dir`, `--file`, `--test`, `--prefix`, `--suffix`, `--include-subdirs` (default false), `--wait`, `--wait-timeout`.

HTTP exec names: `autowork_run`, `autowork_status`, `autowork_results`.
Snapshot exec: `snapshot_editor` / `snapshot_scene`.

## Ports

| Scan | Range |
|------|-------|
| `--discover` / `instances` | 6500–6520 |
| `doctor` | 6500–6599 |

Game MCP stays **6507**. Hub remote stays **39218**.

## Enable / config

- `enable --allow-eval` writes `blazium/remote_control/allow_eval`.
- `config set enable-mcp-on-load true|false` is a CLI pref in `cli.json`.
- Token: settings or `BLAZIUM_REMOTE_TOKEN`. Prefer loopback.
