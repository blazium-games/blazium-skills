---
name: blazium-itch-publish
pack: growth
---

# blazium-itch-publish

Engine baseline: **Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`)**. Use APIs that exist on `blazium_4.8`.

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

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.8.x (Godot 4.8.x fork, branch `blazium_4.8`). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-export` — builds
- `blazium-ci-export` — GHA
