---
name: blazium-genre-idle
description: >
  Composes an idle or incremental clicker from pinned Blazium 0.6.x skills
  (BlaziumBigNum, user:// saves, juice, HUD, CSV balance). Use when the
  request is idle game, incremental, cookie clicker, prestige, or offline
  earnings. Load this adapter plus one pin at a time. Not BigNum-only and
  not a full idle framework.
when-to-use: >
  idle game, incremental, cookie clicker, prestige, offline earnings,
  generators, upgrade tree, BigNum HUD
metadata:
  author: blazium-games
  short-description: Compose an idle/clicker from BigNum, saves, juice, HUD, CSV
---

# Blazium genre: idle

Thin adapter — not an idle framework. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**. Inspect `config_version` / `features`; keep 4.3.2-safe
APIs unless the user asks to migrate.

Do not fork a studio-clone skill pack. Compose pins; implement one pin per
turn.

## When to use

- Use when building an idle / incremental / cookie-clicker loop.
- Use when the user says prestige, generators, offline earnings, or
  "make a clicker game" as a *game*, not just huge numbers.

**When not to use:** BigNum ops only → `blazium-clicker`. Platformer jump
→ `blazium-genre-platformer`. Economy tables without a loop →
`blazium-csv` / `blazium-resources`. Juice only → `blazium-game-feel`.

## Grok host

On Grok, keep context small: read this file, then **one** pin `SKILL.md`.
Spawn `systems-designer` or `economy-designer` for the loop and
`blazium-gdscript-specialist` for the HUD script. Child prompts must
include scene path, save path (`user://`), and the 4.3.2 pin. Do not dump
the catalog.

Prefer project files over memory. Evidence is Autowork (BigNum round-trip
+ save load), not a screenshot and not Grok `code_execution` math.

## Workflow

1. **Inspect.** `project.blazium` / `config_version`. Existing currency
   type, HUD labels, `user://` save.
2. **Choose.** Pins below — no custom framework. Order: BigNum → save
   slots → CSV/resources balance → HUD → juice → Autowork.
3. **Implement.** This adapter + **one** pin at a time (router + two max).
4. **Verify.** Autowork on `from_string` / `as_string` and save load —
   not screenshots.
5. **Handoff.** Pins used, scene path, save path. Steam page →
   `blazium-steam-publish`. Feel last.

## Patterns

| Pin | Owns |
|-----|------|
| `blazium-clicker` | `BlaziumBigNum` construct / ops / serialize |
| `blazium-save-systems` | versioned `user://` slots (`as_string()`) |
| `blazium-csv` | generator / upgrade tables |
| `blazium-resources` | `.tres` upgrade defs |
| `blazium-ui` | currency HUD / shop |
| `blazium-game-feel` | click punch / number pop |
| `blazium-autowork` | tests |

### Scene sketch (4.3.2)

`Control` HUD (currency `Label`, click `Button`, shop list) + one Autoload
economy node that owns `BlaziumBigNum` fields. Persist with
`blazium-save-systems` using `as_string()`. Balance rows live in CSV or
`.tres` — not hardcoded `float`.

```gdscript
extends AutoworkTest
func test_gold_round_trip() -> void:
	var g := BlaziumBigNum.from_string("1e20")
	g = g.add(BlaziumBigNum.from_string("50"))
	assert_true(g.is_equal_to(BlaziumBigNum.from_string(g.as_string())))
```

## Output contract

- Scene path(s) touched
- Currency fields (`BlaziumBigNum` vs leftover `float`)
- Save path (`user://…`) and schema version
- Pins loaded
- Autowork test name and pass/fail

## Pitfalls

- **Rewrote the genre skill** → read it; implement with pins.
- **Used `int`/`float` for 1e40 cookies** → `blazium-clicker`.
- **Saved BigNum as float** → `as_string()` into the save slot.
- **Tuned juice before the counter increments** → numbers + save first.
- **Built a custom idle framework** → compose pins.

## Related skills

- `blazium-clicker`, `blazium-save-systems`, `blazium-csv`,
  `blazium-resources`, `blazium-ui`, `blazium-game-feel`,
  `blazium-autowork`
