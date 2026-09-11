---
name: blazium-steam-publish
description: >
  Ships a Blazium build to Steam (SteamPipe / steamcmd / depots). Use for
  store page + depot upload. Not Steamworks runtime JWT
  (authenticate_with_server).
when-to-use: >
  SteamPipe, steamcmd, depot upload, app_build vdf, Steam store build
metadata:
  author: blazium-games
  short-description: Upload Steam depots with steamcmd; runtime stays blazium-steam
---

# Blazium Steam publish

Publish is not runtime auth. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when uploading a depot, setting a build live, or wiring SteamPipe.

**When not to use:** session tickets / achievements → `blazium-steam`.
itch.io → `blazium-itch-publish`. blazium.games page →
`blazium-games-publish`.

## Grok host

Read this skill plus `blazium-export` if the artifact is missing. Spawn
`tools-programmer` for steamcmd. Child prompts must include the user App ID
and depot IDs — do not invent an App ID. Never print steamcmd passwords.

Evidence is steamcmd success / build ID — not a screenshot of the Steam
client.

## Workflow

1. **Inspect.** Export preset + `steam_appid.txt` if present. App ID from
   the user — do not invent one.
2. **Choose.** Desktop artifact via `blazium-export`. Use steamcmd /
   `app_build_*.vdf` with the user App ID.
3. **Implement.** Build first (`blazium-export` / CI). Then depot upload
   with steamcmd. Runtime Steam singleton stays on `blazium-steam`.
4. **Verify.** steamcmd success / build ID on a branch — not a screenshot
   of the Steam client.
5. **Handoff.** Build path + depot IDs (not secrets). JWT login is not this
   skill.

## Patterns

| Pin | Owns |
|-----|------|
| steamcmd / SteamPipe | depots, `app_build_*.vdf` |
| `blazium-export` | Blazium export artifacts |
| `blazium-ci-export` | GHA upload if used |
| `blazium-steam` | runtime Steamworks only |

## Output contract

- App ID (user-provided)
- Depot / branch IDs
- Artifact path
- steamcmd result / build ID
- Secrets: never committed

## Pitfalls

- **Taught `authenticate_with_server` here** → `blazium-steam`.
- **Invented GodotSteam publish APIs** → wrong stack.
- **Committed steamcmd passwords** → user env / secrets store.

## Related skills

- `blazium-steam` — runtime
- `blazium-export` — builds
- `blazium-ci-export` — CI
