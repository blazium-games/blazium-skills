---
name: blazium-genre-fps-shooter
description: >
  Composes an FPS or 3D shooter from pinned Blazium 0.6.x skills (3D, input,
  physics, navigation, multiplayer-core). Use when the request is first-person,
  hitscan, projectile gunplay, or CharacterBody3D look/fire. Not a 2D
  platformer and not a dedicated-server ops kit.
when-to-use: >
  FPS, first-person, shooter, hitscan, projectile, CharacterBody3D look,
  Camera3D gunplay
metadata:
  author: blazium-games
  short-description: Compose an FPS from 3D, input, physics, net pins
---

# Blazium genre: FPS / shooter

Thin adapter — not a shooter framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when building first-person or 3D hitscan/projectile gunplay.
- Use when look/fire actions, a current `Camera3D`, and a physics query
  are the next change.

**When not to use:** 2D platformer → `blazium-genre-platformer`. Dedicated
server ops → `blazium-enet-server` after `blazium-multiplayer-core`. Steam
ticket / achievements → `blazium-steam` after the local shot works.

## Grok host

Read this adapter, then **one** pin. Spawn `gameplay-programmer` for
`CharacterBody3D` look/fire and `qa-tester` for the Autowork shot. Child
prompts must include scene path, look/fire action names, and whether the
body is an authority peer. Do not dump the catalog.

Evidence is Autowork on look/fire — not a screenshot of the crosshair.

## Workflow

1. **Inspect.** Camera / InputMap (`look_*`, `fire`) / existing peers.
2. **Choose.** Pins below. Order: input → 3D camera/body → physics query →
   navigation bots → multiplayer-core authority.
3. **Implement.** Router + this adapter + **one** pin at a time.
4. **Verify.** Autowork on look/fire — not screenshots.
5. **Handoff.** Authority → `blazium-multiplayer-core`. Steam ticket →
   `blazium-steam`. Feel → `blazium-game-feel` after the shot lands.

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

Hitscan stays in `blazium-physics` (`PhysicsRayQueryParameters3D` from the
camera). Do not invent a custom netcode stack.

## Output contract

- Scene path and body/camera nodes
- InputMap actions (`look_*`, `fire`)
- Pins loaded
- Autowork test name and pass/fail for look/fire
- Whether `@rpc` authority is wired

## Pitfalls

- **Godot 4.7 character APIs** → 4.3.2 `CharacterBody3D`.
- **Invented a netcode stack** → `blazium-multiplayer-core` first.
- **Invented a shooter framework** → compose the pinned skills.
- **Tuned recoil before the ray hits** → shot first, `blazium-game-feel` second.

## Related skills

- `blazium-3d`, `blazium-input`, `blazium-physics`, `blazium-navigation`,
  `blazium-multiplayer-core`, `blazium-steam`, `blazium-autowork`
