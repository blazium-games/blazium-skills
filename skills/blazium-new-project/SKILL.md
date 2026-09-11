---
name: blazium-new-project
description: >
  Bootstraps a version-controlled Blazium project via Hub/CLI (blazium://open)
  with Autowork, res://mcp, and .gitignore. Use when starting a new Blazium
  game. Does not implement gameplay. Not project.blazium settings-only and
  not blazium-cli editor install.
when-to-use: >
  new Blazium game, greenfield, bootstrap, blazium://open, scaffold Autowork,
  res://mcp, .gitignore, empty folder
metadata:
  author: blazium-games
  short-description: Scaffold a versioned Blazium game via Hub/CLI
---

# Blazium new project

Hub manages editors. This skill manages **game content**. If no editor is
installed, tell the user to install via `blazium-cli` before continuing.

`blazium://open?path=` is the OS/CLI protocol. It is not a JustAMCP
`blazium://scene/` URI.

## When to use

- Use when the folder has no `project.blazium` / `project.godot`.
- Use when the user says "new Blazium game" or wants a greenfield Blazium project.

**When not to use:** existing project settings → `blazium-project-config`.
Installing editors/templates only → `blazium-cli` spec. Do not install
Xbox modules unless asked. Do not implement gameplay.

## Grok host

On Grok, keep context small: read this file, then copy sibling assets
(`blazium-autowork/assets/`, `blazium-game-mcp/assets/`). Spawn
`blazium-orchestrator` or `producer` after the tree exists — not during
scaffold. Child prompts must include the absolute project path and the
4.3.2 pin.

Use Grok `bash` for `git init` and `blazium-cli open`. Do not invent a
Unity/Unreal layout. Do not implement a player controller in this skill.

## Workflow

1. **Intake.** Ask (or infer): concept, platforms (desktop/web/mobile),
   live-ops (Services vs local-only).
2. **Editor.** Confirm a Blazium 0.6.x editor exists
   (`blazium-cli editors`).
3. **Scaffold** Autowork, `res://mcp`, and `.gitignore` from sibling assets.
4. **Git.** `git init` if missing. Apply [assets/.gitignore](assets/.gitignore).
5. **Open.** `blazium-cli open` or `blazium-cli handle-uri` with
   `blazium://open?path=<abs>`.
6. **Verify.** Editor opens. GDScript-only:
   `blazium --headless --path <dir> --aw-dir=res://tests/gdscript`. Mixed
   suffixes: `-s run_tests.gd`. Exit 0.
7. **Handoff** to `blazium-router` for the next task (gameplay, MCP, Services).

Config lives in `%APPDATA%\blazium\hub.json` (Windows).

## Scaffold

| Path | Source |
|------|--------|
| `project.blazium` | [assets/project.blazium](assets/project.blazium) then `blazium-project-config` |
| `res://mcp/register.gd` | `blazium-game-mcp/assets/register.gd` |
| `res://run_tests.gd` | `blazium-autowork/assets/run_tests.gd` |
| `res://.autoworkconfig.json` | `blazium-autowork/assets/.autoworkconfig.json` |
| `res://tests/gdscript/test_smoke.gd` | `blazium-autowork/assets/test_smoke.gd` |
| `.gitignore` | [assets/.gitignore](assets/.gitignore) |
| `README.md` | one-paragraph game concept — no extra docs |

Optional: `res://mcp/register.luau` from game-mcp assets if the user wants Luau.

Enable `blazium/justamcp/server_enabled` after create if the user wants agents
immediately. Leave `allow_eval` and E2E **off**.

## Patterns

### Intake (keep it short)

- Concept in one sentence
- Platforms: desktop / web / Android
- Live-ops: local-only vs Blazium Services (do not implement auth here)

### Open after create

```bash
blazium-cli open "<abs project>"
# or
blazium-cli handle-uri "blazium://open?path=<abs project>"
```

## Output contract

- Absolute project path
- Files scaffolded
- Editor confirmed (`blazium-cli editors`) or blocked on install
- Autowork smoke command + exit code
- Next skill (`blazium-router`, `blazium-project-config`, genre adapter)

## Pitfalls

- **Used `blazium://scene/` to open the project** → wrong URI family.
- **Implemented a player controller in this skill** → stop; hand off to router.
- **Skipped Autowork scaffold** → first agent session has no verify path.
- **Invented mcp.tscn** → `register.gd` only.
- **Installed Xbox / specialty modules unasked** → leave them off.

## Resources

- `blazium-cli/hub/`
- Sibling assets: `skills/blazium-autowork/assets/`,
  `skills/blazium-game-mcp/assets/`

## Related skills

- `blazium-cli` — install editor if missing
- `blazium-project-config` — settings after create
- `blazium-autowork` — tests
- `blazium-game-mcp` — `res://mcp`
- `blazium-router` — next task after bootstrap
