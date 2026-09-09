---
name: blazium-environment
description: >
  Configures WorldEnvironment / Environment (glow, tonemap, SSAO, sky) on
  Prefer JustAMCP environment_create.
---

# Blazium environment

URP Volume analog — Godot `WorldEnvironment` + `Environment` resource.
No URP Renderer Features. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding sky, glow, tonemap, fog, or SSAO.

**When not to use:** custom `.gdshader` → `blazium-shaders`. Mesh/camera setup
→ `blazium-3d`.

## Workflow

1. **Inspect.** Existing WorldEnvironment and renderer (Forward+ / compatibility).
2. **Create/assign** Environment via MCP `environment_create` / `setup_environment`.
3. **Tune** glow/tonemap last (easy to blow out).
4. **Verify.** Autowork `assert_true(world.environment != null)` or play-mode
   tree: one WorldEnvironment with an assigned Environment. Not a screenshot alone.
5. **Handoff.** Environment path + renderer caveat.

## Patterns

One WorldEnvironment per scene (or per world). Compatibility renderer: skip
features that require Forward+ (SSAO and similar).

```gdscript
extends WorldEnvironment

func _ready() -> void:
	# Resource from environment_create / setup_environment
	environment = load("res://env/world.tres") as Environment
```

JustAMCP: `environment_create` then `setup_environment` (also on `scene3d_tools`).

## Pitfalls

- **Invented URP Volume profiles** → Environment resource on WorldEnvironment.
- **Glow + untonemapped HDR** → blown whites. Set tonemap before raising glow.
- **Copied Godot 4.7 Environment properties** → check 4.3.2 class docs.
- **Two WorldEnvironment nodes** → last processed wins. Keep one per world.
- **SSAO on Compatibility** → no effect. Drop SSAO or use Forward+.

## Resources

- JustAMCP: `environment_tools`, `scene3d_tools`

## Related skills

- `blazium-3d` — scene
- `blazium-shaders` — custom post
- `blazium-autowork` — environment asserts
