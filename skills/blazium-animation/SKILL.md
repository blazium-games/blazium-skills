---
name: blazium-animation
description: >
  Authors Blazium animation (AnimationPlayer, AnimationTree, Tween) on 4.3.2.
  Use when adding clips, state machines, or UI tweens. Prefer JustAMCP
  animation_tools. SpriteFrames flipbooks go to blazium-sprites.
---

# Blazium animation

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. JustAMCP: `create_animation`,
`set_animation_keyframe`, `add_animation_track`, `configure_sprite_frames`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when keyframing properties, AnimationTree states, or `create_tween()`.

**When not to use:** SpriteFrames-only flipbooks → `blazium-sprites`. Shaders
that animate UVs → `blazium-shaders`.

## Workflow

1. **Inspect.** Existing AnimationPlayer libraries.
2. **Choose.** Player for clips; Tree for characters; Tween for one-shot UI.
3. **Implement.** `create_animation` / `add_animation_track` /
   `set_animation_keyframe`, or `create_tween()`.
4. **Verify.** Play the clip in play mode. Autowork `wait_for_signal` on
   `animation_finished`. Tweens: Autowork `assert_eq` on the property after
   the duration. Not a screenshot of the timeline.
5. **Handoff.** Clip names + which node owns the AnimationPlayer.

## Patterns

```gdscript
var tw := create_tween()
tw.tween_property(self, "modulate:a", 0.0, 0.25)
```

JustAMCP: `create_animation` then `add_animation_track` /
`set_animation_keyframe`. Flipbooks: `configure_sprite_frames` →
`blazium-sprites`.

## Pitfalls

- **Mixed SpriteFrames and AnimationPlayer on the same sprite without a plan**
  → pick one owner.
- **Tween after node freed** → `autofree` / bind the tween.
- **Played a clip before the player is in the tree** → call play from `_ready()`
  or after `add_child`.

## Resources

- JustAMCP: `animation_tools`

## Related skills

- `blazium-sprites` — frames
- `blazium-ui` — UI motion
- `blazium-autowork` — wait_for_signal
