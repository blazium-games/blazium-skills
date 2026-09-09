---
name: blazium-csharp
description: >
  Writes Godot/Blazium C# gameplay (partial classes, Export/Signal, GDScript
  interop) on Blazium 0.6.x. Use when the project already uses .NET/C#.
  AutoworkTest discovery works when MODULE_MONO_ENABLED; no C# assert DSL.
---

# Blazium C#

C# on Blazium is the Godot .NET stack (`blazium/modules/mono/`). Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**. MCP coverage is **thinner** than GDScript
— prefer `script_tools` only when they accept the path; otherwise edit files
and verify in-editor.

When `MODULE_MONO_ENABLED`, Autowork discovers C# `AutoworkTest` subclasses
with `test_*` methods (default `.gd` suffix also matches `.cs`). Empty
`test_*` lists print a `--build-solutions` hint. Use existing ClassDB asserts
— do not invent a C# assert DSL.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when editing `.cs` gameplay in a Blazium/.NET project.

**When not to use:** new scripts on a GDScript project → `blazium-gdscript`.
Autowork authoring details → `blazium-autowork`.

## Workflow

1. **Inspect.** `.csproj` / Godot .NET features. Confirm 4.3-compatible bindings.
2. **Implement.** Partial classes, `[Export]`, `[Signal]`, `Callable` interop.
3. **Verify.** Editor build (`--build-solutions` if needed). C# `AutoworkTest`
   + `test_*` when mono is enabled.
4. **Handoff.** Note thinner JustAMCP support.

## Patterns

```csharp
using Godot;

public partial class Spinner : Node2D
{
    [Export] public float Speed { get; set; } = 90f;

    public override void _Process(double delta)
    {
        RotationDegrees += Speed * (float)delta;
    }
}
```

## Pitfalls

- **Empty C# Autowork suite** → build the C# solution; inherit AutoworkTest
  and name methods `test_*`.
- **Invented C# assert helpers** → use ClassDB asserts only.
- **Copied Godot 4.7 C# APIs** → pin 4.3.2 bindings.
- **Expected full `script_tools` parity** → GDScript-first MCP.
- **`SetScript()` after you keep the wrapper** → `SetScript()` disposes the C#
  wrapper. Attach scripts last; re-fetch the node if you still need the typed
  instance. Do not invent a C# `SceneTree` scene builder as the Blazium path
  — scenes stay `.tscn` + JustAMCP / editor (`blazium-nodes-scenes`).
- **Guessed C# enum names** → training data is GDScript-biased
  (`BGMode.Sky`, not a guessed `BGModeEnum.Sky`). Verify against 4.3.2
  assemblies, not memory.

## Resources

- `blazium/modules/mono/`

## Related skills

- `blazium-gdscript` — default
- `blazium-autowork` — AutoworkTest discovery and locked asserts
