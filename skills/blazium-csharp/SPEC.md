---
name: blazium-csharp
pack: engine
---

# blazium-csharp

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

C# projects still exist; MCP coverage is thinner than GDScript.

## What

Partial classes, [Export]/[Signal], GDScript interop. AutoworkTest + `test_*` when `MODULE_MONO_ENABLED` (default `.gd` suffix also matches `.cs`).

**Non-goals:** Do not invent a C# Autowork assert DSL. Do not document a C# `BuildX.cs` / `PackAndSave` scene generator as the Blazium path.

Silent-failure C# traps: `SetScript()` disposes the typed wrapper — attach last and re-fetch. Guessed C# enum names are often wrong; verify 4.3.2 assemblies.

## How

1. Inspect project version (4.3.2 / 0.6.x). Reject Godot 4.7-only APIs.
2. Prefer JustAMCP tools when the editor MCP is connected.
3. Implement the smallest 4.3.2-safe pattern.
4. Verify with Autowork or play-mode MCP, not screenshots alone.

Engine / module path: `blazium/modules/mono/`.

## Reasoning

Godot-parity skill, Blazium-pinned, with JustAMCP handoff. Distinct so the router can load one engine surface at a time.

## Sources

- Blazium: blazium/modules/mono/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-gdscript` — adjacent
- `blazium-autowork` — adjacent
