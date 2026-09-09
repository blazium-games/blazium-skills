---
name: blazium-itch-publish
pack: growth
---

# blazium-itch-publish

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Butler + CI is a known workflow; pin Blazium export output.

## What

`butler push` of `blazium-export` / `blazium-export-web` artifacts.

**Non-goals:** Do not invent a Blazium-only store on itch.

## How

Build first. Then `butler push user/game:channel`. CI → `blazium-ci-export`.

## Reasoning

Publish adapter.

## Sources

- `blazium-export`
- `blazium-ci-export`

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-export` — builds
- `blazium-ci-export` — GHA
