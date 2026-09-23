---
name: blazium-dialogue
pack: growth
---

# blazium-dialogue

Data-driven talk graph. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.
Use APIs that exist on `blazium_4.8`.

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

- Blazium: `Resource`, `tr()` (4.8.x)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-localization` — adjacent
- `blazium-genre-visual-novel` — adjacent
- `blazium-save-systems` — adjacent
