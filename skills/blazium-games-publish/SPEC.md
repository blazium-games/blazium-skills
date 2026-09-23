---
name: blazium-games-publish
pack: growth
---

# blazium-games-publish

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

## What

Thin adapter: `blazium-games-mcp` prompts (`draft_game_page`, `bootstrap_game`) + deploy keys + builds.

**Non-goals:** Do not edit engine scenes.

## How

See `blazium-games-mcp` tool list. This adapter is the 'ship a page' checklist.

## Reasoning

Store publish skill so Games MCP is not only ops.

## Sources

- blazium.games/games_mcp/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-games-mcp` — tools
- `blazium-ci-export` — upload
