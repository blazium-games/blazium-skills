---
name: blazium-release-checklist
description: >
  Runs a launch and patch gate: export preset present, project version
  bumped, CI green, and store page fields filled. Use before shipping a
  Blazium build. Export steps stay on blazium-export. CI logs stay on
  blazium-ci-watch. Page copy stays on blazium-games-publish.
---

# Blazium release checklist

Gate before a launch or a patch. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

Do not re-teach export, CI, or the store page. Confirm each owner skill
has already been applied, then report gaps.

## When to use

- Use when asking if this build can ship or if a patch is ready.
- Use when listing the remaining gate items.

**When not to use:** creating presets → `blazium-export` or
`blazium-export-web`. Reading a failed job → `blazium-ci-watch`. Writing
the store page → `blazium-games-publish`.

## Grok host

Read this file only. Spawn `release-manager`. Child prompts must include
the version string and the preset name. Evidence is preset presence, the
version field, CI status, and the page checklist — or `INCONCLUSIVE`.

## Workflow

1. **Inspect.** `export_presets.cfg`, project version, open CI result,
   store page fields.
2. **Choose.** Launch (all gates) or patch (version bump, notes, CI).
3. **Implement.** Fix only missing gates by handing off to the owner skill.
   Do not duplicate their steps here.
4. **Verify.** Each gate is pass or an explicit gap. No screenshot of the
   export dialog as proof.
5. **Handoff.** Gate table and the next owner.

## Patterns

| Gate | Pass when | Owner if missing |
|------|-----------|------------------|
| Preset | Named preset exists | `blazium-export` |
| Version | Project version bumped for this patch | `blazium-project-config` |
| CI | Latest requested job green | `blazium-ci-watch` |
| Store | Page fields filled | `blazium-games-publish` |
| Notes | Player-facing changes listed | this checklist |

Patch notes are a short list of what changed. They are not a second changelog skill.

## Output contract

- Version string
- Preset name
- CI result or `INCONCLUSIVE`
- Store gate
- Remaining owners

## Pitfalls

- **Re-wrote the export preset here** → `blazium-export`.
- **Called CI green without the job result** → `blazium-ci-watch`.
- **Shipped with the previous version string** → bump first.
- **Treated a web host header issue as a store-page issue** → `blazium-export-web`.

## Resources

- Owner skills listed in the gate table

## Related skills

- `blazium-export` — presets
- `blazium-ci-watch` — job result
- `blazium-games-publish` — page
- `blazium-project-config` — version field
