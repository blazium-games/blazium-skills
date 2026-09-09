---
name: blazium-games-mcp
pack: live-ops
---

# blazium-games-mcp

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Cloud MCP is the UGS dashboard analog: store pages, analytics, crashes, deploy keys.

## What

Use `https://mcp.blazium.games/mcp` tools and prompts. Never confuse with editor JustAMCP.

**Non-goals:** Do not edit scenes. Do not invent editor tool names.

## How

- Code: `blazium.games/games_mcp/`.
- Tools: get_profile, list_games, create_game, update_game, get_game_analytics, list_game_crashes, get_crash, request_crash_download, request_mcp_key, request_deploy_key, get_setup, get_deploy_info, list_game_builds, get_game_build, list_mcp_keys.
- Prompts: draft_game_page, improve_game_copy, analytics_summary, bootstrap_game.
- Resources: `blazium-games://me`, `blazium-games://games`, `blazium-games://games/{uid}/…`.

## Reasoning

Third MCP layer. Distinct from JustAMCP and from crash sidecar config.

## Sources

- Blazium: blazium.games/games_mcp/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-crash-analytics` — in-engine sidecar / build ids
- `blazium-ci-export` — uses deploy keys
- `blazium-games-publish` — store copy workflow
