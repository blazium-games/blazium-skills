---
name: blazium-toolchain
description: >
  Uses the GPL blazium-toolchain sidecar (ps1/ps2/n64/interdvd setup, build,
  run, iso, export-guest). Use when compiling retro or Interactive DVD
  products. Do not use for Windows wallpaper (blazium-specialty-export) or
  installing the editor (blazium-cli).
---

# Blazium toolchain

Retro compilers are a **separate GPL binary**. The editor only spawns it.
Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not vendor GPL sources
into the engine or this skill pack.

Install the sidecar: `blazium-cli update apply --product toolchain`.
Config: `.blazium-toolchain.yml` or `blazium-toolchain.yml` (or
`--settings` / `$BLAZIUM_TOOLCHAIN_SETTINGS`). Dump resolved:
`blazium-toolchain settings`.

`ps3` and `ps4` are reserved and exit `2`. `n64` has **no ISO** — product is
a big-endian `.z64`. `n64 iso` is rejected; use `n64 rom`.

Verb catalog: [references/verbs.md](references/verbs.md).

## When to use

- Use when setting up or building PS1 / PS2 / N64 / InterDVD via the CLI.
- Use when the editor reports a missing `blazium-toolchain` binary.

**When not to use:** InterDVD scene/menu authoring →
`blazium-specialty-export`. Normal players → `blazium-export`.
Installing the Blazium editor itself → `blazium-cli`.

## Workflow

1. **Inspect.** Binary on PATH? `blazium-toolchain version`.
2. **Choose.** Target + profile (`compile` | `dev` | `iso` / `rom`).
3. **Implement.** `setup` then `build` / `run` / `iso` / `export-guest`.
4. **Verify.** Artifact path from stdout (`wrote …`) and a `run` smoke if
   emulators are configured.
5. **Handoff.** Prefix cache dir + artifact. Authoring → specialty-export.

## Patterns

```text
blazium-toolchain [--json] [--prefix DIR] version
blazium-toolchain export-guest …
blazium-toolchain n64 rom …
blazium-toolchain ps2 elf-info FILE.elf
blazium-toolchain ps2 chd …
blazium-toolchain ps1 fmv …
blazium-toolchain interdvd ffmpeg|ffprobe …
blazium-toolchain interdvd meta init --out disc.interdvd.json
blazium-toolchain interdvd meta validate …
```

The MIT editor process spawns this binary. Do not reimplement cooks in GDScript.

## Pitfalls

- **Vendored GPL into the engine repo** → sidecar only.
- **`n64 iso`** → rejected; ship `.z64` via `n64 rom`.
- **`ps3` / `ps4`** → exit 2; not implemented.
- **Taught InterDVD Control nodes here** → `blazium-specialty-export`.

## Resources

- https://github.com/blazium-games/blazium-toolchain
- [references/verbs.md](references/verbs.md)

## Related skills

- `blazium-specialty-export` — InterDVD nodes + Windows novelty
- `blazium-cli` — install / update products
- `blazium-export` — normal players
