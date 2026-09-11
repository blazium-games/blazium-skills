---
name: blazium-itch-publish
description: >
  Ships a Blazium build to itch.io with butler. Use for butler push /
  channels / status. Not a Blazium-only store and not SteamPipe.
when-to-use: >
  itch.io, butler push, butler status, itch channel, html5 itch
metadata:
  author: blazium-games
  short-description: Push export artifacts to itch.io with butler
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

## Grok host

Read this skill plus `blazium-export` if the artifact is missing. Spawn
`tools-programmer` for butler and `qa-tester` for `butler status`. Child
prompts must include user/game slug and channel name. Do not invent a
Blazium itch API.

Evidence is `butler status` / channel version — not a screenshot of the
itch page.

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

## Output contract

- Channel name
- Artifact path (export output, not `res://`)
- butler command + status
- Whether CI will own the next push

## Pitfalls

- **Invented a Blazium-only itch store** → butler + itch.io page.
- **Pushed `res://` instead of export output** → export first.
- **Used steamcmd here** → `blazium-steam-publish`.

## Related skills

- `blazium-export` — builds
- `blazium-export-web` — HTML5
- `blazium-ci-export` — GHA
