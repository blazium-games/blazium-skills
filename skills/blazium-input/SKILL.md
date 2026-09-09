---
name: blazium-input
description: >
  Configures Blazium InputMap (actions, remapping, multi-device) on 4.3.2.
  Use when adding input actions, rebinding, or simulating input via JustAMCP
  input_tools.
---

# Blazium input

InputMap is first-class. Baseline:
**Blazium 0.6.x**.

JustAMCP: `simulate_key`, `simulate_mouse_click`, `simulate_action`,
`simulate_sequence`, `input_record`, `input_replay`. Resource:
`blazium://input_map`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when defining actions, deadzones, or multi-device bindings.

**When not to use:** movement math → `blazium-2d-movement`. Autowork
`AutoworkInputSender` → instantiate in tests (`blazium-autowork`).

## Workflow

1. **Inspect.** `blazium://input_map` or ProjectSettings Input Map.
2. **Add actions** with keyboard/gamepad events (4.3.2 InputEvent types).
3. **Read** with `Input.is_action_pressed` / `get_axis` / `get_vector`.
4. **Verify.** MCP simulate_action or Autowork InputSender.

## Patterns

Name gameplay actions (`jump`, `move_left`) — do not hardcode `KEY_SPACE` in
systems that should be rebindable.

```gdscript
var axis := Input.get_axis("move_left", "move_right")
```

## Pitfalls

- **Polled scancodes in gameplay** → use actions.
- **Copied Unity Input System C#** → InputMap + InputEvent*.
- **Simulated input without play mode** → editor MCP runtime tools need play.

## Resources

- JustAMCP: `input_tools`, `blazium://input_map`

## Related skills

- `blazium-2d-movement` — consumers
- `blazium-ui` — focus / ui_accept
- `blazium-autowork` — InputSender
