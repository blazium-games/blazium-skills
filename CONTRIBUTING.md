# Contributing to blazium-skills

Canonical skills live in `skills/<name>/` with `SKILL.md` plus `SPEC.md`.
Do not invent APIs, CLI verbs, or Godot 4.7-only calls. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

## Add a skill

1. Copy `templates/SKILL.template.md` and `templates/SPEC.template.md`.
2. Put catalogs in `references/` (keep `SKILL.md` under ~500 lines).
3. Register the path on the topic pack **and** the `blazium` bundle in
   [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).
4. Add a classifier row in [`skills/blazium-router/SKILL.md`](skills/blazium-router/SKILL.md)
   and a README index row.
5. Add a trigger case in [`evals/smoke/fixtures/triggers.json`](evals/smoke/fixtures/triggers.json)
   when the skill could collide with a sibling.
6. Keep the YAML `description` dense: outcome, trigger nouns, hard negatives.
   Optional Grok keys: `when-to-use`, `metadata.short-description`.
7. Sync and validate:

```bash
python scripts/sync-plugin-packs.py
python scripts/validate-plugin-packs.py
python evals/smoke/check_triggers.py
```

`plugins/<pack>/skills/` is generated (junctions on Windows). Do not
hand-edit those links.

## Hosts

One catalog, three marketplaces (sync writes Cursor + Codex from Claude).
Grok auto-reads the Claude marketplace and also discovers `./.grok/skills/`
and `~/.grok/skills/`. See [GROK.md](GROK.md). Do not invent a fourth
marketplace schema.

| Host | File |
|------|------|
| Claude Code | `.claude-plugin/marketplace.json` |
| Cursor | `.cursor-plugin/marketplace.json` |
| Codex | `.agents/plugins/marketplace.json` |
| Grok | `skills/*/SKILL.md` + [GROK.md](GROK.md) |

Official docs links: `https://docs.blazium.app` or `https://cdn.blazium.app` only.
