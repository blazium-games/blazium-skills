---
name: blazium-project-config
description: >
  Creates or migrates project.blazium / project.godot and safe blazium/*
  ProjectSettings (JustAMCP, remote_control, Autowork, tags). Use when pinning
  the editor, enabling MCP/remote, migrating from Godot, or auditing dangerous
  flags such as allow_eval or bind 0.0.0.0. Not .env secrets and not a
  greenfield scaffold.
when-to-use: >
  project.blazium, ProjectSettings, blazium/justamcp, remote_control,
  allow_eval, bind 0.0.0.0, migrate from Godot, config_version
metadata:
  author: blazium-games
  short-description: Own project.blazium and safe blazium/* settings
---

# Blazium project config

Own the project file and `blazium/*` settings. Other infra skills assume
this is correct. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Prefer **`project.blazium`** (`blazium-cli` hub does). `project.godot` remains
readable for Godot tools.

Do not invent ProjectSettings keys. Do not enable privileged eval or Autowork
E2E by default.

## When to use

- Use when creating or migrating the project file.
- Use when enabling JustAMCP, remote_control, or Autowork settings.
- Use when a Godot project needs `blazium/` keys.

**When not to use:** greenfield scaffold of tests/MCP files →
`blazium-new-project` (then return here for settings). Connecting MCP after
settings are correct → `blazium-mcp`. `.env` / `.ini` secrets →
`blazium-config`.

## Grok host

On Grok, read `project.blazium` (or `project.godot`) with `read_file` before
any patch. Spawn `blazium-specialist` or `tools-programmer` only for the
settings edit. Child prompts must list the exact keys to change and the
4.3.2 pin.

Do not invent `blazium/foo` keys. Confirm names against
`ProjectSettings.xml` / `https://docs.blazium.app`. Grok `code_execution` is
not a settings store.

## Workflow

1. **Inspect.** Read `project.blazium` or `project.godot`. Note `config_version`,
   `features`, and existing `blazium/` keys.
2. **Choose.** Prefer `project.blazium`. Keep Godot files if the user still
   opens vanilla Godot.
3. **Apply** only the namespaces needed (cookbook below).
4. **Refuse** dangerous flags unless the user asked (list below).
5. **Verify.** Hub `load` / editor opens. `blazium-cli remote doctor` if remote
   was enabled.
6. **Handoff.** List keys changed.

CLI: `blazium-cli load`, `blazium-cli open`. Log path default:
`user://logs/blazium.log`.

## Patterns

### Namespace cookbook

| Prefix | Safe default | Skill |
|--------|--------------|-------|
| `blazium/justamcp/server_enabled` | true for agent work | `blazium-mcp` |
| `blazium/justamcp/game_control_enabled` | true only if `res://mcp` exists | `blazium-game-mcp` |
| `blazium/justamcp/tools/autowork_tools` | **false** until tests | `blazium-autowork` |
| `blazium/remote_control/server_enabled` | true for CI/remote | `blazium-cli-remote` |
| `blazium/remote_control/server_port` | **6508** (game MCP stays 6507) | |
| `blazium/remote_control/bind_address` | loopback | |
| `blazium/remote_control/allow_eval` | **false** | |
| `blazium/autowork/e2e_enabled` | **false** | `blazium-autowork` |
| `blazium/autowork/show_runtime_ui` | **false** | `blazium-autowork` |
| `blazium/assettags/*` | leave default | `blazium-asset-tags` |
| `blazium/semanticsearch/*` | leave default | `blazium-semantic-search` |
| `blazium/coldstorage/*` | leave default | `blazium-coldstorage` |
| `blazium/gif/*` | leave default | `blazium-gif` |

Pin editor version to the installed Blazium 0.6.x build. Do not claim Godot 4.7
`features`.

### Migrate from Godot

1. Keep `project.godot`.
2. Copy or add `project.blazium` if Hub/CLI expects it.
3. Add only the `blazium/` keys you need.
4. Do not rename nodes or upgrade to 4.7-only APIs.
5. Add Autowork / `res://mcp` only if the user wants agent workflows.

### Dangerous flags (do not enable by default)

- `blazium/remote_control/allow_eval`
- Privileged MCP: `remote_control_exec`, `execute_tool` bypass
- `blazium/autowork/e2e_enabled`
- Binding MCP or remote_control to `0.0.0.0` / public interfaces
- Shipping Autowork in template_release (not available)

## Output contract

- Project file touched (`project.blazium` and/or `project.godot`)
- Keys changed (name = value)
- Dangerous flags left off, or user-requested exceptions
- Verify path (`blazium-cli load` / `remote doctor` / editor opened)
- Next skill (`blazium-mcp`, `blazium-cli-remote`, `blazium-new-project`)

## Pitfalls

- **Godot skill rewrote `project.godot` as 4.7** → restore 4.3.2-safe features.
- **Enabled eval and bound 0.0.0.0** → treat as incident; revert.
- **Game MCP and remote both on 6507** → remote default is 6508; change the leftover pin.
- **Invented a `blazium/foo` key** → check `ProjectSettings.xml` first.
- **Wrote secrets into ProjectSettings** → `blazium-config` + `user://`.

## Resources

- `blazium/doc/classes/ProjectSettings.xml`

## Related skills

- `blazium-router` — detects the file this skill edits
- `blazium-mcp` — JustAMCP keys
- `blazium-cli-remote` — remote_control keys
- `blazium-new-project` — writes the initial tree
- `blazium-config` — `.env` / `.ini` (not ProjectSettings)
