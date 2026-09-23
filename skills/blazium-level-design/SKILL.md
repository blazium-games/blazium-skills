---
name: blazium-level-design
description: >
  Lays out pacing, encounter beats, and tile or meter metrics for a Blazium
  space. Use when a level needs a beat map before paint. Cell paint stays on
  blazium-tilemap. Seeded layouts stay on blazium-procedural.
---

# Blazium level design

Pacing and metrics before paint. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

This skill writes the beat map and the numbers a painter or generator uses.
It does not replace `TileMapLayer` or GridMap.

## When to use

- Use when blocking a level: intro, teach, twist, rest, finale.
- Use when stating width in tiles, jump gaps, or encounter spacing.

**When not to use:** painting cells → `blazium-tilemap`. TMX import →
`blazium-tiled`. Seeded dungeons → `blazium-procedural`. Nav bake →
`blazium-navigation`.

## Grok host

Read this file only. Spawn `level-designer`. Child prompts must include the
beat list and the metric unit (tiles or meters). Evidence is the beat note
plus the scene or tile bounds that match it.

## Workflow

1. **Inspect.** Genre skill already loaded, player speed, jump distance.
2. **Choose.** One critical path. Side rooms are optional, not the spine.
3. **Implement.** Write beats and metrics. Hand paint to `blazium-tilemap`
   or `blazium-3d`. Keep the first teach beat free of extra mechanics.
4. **Verify.** Walk the path in play mode or Autowork a body across the
   first gap using the stated speed. Not a screenshot of an empty grid.
5. **Handoff.** Beat list, metric table, scene path.

## Patterns

| Beat | Purpose | Metric |
|------|---------|--------|
| Intro | Safe movement | wider than two screens |
| Teach | One new verb | gap ≤ tested jump distance |
| Twist | Combine two verbs | one hazard family |
| Rest | No new threats | pickup or view |
| Finale | The taught set | no unseen mechanic |

State distances in tiles (2D) or meters (3D). Do not invent a second grid.

## Output contract

- Beat list (name, purpose)
- Metric table (unit, gap, spacing)
- Scene or layer the numbers apply to
- Play-mode or Autowork check of the first gap, or `INCONCLUSIVE`

## Pitfalls

- **Painted the map inside this skill** → `blazium-tilemap` or `blazium-3d`.
- **Gap larger than the tested jump** → the teach beat is unfair.
- **Finale introduces a new verb** → move it to a teach beat.
- **Mixed tile and meter units** → pick one and label it.

## Resources

- Pair with `blazium-tilemap`, `blazium-3d`, `blazium-2d-movement`

## Related skills

- `blazium-tilemap` — paint
- `blazium-tiled` — authored maps
- `blazium-procedural` — seeded space
- `blazium-3d` — GridMap / mesh space
