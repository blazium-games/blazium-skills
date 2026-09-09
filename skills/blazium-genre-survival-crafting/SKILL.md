---
name: blazium-genre-survival-crafting
description: >
  Composes survival/crafting from pinned Blazium skills (resources, SQLite,
  genres/survival-crafting — do not rewrite it.
---

# Blazium genre: survival / crafting

Thin adapter — not a survival framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone
skill pack.

## When to use

- Use when gathering, crafting, hunger/heat, or base pieces are the loop.

**When not to use:** shop-only idle → `blazium-clicker`. Pure FPS →
`blazium-genre-fps-shooter`.

## Workflow

1. **Inspect.** Item defs / world / existing save.
2. **Choose.** Pins below.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on craft + save round-trip — not screenshots.
5. **Handoff.** 2D world → `blazium-tilemap`. Multiplayer → core.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-resources` | items / recipes |
| `blazium-sqlite` | world / inventory save |
| `blazium-3d` | world / props |

Recipe as a `Resource`; persist crafted counts in `user://`:

```gdscript
extends Resource
class_name RecipeData
@export var id: StringName
@export var outputs: PackedStringArray

var db := SQLite.new()
if not db.load_from("user://world.sqlite"):
	push_error(db.get_last_error_message())
```

Persist needs/recipes with `blazium-sqlite`, not a custom
binary dump.

## Pitfalls

- **Wrote a custom binary save** → `blazium-sqlite`.
- **Godot 4.7 Voxel APIs** → not in 4.3.2; stay on meshes/grids you have.
- **Rewrote a studio survival pack** → compose pins.

## Related skills

- `blazium-resources`, `blazium-sqlite`, `blazium-3d`
