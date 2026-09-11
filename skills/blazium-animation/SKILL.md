---
name: blazium-animation
description: >
  Authors AnimationPlayer clips, AnimationTree states, and Tween one-shots on
  Blazium 0.6.x / Godot 4.3.2. Use when keyframing properties, wiring state
  machines, or fading UI. Prefer JustAMCP animation_tools. SpriteFrames
  flipbooks go to blazium-sprites. Not shaders that scroll UVs.
when-to-use: >
  AnimationPlayer, AnimationTree, create_tween, keyframe, clip, state machine,
  UI fade, animation_finished
metadata:
  author: blazium-games
  short-description: AnimationPlayer, AnimationTree, and Tween on 4.3.2
---

# Blazium animation

Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. JustAMCP: `create_animation`,
`set_animation_keyframe`, `add_animation_track`, `configure_sprite_frames`.
Do not apply Godot 4.7-only AnimationMixer APIs.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when keyframing properties, AnimationTree states, or `create_tween()`.
- Use when a clip already exists and the bug is play-from-tree or finished signal.

**When not to use:** SpriteFrames-only flipbooks → `blazium-sprites`. Shaders
that animate UVs → `blazium-shaders`. Hit-stop / camera punch →
`blazium-game-feel` after the clip plays.

## Grok host

Load this file plus at most one pin (`blazium-sprites` or `blazium-ui`).
Spawn `gameplay-programmer` or `technical-artist`. Child prompts must include
the AnimationPlayer path and clip names. Do not dump the catalog.

Grok `code_execution` and timeline screenshots are not evidence. Quote Autowork
`wait_for_signal("animation_finished")` or JustAMCP `animation_tools`.

## Workflow

1. **Inspect.** Existing AnimationPlayer libraries and whether the node is in-tree.
2. **Choose.** Player for clips; Tree for characters; Tween for one-shot UI.
3. **Implement.** `create_animation` / `add_animation_track` /
   `set_animation_keyframe`, or `create_tween()`.
4. **Verify.** Autowork `wait_for_signal` on `animation_finished`. Tweens:
   Autowork `assert_eq` on the property after the duration.
5. **Handoff.** Clip names + which node owns the AnimationPlayer.

## Patterns

```gdscript
var tw := create_tween()
tw.tween_property(self, "modulate:a", 0.0, 0.25)
```

JustAMCP: `create_animation` then `add_animation_track` /
`set_animation_keyframe`. Flipbooks: `configure_sprite_frames` →
`blazium-sprites`.

```gdscript
func test_intro_finishes() -> void:
	var p := $AnimationPlayer
	p.play("intro")
	wait_for_signal(p, "animation_finished", 2.0)
```

## Output contract

- AnimationPlayer / Tween owner path
- Clip or tween names
- Autowork test name + pass/fail, or `INCONCLUSIVE`
- Next skill (`blazium-sprites`, `blazium-game-feel`, `blazium-ui`)

## Pitfalls

- **Mixed SpriteFrames and AnimationPlayer on the same sprite without a plan**
  → pick one owner.
- **Tween after node freed** → `autofree` / bind the tween.
- **Played a clip before the player is in the tree** → call play from `_ready()`
  or after `add_child`.
- **Tuned juice before the clip plays** → this skill first, `blazium-game-feel` second.

## Resources

- JustAMCP: `animation_tools`
- Docs: https://docs.blazium.app (AnimationPlayer, 4.3.2-safe)

## Related skills

- `blazium-sprites` — frames
- `blazium-ui` — UI motion
- `blazium-game-feel` — juice after the clip plays
- `blazium-autowork` — wait_for_signal
