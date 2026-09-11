---
name: blazium-ui
description: >
  Builds Blazium 0.6.x Control UI (anchors, Containers, Theme, focus) on
  Godot 4.3.2. Use for HUDs, menus, layout, and JustAMCP theme_tools
  (create_theme, set_control_theme_color, setup_control,
  runtime_find_ui_elements). Prefer Label / RichTextLabel. Not InputMap
  and not localization tables.
when-to-use: >
  Control HUD, Theme, anchors, BoxContainer, focus neighbor,
  runtime_click_button_by_text, create_theme, setup_control, menu UI
metadata:
  author: blazium-games
  short-description: Control HUD, Theme, anchors, and focus
---

# Blazium UI

Control nodes — not UITK/uGUI/IMGUI. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
JustAMCP: `theme_tools` (`create_theme`, `set_control_theme_color`,
`setup_control`), prompt `blazium_ui_scaffolder`.

**Version drift:** inspect `config_version` / `features` in `project.blazium`.
Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when building HUD, menus, focus navigation, or Theme resources.

**When not to use:** InputMap actions → `blazium-input`. Localization strings →
`blazium-localization`. World-space 3D labels → `blazium-3d`.

## Grok host

Read this file only. Spawn `ui-programmer` for anchors/Theme. Child prompts
must include scene path, Theme path, and focus neighbors. Evidence is
`runtime_click_button_by_text` or Autowork text assert — not a HUD screenshot.

## Workflow

1. **Inspect.** Anchors vs Containers; existing Theme.
2. **Layout.** Containers for lists; anchors for HUDs. Do not mix both on one Control.
3. **Theme.** Colors/fonts via Theme, not per-control one-offs (`create_theme`).
4. **Verify.** Focus next/prev; play-mode `runtime_click_button_by_text` and
   `runtime_find_ui_elements`. Autowork `assert_eq` on Label/button text.
5. **Handoff.** Theme path + focus neighbor chain.

## Patterns

```gdscript
extends Control
@onready var title: Label = $Title
func _ready() -> void:
	theme = load("res://ui/main_theme.tres") as Theme
	title.text = "HUD"
```

## Output contract

- Scene path and root Control
- Theme path
- Focus neighbor chain
- Click / text evidence

## Pitfalls

- **Used Unity RectTransform APIs** → anchors + offsets on Control.
- **Hardcoded English in buttons** → `blazium-localization` + `tr()`.
- **Theme overridden on every node** → one Theme resource.
- **Anchors and a Container on the same Control** → Container owns size.

## Related skills

- `blazium-localization`, `blazium-input`, `blazium-animation`, `blazium-autowork`
