---
name: replace-with-skill-name
description: >
  State the concrete outcome this skill delivers. Use when the request mentions
  specific tasks, files, APIs, symptoms, or goals that should activate it.
---

# Replace with skill title

Deliver the outcome in one sentence. State the baseline version for new projects:
**Blazium 0.6.x (Godot 4.3.2 fork)**. Preserve an existing project's pinned version
unless migration is requested. Do not apply Godot 4.7-only APIs.

## When to use

- Use when …
- Use when …

**When not to use:** hand off nearby work to `$related-skill` or the relevant engine skill.

## Workflow

1. **Inspect.** Read `project.blazium` or `project.godot`, relevant files, existing conventions, and constraints.
2. **Choose.** Select the smallest compatible approach and state any consequential assumption.
3. **Implement.** Make the focused change using the project's current version and patterns.
4. **Verify.** Prefer Autowork, JustAMCP, or `blazium-cli remote` over unverified editor clicks.
5. **Handoff.** Report changed files, evidence, caveats, and the next useful action.

## Patterns

### Focused pattern

```text
Use a compact, verified example. Do not invent APIs.
```

## Pitfalls

- **Visible symptom** → likely cause; concrete fix and verification.
- **Version mismatch** → inspect the installed Blazium version and use matching docs.

## Resources

- Keep this file to workflow + gotchas (aim under 500 lines). Put catalogs in `references/`.
- Read `references/example.md` only when deeper detail is needed.
- Prefer JustAMCP tools when the editor MCP is connected.
- Copy `assets/example.ext` only when the task needs the starter asset. Do not link missing assets.

## Related skills

- `$related-skill` — the adjacent responsibility it owns.
