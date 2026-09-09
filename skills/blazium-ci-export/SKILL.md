---
name: blazium-ci-export
description: >
  Wires GitHub Actions for Blazium (setup-blazium-engine, setup-blazium-cli,
  export-blazium-game, deploy-blazium-game). Use for CI export, Autowork jobs,
  and deploy keys from Games MCP. Not engine SCons CI and not local presets.
---

# Blazium CI export

GitHub Actions matrix for games — not the engine’s SCons `ci_cd`. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Actions live under `github_actions/` (published as `blazium-engine/…`):

- `setup-blazium-engine` — `blazium-cli install` (+ optional `--templates`)
- `setup-blazium-cli` — CLI from `https://cdn.blazium.app/cli/cli.json`
- `export-blazium-game` — preset-named platform export
- `deploy-blazium-game` — Docker / itch / stores / Steam **after** an artifact

Deploy keys: `blazium-games-mcp` (`request_deploy_key`). Build identity:
`X-App-Id` / `X-Build-Id` via `blazium-crash-analytics` (do not skip consent).
Steam/itch **store copy** stays with publish adapters.

## When to use

- Use when adding or fixing a game repo’s `.github/workflows` export/test/deploy.

**When not to use:** local JustAMCP export → `blazium-export`. Editor install
on a workstation → `blazium-cli`. Engine source CI → do not touch
`blazium/ci_cd` unless the user is working on the engine itself.

## Workflow

1. **Inspect.** Existing workflows, `export_presets.cfg` preset **names**
   (must match `platform-name`), secrets already in the repo.
2. **Choose.** Setup + Autowork job, export matrix, then deploy only if keys
   exist.
3. **Implement.** Official actions only. Autowork GDScript-only:
   `blazium --headless --path $PROJECT --aw-dir=res://tests/gdscript`.
   Mixed `.gd` / `.luau` or Hub: `-s run_tests.gd`.
4. **Verify.** Workflow dry-run or a CI log — not a screenshot.
5. **Handoff.** Artifact names + which secrets are still missing.

## Patterns

### Setup + Autowork

```yaml
- uses: blazium-engine/setup-blazium-cli@master
- uses: blazium-engine/setup-blazium-engine@master
  with:
    version: latest-release-0.6
    download_template: "true"
- run: blazium --headless --path . --aw-dir=res://tests/gdscript
# mixed suffixes / Hub: blazium --headless --path . -s run_tests.gd
```

`version` aliases: concrete (`0.6.725`), `nightly`, `latest-release`, `lts`,
`latest-0.6`. `latest` tracks the nightly CDN channel.

### Export + deploy

`export-blazium-game` `platform-name` must match the editor preset
(e.g. `Windows Desktop x86_64`, `Web`). Upload the artifact, then
`deploy-blazium-game` reusable workflows (`deploy-itchio.yml`,
`deploy-docker.yml`, …).

Get deploy credentials from `blazium-games-mcp` — do not invent key names.

Hub Autowork pattern: `blazium-hub/.github/workflows/autowork.yml`.

## Pitfalls

- **Rewrote engine SCons CI** → out of scope for a game repo.
- **Preset name ≠ `platform-name`** → export action fails.
- **Committed deploy keys** → rotate via Games MCP.
- **Taught SteamPipe copy here** → `blazium-steam-publish`.

## Resources

- `github_actions/setup-blazium-engine/action.yml`
- `github_actions/export-blazium-game/action.yml`
- Asset: `assets/ci-autowork.yml`
- `blazium-autowork` — test authoring

## Related skills

- `blazium-export` — local presets
- `blazium-games-mcp` — deploy / MCP keys
- `blazium-autowork` — `--aw-dir=` or `-s run_tests.gd`
- `blazium-crash-analytics` — build ids
- `blazium-cli` — workstation install
