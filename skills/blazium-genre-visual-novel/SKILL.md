---
name: blazium-genre-visual-novel
description: >
  Composes a visual novel from pinned Blazium skills (localization, UI, audio,
  resources). Use for dialogue/choice/scene games.
---

# Blazium genre: visual novel

Thin adapter — not a VN engine. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when the core loop is dialogue, choices, and scene art.

**When not to use:** RPG combat + quests → `blazium-genre-rpg`. A talk
graph only (no VN scene flow) → `blazium-dialogue`. Raw locale files
only → `blazium-localization`.

## Workflow

1. **Inspect.** Dialogue source / locales / UI theme.
2. **Choose.** Pins below.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on choice flags + `tr()` — not screenshots.
5. **Handoff.** Dialogue graph → `blazium-dialogue`. Persist flags →
   `blazium-save-systems`. Music → `blazium-audio`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-dialogue` | graph / choices / flags |
| `blazium-localization` | lines / locales |
| `blazium-ui` | textbox / choices |
| `blazium-audio` | voice / BGM buses |
| `blazium-resources` | character / scene defs |

Drive the textbox and choice buttons with `tr()`, not concatenated English:

```gdscript
TranslationServer.set_locale(locale)
textbox.text = tr("VN_LINE_01")
choice_a.text = tr("VN_CHOICE_A")
choice_b.text = tr("VN_CHOICE_B")
```

`textbox` / `choice_*` are `Label` or `Button` Controls (`blazium-ui`).

## Pitfalls

- **Hardcoded English script** → localization.
- **Invented a Ren'Py runtime** → compose pins.
- **Stored flags in `res://`** → sqlite `user://` if persistent.

## Related skills

- `blazium-localization`, `blazium-ui`, `blazium-audio`, `blazium-resources`
