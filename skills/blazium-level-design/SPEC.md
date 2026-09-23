---
name: blazium-level-design
pack: growth
---

# blazium-level-design

Beat maps and spatial metrics. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Painters need a pace and a measured gap. A tile skill does not decide the teach order.

## What

Beat lists and tile or meter metrics.

**Non-goals:** `set_cell`, TMX import, seeded noise.

## How

1. Read jump or move distance from the controller skill.
2. Write beats and one unit system.
3. Hand off paint. Verify the first gap.

## Reasoning

Distinct from `blazium-tilemap` (cells) and `blazium-procedural` (seeds).

## Sources

- Blazium scenes and TileMapLayer bounds. No level-editor class.

## Limits

Do not invent a level-editor API. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`).

## Related skills

- `blazium-tilemap` — paint
- `blazium-procedural` — generation
