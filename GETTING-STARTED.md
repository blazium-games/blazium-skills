# Getting started — blazium-skills

Agent skills for **Blazium 0.6.x (Godot 4.3.2 fork)**. GDScript-first.
Same files load on Claude Code, Cursor, and Codex.

## Install the marketplace

After clone:

```bash
python scripts/sync-plugin-packs.py
python scripts/validate-plugin-packs.py
```

| Host | Add | Install |
|------|-----|---------|
| Claude Code | `/plugin marketplace add blazium-games/blazium-skills` | `/plugin install blazium-infra@blazium-skills` (repeat for other packs or `blazium@blazium-skills`) |
| Cursor | Add `blazium-games/blazium-skills` as a marketplace | Install `blazium-infra` … `blazium-growth` or `blazium` |
| Codex | `codex plugin marketplace add blazium-games/blazium-skills` | Plugins Directory → **Blazium Skills** |

## First session

1. Load `blazium-router` (or start from `blazium-orchestrator` in
   [blazium-subagents](https://github.com/blazium-games/blazium-subagents)).
2. Detect `project.blazium` before Godot.
3. Open **one** domain skill from the classifier table. Do not dump the catalog.

## Four surfaces (never mix)

| Surface | Default | Skill |
|---------|---------|-------|
| Editor JustAMCP | `:6506/mcp` | `blazium-mcp` |
| Game JustAMCP | `:6507/mcp` (`res://mcp`) | `blazium-game-mcp` |
| remote_control | HTTP `/v1` `:6508` | `blazium-cli-remote` |
| Hub remote | `:39218` (full `/v1` + `show_hub`) | `blazium-hub` |

Games cloud is `https://mcp.blazium.games/mcp` (`blazium-games-mcp`).

Prefer Autowork, JustAMCP, or `blazium-cli --json` over unverified clicks.
See [CONTRIBUTING.md](CONTRIBUTING.md) to add a skill.
