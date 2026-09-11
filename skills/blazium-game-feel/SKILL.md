---
name: blazium-game-feel
description: >
  Adds juice on Blazium 0.6.x with Tween, AnimationPlayer, particles, and
  camera punch (hit-stop, squash, screenshake). Use for feedback polish
  on an existing mover or Control. Movement controllers stay on
  blazium-2d-movement; clip libraries on blazium-animation.
when-to-use: >
  game feel, juice, hit-stop, squash stretch, camera punch, screenshake,
  create_tween, GPUParticles2D burst
metadata:
  author: blazium-games
  short-description: Tween juice, hit-stop, squash, and camera punch
---

# Blazium game feel

Short feedback on hit, land, and UI press. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Use 4.3.2 `Tween`, `AnimationPlayer`,
`GPUParticles2D` / `CPUParticles2D`, `Camera2D` offset.

## When to use

- Use when adding hit-stop, squash, camera punch, or particle bursts
  on an existing controller.

**When not to use:** writing the mover → `blazium-2d-movement`. AnimationTree
→ `blazium-animation`. Pixel snap → `blazium-pixel-perfect`.

## Grok host

Read this file only after the mover exists. Spawn `gameplay-programmer`
and `qa-tester`. Child prompts must include target node path and rest
scale/offset. Evidence is Autowork after the tween duration.

## Workflow

1. **Inspect.** Who owns velocity / camera.
2. **Choose.** `create_tween()` for one-shots.
3. **Implement.** Durations ≤ 200 ms. Restore camera offset and `time_scale`.
4. **Verify.** Autowork `assert_eq` on restored scale/offset.
5. **Handoff.** Which node plays the punch.

## Patterns

```gdscript
func punch_camera(cam: Camera2D, strength: float = 4.0) -> void:
	var tw := create_tween()
	tw.tween_property(cam, "offset", Vector2(strength, 0), 0.04)
	tw.tween_property(cam, "offset", Vector2.ZERO, 0.08)
```

## Output contract

- Target node path
- Effect type
- Restored properties
- Autowork restore assert

## Pitfalls

- **Rewrote `move_and_slide`** → `blazium-2d-movement`.
- **Left camera `offset` dirty** → tween back to `Vector2.ZERO`.
- **Forgot to restore `time_scale`** → game stays slow.
- **Used Godot 4.7-only tweeners** → 4.3.2 `create_tween()` only.

## Related skills

- `blazium-animation`, `blazium-2d-movement`, `blazium-audio`, `blazium-ui`
