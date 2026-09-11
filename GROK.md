# Grok host — blazium-skills

How Grok should load and use this catalog. Same files as Claude, Cursor, and
Codex. No invented marketplace schema.

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. GDScript-first. Do not apply
Godot 4.7-only APIs. Do not invent JustAMCP tools, `blazium-cli` verbs, or
classes.

## Install

Grok routes on each skill's YAML `description`. It reads `SKILL.md` from a
skills directory. Grok also auto-reads Claude Code marketplaces, plugins, and
skills with zero extra config — so `.claude-plugin/marketplace.json` works when
that plugin layout is present. A symlink into `./.grok/skills/` or
`~/.grok/skills/` is the explicit path when you are not loading the Claude
plugin.

From a clone of this repo:

```bash
python scripts/sync-plugin-packs.py
python scripts/validate-plugin-packs.py
```

Then expose skills to Grok in **one** of these ways (pick the path your Grok
runtime actually scans):

| Method | What to do |
|--------|------------|
| Project skills | Symlink or copy `skills/<name>/` into the workspace skills root Grok already lists |
| User skills | Symlink `skills/` into `~/.grok/skills/` (or the runtime equivalent) |
| Pack install | After `sync-plugin-packs.py`, point Grok at `plugins/blazium/skills/` for the full bundle, or a topic pack under `plugins/blazium-<pack>/skills/` |
| Claude plugin | Leave `.claude-plugin/marketplace.json` in place — Grok reads it automatically |

Do not invent `.grok-plugin/marketplace.json`. If a future Grok marketplace
lands, register the existing Claude catalog paths — do not fork the skill
bodies.

Pair with [blazium-subagents](https://github.com/blazium-games/blazium-subagents)
and its `GROK.md` when you want a studio roster.

## First session

1. Read `skills/blazium-router/SKILL.md`.
2. Detect `project.blazium` (or `project.godot` with `blazium/` keys) before
   treating the tree as stock Godot.
3. Load **router + at most two** domain `SKILL.md` files. Do not dump the
   catalog into context.
4. Prefer evidence from Autowork, JustAMCP, or `blazium-cli --json` over a
   screenshot of a dock.

## Tool mapping (Grok → Blazium)

Use Grok tools to inspect and edit. Use Blazium surfaces to mutate the running
editor or game. Never mix ports.

| Job | Grok tool | Blazium surface |
|-----|-----------|-----------------|
| Read `project.blazium`, scripts, scenes | `read_file` | — |
| Search the tree | `bash` (`rg`, `find`) | — |
| Patch a `.gd` / `.tscn` / `.tres` | `edit_file` / `write_file` | JustAMCP `script_tools` when `:6506` is connected |
| Run Autowork / CLI | `bash` | `blazium --headless --aw-dir=…` or `blazium-cli remote` on **6508** |
| Editor catalog | connected MCP / HTTP | JustAMCP `http://127.0.0.1:6506/mcp` |
| Game tools | connected MCP / HTTP | `res://mcp` on **6507** |
| Hub remote | `bash` / HTTP | Hub **39218** |
| Docs / module XML | `browse_page`, `web_search` | `https://docs.blazium.app` or `https://cdn.blazium.app` only |
| GitHub export / PR / Actions | GitHub connected tools | `blazium-ci-export`, `blazium-ci-watch` |

If JustAMCP is not connected, edit files with Grok tools and verify headless
(`blazium --headless` or Autowork). Do not pretend an MCP tool ran.

Grok `code_execution`, chat Python, `web_search`, and dock screenshots are
**not** Blazium evidence. Quote Autowork JSON, CLI `--json`, or an MCP tool
result.

## Four surfaces (never mix)

| Surface | Default | Skill |
|---------|---------|-------|
| Editor JustAMCP | `:6506/mcp` | `blazium-mcp` |
| Game JustAMCP | `:6507/mcp` | `blazium-game-mcp` |
| remote_control | HTTP `/v1` `:6508` | `blazium-cli-remote` |
| Hub remote | `:39218` | `blazium-hub` |

Games cloud is `https://mcp.blazium.games/mcp` (`blazium-games-mcp`).
`blazium://open?path=` is the OS/CLI protocol. `blazium://scene/…` is a
JustAMCP resource. They are not the same.

## Description field (routing)

Grok decides whether to open a skill from the frontmatter `description`.
Keep it dense:

- Concrete outcome
- Trigger nouns (files, APIs, ports, symptoms)
- Hard negatives (`Do not use for …`)

Optional Grok keys: `when-to-use`, `metadata.short-description`.
Thin descriptions miss. Host-specific browser harnesses do not belong here.

## Workflow every skill already encodes

1. **Inspect.** Version pin, existing files, current conventions.
2. **Choose.** Smallest 4.3.2-safe approach. State assumptions.
3. **Implement.** Project patterns. No invented APIs.
4. **Verify.** Autowork, JustAMCP, or CLI `--json`.
5. **Handoff.** Changed files, evidence, caveats, next skill.

## Output contract

When Grok finishes a Blazium task, report:

- Skills loaded
- Files changed
- Surface used (or "files only — MCP off")
- Evidence (command + result, or `INCONCLUSIVE`)
- Next skill or agent

## Quality bar

- Pin **0.6.x / 4.3.2**. Reject Godot 4.7-only APIs.
- Skills own verbs. Do not invent `blazium-cli hub install`.
- Catalogs live in `SPEC.md` / `references/`. Keep `SKILL.md` under ~500 lines.
- Official docs links only: `https://docs.blazium.app` or `https://cdn.blazium.app`.

See [GETTING-STARTED.md](GETTING-STARTED.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
