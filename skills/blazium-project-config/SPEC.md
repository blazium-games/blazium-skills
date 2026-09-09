---
name: blazium-project-config
pack: infra
---

# blazium-project-config

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

`project.blazium` vs `project.godot` and ~588 `blazium/*` settings are invisible to Godot skills. Every other skill assumes this file is correct.

## What

Create or migrate the project file. Pin editor version. Enable MCP, remote_control, Autowork, and Services keys safely. List dangerous flags.

**Non-goals:** Do not invent ProjectSettings keys. Do not enable privileged remote eval or Autowork E2E by default.

## How

- Prefer `project.blazium` (CLI `blazium-cli/hub/projects.go`).
- Namespaces: `blazium/justamcp/*`, `blazium/remote_control/*` (`server_port` default **6508**), `blazium/semanticsearch/*`, `blazium/assettags/*`, `blazium/coldstorage/*`, `blazium/autowork/e2e_enabled`, `blazium/autowork/show_runtime_ui` (default false), `blazium/gif/*`.
- Log path default `user://logs/blazium.log`.
- CLI: `hub load`, `hub open`.
- Migrate-from-Godot: keep `project.godot` readable; add `blazium/` keys; do not claim 4.7 features.

## Reasoning

Router detects the project; this skill owns the settings cookbook.

## Sources

- Blazium: `blazium/doc/classes/ProjectSettings.xml`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-router` — detects the file this skill edits
- `blazium-mcp` — justamcp keys
- `blazium-cli-remote` — remote_control keys
- `blazium-new-project` — writes the initial file
