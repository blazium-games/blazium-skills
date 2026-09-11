---
name: blazium-jwt
description: >
  Encodes, decodes, and validates JWTs on Blazium 0.6.x with the in-engine
  jwttool module (JWT, JWTBuilder, DecodedJWT) on Godot 4.3.2. Use for
  HS256/RS256 sign/verify, claims, timing, and JTI revoke. Not LoginClient
  OAuth and not lobby rooms.
when-to-use: >
  JWT, JWTBuilder, DecodedJWT, HS256, RS256, validate_timing, revoke_jti,
  create_jwt, jwttool
metadata:
  author: blazium-games
  short-description: jwttool sign, verify, claims, and JTI revoke
---

# Blazium JWT

In-engine JWT tools. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.
Module: `blazium/modules/jwttool/` — `JWT`, `JWTBuilder`, `DecodedJWT`.

Login / Discord OAuth / Steam ticket exchange → `blazium-services`.
Store tokens in `user://blazium.cfg` — never `res://`.
Pin methods from https://github.com/blazium-games/jwttool_module_tests.

## When to use

- Use when signing, parsing, or validating a JWT in GDScript.
- Use when checking `exp` / `nbf`, claims, or rotating keys.

**When not to use:** `LoginClient` / `received_jwt` → `blazium-services`.
Rooms → `blazium-lobby`.

## Grok host

Read this file only. Spawn `blazium-live-ops-specialist` or
`security-engineer`. Child prompts must include algorithm (HS256/RS256),
secret location (`user://` never `res://`), and claims to assert. Evidence
is Autowork against `jwttool_module_tests` patterns (expired, wrong secret,
missing claim) — not a printed token.

## Workflow

1. **Inspect.** `ClassDB.class_exists("JWT")`. Existing token path.
2. **Choose.** HS256 string secret vs RS256 `CryptoKey`.
3. **Implement.** Sign with `JWTBuilder` or `JWT.create_jwt`. Validate
   before trusting claims.
4. **Verify.** Autowork: expired, wrong secret, missing claim.
5. **Handoff.** Token path. Login flow stays on `blazium-services`.

## Patterns

```gdscript
var obj: DecodedJWT = JWT.parse(token)
assert_false(JWT.is_expired(token))
assert_true(JWT.validate(token, secret))
assert_true(JWT.validate_timing(token))
```

```gdscript
var jwt_str: String = JWTBuilder.new() \
	.set_algorithm("HS256") \
	.set_subject("user_build") \
	.set_issuer("engine") \
	.set_expiration(3600) \
	.sign("build_secret")
```

Also: `JWT.create_jwt_hs256`, `JWT.create_jwt_timed`, `JWT.validate_claims`,
`JWT.validate_any`, `JWT.validate_with_map`, `JWT.validate_diagnostic`.
Revoke: `JWT.revoke_jti(id)` then `JWT.is_revoked(id)`.

## Output contract

- Algorithm used
- Secret location (not the secret)
- Claims asserted
- Autowork expired / wrong-secret result

## Pitfalls

- **Stored JWT in `res://`** → `user://blazium.cfg`.
- **Trusted `JWT.decode` without `validate`** → signature unchecked.
- **Invented LoginClient methods here** → `blazium-services`.
- **Skipped expiry** → `validate_timing` / `is_expired`.

## Related skills

- `blazium-services`, `blazium-lobby`, `blazium-config`
