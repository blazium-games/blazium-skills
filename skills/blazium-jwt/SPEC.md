---
name: blazium-jwt
pack: live-ops
---

# blazium-jwt

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

## Why

`jwttool` is a full sign/verify/revoke API. Folding it into login hides the proven methods.

## What

`JWT`, `JWTBuilder`, `DecodedJWT`: create/validate HS256/RS256, claims, timing, kid maps, JTI revoke.

**Non-goals:** `LoginClient` OAuth (`blazium-services`). Lobby rooms.

## How

- Module: `blazium/modules/jwttool/`
- Tests: https://github.com/blazium-games/jwttool_module_tests `tests/test_jwt.gd`
- Canonical Autowork: unit `--aw-dir=` self-starts; mixed suffixes still use `-s run_tests.gd`

## Reasoning

Identity login vs local JWT crypto are different jobs.

## Sources

- https://github.com/blazium-games/jwttool_module_tests
- `blazium/modules/jwttool/`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-services` — login
- `blazium-lobby` — rooms
