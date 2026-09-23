---
name: blazium-procedural
description: >
  Generates seeded maps, noise fields, room-and-corridor layouts, and weighted
  loot with RandomNumberGenerator and FastNoiseLite. Use when a seed must
  reproduce the same world. Genre composition stays on blazium-genre-*.
---

# Blazium procedural

Deterministic content from a seed. Baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**.

One `RandomNumberGenerator.seed` (or `FastNoiseLite.seed`) must rebuild the
same layout. Do not call unseeded `randf()` inside generation.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep `blazium_4.8`-safe APIs unless the user asks to migrate.

## When to use

- Use when generating maps, dungeons, height fields, or loot from a seed.
- Use when a daily challenge or a shared world must replay from that seed.

**When not to use:** hand-painted cells → `blazium-tilemap`. Authored rooms
in Tiled → `blazium-tiled`. Economy curves and drop-rate design →
`blazium-balance`. Roguelike scene composition → `blazium-genre-roguelike`.

## Workflow

1. **Inspect.** What must be reproducible: layout, loot, or both.
2. **Choose.** `FastNoiseLite` for fields. A room list plus corridors for
   dungeons. A weighted table for drops.
3. **Implement.** Store the seed on a `Resource`. Draw from one
   `RandomNumberGenerator`. Paint results with `TileMapLayer.set_cell`.
4. **Verify.** Autowork: same seed, `assert_eq` on the first cells and the
   first drop. A second seed must differ. Not a screenshot of one map.
5. **Handoff.** Seed field, generator script, and which genre skill consumes it.

## Patterns

```gdscript
var rng := RandomNumberGenerator.new()
rng.seed = world_seed

var noise := FastNoiseLite.new()
noise.seed = int(world_seed)
noise.noise_type = FastNoiseLite.TYPE_SIMPLEX

func height_at(cell: Vector2i) -> float:
	return noise.get_noise_2d(float(cell.x), float(cell.y))

func roll_loot(table: Array) -> StringName:
	var total := 0
	for row in table:
		total += int(row["weight"])
	var pick := rng.randi_range(1, total)
	var acc := 0
	for row in table:
		acc += int(row["weight"])
		if pick <= acc:
			return row["id"]
	return &""
```

Dungeon: place non-overlapping rooms, then connect room centers with
L-shaped corridors. Keep the room list in seed order so the layout replays.

## Pitfalls

- **`randf()` without a seed** → cannot replay a bug.
- **Noise seed and RNG seed diverge** → layout and loot do not share a world.
- **Generation in `_process`** → rebuilds every frame. Generate once, then paint.
- **Weighted pick uses float drift** → integer weights and `randi_range`.

## Resources

- https://docs.blazium.app — `RandomNumberGenerator`, `FastNoiseLite`, `TileMapLayer`

## Related skills

- `blazium-tilemap` — paint the cells
- `blazium-balance` — weight design
- `blazium-genre-roguelike` — run structure
- `blazium-level-design` — pacing of the generated space
