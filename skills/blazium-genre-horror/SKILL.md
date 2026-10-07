---
name: blazium-genre-horror
description: >
  Composes a tension scene from pinned Blazium 0.8.x skills.
when-to-use: >
  horror, flashlight, stalker, dread, limited view
metadata:
  author: blazium-games
  short-description: Compose a horror scene from audio, light, and camera pins
---

# Blazium genre: horror

Thin adapter — not a genre framework. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**. Inspect `config_version` / `features`; keep `blazium_4.8`-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the request is dread, a stalker, a flashlight, or a limited view.

**When not to use:** Jump-scare juice only → `blazium-game-feel`.

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
| `blazium-audio` | stingers / beds |
| `blazium-environment` | dark exposure |
| `blazium-camera` | limited view |
| `blazium-3d` | space |
| `blazium-autowork` | light-off assert |

One Autowork: with the flashlight off, the player node is still in the scene and the ambient bus is audible.

## Output contract

- Scene path(s) touched
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used non-`blazium_4.8` APIs** → stay on 4.8.x.
- **Skipped Autowork** → add the verb assert before juice.

## Related skills

`blazium-audio`, `blazium-environment`, `blazium-camera`, `blazium-3d`, `blazium-autowork`
