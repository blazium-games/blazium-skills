---
name: blazium-physics-tuning
pack: engine
---

# blazium-physics-tuning

Gravity, friction, bounce, and damping. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

A correct collision matrix can still feel icy or floaty. Those knobs are not layer bits.

## What

Project gravity, `PhysicsMaterial` friction and bounce, rigid-body damping.

**Non-goals:** collision layers, raycasts, coyote time.

## How

1. Confirm overlaps already work (`blazium-physics`).
2. Change one feel parameter.
3. Autowork a settle or jump apex.

## Reasoning

`blazium-physics` owns whether bodies hit. This skill owns how the hit feels.

## Sources

- Blazium: `PhysicsMaterial`, `physics/2d/default_gravity`, `physics/3d/default_gravity`

## Limits

Do not invent physics engines. Pin Blazium 0.6.x (Godot 4.3.2 fork).

## Related skills

- `blazium-physics` — setup
- `blazium-2d-movement` — controllers
