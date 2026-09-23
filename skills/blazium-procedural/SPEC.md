---
name: blazium-procedural
pack: growth
---

# blazium-procedural

Seeded generation. Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Unseeded rolls hide bugs and block shared challenges. Genres need a generator they can call, not a one-off `randf()` in a scene script.

## What

`RandomNumberGenerator`, `FastNoiseLite`, room-and-corridor layouts, weighted loot.

**Non-goals:** tile painting API, economy tuning, genre scene trees.

## How

1. Pin one seed on a Resource.
2. Generate once.
3. Paint with `TileMapLayer`.
4. Autowork the same seed twice.

## Reasoning

Distinct from `blazium-tilemap` (authored cells) and `blazium-balance` (designed weights).

## Sources

- Blazium: `RandomNumberGenerator`, `FastNoiseLite`

## Limits

Do not invent a noise module. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`).

## Related skills

- `blazium-tilemap` — cells
- `blazium-balance` — tables
