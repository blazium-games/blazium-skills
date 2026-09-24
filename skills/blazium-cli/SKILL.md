---
name: blazium-cli
description: >
  Installs and updates Blazium editors, templates, Hub, Crash Reporter, and
  the toolchain via top-level blazium-cli verbs. Use when the editor is
  missing or update apply --product is needed. Do not use for Hub UI
  (blazium-hub) or a running editor's HTTP /v1 (blazium-cli-remote).
---

# Blazium CLI

Editor and product lifecycle. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

**Do not invent `blazium-cli hub install`.** Verbs are top-level. Full list:
[references/verbs.md](references/verbs.md). Agent contract:
[references/agent-cli.md](references/agent-cli.md).

`update apply --product` is only `cli|hub|crash_reporter|toolchain`.
Editors/templates use `install` / `templates download`.
`update check --product` may include `editor|templates`.

Config: `%APPDATA%\blazium\cli.json` (Linux/macOS: `~/.config/blazium/`).
Editors/projects list: `hub.json` (shared with Hub). Channels:
`release` / `prerelease` / `nightly`. `--json` for machine output (`--format json`; implies `--quiet`).
`--dry-run` exists only on `upgrade` and `update apply`.

Never conflate `blazium://open?path=` (this CLI) with JustAMCP
`blazium://scene/…`. Hub window / `blazium://hub` → `blazium-hub`.
HTTP `/v1` of a running instance → `blazium-cli-remote`.

## When to use

- Use when installing/uninstalling editors, templates, or sidecar products.
- Use when `upgrade`, `projects create`, or `update apply --product`.

**When not to use:** Hub UI / `hub-remote ensure` / port 39218 →
`blazium-hub`. Control a **running** editor → `blazium-cli-remote`.
Create game files → `blazium-new-project` (after an editor exists).
Export presets → `blazium-export`. Retro cooks → `blazium-toolchain`
(this skill only **installs** that binary). Sidecar crash UI →
`blazium-crash-reporter`.

## Workflow

Get the binary from npm before any verb. Linux and Windows, x64 and ia32. When npm installed the matching optional package, that binary is used.

```text
npx @blazium-engine/cli
npm install -g @blazium-engine/cli
```

A blog zip is still wrong. After the binary exists, `install` and `update apply` remain the verbs.

1. **Inspect.** `blazium-cli editors`, `install-path`, `templates path`.
2. **Choose.** Channel + version. Default policy: latest **release** among
   installed editors unless pinned.
3. **Implement.** `install` / `templates download` / `update apply` / `upgrade`.
4. **Verify.** `editors path <ver>` launches; `--json` status is clean.
5. **Handoff.** Installed version → `blazium-new-project` or `blazium-export`.

## Agent invocation

Flags before prompts. Discover `blazium-cli --help` then
`blazium-cli <verb> --help`. Prefer `--json`. Retry `install` /
`hub-remote ensure` — they are idempotent. Never invent verbs. Details:
[references/agent-cli.md](references/agent-cli.md).

## Patterns

```text
blazium-cli install 0.6.714 --json
blazium-cli projects create D:\games\my_game
blazium-cli update check --product editor
blazium-cli update apply --product cli
blazium-cli upgrade
blazium-cli open D:\games\my_game --crash-reporter C:\Blazium\crash_reporter.exe
blazium-cli open D:\games\my_game --analytics accepted --analytics-mode anonymous
blazium-cli run D:\games\my_game
```

Launch flags: `--crash-reporter`, `--no-crash-reporter`, `--analytics`,
`--analytics-mode`. More verbs: [references/verbs.md](references/verbs.md).

## Pitfalls

- **`open` to play the game** → `open` and `load` pass `--editor`. Use `run` (alias `play`) to play. `run` fails with `no main scene` until `application/run/main_scene` is set.
- **Nested `hub install`** → not a verb; use `install`.
- **`update apply --product editor`** → use `install` instead.
- **Downloaded a random zip from a blog** → CDN / `install` only.
- **Opened Hub to log into LobbyClient** → `blazium-services` / `blazium-lobby`.

## Resources

- https://github.com/blazium-games/blazium-cli
- [references/verbs.md](references/verbs.md)
- [references/agent-cli.md](references/agent-cli.md)

## Related skills

- `blazium-hub` — desktop Hub / `hub-remote` / port 39218
- `blazium-crash-reporter` — sidecar binary after `--product crash_reporter`
- `blazium-toolchain` — after `--product toolchain`
- `blazium-new-project` — create game after editor exists
- `blazium-cli-remote` — running editor HTTP `/v1`
