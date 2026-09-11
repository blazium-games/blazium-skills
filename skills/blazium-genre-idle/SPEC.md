---
name: blazium-genre-idle
pack: growth
---

# blazium-genre-idle

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Genre on-ramp so agents compose engine/module pack skills instead of inventing an idle framework or overflowing `int`/`float`.

## What

Compose pinned Blazium skills: clicker (BigNum), save-systems, csv/resources, ui, game-feel, autowork.

**Non-goals:** Do not fork a studio-clone skill pack. Do not own BigNum ops (`blazium-clicker`).

## How

1. Compose the pinned Blazium skills (4.3.2 APIs) one pin per turn.
2. Order: BigNum → `user://` saves → balance tables → HUD → juice → Autowork.
3. Verify with Autowork round-trip + save load.

## Reasoning

Compositional. Exists so the router can load an idle game without treating `blazium-clicker` as a genre kit.

## Sources

- Pinned skills: clicker, save-systems, csv, resources, ui, game-feel, autowork

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-clicker` — pin
- `blazium-save-systems` — pin
- `blazium-csv` — pin
- `blazium-ui` — pin
- `blazium-game-feel` — pin
