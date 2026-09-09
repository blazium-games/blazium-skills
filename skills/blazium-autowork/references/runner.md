# Autowork runner catalog

Do not invent `assert_*` names or ports. Copy locked helpers from pack
reference `07-autowork-reference.md`.

## Discovery

| Rule | Value |
|------|-------|
| Base class | `extends AutoworkTest` |
| Methods | `test_*` |
| Files | prefix `test_`, default suffix `.gd` |
| Luau | override suffix `.luau`; `extends = "AutoworkTest"` |
| C# | when `MODULE_MONO_ENABLED`, default `.gd` suffix also matches `.cs` |
| Subdirs | `include_subdirectories` / `include_subdirs` default **false** |
| Config | `res://.autoworkconfig.json` (legacy `.gutconfig.json`) |
| Inner classes | constants starting with `Test` |

`AutoworkConfig.apply_options()` sets `include_subdirs` **before**
`add_directory()`.

## Invoke paths

| Path | When |
|------|------|
| `blazium --headless --path "$PROJECT" --aw-dir=res://tests/gdscript` | One suffix (GDScript-only CI). Unit `--aw-*` self-starts. |
| `blazium --headless --path "$PROJECT" -s run_tests.gd` | Mixed `.gd` / `.luau`. If both `-s` and unit `--aw-*` are present, `-s` wins. |
| `blazium-cli remote autowork run --dir … --include-subdirs --wait --json` | Running editor / CI HTTP. |
| JustAMCP `blazium_autowork_*` | Editor MCP. Family `blazium/justamcp/tools/autowork_tools` defaults **off**. |

`--aw-*` skips MCP unless `--enable-mcp` is also passed. Nested Autowork
runs are blocked.

## MCP family (default off)

Enable `blazium/justamcp/tools/autowork_tools` first. Then:

- `blazium_autowork_run_all_tests`
- `run_tests_in_directory`
- `run_test_script`
- `run_test_by_name`
- `list_tests`
- `is_running`

JUnit path must be under `user://`. Results: `user://autowork_results.json`
or `autowork://latest_results`.

## Build

Editor: on by default. `template_debug`: `module_autowork_enabled=yes`.
**Never in `template_release`.**
