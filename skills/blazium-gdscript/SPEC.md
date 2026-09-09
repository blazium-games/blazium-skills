---
name: blazium-gdscript
pack: engine
---

# blazium-gdscript

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Write typed GDScript 2.0 as it exists on Godot 4.3.2 / Blazium 0.6.x.

## What

Lifecycle, @export/@onready, signals, await. No 4.7-only syntax.

**Non-goals:** Do not teach Luau or C#. Do not apply Godot 4.7-only APIs.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/gdscript/`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/gdscript/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-luau` — adjacent
- `blazium-csharp` — adjacent
- `blazium-gdscript-templates` — adjacent
- `blazium-signals-groups` — adjacent
