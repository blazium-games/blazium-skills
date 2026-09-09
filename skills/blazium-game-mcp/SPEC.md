---
name: blazium-game-mcp
pack: infra
---

# blazium-game-mcp

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Runtime `user-blazium-game` only exposes project tools. No `res://mcp` template ships in the ecosystem, so agents invent `mcp.gd` / `mcp.tscn`.

## What

Author `res://mcp/register.gd` and/or `register.luau`. Register tools and prompts via `JustAMCPRuntime`. Enable game control flags. State export-host limits.

**Non-goals:** Do not expose the editor catalog on the game host. Do not invent `mcp.gd` / `mcp.tscn`.

## How

- Dir: `blazium/justamcp/project_mcp_dir` default `res://mcp`.
- API: `JustAMCPRuntime.register_tool`, `register_prompt`, `register_custom_command`, `load_project_mcp_scripts`.
- Enable: `blazium/justamcp/game_control_enabled` or `--enable-mcp-game-control` / `--mcp-game-port`. Off: `--disable-game-mcp`.
- Starter: `assets/register.gd` / `assets/register.luau`.
- Default port **6507**. remote_control defaults to **6508**.
- External examples: https://github.com/blazium-games/justamcp_module_tests
- Docs: `blazium/modules/justamcp/doc_classes/JustAMCPRuntime.xml`

## Reasoning

Mixing editor and game MCP is the number-one agent error. This skill exists so that mistake has a dedicated handoff.

## Sources

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-mcp` — editor catalog during play
- `blazium-luau` — register.luau
- `blazium-new-project` — scaffold res://mcp
