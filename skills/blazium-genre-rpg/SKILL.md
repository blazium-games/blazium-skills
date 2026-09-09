---
name: blazium-genre-rpg
description: >
  Composes an RPG from pinned Blazium skills (resources, localization, UI,
  GOAP, SQLite). Use for party/quest/stat games
---

# Blazium genre: RPG

Thin adapter — not an RPG framework. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when building quests, parties, stats, or dialogue-driven RPG loops.

**When not to use:** card combat only → `blazium-genre-card-game`. NPC
pathing without plans → `blazium-navigation`.

## Workflow

1. **Inspect.** Existing items / locales / save.
2. **Choose.** Pins below for APIs.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on inventory/save; `tr()` smoke — not screenshots.
5. **Handoff.** Planner → `blazium-goap`. Streamer → `blazium-streaming`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-resources` | items / stats `.tres` |
| `blazium-localization` | `tr()` / locales |
| `blazium-ui` | menus / HUD |
| `blazium-goap` | NPC plans (`init(actor)`) |
| `blazium-sqlite` | save (`user://`) |

Plan NPCs with GOAP; persist slot data with SQLite:

```gdscript
agent.init(actor)  # BlaziumGoapAgent — required or planning never starts
var db := SQLite.new()
if not db.load_from("user://rpg.sqlite"):
	push_error(db.get_last_error_message())
	return
var q: SQLiteQuery = db.create_query("SELECT quest FROM saves WHERE id = ?")
var rows := q.execute([slot])
```

## Pitfalls

- **Invented a Unity ScriptableObject stack** → resources + csv.
- **Rewrote GOAP as a behavior tree** → `blazium-goap`.
- **Hardcoded English strings** → localization.

## Related skills

- `blazium-resources`, `blazium-localization`, `blazium-ui`, `blazium-goap`,
  `blazium-sqlite`
