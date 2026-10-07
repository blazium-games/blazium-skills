---
name: blazium-visual-proof
description: >
  Proves a visual change with the same editor camera, a before screenshot,
  the change, an after screenshot, and blazium_runtime_compare_screenshots.
  Use when a scene, material, or particle edit must be shown, not described.
---

# Blazium visual proof

Same camera, two shots, one compare. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Prompt: `blazium_visual_proof`.

## When to use

- Use when a 3D or 2D edit should be shown with a before and after image.
- Use when the camera pose must stay fixed across the change.

**When not to use:** a playable bug → `blazium-playtest`. A pass/fail claim → `blazium-verify`.

## Workflow

1. Read `blazium_editor_get_camera`.
2. Set position, rotation, and fov with `blazium_editor_set_camera`.
3. Capture with `blazium_editor_take_screenshot`.
4. Make the change with the existing scene, shader, or particle tools.
5. Set the same camera again.
6. Capture the second shot.
7. Compare the PNG paths with `blazium_runtime_compare_screenshots`.
8. Name the loaded `res://` path of the asset under test in the shot pair. A placeholder does not pass.

## Output contract

- Camera pose
- Both screenshot paths
- Loaded `res://` path
- Compare result

## Related skills

- `blazium-playtest` — session notes
- `blazium-vfx` — particle and shader looks
- `blazium-editor-ui` — dialogs and unsaved files
