---
name: blazium-gdscript
pack: engine
---

# blazium-gdscript

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Write typed GDScript 2.0 as it exists on Godot 4.8.x / Blazium 0.8.x.

## What

Lifecycle, @export/@onready, signals, await. No syntax outside `blazium_4.8`.

**Non-goals:** Do not teach Luau or C#. Use APIs that exist on `blazium_4.8`.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/gdscript/`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/gdscript/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-luau` — adjacent
- `blazium-csharp` — adjacent
- `blazium-gdscript-templates` — adjacent
- `blazium-signals-groups` — adjacent
