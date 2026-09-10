---
name: blazium-genre-card-game
description: >
  Composes a deck/hand/table card game from pinned Blazium 0.6.x skills
  (resources, UI, CSV, localization). Use when the request is deckbuilder,
  hand of cards, play/resolve, collectible table, or card combat kit. Not an
  RPG quest framework and not a visual-novel director.
when-to-use: >
  card game, deckbuilder, hand, play card, resolve stack, collectible table,
  CardData resource
metadata:
  author: blazium-games
  short-description: Compose a card game from resources, UI, CSV, locale pins
---

# Blazium genre: card game

Thin adapter — not a card engine. Baseline: **Blazium 0.6.x (Godot 4.3.2
fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe APIs unless
the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when the core loop is draw / play / resolve cards on a hand or table.
- Use when card text, costs, or balance live in `.tres` or CSV — not a
  hardcoded script table.

**When not to use:** full RPG quests / party / inventory → `blazium-genre-rpg`.
Talk graph only → `blazium-dialogue`. Huge tables without UI → `blazium-csv`
only. Idle currency overflow → `blazium-clicker` after the resolve loop.

## Grok host

Read this adapter, then **one** pin `SKILL.md`. Spawn `systems-designer` for
`CardData` / CSV columns and `gameplay-programmer` for draw/play. Child
prompts must include the card Resource path, who owns shuffle, and the
`tr()` key prefix. Do not dump the catalog.

Evidence is Autowork on shuffle/play resolve — not a screenshot of the hand.

## Workflow

1. **Inspect.** Card defs / locales / existing Control tree / CSV path.
2. **Choose.** Pins below. Order: resources defs → CSV balance → localization
   keys → UI hand/board → Autowork resolve.
3. **Implement.** Router + this adapter + **one** pin at a time.
4. **Verify.** Autowork shuffle/play resolve — not screenshots.
5. **Handoff.** Economy overflow → `blazium-clicker`. Save decks →
   `blazium-sqlite`. Juice → `blazium-game-feel` after resolve works.

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
@export var name_key: String

func draw(deck: Array[CardData]) -> CardData:
	deck.shuffle()
	return deck.pop_back()
```

Show names with `tr(card.name_key)` on hand Controls (`blazium-ui` +
localization). Do not parse CSV with `FileAccess` + `split(",")`.

## Output contract

- Card Resource / CSV paths
- Locale key prefix
- Who shuffles (deck owner script)
- Autowork test name and pass/fail for play/resolve

## Pitfalls

- **Invented FileAccess CSV** → `blazium-csv`.
- **Hardcoded card names** → localization `tr()` keys.
- **Copied a Unity card framework** → compose pins.
- **Mutated the shared `.tres` in the deck** → duplicate before play.

## Related skills

- `blazium-resources`, `blazium-ui`, `blazium-csv`, `blazium-localization`,
  `blazium-sqlite`, `blazium-clicker`
