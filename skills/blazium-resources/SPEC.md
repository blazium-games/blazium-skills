---
name: blazium-resources
pack: engine
---

# blazium-resources

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Resource is the ScriptableObject analog.

## What

Custom Resource, .tres/.res, ResourceLoader. Data-driven items/stats.

**Non-goals:** Do not own CSV tables (`blazium-csv`) or SQLite.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `core Resource + JustAMCP resource_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: core Resource + JustAMCP resource_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-csv` — adjacent
- `blazium-sqlite` — adjacent
- `blazium-gdscript` — adjacent
