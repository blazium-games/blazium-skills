---
name: blazium-autowork
description: >
  Authors and runs Blazium Autowork tests (extends AutoworkTest, test_*
  methods, .autoworkconfig.json). Use when adding unit/integration tests,
  CI headless runs, JustAMCP autowork_* tools, or blazium-cli remote
  autowork. GDScript, Luau, and C# AutoworkTest when MODULE_MONO_ENABLED.
  Not a verify verdict and not only invoking a runner.
when-to-use: >
  AutoworkTest, test_*, .autoworkconfig.json, --aw-dir, run_tests.gd,
  autowork_results.json, JustAMCP autowork_tools, blazium-cli remote autowork
metadata:
  author: blazium-games
  short-description: Author and run AutoworkTest test_* on 0.6.x / 4.3.2
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

Mixed `.gd` / `.luau` still needs `-s run_tests.gd`.

All Autowork classes are marked experimental. Copy locked APIs from pack
reference `07-autowork-reference.md` — do not invent `assert_*` names or ports.

When `MODULE_MONO_ENABLED`, default suffix `.gd` also matches `.cs`.

## When to use

- Use when writing `test_*.gd` (or `.luau` / `.cs`) that `extends AutoworkTest`.
- Use when adding `.autoworkconfig.json` / `run_tests.gd`.
- Use when running tests from MCP or `blazium-cli remote autowork`.

**When not to use:** only invoking a runner without writing tests →
`blazium-cli-remote` or `blazium-mcp`. Verdict on a claim → `blazium-verify`.
E2E WebSocket is optional — do not make it the default path.

## Grok host

On Grok, keep context small: read this file, then `references/runner.md` only
if the invoke path is unclear. Spawn `blazium-autowork-specialist` to author
tests and `qa-tester` to run them. Child prompts must include the test path,
`--aw-dir` or `-s run_tests.gd`, and the 4.3.2 pin.

Use Grok `bash` for `blazium --headless --aw-dir=…`. Use connected MCP only
when JustAMCP `:6506` is actually attached. Grok `code_execution` is **not**
the Autowork runner — quote `user://autowork_results.json` or
`autowork://latest_results`.

## Workflow

1. **Inspect.** Look for `.autoworkconfig.json`, `run_tests.gd`, `res://tests/`.
2. **Scaffold** if missing: copy [assets/](assets/) files when present.
3. **Author.** `extends AutoworkTest`; methods `test_*`; files `test_` + `.gd`.
4. **Run.** `--aw-dir=` for one suffix, or `-s run_tests.gd` for mixed/Hub, or
   MCP (enable family first), or
   `blazium-cli remote autowork run --dir res://tests/gdscript --include-subdirs --wait`.
5. **Read.** `user://autowork_results.json` or `autowork://latest_results`.
6. **Fix.** Prompt `blazium_autowork_fix_loop` / `analyze_autowork_test_failures`.
7. **Handoff.** Pass/fail counts. Exit code = fail count in headless.

## Patterns

```gdscript
extends AutoworkTest

func test_adds() -> void:
	assert_eq(1 + 1, 2, "one plus one")
```

Discovery is locked: inherit `AutoworkTest`; methods `test_*`; suffix `.gd`
(override for `.luau`). `include_subdirectories` default **false**. MCP family
`blazium/justamcp/tools/autowork_tools` defaults **false**. JUnit path must be
under `user://`. Nested runs are blocked. E2E autoload name is
`AutomationServer` on port **6008**. Never in template_release.

## Output contract

- Test paths authored or run
- Invoke path (`--aw-dir` / `-s run_tests.gd` / MCP / remote)
- Pass / fail / pending counts (or `INCONCLUSIVE` if the runner did not start)
- Results artifact (`user://autowork_results.json`)
- Next skill (`blazium-verify` for a claim, `blazium-cli-remote` to invoke only)

## Pitfalls

- **`--aw-e2e*` did nothing for unit tests** → those flags are not the unit runner.
- **`-s` ignored `--aw-dir`** → `-s` wins if both are present.
- **Grok `code_execution` used as the runner** → headless Autowork or remote.
- **Looked up `AutoworkE2EServer` autoload** → name is `AutomationServer`.
- **MCP autowork tools missing** → family default off.
- **Second run errors "already running"** → nested Autowork blocked.

## Resources

- Runner catalog: [references/runner.md](references/runner.md)
- Full locked API: pack reference `07-autowork-reference.md`
- Samples: https://github.com/blazium-games/autowork_module_tests

## Related skills

- `blazium-cli-remote` — invoke Autowork over HTTP
- `blazium-mcp` — MCP invoke + fix_loop prompt
- `blazium-verify` — verdict from a run
- `blazium-new-project` — scaffold tests/
