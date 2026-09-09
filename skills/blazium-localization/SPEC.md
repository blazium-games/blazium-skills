---
name: blazium-localization
pack: engine
---

# blazium-localization

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

CSV + TranslationServer + `tr()` is the Blazium locale path.

## What

TranslationServer, CSV imports. Pair with `blazium-csv` for large tables.

**Non-goals:** Do not invent a second string table API. Use `tr()`.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `core TranslationServer + dotcsv when tables are large`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: core TranslationServer + dotcsv when tables are large

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-csv` — adjacent
- `blazium-ui` — adjacent
