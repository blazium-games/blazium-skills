---
name: blazium-jwt
description: >
  Encodes, decodes, and validates JWTs with the in-engine jwttool module
  (JWT, JWTBuilder, DecodedJWT). Use for HS256/RS256 sign/verify, claims,
  timing, and JTI revoke. Not LoginClient OAuth and not lobby rooms.
---

# Blazium JWT

In-engine JWT tools. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

Module: `blazium/modules/jwttool/` — `JWT`, `JWTBuilder`, `DecodedJWT`.

Login / Discord OAuth / Steam ticket exchange → `blazium-services`.
Store tokens in `user://blazium.cfg` — never `res://`.

Do not invent APIs. Pin methods from
https://github.com/blazium-games/jwttool_module_tests (`tests/test_jwt.gd`).

## When to use

- Use when signing, parsing, or validating a JWT in GDScript.
- Use when checking `exp` / `nbf`, claims, or rotating keys.

**When not to use:** `LoginClient` / `received_jwt` templates →
`blazium-services`. Rooms → `blazium-lobby`.

## Workflow

1. **Inspect.** `ClassDB.class_exists("JWT")`. Existing token path.
2. **Choose.** HS256 string secret vs RS256 `CryptoKey`. Builder vs raw
   `create_jwt`.
3. **Implement.** Sign with `JWTBuilder` or `JWT.create_jwt`. Validate
   before trusting claims.
4. **Verify.** Autowork against `jwttool_module_tests` patterns — expired,
   wrong secret, missing claim.
5. **Handoff.** Token path. Login flow stays on `blazium-services`.

## Patterns

### Parse

```gdscript
var header: Dictionary = JWT.get_header(token)
var payload: Dictionary = JWT.get_payload(token)
var decoded: Dictionary = JWT.decode(token)  # header / payload / signature
var obj: DecodedJWT = JWT.parse(token)
print(obj.get_subject(), obj.get_issuer(), obj.get_claim_as_string("role"))
assert_false(JWT.is_expired(token))
```

`DecodedJWT`: `get_algorithm`, `get_claim`, `has_claim`, `is_expired`,
`get_issuer`, `get_subject`, `get_audience`, `get_jwt_id`,
`get_expiration_time`, `get_issued_at`, `get_not_before`,
`get_claim_as_string` / `_int` / `_bool` / `_array` / `_dictionary`,
`has_header_claim`, `get_header_claim_as_string`.

### Sign

```gdscript
var jwt_str: String = JWTBuilder.new() \
	.set_algorithm("HS256") \
	.set_subject("user_build") \
	.set_issuer("engine") \
	.set_audience("clients") \
	.set_jwt_id("session_982") \
	.add_claim("role", "admin") \
	.set_expiration(3600) \
	.sign("build_secret")
# or
var hs: String = JWT.create_jwt_hs256({"alg": "HS256", "typ": "JWT"}, payload, secret)
var timed: String = JWT.create_jwt_timed(header, payload, secret, 3600)
```

`JWT.create_jwt(header, payload, secret_or_key)` picks HS256 vs RS256 from
`header.alg`. RS256 takes a `CryptoKey` from `Crypto.generate_rsa(2048)`.

### Validate

```gdscript
assert_true(JWT.validate(jwt_str, secret))
assert_true(JWT.validate_signature_hs256(jwt_str, secret))
assert_true(JWT.validate_timing(jwt_str))          # optional leeway seconds
assert_true(JWT.validate_timing(jwt_str, 15.0))
assert_true(JWT.validate_claims(jwt_str, {"sub": "123", "iss": "master"}))
assert_true(JWT.validate_header_claims(jwt_str, {"alg": "HS256"}))
assert_true(JWT.validate_any(jwt_str, ["bad", "build_secret"]))
assert_true(JWT.validate_with_map(jwt_str, {"key_b_id": "key_b"}))  # uses kid
var diag: Dictionary = JWT.validate_diagnostic(jwt_str, secret)
# diag.valid, diag.error
```

Also: `has_claim`, `get_claim`, `get_algorithm`, `get_kid`,
`get_signature`, `base64url_encode` / `base64url_decode` (no padding),
`validate_claims_diagnostic`.

### Revoke JTI

```gdscript
JWT.revoke_jti("session_982")
assert_true(JWT.is_revoked("session_982"))
assert_false(JWT.validate(jwt_str, "sec"))
JWT.clear_revoked()
```

## Pitfalls

- **Stored JWT in `res://`** → `user://blazium.cfg`.
- **Trusted `JWT.decode` without `validate`** → signature unchecked.
- **Invented LoginClient methods here** → `blazium-services`.
- **Skipped expiry** → `validate_timing` / `is_expired`.

## Resources

- Tests: https://github.com/blazium-games/jwttool_module_tests
- `blazium/modules/jwttool/`

## Related skills

- `blazium-services` — login templates / OAuth
- `blazium-lobby` — rooms after a valid JWT
- `blazium-config` — secrets in `user://`
