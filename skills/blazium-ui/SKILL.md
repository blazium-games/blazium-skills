---
name: blazium-ui
description: >
  Builds Blazium Control UI (anchors, Containers, Theme, focus) on 4.3.2 /
  0.6.x. Use for HUDs, menus, and layout. Prefer JustAMCP theme_tools.
  Prefer Label / RichTextLabel over invented text-mesh APIs.
---

# Blazium UI

Control nodes — not UITK/uGUI/IMGUI. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
JustAMCP: `theme_tools` (`create_theme`, `set_control_theme_color`,
`setup_control`), prompt `blazium_ui_scaffolder`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when building HUD, menus, focus navigation, or Theme resources.

**When not to use:** InputMap actions → `blazium-input`. Localization strings →
`blazium-localization`. World-space 3D labels → `blazium-3d`.

## Workflow

1. **Inspect.** Anchors vs Containers; existing Theme.
2. **Layout.** Containers for lists; anchors for HUDs. Do not mix both on one Control.
3. **Theme.** Colors/fonts via Theme, not per-control one-offs (`create_theme`).
4. **Verify.** Focus next/prev; play-mode `runtime_click_button_by_text` and
   `runtime_find_ui_elements`. Autowork `assert_eq` on the Label/button text
   after the click. Not a screenshot alone.
5. **Handoff.** Theme path + focus neighbor chain.

## Patterns

`Control` + `BoxContainer` / `GridContainer` / `MarginContainer`.
`Label` / `RichTextLabel` instead of TextMeshPro. Safe area / stretch via
anchors (`full rect` for overlays).

```gdscript
extends Control

@onready var title: Label = $Title

func _ready() -> void:
	theme = load("res://ui/main_theme.tres") as Theme
	title.text = "HUD"
```

JustAMCP: `setup_control` for anchors; `set_control_theme_color` on the Theme.

## Pitfalls

- **Used Unity RectTransform APIs** → anchors + offsets on Control.
- **Hardcoded English in buttons** → `blazium-localization` + `tr()`.
- **Theme overridden on every node** → one Theme resource.
- **Anchors and a Container on the same Control** → Container owns size. Pick one.

## Resources

- JustAMCP: `theme_tools`, `runtime_find_ui_elements`

## Related skills

- `blazium-localization` — strings
- `blazium-input` — ui_accept
- `blazium-animation` — UI tweens
- `blazium-autowork` — text asserts
