---
name: blazium-input
pack: engine
---

# blazium-input

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

InputMap and remapping are ProjectSettings. Agents must not hardcode keys.

## What

InputMap, remapping, multi-device. MCP simulate_key/mouse/action + record/replay.

**Non-goals:** Do not own CharacterBody movement math.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP input_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP input_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-2d-movement` — adjacent
- `blazium-autowork` — adjacent
