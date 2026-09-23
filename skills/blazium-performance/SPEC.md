---
name: blazium-performance
pack: growth
---

# blazium-performance

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

Agents skip JustAMCP monitors and Autowork soak.

## What

Use `get_performance_monitors`, `profiling_detect_bottlenecks`, `profiling_monitor`. Soak via Autowork waits/simulate.

**Non-goals:** Do not invent profiler APIs.

## How

JustAMCP profiling_tools + Autowork. Pin 4.8.x profiler panels.

## Reasoning

Blazium-flavored wrapper around the discipline skill.

## Sources

- disciplines/performance-optimization
- JustAMCP profiling_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-autowork` — soak
- `blazium-mcp` — profiling tools
