---
name: blazium-version-migration
description: >
  Moves a Godot 4.x project onto the Blazium 4.8 line. Use when the user
  asked to migrate. Keep the current pin otherwise. Godot 3 renames stay
  in blazium-gdscript.
when-to-use: >
  migrate to Blazium 4.8, Godot 4.x hop, HDR, AreaLight3D, virtual joystick,
  tween await
metadata:
  author: blazium-games
  short-description: Godot 4.x hop onto the Blazium 4.8 line
---

# Blazium version migration

Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Keep the project's pin unless the user asked to migrate. Godot 3 names
(`yield`, bare `export` / `onready`, `.instance()`, `KinematicBody2D`,
`Spatial`, unsuffixed `Sprite`, `File` / `Directory`, `Pool*Array`,
three-argument `connect`) stay in `blazium-gdscript`. Do not paste that
table here.

## When to use

- Use when the user asked to move a Godot 4.x project onto `blazium_4.8`.
- Use for the 4.x hop items below.

**When not to use:** the project is already on `blazium_4.8` and nobody asked to migrate. A Godot 3 script rewrite → `blazium-gdscript`.

## Workflow

1. **Inspect.** `config_version` and `features` in `project.godot` / `project.blazium`.
2. **Choose.** Stay on the pin unless migration was requested.
3. **Implement.** One hop item per turn.
4. **Verify.** The project still opens on the 4.8 editor. Parse or play the scene you touched.
5. **Handoff.** Old pin, new pin, files touched.

## Patterns

| Hop | 4.8 note |
|-----|----------|
| HDR | WorldEnvironment uses the 4.8 glow / tonemap path. Do not keep a 4.2 glow stack. |
| AreaLight3D | Replace older area-light nodes with `AreaLight3D`. |
| Virtual joystick | Touch controls use the 4.8 virtual joystick nodes, not a custom Godot 3 analog. |
| Tween await | `await` the tween signal. Do not poll a finished flag from a 4.0 pattern. |

After a `class_name` add, rename, or delete, finish the editor class scan or run `blazium --headless --import` before the next script uses that name.

## Output contract

- Previous pin and target pin
- Hop items applied
- Parse or play evidence

## Pitfalls

- **Migrated when the user did not ask** → keep the pin.
- **Pasted the Godot 3 rename table** → that table lives in `blazium-gdscript`.
- **Rebuilt the engine** → this skill only moves the project.

## Related skills

- `blazium-gdscript`, `blazium-project-config`, `blazium-cli`, `blazium-environment`
