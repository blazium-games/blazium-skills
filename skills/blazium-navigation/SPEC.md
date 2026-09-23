---
name: blazium-navigation
pack: engine
---

# blazium-navigation

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

NavigationRegion / Agent bake is a first-class 4.8.x path.

## What

NavigationRegion/Agent bake, layers, MCP spatial_tools (`spatial_bake_navigation`).

**Non-goals:** Do not rewrite Godot NavigationServer internals. Skip editor-only `navigation` module generator details.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `JustAMCP spatial_tools`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: JustAMCP spatial_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-physics` — adjacent
- `blazium-goap` — adjacent
