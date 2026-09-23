---
name: blazium-genre-idle
pack: growth
---

# blazium-genre-idle

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Genre on-ramp so agents compose engine/module pack skills instead of inventing an idle framework or overflowing `int`/`float`.

## What

Compose pinned Blazium skills: clicker (BigNum), save-systems, csv/resources, ui, game-feel, autowork.

**Non-goals:** Do not fork a studio-clone skill pack. Do not own BigNum ops (`blazium-clicker`).

## How

1. Compose the pinned Blazium skills (4.8.x APIs) one pin per turn.
2. Order: BigNum → `user://` saves → balance tables → HUD → juice → Autowork.
3. Verify with Autowork round-trip + save load.

## Reasoning

Compositional. Exists so the router can load an idle game without treating `blazium-clicker` as a genre kit.

## Sources

- Pinned skills: clicker, save-systems, csv, resources, ui, game-feel, autowork

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-clicker` — pin
- `blazium-save-systems` — pin
- `blazium-csv` — pin
- `blazium-ui` — pin
- `blazium-game-feel` — pin
