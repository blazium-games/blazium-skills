---
name: blazium-genre-stealth
description: >
  Composes vision and noise from pinned Blazium 0.8.x skills.
when-to-use: >
  stealth, vision cone, noise, hide, undetected
metadata:
  author: blazium-games
  short-description: Compose vision and noise from physics and navigation pins
---

# Blazium genre: stealth

Thin adapter — not a genre framework. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**. Inspect `config_version` / `features`; keep `blazium_4.8`-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the request is a vision cone, noise, or staying undetected.

**When not to use:** Horror with no detection meter → `blazium-genre-horror`.

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
| `blazium-physics` | vision / noise |
| `blazium-navigation` | patrol |
| `blazium-input` | crouch |
| `blazium-3d` | cover |
| `blazium-autowork` | undetected assert |

One Autowork: crouched outside the vision cone keeps the detection meter at zero.

## Output contract

- Scene path(s) touched
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used non-`blazium_4.8` APIs** → stay on 4.8.x.
- **Skipped Autowork** → add the verb assert before juice.

## Related skills

`blazium-physics`, `blazium-navigation`, `blazium-input`, `blazium-3d`, `blazium-autowork`
