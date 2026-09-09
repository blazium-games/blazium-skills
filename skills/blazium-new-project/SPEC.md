---
name: blazium-new-project
pack: infra
---

# blazium-new-project

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

## What

Turn an idea into a running, version-controlled Blazium project via CLI/Hub (`blazium://open`). Scaffold `res://mcp`, Autowork, and `.gitignore`.

**Non-goals:** Do not implement gameplay. Do not install unrelated modules (Xbox) unless asked.

## How

- CLI: `blazium-cli install|open|load|projects|handle-uri`. Config: `%APPDATA%\blazium\hub.json`.
- URI: `blazium://open?path=…` (OS protocol — not JustAMCP `blazium://scene/`).
- Scaffold: `project.blazium`, `res://mcp/register.gd`, `res://tests/gdscript/`, `.autoworkconfig.json`, `run_tests.gd`, `.gitignore`.
- Gather concept / platforms / live-ops need (Services vs local-only) before scaffolding.

## Reasoning

First-session success is the userbase skill. Distinct from Hub install (`blazium-cli`) which manages editors, not game content.

## Sources

- Blazium: `blazium-cli/hub/`, `blazium-hub/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-cli` — editor install if missing
- `blazium-autowork` — scaffold tests
- `blazium-game-mcp` — scaffold res://mcp
- `blazium-project-config` — settings after create
