---
name: blazium-luau
pack: engine
---

# blazium-luau

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Luau is first-class in Blazium; Godot skills never mention it.

## What

`.luau` scripts, LSP, formatter, MCP `register.luau`, sandboxed remote eval.

**Non-goals:** Do not invent Autowork assertion names. Hub release-editor CI may still use `error()` / `must()`.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/luau_module/ (18 classes)`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/luau_module/ (18 classes)

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — adjacent
- `blazium-game-mcp` — adjacent
- `blazium-autowork` — adjacent
