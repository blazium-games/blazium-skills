---
name: blazium-xbox
description: >
  Guards Xbox GDK usage (GDK singleton, GDKResult). Not in the default
  editor — feature-detect a Windows GDK build first. Do not assume GDK is
  compiled in or enable it on non-Windows.
---

# Blazium Xbox (GDK)

**Not in the default editor.** GDK is disabled in `config.py`. Verify the
installed build (`ClassDB.class_exists("GDK")`) before writing calls.
Do not write tutorials that assume it exists. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/xbox_module/` — SCons `is_enabled()` returns
**false**. Enable only with `module_xbox_module_enabled=yes` on
**Windows + MSVC + Microsoft GDK** (`gdk_path` / `GameDKLatest`). Without
GDK headers the module builds a **stub**.

Documented classes (XML): `GDK`, `GDKResult`, `XboxEditorPlugin`.
Many `GDKUser` / `GDKStore` / … names are **registered in `config.py` but
lack XML** — do not invent method signatures for them.

Settings (not `blazium/xbox/*`): `gdk/runtime/initialize_on_startup`
(default false), `gdk/runtime/embed_dispatch` (default true),
`gdk/runtime/auto_add_primary_user` (default false).

## When to use

- Use when the user asked for Xbox / GDK **and** the build has GDK.

**When not to use:** Steamworks → `blazium-steam`. Desktop export without
GDK → `blazium-export`. Any non-Windows target.

## Workflow

1. **Inspect.** `ClassDB.class_exists("GDK")`. If missing, stop — module
   not compiled in.
2. **Choose.** If `GDK.is_available()` is false, report stub build; do
   not call store APIs.
3. **Implement.** `GDK.initialize(config)` → check `GDKResult.is_ok()`.
   Pump `dispatch()` unless `gdk/runtime/embed_dispatch` is on.
4. **Verify.** `is_initialized()`. Autowork only on a GDK-enabled editor.
5. **Handoff.** Available vs stub. Do not invent `GDKStore` calls.

## Patterns

### Feature-detect first

```gdscript
if not ClassDB.class_exists("GDK"):
	push_error("xbox_module not compiled (module_xbox_module_enabled=yes)")
	return
var gdk := Engine.get_singleton("GDK")
if not gdk.is_available():
	push_error("GDK stub — Microsoft GDK / MSVC required")
	return
var result: GDKResult = gdk.initialize()
if not result.is_ok():
	push_error(result.get_message())
	return
```

`GDKResult`: `is_ok()`, `get_hresult()`, `get_code()`, `get_message()`,
`get_data()`. `GDK.shutdown()` when tearing down.

### Store / achievements

**No XML** for `GDKAchievements` / `GDKStore` in the installed editor class docs. If the
user needs them, read the C++ bindings in `xbox_module/` — do not copy
Unity Xbox APIs or guess methods.

## Pitfalls

- **Assumed GDK in a default editor** → disabled in `config.py`.
- **Enabled Xbox on Linux/macOS** → `can_build` is Windows only.
- **Invented `blazium/xbox/*` keys** → `gdk/runtime/*`.
- **Documented unpublished GDKUser methods** → XML-only in this skill.

## Resources

- Tests: https://github.com/blazium-games/xbox_module_tests

- `blazium/modules/xbox_module/doc_classes/GDK.xml`
- `GDKResult.xml`
- `xbox_module/config.py` — `is_enabled()`, `gdk_path`

## Related skills

- `blazium-steam` — other store
- `blazium-export` — desktop without GDK
