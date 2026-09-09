---
name: blazium-luau
description: >
  Writes first-class Blazium Luau (.luau): scripts, LSP, JustAMCP
  register.luau, sandboxed remote eval. Use when editing Luau in a Blazium
  project. AutoworkTest binds assert_* on newer engines; Hub release CI may
  still use error()/must().
---

# Blazium Luau

Luau is a Blazium language Godot skills never mention. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**. Module: `blazium/modules/luau_module/` (18 classes).

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate. This is not Roblox Luau.

## When to use

- Use when writing `.luau` gameplay or `res://mcp/register.luau`.
- Use when choosing Luau vs GDScript for a new script.

**When not to use:** `.gd` → `blazium-gdscript`. Inventing Autowork assertion
names → use locked helpers in `blazium-autowork`.

## Workflow

1. **Inspect.** Confirm Luau module present (`LuauScript` / `LuauScriptLanguage`).
2. **Choose.** Table export with `extends = "Node"` (or the target class).
3. **Implement.** Same ClassDB API as GDScript (`JustAMCPRuntime.register_tool`,
   nodes, signals). Prefer editor LSP/formatter.
4. **Verify.** Load the script on a node; AutoworkTest `assert_*` on newer
   engines, or `error()`/`must()` for Hub release-editor CI.
5. **Handoff.** Paths + whether remote eval was used.

## Patterns

### Script shape

```luau
local M = { extends = "Node" }

function M:_ready()
	-- children exist here
end

return M
```

### MCP + remote eval

- Game MCP: copy `blazium-game-mcp/assets/register.luau`.
- `blazium-cli remote eval-lua` is sandboxed vs GDScript eval — still
  trusted-dev only (`blazium-cli-remote`).

### Autowork

`extends = "AutoworkTest"` works for discovery. Newer engines bind `assert_*`,
`wait_*`, `pass_test`, `fail_test`, `pending`, `print_log`, `p`. Do not invent
names. Doubles are GDScript-only. Hub release CI may still use `error()` /
`must()`. See Hub `tests/luau/test_001_hub_logic.luau`.

## Pitfalls

- **Invented `assert_foo` in Luau** → only locked helper names. Hub release CI
  may still need `error()` / `must()`.
- **Assumed Roblox `game:GetService`** → wrong VM.
- **Prefixed tools `blazium_`** → reserved on game MCP.

## Resources

- Tests: https://github.com/blazium-games/luau_module_tests

- Fixtures in tests: `require()`, table DSL, `gdclass()`
- `blazium/modules/luau_module/`
- `blazium-game-mcp/assets/register.luau`

## Related skills

- `blazium-gdscript` — default language
- `blazium-game-mcp` — register.luau
- `blazium-autowork` — AutoworkTest helpers
- `blazium-cli-remote` — eval-lua
