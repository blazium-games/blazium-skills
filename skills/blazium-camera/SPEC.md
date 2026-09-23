---
name: blazium-camera
pack: engine
---

# blazium-camera

Follow and framing. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

A camera that jitters, peeks past the level, or lags the body makes motion feel broken even when the controller is correct.

## What

`Camera2D` smoothing, drag margins, limits, look-ahead offset, `Camera3D` orbit, `SpringArm3D` collision, multi-target framing.

**Non-goals:** pixel snap, hit-stop, and player movement.

## How

1. Inspect the current camera and who writes `offset`.
2. Prefer built-in smoothing and drag margins.
3. Follow after physics. Smooth with `1.0 - exp(-rate * delta)`.
4. Verify limits and spring-arm collision with Autowork or play mode.

## Reasoning

Distinct from `blazium-pixel-perfect` (integer snap) and `blazium-game-feel` (punch). The router can load framing without loading juice.

## Sources

- Blazium: `Camera2D`, `Camera3D`, `SpringArm3D`

## Limits

Do not invent camera classes. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-pixel-perfect` — snap
- `blazium-game-feel` — punch
