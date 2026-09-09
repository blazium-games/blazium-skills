---
name: blazium-autowork
description: >
  Authors and runs Blazium Autowork tests (extends AutoworkTest, test_* methods,
  .autoworkconfig.json). Use when adding unit/integration tests, CI headless
  runs, JustAMCP autowork_* tools, or blazium-cli remote autowork. GDScript,
  Luau, and C# AutoworkTest when MODULE_MONO_ENABLED.
---

# Blazium Autowork

Native GUT-compatible tests. Three invoke paths: unit `--aw-*` / `run_tests.gd`,
JustAMCP, and `blazium-cli remote autowork`. Baseline: **Blazium 0.6.x (Godot
4.3.2 fork)**.

Unit `--aw-*` flags (not `--aw-e2e*`) self-start `run_tests()` without `-s`.
If both `-s` and unit `--aw-*` are present, `-s` wins. `--aw-*` still skips
MCP unless `--enable-mcp`.

GDScript-only CI:

```bash
blazium --headless --path "$PROJECT" --aw-dir=res://tests/gdscript
```

Mixed `.gd` / `.luau` still needs `-s run_tests.gd` (one config suffix cannot
cover both):

```bash
blazium --headless --path "$PROJECT" -s run_tests.gd
```

All Autowork classes are marked experimental. Copy locked APIs from the pack
reference `07-autowork-reference.md` — do not invent `assert_*` names or ports.

When `MODULE_MONO_ENABLED`, default suffix `.gd` also matches `.cs`.

## When to use

- Use when writing `test_*.gd` (or `.luau` / `.cs`) that `extends AutoworkTest`.
- Use when adding `.autoworkconfig.json` / `run_tests.gd`.
- Use when running tests from MCP or `blazium-cli remote autowork`.

**When not to use:** only invoking a runner without writing tests →
`blazium-cli-remote` or `blazium-mcp`. E2E WebSocket is optional — do not
make it the default path.

## Workflow

1. **Inspect.** Look for `.autoworkconfig.json`, `run_tests.gd`, `res://tests/`.
2. **Scaffold** if missing: copy [assets/](assets/) files when present.
3. **Author.** `extends AutoworkTest`; methods `test_*`; files `test_` + `.gd`
   (override suffix for `.luau`). Use lifecycle hooks and locked assertions only.
4. **Run.** `--aw-dir=` for one suffix, or `-s run_tests.gd` for mixed/Hub, or
   MCP (enable family first), or
   `blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait`.
5. **Read.** `user://autowork_results.json` or `autowork://latest_results`.
   JUnit is one `<testsuite>` per script and one `<testcase>` per method.
6. **Fix.** Prompt `blazium_autowork_fix_loop` / `analyze_autowork_test_failures`.
7. **Handoff.** Pass/fail counts. Exit code = fail count in headless.

## Patterns

### Minimal GDScript test

```gdscript
extends AutoworkTest

func test_adds() -> void:
	assert_eq(1 + 1, 2, "one plus one")
```

### Discovery (locked)

- Inherit `AutoworkTest`; methods `test_*`
- Prefix `test_`, suffix `.gd` (override for `.luau`)
- When `MODULE_MONO_ENABLED`, default `.gd` suffix also matches `.cs`
- `include_subdirectories` default **false**
- `AutoworkConfig.apply_options()` sets `include_subdirs` **before** `add_directory()`
- Inner classes: constants starting with `Test`
- Config: `res://.autoworkconfig.json` or legacy `.gutconfig.json`

### MCP

Family `blazium/justamcp/tools/autowork_tools` defaults **false**. Enable it,
then: `blazium_autowork_run_all_tests`, `run_tests_in_directory`,
`run_test_script`, `run_test_by_name`, `list_tests`, `is_running`.

JUnit path must be under `user://`. Nested runs are blocked. `--aw-*` disables
MCP unless `--enable-mcp` is also passed.

### Luau

`extends = "AutoworkTest"` works. Newer engines bind `assert_*`, `wait_*`,
`pass_test`, `fail_test`, `pending`, `print_log`, `p`. Do not invent names.
Doubles are **GDScript only**. Hub release-editor CI may still use `error()` /
`must()`. Hub example: `blazium-hub/tests/luau/test_001_hub_logic.luau`.

### C#

When `MODULE_MONO_ENABLED`, discover `AutoworkTest` subclasses with `test_*`.
Empty `test_*` list prints a `--build-solutions` hint. Use existing ClassDB
asserts — do not invent a C# assert DSL.

### E2E (optional)

`blazium/autowork/e2e_enabled` registers autoload **`AutomationServer`**
(`AutoworkE2EServer`). Port **6008**. First command **`hello`** + HMAC.
`AutoworkInputSender` is **not** injected — instantiate it.

### Runtime UI

`blazium/autowork/show_runtime_ui` (default **false**) places `AutoworkRuntimeUI`.

### Build

Editor: on by default. template_debug: `module_autowork_enabled=yes`.
**Never in template_release.**

## Pitfalls

- **`--aw-e2e*` did nothing for unit tests** → those flags are not the unit runner.
- **`-s` ignored `--aw-dir`** → `-s` wins if both are present.
- **Luau `assert_foo` invented** → only locked helper names.
- **`double_script` on Luau** → GDScript only.
- **MCP autowork tools missing** → family default off.
- **Second run errors "already running"** → nested Autowork blocked.
- **`include_subdirs` false on remote** → default; pass `--include-subdirs`.
- **`AutoworkRuntimeUI` missing** → enable `blazium/autowork/show_runtime_ui`.
- **Looked up `AutoworkE2EServer` autoload** → name is `AutomationServer`.
- **C# tests empty** → build the C# solution first.

## Resources

- Runner catalog: [references/runner.md](references/runner.md)
- Full locked API: pack reference `07-autowork-reference.md`
- Hub: `blazium-hub/run_tests.gd`, `blazium-hub/.autoworkconfig.json`
- Samples: https://github.com/blazium-games/autowork_module_tests

## Related skills

- `blazium-cli-remote` — invoke Autowork over HTTP
- `blazium-mcp` — MCP invoke + fix_loop prompt
- `blazium-new-project` — scaffold tests/
- `blazium-luau` — Luau AutoworkTest helpers
- `blazium-csharp` — C# AutoworkTest discovery
