---
name: blazium-gdscript
description: >
  Writes typed GDScript on Blazium 0.6.x / Godot 4.3.2 (static types,
  signals, await, class_name). Use when authoring or fixing .gd files.
  Not C#, not Luau, not a scene layout skill, and not Godot 4.7-only syntax.
when-to-use: >
  GDScript, .gd, typed gdscript, class_name, signal, await, @onready,
  @export, Godot 4.3.2 script
metadata:
  author: blazium-games
  short-description: Typed GDScript on Blazium 0.6.x / Godot 4.3.2
---

# Blazium GDScript

Typed `.gd` on **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot
4.7-only syntax. Inspect `config_version` / `features` in `project.blazium`
(or `project.godot`) before treating the tree as stock Godot.

## When to use

- Use when writing or repairing a `.gd` file.
- Use when the user asks for typed GDScript, signals, `await`, or `class_name`.

**When not to use:** C# → `blazium-csharp`. Luau → `blazium-luau`.
Scene tree / packed scenes → `blazium-nodes-scenes`. Tests →
`blazium-autowork`. Project settings → `blazium-project-config`.

## Grok host

On Grok, keep context small: read this file plus the one `.gd` being edited.
Spawn `blazium-gdscript-specialist` for the script and `qa-tester` for
Autowork. Child prompts must include the script path and the 4.3.2 pin.

Edit with Grok file tools or JustAMCP `script_tools` when `:6506` is
connected. Evidence is Autowork or `--headless` parse — not a screenshot
and not Grok `code_execution` pretending to be the GDScript VM.

## Workflow

1. **Inspect.** Existing style (`class_name`, types, signal names).
2. **Choose.** Typed GDScript. State assumptions.
3. **Implement.** Match project patterns. No invented ClassDB APIs.
4. **Verify.** Autowork or `blazium --headless --check-only` if available.
5. **Handoff.** Script path, types added, next skill.

## Patterns

Prefer explicit types, `class_name` for reusable types, `@export` for
designer knobs, `@onready` for node refs after the tree is ready.
Connect signals in code when the hook is gameplay-critical.

```gdscript
class_name CoinPickup
extends Area2D

signal collected(amount: int)

@export var amount: int = 1

func _ready() -> void:
	body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		collected.emit(amount)
		queue_free()
```

## Output contract

- Script path(s)
- Types / signals / exports added
- Autowork or parse evidence (or `INCONCLUSIVE`)
- Next skill

## Pitfalls

- **Used Godot 4.7-only syntax** → stay on 4.3.2.
- **Untyped public API** → annotate params and returns.
- **Edited C# / Luau here** → wrong skill.
- **Invented a ClassDB method** → check docs.blazium.app.

## Related skills

- `blazium-autowork` — test the script
- `blazium-nodes-scenes` — scene tree
- `blazium-csharp` / `blazium-luau` — other languages
- `blazium-gdscript-templates` — starter snippets
