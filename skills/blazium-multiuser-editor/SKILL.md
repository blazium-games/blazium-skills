---
name: blazium-multiuser-editor
description: >
  Hosts or joins Blazium Multiuser Editor sessions (permissions, chat, kick,
  Autowork trigger). Use when collaborating on scenes. Not the full JustAMCP
  catalog.
---

# Blazium Multiuser Editor

Collaborative editor sessions — do not fight other peers. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Module: `blazium/modules/multiuser_editor/` (editor-only). Classes:
`MultiuserEditorPlugin`, `MultiuserEditorPermissions`, dock / cursor /
settings UI.

Killswitch **EditorSettings** `blazium/multiuser_editor/enabled` defaults
**false**. Other keys are EditorSettings, not ProjectSettings.

JustAMCP `multiuser_tools` only when `multiuser_editor` + `justamcp` are
compiled in: `multiuser_get_status`, `multiuser_send_chat` (`message`),
`multiuser_kick_peer` (`peer_id`), `multiuser_trigger_autowork`.

## When to use

- Use when hosting/joining a collab session, changing roles, or triggering
  Autowork for peers.

**When not to use:** discovering all MCP tools → `blazium-mcp`.
Authoring tests → `blazium-autowork`. Project `addons/` plugins →
`blazium-addons`.

## Workflow

1. **Inspect.** `multiuser_get_status` or `get_status_text`. Killswitch
   and `role` (`Host` required to host).
2. **Choose.** Host vs join. Do not mutate the same node another peer
   locked.
3. **Implement.** `host_session(port, password)` / `join_session(host, port, password)`
   or `*_from_settings()`. Chat / kick / `trigger_autowork` only with
   permission.
4. **Verify.** `is_session_connected()`. MCP: `ok` + `is_connected`.
5. **Handoff.** Peer id + role. Tests → autowork.

## Patterns

### Host / join

```text
host_session(8910, password)   # port 1024–65535; web client cannot host
join_session(host, port, password)
```

`can_host_sessions()` checks killswitch + role Host + access list.
`is_local_admin()` gates kick / force-push.

### Permission matrix

Roles: `Viewer`, `Editor`, `Admin`. Overrides:
`blazium/multiuser_editor/permissions/overrides` —
`action=role,role[@host_only|any];...` e.g.
`chat=Editor,Admin;scene_sync=Editor,Admin@any`.

`MultiuserEditorPermissions.load_defaults` / `apply_overrides` /
`can_perform(action, role)`.

### MCP

| Tool | Args |
|------|------|
| `multiuser_get_status` | `{}` |
| `multiuser_send_chat` | `{ "message": "..." }` |
| `multiuser_kick_peer` | `{ "peer_id": "..." }` |
| `multiuser_trigger_autowork` | `{}` |

Plugin: `send_chat`, `kick_peer`, `trigger_autowork`, checkpoints
`create_checkpoint` / `load_checkpoint`.

### Conflict etiquette

Do not overwrite a peer’s locked node or force-push unless the user is
admin and asked. JWT secrets stay in EditorSettings (`require_jwt`,
`jwt_secret_key`) — never commit them.

## Pitfalls

- **Edited while a peer held the lock** → wait or ask.
- **Called multiuser_* without the module** → tools missing.
- **Dumped the whole JustAMCP catalog** → this skill owns the session.
- **Treated settings as ProjectSettings** → EditorSettings
  `blazium/multiuser_editor/*`.

## Resources

- `blazium/modules/multiuser_editor/doc_classes/MultiuserEditorPlugin.xml`
- JustAMCP: `JustAMCPMultiuserTools.xml`

## Related skills

- `blazium-mcp` — tool discovery
- `blazium-autowork` — tests triggered from peers
