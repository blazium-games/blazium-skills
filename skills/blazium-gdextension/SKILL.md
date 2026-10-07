---
name: blazium-gdextension
description: >
  Wraps a hot path or a C library with godot-cpp. Use only after a profile
  shows GDScript or C# is too slow, or a C library must be wrapped. Not an
  engine rebuild.
when-to-use: >
  GDExtension, godot-cpp, native plugin, C library wrapper, profile says
  GDScript is too slow
metadata:
  author: blazium-games
  short-description: godot-cpp extension after a profile, not an engine rebuild
---

# Blazium GDExtension

Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Use godot-cpp against the installed 4.8 editor. Do not rebuild the engine.

## When to use

- Use after `blazium-performance` shows a GDScript or C# hot path that a native function would fix.
- Use when a C library must be called from the game.

**When not to use:** the script has not been profiled. Gameplay that fits GDScript or C# → those skills. An engine fork → stop.

## Workflow

1. **Inspect.** Profile numbers from `blazium-performance`, or the C headers that must be wrapped.
2. **Choose.** One function. Keep the rest in GDScript or C#.
3. **Implement.** A godot-cpp class, a `.gdextension` file, and a thin GDScript caller.
4. **Verify.** The same Autowork that showed the cost still passes, and the native call is the one that ran.
5. **Handoff.** Library path, class name, and the profile before/after.

## Patterns

`.gdextension` entry points at the 4.8 binary. The GDScript side calls one method. Do not move the whole scene tree into C++.

## Output contract

- Why GDScript or C# was not enough (profile or C API)
- Extension path and class
- Autowork or call evidence

## Pitfalls

- **Rebuilt Blazium** → godot-cpp only.
- **Moved gameplay into C++ before a profile** → stay in `blazium-gdscript` or `blazium-csharp`.
- **Invented a second MCP server for the extension** → call it from the game script.

## Related skills

- `blazium-performance`, `blazium-gdscript`, `blazium-csharp`
