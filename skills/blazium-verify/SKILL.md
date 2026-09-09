---
name: blazium-verify
description: >
  Proves or disproves a falsifiable Blazium claim with one local surface:
  Autowork test_*, blazium-cli remote, or editor/game JustAMCP. Returns
  VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Use when asked to verify, prove,
  or show evidence. Not a recap and not a host-specific browser harness.
---

# Blazium verify

Evidence, not a recap. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Restate the claim so it can fail. Pick **one** surface. Capture the same
command before and after when comparing. Return exactly one verdict:
`VERIFIED`, `NOT VERIFIED`, or `INCONCLUSIVE`.

Works the same on Claude, Cursor, and Codex — no host plugin required.

## When to use

- Use when the user asks to verify, prove a fix, or show evidence.
- Use when a test is green but play-mode behavior still needs a check.

**When not to use:** vague "the code is cleaner" — ask for a measurable
claim first. Authoring the suite → `blazium-autowork`. Watching export CI
→ `blazium-ci-watch`. Connecting the editor catalog → `blazium-mcp`.

## Workflow

1. **Restate.** Condition, metric, threshold (e.g. `test_adds` pass count = 1).
2. **Pick one surface.** Autowork `test_*`, `blazium-cli remote`, editor
   MCP `:6506`, or game MCP `:6507`. Do not mix ports.
3. **Measure.** Same command, same project path, same warmup.
4. **Compare.** Raw output: Autowork JSON, remote `--json`, MCP tool result.
5. **Verdict.** One of the three labels. Quote the artifact.

## Surfaces

| Claim kind | Surface |
|------------|---------|
| Unit / integration | `blazium --headless --path . --aw-dir=res://tests/gdscript` or `blazium-cli remote autowork run --wait --json` |
| Running editor | `blazium-cli remote status --json` / `exec` / `eval` (`blazium-cli-remote`) |
| Scene / settings | Editor JustAMCP (`blazium-mcp`) — discover, do not dump tools |
| Gameplay hook | Game MCP `res://mcp` (`blazium-game-mcp`) |

Never use a browser smoke harness. Never invent assert names.

## Pitfalls

- **Recapped the chat** → not evidence.
- **Mixed 6506 / 6507 / 6508** → one surface.
- **Screenshot of a dock** → use Autowork or `--json`.
- **INCONCLUSIVE hidden as VERIFIED** → say when the runner did not start.

## Related skills

- `blazium-autowork` — write / run `test_*`
- `blazium-cli-remote` — HTTP `/v1` on 6508
- `blazium-mcp` — editor catalog
- `blazium-game-mcp` — `res://mcp`
- `blazium-ci-watch` — CI / export jobs
