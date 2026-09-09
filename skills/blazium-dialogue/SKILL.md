---
name: blazium-dialogue
description: >
  Authors a data-driven dialogue graph on Blazium 0.6.x (.tres or JSON nodes
  with lines, choices, and flags). All strings go through tr(). Use for
  branching talk, not a full visual-novel scene flow. Do not require Ink or Yarn.
---

# Blazium dialogue

A graph of lines, choices, and flags — not a VN director. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**. Store the graph as a `Resource` `.tres`
or JSON under `res://`. Every player-facing string is `tr("key")`.

Ink / Yarn are **optional addons** only (`blazium-addons`). Do not require
them. Do not invent a runtime DSL.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding a talk graph: speaker, line key, choices, set/check flags.
- Use when RPG or adventure NPCs need branching lines without a VN loop.

**When not to use:** full VN composition (scenes, letterbox, CG) →
`blazium-genre-visual-novel`. Locale tables only → `blazium-localization`.
Persist flags across sessions → `blazium-save-systems` after the graph.

## Workflow

1. **Inspect.** Existing `.tres` / JSON, locale keys, UI textbox.
2. **Choose.** Resource graph vs JSON. Keep nodes as data (id, line, choices).
3. **Implement.** Walker: show `tr(line_key)`, apply choice → next id / flags.
   UI chrome → `blazium-ui`.
4. **Verify.** Autowork: pick a choice, `assert_eq` on the next node id and a
   flag. Not a screenshot of the textbox.
5. **Handoff.** Graph path + flag names. VN flow → genre skill.

## Patterns

```gdscript
# DialogueNode.gd — Resource, not a scene director
class_name DialogueNode
extends Resource

@export var id: String
@export var line_key: String
@export var choices: Array[Dictionary]  # { "text_key": String, "next": String, "set_flag": String }
```

```gdscript
func show_node(node: DialogueNode) -> void:
	label.text = tr(node.line_key)
	for choice in node.choices:
		var btn := Button.new()
		btn.text = tr(String(choice["text_key"]))
		btn.pressed.connect(func() -> void:
			if choice.get("set_flag", "") != "":
				flags[String(choice["set_flag"])] = true
			goto_id(String(choice["next"]))
		)
```

Keep speakers and portraits as Resource fields. Do not bake English into
the walker.

## Pitfalls

- **Hardcoded English in the walker** → `tr()` keys only.
- **Required Ink/Yarn** → optional addon; default is `.tres` / JSON.
- **Owned the whole VN loop here** → `blazium-genre-visual-novel`.
- **Saved flags as node paths** → save flag names via `blazium-save-systems`.

## Resources

- https://docs.blazium.app — `Resource`, `tr()`
- JustAMCP: `resource_tools`, `script_tools`

## Related skills

- `blazium-localization` — keys and locales
- `blazium-genre-visual-novel` — VN scene composition
- `blazium-ui` — textbox / choice buttons
- `blazium-resources` — `.tres` shape
- `blazium-addons` — optional Ink/Yarn
- `blazium-save-systems` — persist flags
