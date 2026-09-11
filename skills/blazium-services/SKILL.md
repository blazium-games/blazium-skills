---
name: blazium-services
description: >
  Implements first-party Blazium 0.6.x login (Discord OAuth, Steam tickets,
  LoginClient templates) on Godot 4.3.2. Use when exchanging platform auth
  for a JWT. Deep JWT encode/decode stays on blazium-jwt. Not lobby rooms
  and not Games cloud MCP.
when-to-use: >
  LoginClient, received_jwt, request_login_info, Discord OAuth login,
  Steam ticket exchange, user://blazium.cfg token
metadata:
  author: blazium-games
  short-description: LoginClient templates to a persisted JWT
---

# Blazium Services

Login → JWT. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
Encode/decode/validate → `blazium-jwt`.

**Nightly caveat:** `LoginClient` / `LobbyClient` / `MasterServerClient` are
script templates and https://docs.blazium.app — not C++/xml class docs in the
installed editor. Copy only template methods (`request_login_info`,
`received_jwt`, `connect_to_server`). Do not invent APIs.

Store tokens in `user://blazium.cfg`. Never conflate this with editor
JustAMCP (`:6506`), game MCP (`:6507`), or cloud
`https://mcp.blazium.games/mcp`.

## When to use

- Use when adding login or token persistence after `received_jwt`.
- Use when Discord OAuth or Steam tickets must become a Blazium JWT.

**When not to use:** sign/verify/revoke JWT locally → `blazium-jwt`.
Matchmaking rooms → `blazium-lobby`. Steam ticket request → `blazium-steam`.
Discord OAuth/presence → `blazium-discord`. Store/deploy →
`blazium-games-mcp`.

## Grok host

Read this file only. Spawn `blazium-live-ops-specialist`. Child prompts must
include the login provider (`discord` / Steam) and the token path
(`user://blazium.cfg`). Evidence is Autowork on `received_jwt` or an
expired-token fail-closed path — not a screenshot of a login page.

## Workflow

1. **Inspect.** Nightly + `ClassDB.class_exists` / templates under
   `script_templates/LoginClient/`.
2. **Choose.** Discord OAuth or Steam ticket → backend JWT.
3. **Implement.** `await request_login_info("discord")`, `OS.shell_open`,
   handle `received_jwt`. Persist in `user://blazium.cfg`.
4. **Verify.** Expired/offline JWT paths. Autowork or play-mode.
5. **Handoff.** Token path + `blazium-lobby` after auth.

## Patterns

```gdscript
var login_result: LoginURLResult = await request_login_info("discord").finished
if login_result.has_error():
	push_error(login_result.error)
	return
OS.shell_open(login_result.login_url)
# wait for received_jwt(jwt, type, access_token)
```

## Output contract

- Login provider
- Token path (`user://…`)
- Template methods used (`request_login_info` / `received_jwt`)
- Expired/offline path asserted

## Pitfalls

- **Invented LoginClient C++ methods** → template + nightly docs only.
- **Stored JWT in `res://`** → `user://blazium.cfg`.
- **Skipped expiry / offline** → parse `exp`, fail closed.
- **Called Games MCP for identity** → wrong layer.

## Related skills

- `blazium-jwt`, `blazium-lobby`, `blazium-steam`, `blazium-discord`, `blazium-games-mcp`
