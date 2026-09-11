---
name: blazium-input
description: >
  Configures Blazium 0.6.x InputMap actions, remapping, deadzones, and
  multi-device bindings on Godot 4.3.2. Use when adding jump/move_* actions,
  rebinding, gamepad axes, or JustAMCP input_tools (simulate_action,
  simulate_key, input_record). Not movement math and not Autowork
  AutoworkInputSender setup.
when-to-use: >
  InputMap, rebind, remap controls, simulate_action, gamepad axis, deadzone,
  ui_accept, jump action, multi-device input
metadata:
  author: blazium-games
  short-description: InputMap actions, rebinds, and JustAMCP input_tools
---

# Blazium input

InputMap is first-class. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
Inspect `config_version` / `features` in `project.blazium` (or
`project.godot`). Keep 4.3.2-safe `InputEvent*` types unless the user asks
to migrate.

JustAMCP: `simulate_key`, `simulate_mouse_click`, `simulate_action`,
`simulate_sequence`, `input_record`, `input_replay`. Resource:
`blazium://input_map`.

## When to use

- Use when defining actions, deadzones, or multi-device bindings.
- Use when the editor must simulate a named action in play mode.

**When not to use:** movement math → `blazium-2d-movement`. Autowork
`AutoworkInputSender` → instantiate in tests (`blazium-autowork`). Focus
neighbors / Theme → `blazium-ui`.

## Grok host

Read this file only. Spawn `gameplay-programmer` for action names on a
mover and `qa-tester` for Autowork InputSender. Child prompts must include
the action list and whether MCP `:6506` is connected. Do not dump the
catalog. Evidence is `simulate_action` or Autowork — not a screenshot of
the Input Map dock.

## Workflow

1. **Inspect.** `blazium://input_map` or ProjectSettings Input Map.
2. **Add actions** with keyboard/gamepad events (4.3.2 InputEvent types).
3. **Read** with `Input.is_action_pressed` / `get_axis` / `get_vector`.
4. **Verify.** MCP `simulate_action` in play mode or Autowork InputSender.
5. **Handoff.** Action names + devices bound.

## Patterns

Name gameplay actions (`jump`, `move_left`) — do not hardcode `KEY_SPACE` in
systems that should be rebindable.

```gdscript
var axis := Input.get_axis("move_left", "move_right")
```

JustAMCP play-mode: `simulate_action` with the same action string the
script reads. Editor MCP runtime tools need play.

## Output contract

- Action names added or rebound
- Devices (keyboard / gamepad) per action
- Surface used (`blazium://input_map`, `simulate_action`, or Autowork)
- Evidence (command + result, or `INCONCLUSIVE`)

## Pitfalls

- **Polled scancodes in gameplay** → use actions.
- **Copied Unity Input System C#** → InputMap + InputEvent*.
- **Simulated input without play mode** → editor MCP runtime tools need play.
- **Renamed an action the mover still reads** → update `blazium-2d-movement`.

## Resources

- JustAMCP: `input_tools`, `blazium://input_map`

## Related skills

- `blazium-2d-movement` — consumers
- `blazium-ui` — focus / ui_accept
- `blazium-autowork` — InputSender
- `blazium-accessibility` — remap pass
