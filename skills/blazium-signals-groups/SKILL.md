---
name: blazium-signals-groups
description: >
  Decouples Blazium nodes with typed signals, Callables, and groups on
  4.3.2 / 0.6.x. Use when connecting signals, call_group, or designing event
  flow. Prefer JustAMCP connect_signal / node_find_in_group.
---

# Blazium signals and groups

Decouple nodes without hard parent paths. Baseline: **Blazium 0.6.x**.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding custom signals, connecting Callables, or `add_to_group` /
  `call_group`.

**When not to use:** scene structure → `blazium-nodes-scenes`. Signal *syntax*
only inside a script → `blazium-gdscript`.

## Workflow

1. **Inspect.** Existing signals via `docs_get_class` / scene connections.
2. **Choose.** Signal for events; groups for bulk calls; avoid polling.
3. **Implement.** JustAMCP `connect_signal` / `node_connect_signal`.
4. **Verify.** Autowork `watch_signal` + `assert_signal_emitted`.
5. **Handoff.** Connection list.

## Patterns

```gdscript
signal died

func _ready() -> void:
	died.connect(_on_died)
	add_to_group("enemies")

func notify_all() -> void:
	get_tree().call_group("enemies", "take_damage", 1)
```

4.x: `signal.emit(...)` and `signal.connect(callable)` — not string connects.

## Pitfalls

- **Connected before the node is in tree** → connect in `_ready()`.
- **Group name typos** → `node_find_in_group` to confirm.
- **Godot 3 `connect("x", self, "y")`** → Callable form.

## Resources

- JustAMCP: `connect_signal`, `node_find_in_group`

## Related skills

- `blazium-gdscript` — declare/emit syntax
- `blazium-nodes-scenes` — who owns the nodes
- `blazium-autowork` — signal assertions
