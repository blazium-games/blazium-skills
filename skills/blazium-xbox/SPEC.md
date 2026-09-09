---
name: blazium-xbox
pack: modules
---

# blazium-xbox

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

GDK surface is huge and **disabled by default**. Agents will break builds if they assume it exists.

## What

Guarded Xbox skill: `GDK`, `GDKUser`, `GDKAchievements`, `GDKStore`, `GDKMultiplayerActivity`, `GDKSocial`. Feature-detect first.

**Non-goals:** Do not write tutorials that assume GDK is compiled in. Do not enable it on non-Windows.

## How

- Module: `blazium/modules/xbox_module/` — custom SCons, not default `modules_enabled.gen.h`.
- 30+ classes in code, 3 XML docs today.
- Build flags → feature detect → store/achievements happy path.

## Reasoning

Console skill as enable-and-guard, not a happy-path default.

## Sources

- xbox_module

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-steam` — other store
- `blazium-export` — desktop
