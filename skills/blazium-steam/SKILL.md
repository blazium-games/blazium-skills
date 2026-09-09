---
name: blazium-steam
description: >
  Integrates Blazium’s native Steam singleton (not GodotSteam): session
  tickets → JWT, achievements, stats, inventory. Use when authenticating
  with Steam or syncing Steamworks runtime data. Not SteamPipe publishing.
---

# Blazium Steam

Native Steamworks (`blazium/modules/steam/` class `Steam`). **Not GodotSteam.**
Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Nightly caveat:** `LoginClient` methods that wrap Steam tickets live in
script templates and https://docs.blazium.app — not as C++/xml class docs
in the installed editor. The `Steam` singleton **is** in installed Blazium.
Do not invent LoginClient APIs.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

The library loads at runtime. If missing, methods fail gracefully
(`is_available()`). Publishing depots / steamcmd → growth pack
`blazium-steam-publish`.

## When to use

- Use when requesting a Steam Web API ticket and exchanging it for a JWT.
- Use when unlocking achievements, stats, or inventory/promo items.

**When not to use:** JWT storage / Discord login → `blazium-services`.
GodotSteam community APIs → do not use. SteamPipe / steamcmd →
`blazium-steam-publish`.

## Workflow

1. **Inspect.** `Steam.is_available()`. Confirm app id. Reject GodotSteam
   callables.
2. **Choose.** Ticket → backend JWT for Services; or local Steamworks
   (achievements/stats) without login.
3. **Implement.** `Steam.initialize(app_id)` → `request_web_api_ticket()` →
   `web_api_ticket_ready` → `authenticate_with_server(url, ticket, app_id)` →
   persist JWT via `blazium-services`. Pump `poll_callbacks()`.
4. **Verify.** Ticket path with Steam running. Autowork cannot fake Steamworks
   — use a Steam-logged client or document the gap.
5. **Handoff.** JWT to `blazium-services` / `blazium-lobby`.

## Patterns

### Ticket → JWT

```gdscript
Steam.initialize(app_id)
Steam.web_api_ticket_ready.connect(_on_ticket)
Steam.request_web_api_ticket("blazium")

func _on_ticket(ticket: String) -> void:
	var result: SteamAuthResult = Steam.authenticate_with_server(auth_url, ticket, app_id)
	# persist result JWT in user://blazium.cfg (blazium-services)
```

### Achievements / stats

```gdscript
Steam.request_current_stats()
Steam.set_achievement("FIRST_WIN")
Steam.store_stats()
```

`clear_achievement` / `clear_stat` also need `store_stats()` to persist.
Inventory: `add_promo_item`, `load_item_definitions` as documented on `Steam`.

## Pitfalls

- **Used GodotSteam** → wrong module. Use Blazium `Steam` only.
- **Forgot `store_stats()`** → achievement stays in memory.
- **Taught SteamPipe here** → publish adapter.
- **Invented LoginClient Steam methods** → template + nightly only.

Live Steamworks cases are gated. Defaults use Spacewar AppID `480` via
`steam_appid.txt`. Override `GAME_STEAM_ID` locally — do not invent an App ID.

## Resources

- Tests: https://github.com/blazium-games/steam_module_tests

- Module: `blazium/modules/steam/doc_classes/Steam.xml`
- Classes: `Steam`, `SteamAuthResult`, `SteamAchievementInfo`,
  `SteamInventoryItem`, `SteamItemDefinition`
- JustAMCP: `docs_get_class` for `Steam`

## Related skills

- `blazium-services` — persist / parse JWT
- `blazium-discord` — alternate identity
- `blazium-steam-publish` — depots
