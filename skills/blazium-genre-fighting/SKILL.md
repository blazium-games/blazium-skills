---
name: blazium-genre-fighting
description: >
  Composes a 2D or 3D bout from pinned Blazium 0.8.x skills.
when-to-use: >
  fighting, hitbox, hurtbox, round, combo, 1v1 bout
metadata:
  author: blazium-games
  short-description: Compose a bout from animation, physics, and input pins
---

# Blazium genre: fighting

Thin adapter — not a genre framework. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**. Inspect `config_version` / `features`; keep `blazium_4.8`-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the request is a fighting bout, hitbox/hurtbox, or round timer.

**When not to use:** Top-down brawler with no rounds → `blazium-2d-movement`.

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
| `blazium-animation` | strike clips |
| `blazium-physics` | hitbox / hurtbox |
| `blazium-input` | punch / block |
| `blazium-game-feel` | hit-stop after the hit lands |
| `blazium-autowork` | round assert |

One Autowork: after the punch action, the hurtbox reports a hit and the round timer is still running.

## Output contract

- Scene path(s) touched
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used non-`blazium_4.8` APIs** → stay on 4.8.x.
- **Skipped Autowork** → add the verb assert before juice.

## Related skills

`blazium-animation`, `blazium-physics`, `blazium-input`, `blazium-game-feel`, `blazium-autowork`
