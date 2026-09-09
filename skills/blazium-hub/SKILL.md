---
name: blazium-hub
description: >
  Operates the Blazium desktop Hub (hub.json, hub-remote ensure, port 39218,
  blazium://hub). Use when focusing Hub or wiring hub_remote.json. Do not use
  for blazium-cli install verbs or running-editor HTTP (blazium-cli-remote).
---

# Blazium Hub

Desktop Hub for editors and projects. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Hub ≠ Services.** No lobby buttons, no JWT login, no store dashboard.
Hub does **not** install editors; it shells `blazium-cli --json`.

Install/update the Hub binary with `blazium-cli update apply --product hub`.
Details: [references/hub.md](references/hub.md).

Config: `%APPDATA%\blazium\hub.json`. Hub remote waits for `/v1/health` on
port **39218**, then `show_hub` / `focus_window`.

## When to use

- Use when the user wants the Hub window, `hub-remote ensure`, or
  `blazium://hub` / `blazium://project/<encoded-path>`.
- Use when diagnosing Hub bind/token on port 39218.

**When not to use:** install editors/templates → `blazium-cli`. Control a
running game editor → `blazium-cli-remote`. Login/JWT → `blazium-services`.
Crash sidecar → `blazium-crash-reporter`.

## Workflow

1. **Inspect.** Hub installed? `hub.json` present? Port 39218 free?
2. **Choose.** Launch Hub (`blazium://hub`) or `hub-remote ensure`.
3. **Implement.** `blazium-cli hub-remote ensure` (optional `--path`).
   `ensure` never rotates a valid token.
4. **Verify.** `/v1/health` on 39218; Hub focuses.
5. **Handoff.** Editor install still uses `blazium-cli install`.

## Patterns

```text
blazium-cli handle-uri blazium://hub
blazium-cli hub-remote ensure
BlaziumHub --headless --ensure-hub-remote --quit
```

Prefer the CLI `hub-remote ensure`. Headless Hub is the installer fallback.

UI: Projects, Editors, News, Settings, tray.

## Pitfalls

- **Treated Hub as blazium.games login** → `blazium-services`.
- **Invented `blazium-cli hub install`** → `blazium-cli install`.
- **Rotated a valid hub-remote token** → `ensure` must not.

## Resources

- https://github.com/blazium-games/blazium-hub
- [references/hub.md](references/hub.md)

## Related skills

- `blazium-cli` — install / update products
- `blazium-cli-remote` — game/editor HTTP `/v1` (not Hub 39218)
- `blazium-new-project` — game content after Hub/CLI has an editor
- `blazium-autowork` — Hub's own Autowork suite
