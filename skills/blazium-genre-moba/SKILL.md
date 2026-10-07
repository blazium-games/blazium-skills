---
name: blazium-genre-moba
description: >
  Composes a lane and last-hits from pinned Blazium 0.8.x skills.
when-to-use: >
  moba, lane, last hit, ability, tower
metadata:
  author: blazium-games
  short-description: Compose a lane from navigation, UI, and ability pins
---

# Blazium genre: moba

Thin adapter — not a genre framework. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**. Inspect `config_version` / `features`; keep `blazium_4.8`-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the request is a lane, last-hits, or a tower.

**When not to use:** Battle royale circle → `blazium-genre-battle-royale`.

## Grok host

On Grok, keep context small: read this file, then **one** pin `SKILL.md`.
Child prompts must include the scene path and the 4.8.x pin. Do not dump the catalog.

Prefer project files over memory. Evidence is Autowork, not a screenshot.

## Workflow

1. **Inspect.** `project.blazium` / `config_version`. Existing scenes and InputMap.
2. **Choose.** Pins below — no custom framework.
3. **Implement.** This adapter + **one** pin at a time (router + two max).
4. **Verify.** One Autowork assert for the verb in the table.
5. **Handoff.** Pins used, scene path, action names.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-navigation` | lane path |
| `blazium-ui` | ability bar |
| `blazium-resources` | hero stats |
| `blazium-3d` | lane |
| `blazium-autowork` | last-hit assert |

One Autowork: killing a lane minion adds gold on the hero resource.

## Output contract

- Scene path(s) touched
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used non-`blazium_4.8` APIs** → stay on 4.8.x.
- **Skipped Autowork** → add the verb assert before juice.

## Related skills

`blazium-navigation`, `blazium-ui`, `blazium-resources`, `blazium-3d`, `blazium-autowork`
