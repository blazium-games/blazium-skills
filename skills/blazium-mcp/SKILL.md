---
name: blazium-mcp
description: >
  Connects the Blazium editor JustAMCP server (user-blazium-mcp on
  127.0.0.1:6506). Discovers toolsets with blazium_list_toolsets / search_tools
  and reads blazium:// resources. Use when enabling or diagnosing editor MCP.
  Do not use when the editor is already connected and the job is scenes or
  tests — load blazium-nodes-scenes or blazium-autowork. Do not use for
  res://mcp game tools (blazium-game-mcp), HTTP /v1 (blazium-cli-remote), or
  cloud Games MCP (blazium-games-mcp).
---

# Blazium MCP (JustAMCP editor)

Connect and discover the **editor** JustAMCP catalog. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

Server: Streamable HTTP `POST http://127.0.0.1:6506/mcp`  
Name: `blazium-mcp-server`  
Cursor namespace: `user-blazium-mcp`

**Never dump ~380 tools.** Discover, then call. Toolset names, prompts, and
`blazium://` URIs live in [references/toolsets.md](references/toolsets.md)
and [references/prompts.md](references/prompts.md).

## When to use

- Use when connecting Cursor / an agent to the **open editor**.
- Use when MCP is off, empty, or on the wrong port.
- Use when choosing a built-in prompt (`blazium_scene_architect`,
  `blazium_autowork_fix_loop`, …).

**When not to use:** the editor is already connected and the job is scenes or
tests → `blazium-nodes-scenes` / `blazium-autowork`. Project-owned runtime
tools → `blazium-game-mcp`. Headless HTTP `/v1` → `blazium-cli-remote`.
Store/crashes/deploy → `blazium-games-mcp`. Do not enable privileged
`remote_control_exec` unless the user asks.

## Workflow

1. **Inspect.** Confirm `blazium/justamcp/server_enabled`. Note port
   (`--mcp-port` or setting).
2. **Connect.** Per-client recipe below. If `--aw-*` is on the editor command
   line, also pass `--enable-mcp` or MCP stays off.
3. **Smoke.** Call `blazium_list_toolsets` or `search_tools`. Stop if the list
   is empty.
4. **Discover.** `describe_toolset` for one family, then one `blazium_*` tool.
5. **Verify.** Re-read `blazium://scene/current` or `blazium://editor/state`.
6. **Handoff.** Report tools used and any disabled families. Scene work then
   loads `blazium-nodes-scenes`.

Enable Autowork MCP tools **before** running tests via MCP:
`blazium/justamcp/tools/autowork_tools` defaults **false**. Tools are
`blazium_autowork_*`. Then use `blazium-autowork`.

## Per-client connect

Do not invent a hosted `mcp.blazium.app` editor MCP. Games cloud stays
`blazium-games-mcp`.

### Cursor

The editor plugin emits Cursor JSON. Namespace: `user-blazium-mcp`.

```json
{
  "mcpServers": {
    "blazium": {
      "type": "http",
      "url": "http://127.0.0.1:6506/mcp"
    }
  }
}
```

Cursor: `.cursor/mcp.json`.

### Claude / Codex / other Streamable HTTP

```text
http://127.0.0.1:6506/mcp
```

```bash
claude mcp add --transport http blazium http://127.0.0.1:6506/mcp
```

Optional OAuth: `--mcp-client-id` / `--mcp-client-secret`.

### Flags

| Flag / setting | Effect |
|----------------|--------|
| `--enable-mcp` | Start editor MCP |
| `--mcp-port` | Override 6506 |
| `--aw-*` without `--enable-mcp` | MCP skipped |
| `blazium/justamcp/server_enabled` | Must be true |

## Patterns

### Connection doctor

| Check | Expected |
|-------|----------|
| `blazium/justamcp/server_enabled` | true |
| URL | `http://127.0.0.1:6506/mcp` |
| `--aw-*` without `--enable-mcp` | MCP skipped |
| Autowork family | off until you enable it |
| Privileged exec | off by default — leave it |

### Discover, do not dump

```text
1. search_tools or blazium_list_toolsets
2. describe_toolset / call_toolset for one family
3. Call the specific blazium_* tool
```

### Extra surfaces (do not expand unless asked)

- `blueprint_tools` — presets
- `multiuser_tools` — collab; session workflow is `blazium-multiuser-editor`
- `mcp_client_*` — outbound bridge to other MCP servers

## Pitfalls

- **Empty tool list during `--aw-*`** → add `--enable-mcp`.
- **Called `project_echo` on :6506** → that is game MCP. Use `blazium-game-mcp`.
- **Port 6507** → game MCP. **Port 6508** → `remote_control`. Neither is the editor catalog.
- **`blazium://open?path=`** → OS/CLI protocol (`blazium-new-project` /
  `blazium-cli`), not a JustAMCP resource.
- **Enabled `remote_control_exec` or `execute_tool` bypass** → privileged.
  Leave off unless requested.

## Resources

- Tests: https://github.com/blazium-games/justamcp_module_tests
- Module: `blazium/modules/justamcp/`
- Settings: `blazium/justamcp/*`
- Catalog: [references/toolsets.md](references/toolsets.md)

## Related skills

- `blazium-nodes-scenes` — scenes after MCP is up
- `blazium-autowork` — enable Autowork family, then run tests
- `blazium-game-mcp` — `res://mcp` runtime tools
- `blazium-cli-remote` — HTTP `/v1`, not MCP
- `blazium-games-mcp` — cloud store / deploy / crashes
- `blazium-router` — pick this skill vs the others
