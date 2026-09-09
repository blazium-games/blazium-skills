---
name: blazium-games-mcp
description: >
  Uses the Blazium Games cloud MCP (https://mcp.blazium.games/mcp) for store
  pages, analytics, crashes, deploy keys, and builds. Use for live-ops
  dashboard work. Never confuse with editor JustAMCP or game MCP.
---

# Blazium Games cloud MCP

Store / ops — **not scene editing**. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Do not conflate with editor JustAMCP.** This is layer 3 only:

| Surface | Default | Kind |
|---------|---------|------|
| Editor JustAMCP | `http://127.0.0.1:6506/mcp` | scenes / tools |
| Game JustAMCP | `http://127.0.0.1:6507/mcp` | `res://mcp` only |
| **Games cloud** | `https://mcp.blazium.games/mcp` | store / deploy / crashes |
| remote_control | HTTP `/v1` on **6508** | `blazium-cli remote` |

Code: `blazium.games/games_mcp/` (OAuth 2.1 + Streamable HTTP).

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when creating/updating a store page, listing builds, rotating deploy
  keys, or reading crash/analytics uploads.

**When not to use:** edit scenes/scripts → `blazium-mcp`. Project
`res://mcp` tools → `blazium-game-mcp`. Sidecar / consent / `app_id` bake →
`blazium-crash-analytics`. CI that *consumes* deploy keys →
`blazium-ci-export`. Store copy workflow → blazium-games-publish
`blazium-games-publish`.

## Workflow

1. **Inspect.** Confirm the cloud MCP is connected — not `:6506`. Auth via
   OAuth / `request_mcp_key`. `get_profile` first.
2. **Choose.** Create vs update game. Crash list vs deploy key vs analytics.
3. **Implement.** Call only the tools below. Resources
   `blazium-games://me` and `blazium-games://games/{uid}/…`.
4. **Verify.** Tool result (game uid, crash id, key id). Not a screenshot.
5. **Handoff.** Deploy key → `blazium-ci-export`. Crash config →
   `blazium-crash-analytics`.

## Patterns

### Tools (cloud only — do not invent editor names)

`get_profile`, `list_games`, `get_game`, `create_game`, `update_game`,
`get_game_analytics`, `list_game_crashes`, `get_crash`,
`request_crash_download`, `list_mcp_keys`, `get_setup`, `get_deploy_info`,
`list_game_builds`, `get_game_build`, `request_mcp_key`, `request_deploy_key`

### Prompts

`draft_game_page`, `improve_game_copy`, `analytics_summary`, `bootstrap_game`

### Resources

`blazium-games://me`, `blazium-games://games`,
`blazium-games://games/{uid}/analytics|crashes|deploy|builds`

### Create / update page

1. `get_profile` / `list_games`
2. `create_game` or `update_game`
3. Optional prompt `draft_game_page` / `improve_game_copy`

### Crashes + keys

- List: `list_game_crashes` → `get_crash` → `request_crash_download`
- Rotate: `request_deploy_key` / `list_mcp_keys` — do not paste keys into
  scenes

## Pitfalls

- **Called these tools on `:6506`** → wrong server. Cloud URL only.
- **Invented editor tool names** (`create_scene`, etc.) here →
  `blazium-mcp`.
- **Skipped consent when configuring uploads** → `blazium-crash-analytics`.
- **Committed deploy keys** → rotate with `request_deploy_key`.

## Resources

- `blazium.games/games_mcp/`

## Related skills

- `blazium-crash-analytics` — in-engine sidecar / consent / ids
- `blazium-mcp` — editor MCP
- `blazium-ci-export` — consume deploy keys
- `blazium-games-publish` — store copy
