---
name: blazium-dialogue
pack: growth
---

# blazium-dialogue

Data-driven talk graph. Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
Do not apply Godot 4.7-only APIs.

## Why

Agents either hardcode English or pull in a VN framework. This skill keeps
a localizable graph.

## What

`.tres` / JSON nodes (line, choices, flags). `tr()` on every string.
Optional Ink/Yarn via addons only.

**Non-goals:** Full VN scene flow, locale pipeline ownership, save I/O.

## How

1. Inspect existing graph and locale keys.
2. Implement a walker over data. Verify choice → next id with Autowork.

## Reasoning

Distinct from `blazium-genre-visual-novel` (composition) and
`blazium-localization` (tables).

## Sources

- Blazium: `Resource`, `tr()` (4.3.2)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-localization` — adjacent
- `blazium-genre-visual-novel` — adjacent
- `blazium-save-systems` — adjacent
