---
name: blazium-game-feel
description: >
  Adds juice on Blazium 0.6.x with Tween, AnimationPlayer, particles, and
  camera punch (hit-stop, squash, screenshake). Use for feedback polish.
  Movement controllers stay on blazium-2d-movement; clip libraries on
  blazium-animation.
---

# Blazium game feel

Short feedback on hit, land, and UI press. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Use 4.3.2 nodes only: `Tween`, `AnimationPlayer`,
`GPUParticles2D` / `CPUParticles2D`, `Camera2D` offset.

Do not invent a juice middleware. Movement math stays on
`blazium-2d-movement`.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding hit-stop, squash/stretch, camera punch, or one-shot
  particle bursts on an existing controller.
- Use when a UI press needs a scale tween.

**When not to use:** writing the mover → `blazium-2d-movement`. Long
AnimationTree state machines → `blazium-animation`. Shader UV loops →
`blazium-shaders`.

## Workflow

1. **Inspect.** Who owns velocity / camera. Existing AnimationPlayer.
2. **Choose.** `create_tween()` for one-shots; AnimationPlayer for authored
   punches; particles for bursts.
3. **Implement.** Keep durations short (≤ 200 ms). Restore camera offset.
4. **Verify.** Autowork: after the tween duration, `assert_eq` on scale or
   offset returning to rest. Play-mode MCP. Not a screenshot of juice.
5. **Handoff.** Which node plays the punch.

## Patterns

```gdscript
func punch_camera(cam: Camera2D, strength: float = 4.0) -> void:
	var tw := create_tween()
	tw.tween_property(cam, "offset", Vector2(strength, 0), 0.04)
	tw.tween_property(cam, "offset", Vector2.ZERO, 0.08)

func squash(target: Node2D) -> void:
	var tw := create_tween()
	tw.tween_property(target, "scale", Vector2(1.2, 0.8), 0.05)
	tw.tween_property(target, "scale", Vector2.ONE, 0.08)
```

Hit-stop: `Engine.time_scale = 0.05` for a few frames, then restore `1.0`
in the same function. Do not leave `time_scale` stuck.

## Pitfalls

- **Rewrote `move_and_slide` here** → `blazium-2d-movement`.
- **Left camera `offset` dirty** → tween back to `Vector2.ZERO`.
- **Forgot to restore `time_scale`** → the game stays slow.
- **Used Godot 4.7-only tweeners** → 4.3.2 `create_tween()` only.

## Resources

- JustAMCP: `animation_tools`, `particle_tools`
- https://docs.blazium.app — `Tween`, `Camera2D`

## Related skills

- `blazium-animation` — clip libraries / AnimationTree
- `blazium-2d-movement` — controllers
- `blazium-audio` — hit SFX buses
- `blazium-ui` — Control tweens
