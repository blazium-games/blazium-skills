---
name: blazium-csharp
pack: engine
---

# blazium-csharp

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

C# projects still exist; MCP coverage is thinner than GDScript.

## What

Partial classes, [Export]/[Signal], GDScript interop. AutoworkTest + `test_*` when `MODULE_MONO_ENABLED` (default `.gd` suffix also matches `.cs`).

**Non-goals:** Do not invent a C# Autowork assert DSL. Do not document a C# `BuildX.cs` / `PackAndSave` scene generator as the Blazium path.

Silent-failure C# traps: `SetScript()` disposes the typed wrapper — attach last and re-fetch. Guessed C# enum names are often wrong; verify 4.8.x assemblies.

## How

1. Inspect project version (4.8.x / 0.8.x). Use APIs that exist on `blazium_4.8`.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest `blazium_4.8`-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/mono/`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/mono/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — adjacent
- `blazium-autowork` — adjacent
