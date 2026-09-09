---
name: blazium-gdscript
description: >
  Writes typed GDScript 2.0 for Blazium 0.6.x (Godot 4.3.2): lifecycle,
  @export/@onready, signals, await. Use when editing .gd files in a Blazium
  project (project.blazium). Do not apply Godot 4.7-only syntax.
---

# Blazium GDScript

Write statically typed GDScript the way Godot 4.3.2 / Blazium 0.6.x intend.
Preserve the project's pinned version unless migration is requested.

**Version drift:** inspect `config_version` / `features` in `project.blazium`.
`script_tools` (`read_script`, `create_script`, `edit_script`, `patch_script`,
`validate_script`) when the editor MCP is connected.

## When to use

- Use when writing or fixing `.gd` files.
- Use when porting Godot 3.x scripts (`yield` → `await`, `export` → `@export`).

**When not to use:** `.luau` → `blazium-luau`. C# → `blazium-csharp`. Scene
tree / instancing → `blazium-nodes-scenes`. Signal *architecture* →
`blazium-signals-groups`. Official templates (Lobby/Login) →
`blazium-gdscript-templates`.

## Workflow

1. **Inspect.** Confirm Blazium 4.3.2-safe features. Reject 4.7-only APIs.
2. **Choose.** Smallest typed pattern. Use `@onready` not `_init()` for children.
3. **Implement.** Prefer JustAMCP script tools over blind file edits.
4. **Verify.** `validate_script` and/or an Autowork `assert_*` on the logic.
5. **Handoff.** Files changed + first parser error if any.

## Patterns

### Typed lifecycle

```gdscript
extends Node2D

@export var speed: float = 90.0
@onready var sprite: Sprite2D = $Sprite2D

func _ready() -> void:
	sprite.modulate = Color.AQUA

func _process(delta: float) -> void:
	rotation_degrees += speed * delta
```

### Signals (4.x Callable)

```gdscript
signal health_changed(current: int, maximum: int)

func take_damage(amount: int) -> void:
	health_changed.emit(maxi(health - amount, 0), 100)

func _ready() -> void:
	health_changed.connect(_on_health_changed)
```

Use `await` for signals/timers — not `yield`.

## Pitfalls

- **Used a Godot 4.7-only API** → revert to 4.3.2 docs / `docs_get_class`.
- **`@onready` in `_init()`** → children do not exist yet.
- **String `connect("signal", self, "method")`** → use Callables.
- **Edited `.luau` with this skill** → hand off.

## Resources

- JustAMCP: `script_tools`, prompt `blazium_gdscript_linter`

## Related skills

- `blazium-luau` — Luau scripts
- `blazium-csharp` — C#
- `blazium-signals-groups` — decoupling
- `blazium-autowork` — tests
