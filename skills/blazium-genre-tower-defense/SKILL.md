---
name: blazium-genre-tower-defense
description: >
  Composes a path-follow wave tower defense from pinned Blazium 0.6.x skills
  (navigation, tilemap, resources, UI). Use when the request is TD, waves,
  creep path, tower placement, or spend-to-build. Not an RTS sandbox and not
  an idle numbers kit.
when-to-use: >
  tower defense, TD, wave, creep path, tower placement, NavigationAgent2D
  lane
metadata:
  author: blazium-games
  short-description: Compose a TD from navigation, tilemap, resources, UI pins
---

# Blazium genre: tower defense

Thin adapter — not a TD framework. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when enemies follow a path and towers spend resources to stop waves.
- Use when a baked nav path plus tower `.tres` defs are the next change.

**When not to use:** RTS without lanes → compose `blazium-navigation` +
`blazium-resources` directly. Idle numbers → `blazium-clicker`. Puzzle grid
with no waves → `blazium-genre-puzzle`.

## Grok host

Read this adapter, then **one** pin. Spawn `gameplay-programmer` for the
creep agent and `systems-designer` for tower defs. Child prompts must
include the lane scene, tower Resource path, and how a wave spend is
asserted. Do not dump the catalog.

Evidence is Autowork on path reach + spend — not a screenshot of the map.

## Workflow

1. **Inspect.** Tile path / NavigationAgent / tower defs.
2. **Choose.** Pins below. Order: tilemap lanes → navigation bake → tower
   resources → UI shop → Autowork path/spend.
3. **Implement.** Router + this adapter + **one** pin at a time.
4. **Verify.** Autowork on path reach + spend — not screenshots.
5. **Handoff.** UI shop → `blazium-ui`. Saves → `blazium-sqlite`. Feel →
   `blazium-game-feel` after a creep reaches the exit test.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-navigation` | agent paths |
| `blazium-tilemap` | lanes / placement grid |
| `blazium-resources` | tower / enemy defs |
| `blazium-ui` | build / wave HUD |

Drive each creep with a baked `NavigationAgent2D` (bake after tile edits):

```gdscript
extends CharacterBody2D
@onready var agent: NavigationAgent2D = $NavigationAgent2D

func _physics_process(_delta: float) -> void:
	agent.target_position = exit.global_position
	var next := agent.get_next_path_position()
	velocity = global_position.direction_to(next) * speed
	move_and_slide()
```

Bake the nav map after lane tiles change. Do not lerp creeps down a
hardcoded point list when a NavigationAgent exists.

## Output contract

- Lane / map scene path
- Tower / enemy Resource paths
- Nav bake note (when last baked)
- Autowork path-reach and spend assertions

## Pitfalls

- **Moved enemies with lerp instead of nav** → `blazium-navigation`.
- **Hardcoded tower tables in scripts** → resources / csv.
- **Rewrote a studio TD kit** → compose pins.
- **Skipped bake after tile edits** → agents walk through walls.

## Related skills

- `blazium-navigation`, `blazium-tilemap`, `blazium-resources`, `blazium-ui`,
  `blazium-sqlite`, `blazium-autowork`
