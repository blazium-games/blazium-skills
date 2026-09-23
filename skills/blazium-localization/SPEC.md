---
name: blazium-localization
pack: engine
---

# blazium-localization

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

CSV + TranslationServer + `tr()` is the Blazium locale path.

## What

TranslationServer, CSV imports. Pair with `blazium-csv` for large tables.

**Non-goals:** Do not invent a second string table API. Use `tr()`.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `core TranslationServer + dotcsv when tables are large`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: core TranslationServer + dotcsv when tables are large

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-csv` — adjacent
- `blazium-ui` — adjacent
