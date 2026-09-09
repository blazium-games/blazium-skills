---
name: blazium-genre-tower-defense
description: >
  Composes a tower defense from pinned Blazium skills (navigation, tilemap,
  resources, UI). Use for path-follow wave games
---

# Blazium genre: tower defense

Thin adapter — not a TD framework. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when enemies follow a path and towers spend resources to stop waves.

**When not to use:** RTS without lanes → compose `blazium-navigation` +
`blazium-resources` directly. Idle numbers → `blazium-clicker`.

## Workflow

1. **Inspect.** Tile path / NavigationAgent / tower defs.
2. **Choose.** Pins below.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on path reach + spend — not screenshots.
5. **Handoff.** UI shop → `blazium-ui`. Saves → `blazium-sqlite`.

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

## Pitfalls

- **Moved enemies with lerp instead of nav** → `blazium-navigation`.
- **Hardcoded tower tables in scripts** → resources / csv.
- **Rewrote a studio TD kit** → compose pins.

## Related skills

- `blazium-navigation`, `blazium-tilemap`, `blazium-resources`, `blazium-ui`
