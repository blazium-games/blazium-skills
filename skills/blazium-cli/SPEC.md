---
name: blazium-cli
pack: ship
---

# blazium-cli

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents try to download random editor zips. Top-level CLI verbs install editors, templates, and sidecar products.

## What

`install`, `uninstall`, `editors`, `install-path`, `templates`, `open`, `load`, `projects create`, `handle-uri`, `upgrade`, `update check|apply|replace-bin`. `update apply --product` is `cli|hub|crash_reporter|toolchain`. `update check` may include `editor|templates`.

**Non-goals:** Hub UI, `hub-remote`, port 39218 (`blazium-hub`). HTTP `/v1` of a running instance (`blazium-cli-remote`). Do not invent `blazium-cli hub install`.

## How

- Product: `blazium-cli/`. Config `%APPDATA%\blazium\cli.json`. Editors/projects: `hub.json`.
- Channels: `release` / `prerelease` / `nightly`. `--json`.
- Editors/templates: `install` / `templates download`. Launch: `--crash-reporter` / `--analytics`.
- Sidecars: `update apply --product hub|crash_reporter|toolchain`.
- Catalog: `references/verbs.md`.

## Reasoning

Editor lifecycle skill. Distinct from Hub window, remote control, and new-project content.

## Sources

- https://github.com/blazium-games/blazium-cli

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-hub` — Hub UI
- `blazium-cli-remote` — running instance HTTP
- `blazium-new-project` — game files after an editor exists
