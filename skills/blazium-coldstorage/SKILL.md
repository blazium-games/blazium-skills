---
name: blazium-coldstorage
description: >
  Connects the Blazium editor to ColdStorageVCS (cstoraged on port 1666),
  not Git. Use when the studio uses ColdStorage. Secrets stay in EditorSettings.
  Do not replace git in this ecosystem repo.
---

# Blazium ColdStorage

Editor VCS against `cstoraged`. **Not Git.** Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/coldstorage/`. Classes: `ColdStorageVCS`,
`ColdStorageEditorPlugin`. Settings namespace: `blazium/coldstorage/*`.

Do **not** invent cstoraged server ops beyond these editor settings. Do **not**
replace git in git-based projects.

## When to use

- Use when the user asked to connect the editor to ColdStorage / cstoraged.

**When not to use:** this ecosystem’s git remotes / PRs → stay on git.
Project setting keys in general → `blazium-project-config`. Installing the
editor → `blazium-cli`.

## Workflow

1. **Inspect.** Is ColdStorage actually required? Existing
   `blazium/coldstorage/*` in Project Settings vs Editor Settings.
2. **Choose.** Git unless the studio already runs cstoraged.
3. **Implement.** Enable + host/port/workspace. Secrets only in
   **EditorSettings**.
4. **Verify.** Editor connects; `validate_on_startup` passes. Do not
   `auto_pull` until the user asked.
5. **Handoff.** Host/port/workspace — never print password/ticket/jwt.

## Patterns

### Git vs ColdStorage

| Need | Use |
|------|-----|
| GitHub / this monorepo | Git |
| Studio `cstoraged` workspace | ColdStorage |
| Both | Git for the game repo; ColdStorage only if they use it |

### Settings cookbook

Project Settings (non-secrets):

- `blazium/coldstorage/enabled` (default false)
- `host` default `127.0.0.1`
- `port` **1666**
- `use_tls` / `tls_insecure` (defaults false)
- `workspace` / `repo` (default `default`)
- `workspace_root`, `ca_file`
- `autoload_on_startup` (false), `validate_on_startup` (true)
- `auto_pull` (**false** — turning this on rewrites the working tree)
- `override_editor_settings` (false)

**EditorSettings only** (never `project.godot` / `project.blazium`):
`password`, `ticket`, `jwt`. Legacy project secrets are cleared on register.

`user` may live in project settings; do not put credentials next to it.

## Pitfalls

- **Installed the Godot Git plugin to “fix” ColdStorage** → wrong VCS.
- **Wrote jwt/password into project settings** → EditorSettings only.
- **Enabled `auto_pull` by default** → unexpected overwrites.
- **Documented cstoraged admin APIs** → out of scope.

## Resources

- `blazium/modules/coldstorage/cold_storage_settings.cpp`
- `docs_get_class` → `ColdStorageVCS`

## Related skills

- `blazium-cli` — local tooling
- `blazium-project-config` — other `blazium/*` keys
