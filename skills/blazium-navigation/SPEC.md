---
name: blazium-navigation
pack: engine
---

# blazium-navigation

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

NavigationRegion / Agent bake is a first-class 4.3.2 path.

## What

NavigationRegion/Agent bake, layers, MCP spatial_tools (`spatial_bake_navigation`).

**Non-goals:** Do not rewrite Godot NavigationServer internals. Skip editor-only `navigation` module generator details.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP spatial_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP spatial_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-physics` — adjacent
- `blazium-goap` — adjacent
