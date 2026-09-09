---
name: blazium-itch-publish
description: >
  Ships a Blazium build to itch.io with butler. Use for butler push / channels.
  Not a Blazium-only store and not SteamPipe.
---

# Blazium itch publish

Butler + Blazium export — not a custom store. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when pushing a Windows/macOS/Linux/HTML5 channel to itch.io.

**When not to use:** Steam depots → `blazium-steam-publish`. Games cloud
page → `blazium-games-publish`. Building the binary → `blazium-export`.

## Workflow

1. **Inspect.** Export preset / existing `.itch.toml` / butler login.
2. **Choose.** Channel names (`windows-stable`, `html5`, etc.). Artifact from
   `blazium-export` (web → `blazium-export-web`).
3. **Implement.** Build, then `butler push` with butler. CI → `blazium-ci-export`.
4. **Verify.** `butler status` / channel version — not a screenshot.
5. **Handoff.** User/game + channel. Do not invent a Blazium itch API.

## Patterns

| Pin | Owns |
|-----|------|
| butler | channels, itch.io page |
| `blazium-export` | desktop artifacts |
| `blazium-export-web` | HTML5 |
| `blazium-ci-export` | GHA |

## Pitfalls

- **Invented a Blazium-only itch store** → butler + itch.io page.
- **Pushed `res://` instead of export output** → export first.
- **Used steamcmd here** → `blazium-steam-publish`.

## Related skills

- `blazium-export` — builds
- `blazium-export-web` — HTML5
- `blazium-ci-export` — GHA
