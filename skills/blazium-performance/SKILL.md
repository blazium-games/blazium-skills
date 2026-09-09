---
name: blazium-performance
description: >
  Profiles a Blazium project with JustAMCP monitors
  (get_performance_monitors, profiling_detect_bottlenecks, profiling_monitor)
  plus Autowork soak. Use for FPS/memory bottlenecks. Not a generic
  profiler.
---

# Blazium performance

JustAMCP + Autowork soak. Baseline: **Blazium
0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Toolset: JustAMCP `profiling_tools`.
`disciplines/performance-optimization` into this skill.

## When to use

- Use when FPS, hitching, or memory needs evidence before a change.

**When not to use:** feature work without a measured problem. Export size
→ `blazium-export`. A generic “optimize everything” pass.

## Workflow

1. **Inspect.** Play-mode vs editor. `list_toolsets` → `profiling_tools`.
2. **Choose.** Snapshot vs threshold watch vs Autowork soak.
3. **Implement.** Call the three tools below. Change one bottleneck at a
   time using the owning domain skill.
4. **Verify.** Re-run `profiling_detect_bottlenecks` / Autowork soak.
5. **Handoff.** Monitor names + before/after. Fix in the domain skill.

## Patterns

### Monitor list

`get_performance_monitors` — memory, FPS, navigation, rendering counters.

### Bottleneck workflow

1. `get_performance_monitors` (baseline)
2. `profiling_detect_bottlenecks` (common counter heuristics)
3. `profiling_monitor` with caller thresholds
4. Fix via the matching skill (3D / physics / UI / …)
5. Repeat

### Autowork soak

Long `wait` / input simulate in `test_*.gd` — see `blazium-autowork`.
Do not treat a single screenshot as proof.

## Pitfalls

- **Guessed a 4.7 profiler panel** → JustAMCP tools + 4.3.2 debugger.
- **Rewrote a performance discipline book** → three tools + soak.
- **Changed three systems at once** → no evidence.

## Resources

- JustAMCP `profiling_tools` (`justamcp_profiling_tools.cpp`)

## Related skills

- `blazium-autowork` — soak
- `blazium-mcp` — tool discovery
