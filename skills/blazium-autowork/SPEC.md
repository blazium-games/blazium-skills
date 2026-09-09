---
name: blazium-autowork
pack: infra
---

# blazium-autowork

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Autowork is the built-in test runner. Agents that skip it ship untested scenes and cannot close `blazium_autowork_fix_loop`.

## What

Author `extends AutoworkTest` scripts. Discover via `.autoworkconfig.json`. Run via unit `--aw-*`, `run_tests.gd` (mixed/Hub), JustAMCP Autowork tools, or `blazium-cli remote autowork`. Read `user://autowork_results.json`. Optional E2E via autoload `AutomationServer`.

**Non-goals:** Do not invent assertion names. Do not invent a C# assert DSL. Do not treat `--aw-e2e*` as the unit runner. Do not treat E2E as the default path.

## How

Discovery: inherit `AutoworkTest`; methods `test_*`; files `test_` + `.gd`; when `MODULE_MONO_ENABLED` default `.gd` also matches `.cs`; inner classes starting with `Test`; `include_subdirectories` default false. `apply_options()` sets `include_subdirs` before `add_directory()`.

Config: `res://.autoworkconfig.json` or legacy `res://.gutconfig.json`.

Unit `--aw-*` (not `--aw-e2e*`) self-starts. GDScript-only: `blazium --headless --path $PROJECT --aw-dir=res://tests/gdscript`. Mixed suffixes / Hub: `-s run_tests.gd`. `-s` wins if both are present.

Assertions, doubles, waits, simulate, InputSender: see the reference. Doubles are **GDScript only**. `AutoworkInputSender` is **not** injected. JUnit is one `<testsuite>` per script and one `<testcase>` per method.

Luau: `extends = "AutoworkTest"` works; newer engines bind `assert_*` / `wait_*` / `pass_test` / `fail_test` / `pending` / `print_log` / `p`. Hub release CI may still use `error()` / `must()`.

MCP family `blazium/justamcp/tools/autowork_tools` defaults **false**. Tools: `blazium_autowork_run_all_tests`, `run_tests_in_directory`, `run_test_script`, `run_test_by_name`, `list_tests`, `is_running`. Resource: `autowork://latest_results`. Prompts: `generate_autowork_test`, `analyze_autowork_test_failures`, `blazium_autowork_fix_loop`. Nested runs blocked. JUnit path must be under `user://`.

remote_control (default **6508**): `autowork_run` / `status` / `results`. CLI `--wait` and `--include-subdirs`. `include_subdirs` honored (default false).

E2E: `blazium/autowork/e2e_enabled` → autoload **`AutomationServer`**. Port **6008**. First command **`hello`** + HMAC. Runtime UI: `blazium/autowork/show_runtime_ui` (default false).

Build: editor default; template_debug opt-in; **never template_release**.

Hub reference: `blazium-hub/run_tests.gd`, `.autoworkconfig.json`, `tests/gdscript/`, `tests/luau/test_001_hub_logic.luau`.

C#: AutoworkTest + `test_*` when `MODULE_MONO_ENABLED`. Empty methods → `--build-solutions`. No C# assert DSL.

## Reasoning

Distinct from `blazium-cli-remote` (invoke vs author) and JustAMCP (one of three runners). This is the quality loop for the userbase.

## Sources

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli-remote` — headless invoke
- `blazium-mcp` — MCP invoke + fix_loop prompt
- `blazium-luau` — Luau AutoworkTest helpers
- `blazium-csharp` — C# AutoworkTest discovery
- `blazium-new-project` — scaffold tests/
