---
name: blazium-prototype
description: >
  Proves one mechanic as a throwaway vertical slice in an existing or
  just-opened Blazium project. Use for an idea-to-running playable proof.
  Project bootstrap, git, and res://mcp stay on blazium-new-project.
---

# Blazium prototype

One verb, playable. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

`blazium-new-project` creates the repo, ignore file, and MCP hook. This
skill starts after that folder exists and stops when one mechanic runs.

## When to use

- Use when proving a dash, jump, or interaction before production structure.
- Use when the slice should be disposable.

**When not to use:** empty folder, git, or `res://mcp` → `blazium-new-project`.
Production architecture → stop and route. Full genre composition →
`blazium-genre-*`.

## Grok host

Read this file only. Spawn `prototyper`. Child prompts must name the one
mechanic and the scene. Evidence is an Autowork smoke or play-mode check
that the verb happened.

## Workflow

1. **Inspect.** Project exists (`blazium-new-project` if not).
2. **Choose.** One mechanic. Cut everything else.
3. **Implement.** One scene, one script, input already on `blazium-input`
   if actions are needed. No save, no net, no store.
4. **Verify.** Autowork smoke: the verb’s outcome is true after simulate
   or a short play. Not a screenshot of the editor.
5. **Handoff.** Keep or delete. List files if kept.

## Patterns

A slice is a scene the player can start and a script that performs one
action. If the proof needs a camera or physics, load that skill next —
do not grow a framework inside the slice.

## Output contract

- Mechanic proved
- Scene and script paths
- Autowork or play evidence, or `INCONCLUSIVE`
- Keep or discard

## Pitfalls

- **Bootstrapped git and MCP here** → `blazium-new-project`.
- **Three mechanics in the slice** → pick one.
- **Left the slice as the production tree without a handoff** → say keep
  and name the next programmer skill.
- **No evidence the verb fired** → `INCONCLUSIVE`.

## Resources

- `blazium-new-project` when the folder is empty
- `blazium-autowork` for the smoke assert

## Related skills

- `blazium-new-project` — folder bootstrap
- `blazium-autowork` — smoke
- `blazium-gdscript` — the script
- `blazium-2d-movement` — if the verb is movement
