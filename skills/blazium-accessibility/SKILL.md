---
name: blazium-accessibility
description: >
  Makes a Blazium 0.6.x game remappable and readable: InputMap remaps, Theme
  font scale, contrast, and locale-safe copy via tr(). Use for accessibility
  pass, remapping, or scalable UI. Visual bible stays with art-director.
when-to-use: >
  remapping, font scale, contrast, subtitle scale, accessibility pass,
  InputMap rebind, Theme default_font_size
metadata:
  author: blazium-games
  short-description: Remap InputMap and scale Theme fonts; persist in user://
---

# Blazium accessibility

Players must remap, read, and play in their locale. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Use `InputMap`, `Theme` font size, and `tr()`.

Do not invent a screen-reader plugin. Do not own the art bible.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding remapping, font scale, color-blind-safe palettes, or
  subtitle scale.
- Use when copy must stay locale-safe (no concatenated sentences).

**When not to use:** designing the InputMap from scratch only →
`blazium-input`. Theme chrome without a11y → `blazium-ui`. Locale files
only → `blazium-localization`. Visual identity → art-director, not this
skill.

## Grok host

Read this skill, then `blazium-input` if actions are missing. Spawn
`ux-designer` for the settings flow and `ui-programmer` for Theme scale.
Child prompts must include action names and the Theme resource path.
Do not dump the catalog.

Evidence is Autowork: rebind an action, `assert_true` on
`InputMap.action_has_event`; scale the Theme and assert font size. Not a
screenshot of a settings menu. Grok `code_execution` is not evidence.

## Workflow

1. **Inspect.** Actions, Theme default font, hardcoded English.
2. **Choose.** Persist remaps and scale in `user://` (`ConfigFile`).
3. **Implement.** `InputMap.action_erase_events` + `action_add_event`.
   Theme `default_font_size`. All strings `tr()`.
4. **Verify.** Autowork: rebind an action, `assert_true` on
   `InputMap.action_has_event`. Scale the Theme and assert font size.
   Not a screenshot of a settings menu.
5. **Handoff.** Action names + Theme resource. Juice → `blazium-game-feel`.

## Patterns

```gdscript
func rebind(action: String, event: InputEvent) -> void:
	InputMap.action_erase_events(action)
	InputMap.action_add_event(action, event)

func apply_font_scale(theme: Theme, scale: float) -> void:
	theme.default_font_size = int(16 * scale)
```

Persist under `user://settings.cfg` (`blazium-save-systems` / `ConfigFile`).
Do not store remaps in `res://`.

Avoid color-only failure states: pair hue with an icon or label via `tr()`.

## Output contract

- Action names rebound
- Theme resource + font scale
- Persist path (`user://settings.cfg`)
- Autowork rebind + font-size asserts

## Pitfalls

- **Hardcoded "Press E"** → `tr()` and the current InputMap event.
- **Contrast-only on one Theme color** → check hover/disabled too.
- **Owned the sprite bible** → art-director.
- **Invented a TTS singleton** → not in 4.3.2 core; say so.

## Resources

- JustAMCP: `input_tools`, `theme_tools`
- https://docs.blazium.app — `InputMap`, `Theme`

## Related skills

- `blazium-input` — action setup
- `blazium-ui` — Control / Theme
- `blazium-localization` — `tr()` tables
- `blazium-save-systems` — persist remaps
- `blazium-game-feel` — motion that must stay skippable
