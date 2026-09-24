# Getting started — blazium-skills

Agent skills for **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. GDScript-first.
Same files load on Claude Code, Cursor, Codex, and Grok.

## Community

- Official website: [https://blazium.app/](https://blazium.app/)
- IndieDB blog: [https://www.indiedb.com/engines/blazium-engine](https://www.indiedb.com/engines/blazium-engine)
- Official community: [Blazium Discord](https://discord.gg/sZaf9KYzDp)
- Docs: [docs.blazium.app](https://docs.blazium.app)

Pack releases: [skills.json](https://cdn.blazium.app/skills/skills.json).

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
| Grok | Clone this repo | Symlink `skills/` or a pack under `plugins/` into the Grok skills root. Grok also auto-reads the Claude marketplace. Full contract: [GROK.md](GROK.md) |

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

Prefer Autowork, JustAMCP, or `blazium-cli --json` over unverified clicks. Get the CLI with `npx @blazium-engine/cli` and the toolchain with `npx @blazium-engine/toolchain` (Linux and Windows, x64 and ia32).
Grok `code_execution` and screenshots are not evidence — see [GROK.md](GROK.md).
See [CONTRIBUTING.md](CONTRIBUTING.md) to add a skill.
