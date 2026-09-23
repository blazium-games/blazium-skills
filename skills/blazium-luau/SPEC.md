---
name: blazium-luau
pack: engine
---

# blazium-luau

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Luau is first-class in Blazium; Godot skills never mention it.

## What

`.luau` scripts, LSP, formatter, MCP `register.luau`, sandboxed remote eval.

**Non-goals:** Do not invent Autowork assertion names. Hub release-editor CI may still use `error()` / `must()`.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/luau_module/ (18 classes)`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/luau_module/ (18 classes)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — adjacent
- `blazium-game-mcp` — adjacent
- `blazium-autowork` — adjacent
