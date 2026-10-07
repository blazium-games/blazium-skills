---
name: blazium-genre-racing
description: >
  Composes a lap racer from pinned Blazium 0.8.x skills.
when-to-use: >
  racing, lap, checkpoint, vehicle, drift
metadata:
  author: blazium-games
  short-description: Compose a lap racer from physics and checkpoint pins
---

# Blazium genre: racing

Thin adapter — not a genre framework. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**. Inspect `config_version` / `features`; keep `blazium_4.8`-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the request is laps, checkpoints, or a vehicle on a track.

**When not to use:** On-foot chase → `blazium-genre-platformer` or `blazium-3d`.

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
| `blazium-physics` | vehicle body |
| `blazium-3d` | track |
| `blazium-input` | throttle / steer |
| `blazium-ui` | lap HUD |
| `blazium-autowork` | checkpoint assert |

One Autowork: crossing checkpoint 1 increments the lap counter.

## Output contract

- Scene path(s) touched
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used non-`blazium_4.8` APIs** → stay on 4.8.x.
- **Skipped Autowork** → add the verb assert before juice.

## Related skills

`blazium-physics`, `blazium-3d`, `blazium-input`, `blazium-ui`, `blazium-autowork`
