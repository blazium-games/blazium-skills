---
name: blazium-router
pack: infra
---

# blazium-router

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Agents miss JustAMCP, Autowork, and Services if they treat a Blazium tree as generic Godot. A Blazium-first router is the adoption gate.

## What

Fingerprint the project and load the smallest Blazium skill set. Detect `project.blazium` first.

**Non-goals:** Do not re-teach APIs. Do not dump the whole catalog.

## How

1. Inspect workspace for `project.blazium` (preferred) or `project.godot` with `blazium/` keys.
2. If Blazium, stay in this pack.
3. Classify the task and name at most router + two domain skills.
4. Never conflate editor MCP :6506, game MCP :6507, cloud `mcp.blazium.games`, and `remote_control` HTTP :6508.

## Reasoning

Without this skill every other spec is optional noise.

## Sources

- `project.blazium`
- Editor JustAMCP `:6506`, game JustAMCP `:6507`, remote_control `:6508`, cloud `https://mcp.blazium.games/mcp`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-project-config` — owns settings once routed
- `blazium-mcp` — editor MCP after detect
- `blazium-new-project` — greenfield path
