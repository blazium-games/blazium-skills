---
name: blazium-genre-visual-novel
description: >
  Composes a visual-novel scene flow from pinned Blazium 0.6.x skills
  (dialogue, localization, UI, audio, resources). Use when the request is VN,
  letterbox, CG swap, choice scene, or dialogue-plus-art loop. Not an RPG
  combat kit and not a talk-graph-only skill.
when-to-use: >
  visual novel, VN, letterbox, CG, choice scene, dialogue scene flow
metadata:
  author: blazium-games
  short-description: Compose a VN from dialogue, UI, audio, locale pins
---

# Blazium genre: visual novel

Thin adapter — not a VN engine. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack. The talk graph lives in
`blazium-dialogue`; this adapter owns scene flow around that graph.

## When to use

- Use when the core loop is dialogue, choices, and scene art.
- Use when letterbox / CG / speaker portraits wrap an existing talk graph.

**When not to use:** RPG combat + quests → `blazium-genre-rpg`. A talk
graph only (no VN scene flow) → `blazium-dialogue`. Raw locale files
only → `blazium-localization`.

## Grok host

Read this adapter, then **one** pin. Spawn `writer` for `tr()` keys and
`game-designer` for scene flow. Child prompts must include the dialogue
graph path, locale prefix, and which Control is the textbox. Do not dump
the catalog.

Evidence is Autowork on choice flags + `tr()` — not a screenshot of the
textbox.

## Workflow

1. **Inspect.** Dialogue source / locales / UI theme / portraits.
2. **Choose.** Pins below. Order: dialogue graph → localization keys → UI
   textbox/choices → resources for CG/speakers → audio buses.
3. **Implement.** Router + this adapter + **one** pin at a time.
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
Portraits and CG are Resource fields, not baked textures in the walker.

## Output contract

- Dialogue graph path
- Locale key prefix and locale used in the test
- Textbox / choice Control paths
- Autowork flag + `tr()` assertions

## Pitfalls

- **Hardcoded English script** → localization.
- **Invented a Ren'Py runtime** → compose pins.
- **Stored flags in `res://`** → sqlite / save-systems `user://` if persistent.
- **Owned the talk graph here** → `blazium-dialogue`.

## Related skills

- `blazium-dialogue`, `blazium-localization`, `blazium-ui`, `blazium-audio`,
  `blazium-resources`, `blazium-save-systems`
