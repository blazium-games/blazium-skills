---
name: blazium-shaders
description: >
  Writes Godot Shading Language (.gdshader) canvas_item and spatial shaders on
  Blazium 0.8.x. Use when authoring or assigning shaders. Prefer JustAMCP
  shader_tools.
---

# Blazium shaders

Text `.gdshader` only. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

JustAMCP: `create_shader`, `edit_shader`, `assign_shader_material`,
`set_shader_param`. Prompt: `blazium_shader_expert`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep `blazium_4.8`-safe APIs unless the user asks to migrate.

## When to use

- Use when writing canvas_item or spatial shaders, uniforms, TIME/UV animation.

**When not to use:** Environment glow/tonemap → `blazium-environment`.

## Workflow

1. **Inspect.** Renderer (Forward+ / compatibility) in project features.
2. **Author.** `shader_type canvas_item;` or `spatial;`.
3. **Assign.** ShaderMaterial via `assign_shader_material`; set uniforms with
   `set_shader_param`.
4. **Verify.** Editor log has no shader compile errors. Autowork
   `assert_true` that `assign_shader_material` stuck (material still set)
   and that `set_shader_param` matches a real `uniform`. Not a screenshot
   alone.
5. **Handoff.** Shader path + uniform names.

## Patterns

```glsl
shader_type canvas_item;
uniform vec4 tint : source_color = vec4(1.0);
void fragment() {
	COLOR = texture(TEXTURE, UV) * tint;
}
```

JustAMCP: `create_shader` / `edit_shader`, then `assign_shader_material` and
`set_shader_param` for `tint`.

### Author checklist

1. `shader_type` is `canvas_item` or `spatial`.
2. Uniforms use hints (`source_color` for colors).
3. `fragment()` or `vertex()` only.
4. `ShaderMaterial` is assigned (`assign_shader_material`).
5. `set_shader_param` names match the `uniform` identifiers.
6. The editor log has no shader compile error.

## Pitfalls

- **Wrote HLSL** → Godot SL only (`.gdshader`).
- **Wrong shader_type** → `canvas_item` vs `spatial`.
- **Copied built-ins that are not on `blazium_4.8`** → check 4.8.x docs via `docs_search`.
- **Uniform name mismatch in `set_shader_param`** → silent no-op. Match the
  shader `uniform` identifier exactly.

## Resources

- JustAMCP: `shader_tools`

## Related skills

- `blazium-environment` — post-fx
- `blazium-3d` — materials on MeshInstance
- `blazium-autowork` — material asserts
