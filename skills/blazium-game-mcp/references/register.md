# Game MCP register

The game host (`user-blazium-game`, default `http://127.0.0.1:6507/mcp`)
exposes **only** tools from `res://mcp`. There is no editor catalog.

## Files

Copy the starters; do not invent `mcp.gd` or `mcp.tscn`.

| File | Role |
|------|------|
| [assets/register.gd](../assets/register.gd) | GDScript `extends Node` + `register()` |
| [assets/register.luau](../assets/register.luau) | Luau equivalent |

The engine instantiates the script, then calls `register()` if that method
exists. Dir setting: `blazium/justamcp/project_mcp_dir` (default `res://mcp`).

## API (`JustAMCPRuntime` singleton — not `.new()`)

```gdscript
JustAMCPRuntime.register_tool(name, description, input_schema, callable)
JustAMCPRuntime.register_prompt(name, description, callable)
JustAMCPRuntime.register_custom_command(name, callable)  # TCP bridge
JustAMCPRuntime.load_project_mcp_scripts()
```

Do not prefix project tools with `blazium_` (reserved / spoof-blocked).

Starters register `project_echo`, `project_get_score`, `project_pause`.
Rename them to match the game.

## Ports

Game MCP **6507**. remote_control **6508**. `--disable-game-mcp` (or
`blazium/justamcp/disable_game_mcp`) turns the host off.
