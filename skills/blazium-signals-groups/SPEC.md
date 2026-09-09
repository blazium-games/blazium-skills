---
name: blazium-signals-groups
pack: engine
---

# blazium-signals-groups

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Decoupled node communication is where agents create spaghetti.

## What

Custom signals, Callables, groups, call_group. MCP connect_signal.

**Non-goals:** Do not redesign the scene tree.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP connect_signal / node_find_in_group`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP connect_signal / node_find_in_group

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — adjacent
- `blazium-nodes-scenes` — adjacent
