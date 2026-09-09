---
name: blazium-mcp
pack: infra
---

# blazium-mcp

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents dump the ~380-tool JustAMCP catalog or mix editor MCP with game MCP, remote_control, and Games cloud.

## What

Enable and connect the editor MCP (`user-blazium-mcp` on :6506). Discover toolsets with `blazium_list_toolsets` / `search_tools`. Use built-in prompts. Read `blazium://` resources. Document Blueprint tools, Multiuser tools, and the MCP client bridge.

**Non-goals:** Do not dump the full catalog. Do not register game tools here (`blazium-game-mcp`). Do not call cloud Games MCP. Do not enable privileged `remote_control_exec` unless the user asks. Do not own scene/test authoring after connect.

## How

- Settings: `blazium/justamcp/*`. Server: Streamable HTTP `POST http://127.0.0.1:6506/mcp`. Name: `blazium-mcp-server`.
- Enable `blazium/justamcp/server_enabled`. Editor plugin emits Cursor JSON.
- CLI: `--enable-mcp`, `--mcp-port`.
- `--aw-*` disables MCP unless `--enable-mcp` is also passed.
- Autowork tool family defaults **false** (`blazium/justamcp/tools/autowork_tools`). Tools are `blazium_autowork_*`.
- Extra: `blueprint_tools`, `multiuser_tools`, `mcp_client_*` outbound bridge.
- Catalog: `references/toolsets.md`.

## Reasoning

Distinct from game MCP (no editor catalog) and from `blazium-cli-remote` (HTTP /v1, not MCP). Product name stays JustAMCP.

## Sources

- Blazium: `blazium/modules/justamcp/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-game-mcp` — runtime project tools
- `blazium-cli-remote` — HTTP automation sibling
- `blazium-autowork` — enable Autowork tool family before running tests via MCP
- `blazium-multiuser-editor` — owns collab session workflow
