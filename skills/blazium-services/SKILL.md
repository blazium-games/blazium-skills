---
name: blazium-services
description: >
  Implements first-party Blazium login (Discord OAuth, Steam tickets,
  LoginClient templates). Use when exchanging platform auth for a JWT.
  Deep JWT encode/decode → blazium-jwt. Not lobby rooms or Games cloud MCP.
---

# Blazium Services

Login → JWT. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
Encode/decode/validate → `blazium-jwt`.

**Nightly caveat:** `LoginClient` / `LobbyClient` / `MasterServerClient` are
script templates and https://docs.blazium.app — not C++/xml class docs in the installed editor. Copy
only template methods (`request_login_info`, `received_jwt`,
`connect_to_server`). Do not invent APIs. Verify against the installed nightly.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Store tokens in `user://blazium.cfg`. JWT crypto → `blazium-jwt`.

Never conflate this with editor JustAMCP (`:6506`), game MCP (`:6507`), or
cloud `https://mcp.blazium.games/mcp`.

## When to use

- Use when adding login or token persistence after `received_jwt`.
- Use when Discord OAuth or Steam tickets must become a Blazium JWT.

**When not to use:** sign/verify/revoke JWT locally → `blazium-jwt`.
Matchmaking rooms → `blazium-lobby`. Steam ticket request → `blazium-steam`.
Discord OAuth/presence → `blazium-discord`. Store/deploy →
`blazium-games-mcp`.

## Workflow

1. **Inspect.** Nightly + `ClassDB.class_exists` / templates under
   `script_templates/LoginClient/`. Reject invented client methods.
2. **Choose.** Discord OAuth or Steam ticket → backend JWT. Local sign/verify
   → `blazium-jwt`.
3. **Implement.** Template `LoginClient`: `await request_login_info("discord")`,
   `OS.shell_open(login_url)`, handle `received_jwt`. Persist JWT in
   `user://blazium.cfg`.
4. **Verify.** Expired/offline JWT paths. Autowork or play-mode — not a
   screenshot.
5. **Handoff.** Token path + next skill (`blazium-lobby` after auth).

## Patterns

### Template login (Discord) — do not invent extra methods

```gdscript
var login_result: LoginURLResult = await request_login_info("discord").finished
if login_result.has_error():
	push_error(login_result.error)
	return
OS.shell_open(login_result.login_url)
# wait for received_jwt(jwt, type, access_token)
```

## Pitfalls

- **Invented LoginClient C++ methods** → use the template + nightly docs only.
- **Stored JWT in `res://`** → use `user://blazium.cfg`.
- **Skipped expiry / offline** → parse `exp`, fail closed, offer re-login.
- **Called Games MCP for identity** → wrong layer; this skill owns JWT.

## Resources

- Nightly check: [references/verify-nightly.md](references/verify-nightly.md)
- Template: `blazium/modules/gdscript/editor/script_templates/LoginClient/default.gd`
- Docs: https://docs.blazium.app (verify nightly)
- JustAMCP: `script_tools` to attach the template — not cloud MCP

## Related skills

- `blazium-jwt` — encode / decode / validate
- `blazium-lobby` — rooms after JWT
- `blazium-steam` — `request_web_api_ticket` → `authenticate_with_server`
- `blazium-discord` — OAuth / Social SDK
- `blazium-games-mcp` — store / crashes, not login
