---
name: blazium-genre-fps-shooter
description: >
  Composes an FPS/shooter from pinned Blazium skills (3D, input, physics,
  navigation, multiplayer-core). Use for first-person or 3D gunplay. Design
---

# Blazium genre: FPS / shooter

Thin adapter — not a shooter framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when building first-person or 3D hitscan/projectile gunplay.

**When not to use:** 2D platformer → `blazium-genre-platformer`. Dedicated
server ops → `blazium-enet-server` after `blazium-multiplayer-core`.

## Workflow

1. **Inspect.** Camera / InputMap / existing peers.
2. **Choose.** Pins below for 4.3.2 APIs.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on look/fire — not screenshots.
5. **Handoff.** Authority → multiplayer-core. Steam ticket → `blazium-steam`.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-3d` | Camera3D / meshes |
| `blazium-input` | look / fire actions |
| `blazium-physics` | hitscan / bodies |
| `blazium-navigation` | bot paths |
| `blazium-multiplayer-core` | `@rpc` / ENet peer |

Look via InputMap actions into a current `Camera3D`:

```gdscript
extends CharacterBody3D
@onready var cam: Camera3D = $Camera3D

func _physics_process(delta: float) -> void:
	var look := Input.get_vector("look_left", "look_right", "look_up", "look_down")
	rotate_y(-look.x * delta)
	cam.rotate_x(-look.y * delta)
	cam.rotation.x = clampf(cam.rotation.x, -1.2, 1.2)
```

## Pitfalls

- **Godot 4.7 character APIs** → 4.3.2 CharacterBody3D.
- **Invented a netcode stack** → multiplayer-core first.
- **Invented a shooter framework** → compose the pinned skills.

## Related skills

- `blazium-3d`, `blazium-input`, `blazium-physics`, `blazium-navigation`,
  `blazium-multiplayer-core`
