---
name: blazium-multiuser-editor
pack: modules
---

# blazium-multiuser-editor

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Collaborative editing changes how agents mutate scenes (permissions, peer kicks, Autowork trigger).

## What

`MultiuserEditorPlugin`, `MultiuserEditorPermissions`, JustAMCP `multiuser_*` (`get_status`, `send_chat`, `kick_peer`, `trigger_autowork`).

**Non-goals:** Do not re-document the whole JustAMCP catalog.

## How

- Module: `blazium/modules/multiuser_editor/`.
- Host/join, permission matrix, do-not-fight-other-peers.

## Reasoning

JustAMCP mentions the toolset; this skill owns the session.

## Sources

- multiuser_editor
- JustAMCP multiuser_tools

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-mcp` — tools
- `blazium-autowork` — triggered from peers
