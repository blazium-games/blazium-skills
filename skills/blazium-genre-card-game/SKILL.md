---
name: blazium-genre-card-game
description: >
  Composes a card game from pinned Blazium skills (resources, UI, CSV,
  localization). Use for deck/hand/table games
---

# Blazium genre: card game

Thin adapter — not a card engine. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack.

## When to use

- Use when the core loop is draw / play / resolve cards.

**When not to use:** full RPG quests → `blazium-genre-rpg`. Huge tables
without UI → `blazium-csv` only.

## Workflow

1. **Inspect.** Card defs / locales / existing Control tree.
2. **Choose.** Pins below for data + UI.
3. **Implement.** Router + this adapter + one pin.
4. **Verify.** Autowork on shuffle/play resolve — not screenshots.
5. **Handoff.** Economy overflow → `blazium-clicker`. Save → sqlite.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-resources` | card `.tres` |
| `blazium-ui` | hand / board Controls |
| `blazium-csv` | balance tables |
| `blazium-localization` | card text |

Typed card `Resource` plus a runtime deck (duplicate `.tres` before mutating):

```gdscript
extends Resource
class_name CardData
@export var id: StringName
@export var cost: int

func draw(deck: Array[CardData]) -> CardData:
	deck.shuffle()
	return deck.pop_back()
```

Show names with `tr()` on hand Controls (`blazium-ui` + localization).

## Pitfalls

- **Invented FileAccess CSV** → `blazium-csv`.
- **Hardcoded card names** → localization.
- **Copied a Unity card framework** → compose pins.

## Related skills

- `blazium-resources`, `blazium-ui`, `blazium-csv`, `blazium-localization`
