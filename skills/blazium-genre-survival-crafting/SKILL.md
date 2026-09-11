---
name: blazium-genre-survival-crafting
description: >
  Composes a gather/craft/needs loop from pinned Blazium 0.6.x skills
  (resources, SQLite, 3D). Use when the request is survival, crafting,
  hunger, heat, recipe, or base piece. Not a shop-only idle and not a pure
  FPS kit.
when-to-use: >
  survival, crafting, gather, recipe, hunger, heat, base building,
  RecipeData resource
metadata:
  author: blazium-games
  short-description: Compose survival/crafting from resources, SQLite, 3D pins
---

# Blazium genre: survival / crafting

Thin adapter — not a survival framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when gathering, crafting, hunger/heat, or base pieces are the loop.
- Use when recipes are data (`Resource` / CSV) and inventory must survive
  in `user://`.

**When not to use:** shop-only idle → `blazium-clicker`. Pure FPS →
`blazium-genre-fps-shooter`. 2D rooms without needs → `blazium-tilemap` +
`blazium-resources` directly.

## Grok host

Read this adapter, then **one** pin. Spawn `systems-designer` for recipes
and `gameplay-programmer` for the craft/save round-trip. Child prompts must
include recipe Resource path, SQLite path, and which need (hunger/heat)
is in scope. Do not dump the catalog.

Evidence is Autowork on craft + save round-trip — not a screenshot of a
crafting menu.

## Workflow

1. **Inspect.** Item defs / world / existing save.
2. **Choose.** Pins below. Order: resources recipes → SQLite `user://` →
   3D/tile world → Autowork craft/save.
3. **Implement.** Router + this adapter + **one** pin at a time.
4. **Verify.** Autowork on craft + save round-trip — not screenshots.
5. **Handoff.** 2D world → `blazium-tilemap`. Multiplayer →
   `blazium-multiplayer-core`. Idle overflow → `blazium-clicker`.

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

Persist needs/recipes with `blazium-sqlite`, not a custom binary dump.
Do not invent Godot 4.7 voxel APIs.

## Output contract

- Recipe / item Resource paths
- Save path (`user://…`) and query
- Need fields in scope (hunger / heat / none)
- Autowork craft + reload assertion

## Pitfalls

- **Wrote a custom binary save** → `blazium-sqlite`.
- **Godot 4.7 Voxel APIs** → not in 4.3.2; stay on meshes/grids you have.
- **Rewrote a studio survival pack** → compose pins.
- **Saved world state in `res://`** → `user://` only.

## Related skills

- `blazium-resources`, `blazium-sqlite`, `blazium-3d`, `blazium-tilemap`,
  `blazium-multiplayer-core`
