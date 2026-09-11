---
name: blazium-games-publish
description: >
  Ships a game page on blazium.games (draft_game_page, bootstrap_game, deploy
  keys, builds). Use for first-party store publish, page copy, or CI deploy
  key. Not scene editing, not Steam, and not itch.
when-to-use: >
  blazium.games page, draft_game_page, bootstrap_game, deploy key,
  list_game_builds, first-party store
metadata:
  author: blazium-games
  short-description: Ship a blazium.games page via cloud MCP, not editor MCP
---

# Blazium Games publish

First-party store checklist — not JustAMCP. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Tools live on `https://mcp.blazium.games/mcp`. Full tool list:
`blazium-games-mcp`. This skill is the **ship a page** order.

## When to use

- Use when creating/updating a blazium.games page, attaching a build, or
  issuing a deploy key for CI.

**When not to use:** edit scenes → `blazium-mcp`. Steam/itch → those
publish skills. Crash sidecar only → `blazium-crash-analytics`. Tool
discovery only → `blazium-games-mcp`.

## Grok host

Read this skill, then `blazium-games-mcp` if the tool names are unknown.
Spawn `producer` for copy approval and `tools-programmer` for the deploy
key handoff. Child prompts must include game uid (if any) and whether CI
needs `request_deploy_key`. Do not dump the catalog.

Evidence is `get_game` / `list_game_builds` JSON — not a screenshot of the
store page. Never call editor JustAMCP on `:6506` for this skill.

## Workflow

1. **Inspect.** Cloud MCP connected (not `:6506`). `get_profile`.
2. **Choose.** New game vs update. Build from `blazium-export` / CI.
3. **Implement.** Checklist below. Do not paste deploy keys into scenes.
4. **Verify.** `get_game` / `list_game_builds` returns the uid + build.
5. **Handoff.** Deploy key → `blazium-ci-export`. Copy → stay on cloud
   prompts.

## Patterns

### Page checklist

1. `get_profile` / `list_games`
2. Prompt `bootstrap_game` or `create_game`
3. Prompt `draft_game_page` / `improve_game_copy`
4. `update_game` with user-approved copy
5. `request_deploy_key` if CI will upload
6. Attach builds: `list_game_builds` / `get_game_build` after CI
   (`blazium-ci-export`)

Do not invent editor tool names. Resources:
`blazium-games://games/{uid}/…`.

## Output contract

- Game uid
- Cloud tools called
- Whether a deploy key was issued (never print the secret)
- Build ids attached
- Evidence: `get_game` / `list_game_builds` result or `INCONCLUSIVE`

## Pitfalls

- **Called JustAMCP `create_game`** → wrong layer.
- **Edited engine scenes to “publish”** → cloud MCP only.
- **Committed a deploy key** → CI secret.

## Resources

- `blazium-games-mcp` — tools / prompts

## Related skills

- `blazium-games-mcp` — tools
- `blazium-ci-export` — upload
- `blazium-crash-analytics` — `app_id` / consent
