---
name: blazium-game-mcp
description: >
  Authors project-owned JustAMCP game tools in res://mcp/register.gd or
  register.luau via JustAMCPRuntime. Use when connecting user-blazium-game
  on :6507, adding play-mode/export MCP tools, or when the game list is empty.
  Do not use for the editor catalog (blazium-mcp), HTTP /v1 (blazium-cli-remote),
  or cloud Games MCP (blazium-games-mcp).
---

# Blazium game MCP

The game host (`user-blazium-game`) exposes **only** tools registered from
`res://mcp`. There is no editor catalog. Do not invent `mcp.gd` or `mcp.tscn`.

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Default URL: `http://127.0.0.1:6507/mcp`  
Server name: `blazium-game`  
Dir: `blazium/justamcp/project_mcp_dir` (default `res://mcp`)

The engine instantiates `register.gd` / `register.luau`, then calls `register()`
if that method exists.

## When to use

- Use when the user wants game-specific MCP tools (score, pause, echo).
- Use when Cursor shows only `project_echo` or an empty game catalog.
- Use when scaffolding a new project (`blazium-new-project` copies these assets).

**When not to use:** editor scene/script tools → `blazium-mcp`. Play-mode
screenshots/tree inspect on the **editor** MCP during play, not this host.

## Workflow

1. **Inspect.** Check `res://mcp/register.gd` and `game_control_enabled`.
2. **Enable.** `blazium/justamcp/game_control_enabled` or
   `--enable-mcp-game-control` / `--mcp-game-port`. `--disable-game-mcp`
   (or `blazium/justamcp/disable_game_mcp`) turns the host off.
3. **Author.** Copy [assets/register.gd](assets/register.gd) (and optional
   [assets/register.luau](assets/register.luau)). Extend `Node`, implement
   `register()`, call `JustAMCPRuntime.register_tool`.
4. **Doctor port.** Game MCP default **6507**; remote_control default **6508**.
   Change `export_port` / `--mcp-game-port` or remote `server_port` if a project
   still pins both to the same port.
5. **Verify.** Restart play/export host; `list_tools` should show project names.
6. **Handoff.** State registered tool names and the game MCP URL.

## Patterns

### Registration API (`JustAMCPRuntime`)

```gdscript
JustAMCPRuntime.register_tool(name, description, input_schema, callable)
JustAMCPRuntime.register_prompt(name, description, callable)
JustAMCPRuntime.register_custom_command(name, callable)  # TCP bridge
JustAMCPRuntime.load_project_mcp_scripts()
```

Do not prefix project tools with `blazium_` (reserved / spoof-blocked).

### Three starter tools

Copy the assets. They register `project_echo`, `project_get_score`,
`project_pause` as examples — rename to match the game.

### Exported builds

The HTTP game host ships in exports. **No editor tools.** Treat it as a local
debug surface: loopback, no secrets in tool output, no unrestricted eval.

External samples: https://github.com/blazium-games/justamcp_module_tests

## Pitfalls

- **`mcp.gd` / `mcp.tscn`** → wrong convention. Use `register.gd` / `register.luau`.
- **Empty game MCP** → missing `register()` or scripts not under `res://mcp`.
- **Script has no instantiable base** → `extends Node`.
- **Port fight with remote_control** → defaults are 6507 vs 6508. Change a leftover 6507 remote pin.
- **`--aw-*` without `--enable-mcp-game-control`** → game MCP may not start.

## Resources

- Register catalog: [references/register.md](references/register.md)
- `JustAMCPRuntime.xml` in `blazium/modules/justamcp/doc_classes/`
- [assets/register.gd](assets/register.gd)
- [assets/register.luau](assets/register.luau)

## Related skills

- `blazium-mcp` — editor catalog
- `blazium-new-project` — scaffolds `res://mcp`
- `blazium-luau` —  for `.luau` language
- `blazium-cli-remote` — port conflict sibling
