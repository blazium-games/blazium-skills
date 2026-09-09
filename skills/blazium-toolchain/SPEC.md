---
name: blazium-toolchain
pack: ship
---

# blazium-toolchain

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

PS1/PS2/N64/Interactive DVD compilers are a GPL sidecar Godot does not have.

## What

`blazium-toolchain` CLI: setup/build/run/iso/`export-guest`. N64: `rom` (no ISO). PS2: `elf-info` / `chd`. PS1: `fmv`. InterDVD: `ffmpeg` / `ffprobe` / `meta init` / `meta validate`.

**Non-goals:** Do not vendor GPL sources into the engine skill. Do not teach InterDVD node authoring in depth (specialty-export + inter_dvd).

## How

- Repo: `blazium-toolchain/`. Config: `.blazium-toolchain.yml`.
- CLI: `ps1|ps2|n64|interdvd setup/build/run` plus [references/verbs.md](references/verbs.md).
- `blazium-cli update apply --product toolchain`.

## Reasoning

Retro is a Blazium differentiator and a separate binary.

## Sources

- https://github.com/blazium-games/blazium-toolchain

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-specialty-export` — InterDVD + Windows novelty exports
- `blazium-cli` — install toolchain
