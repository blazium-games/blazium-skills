# blazium-toolchain verbs

From `blazium-toolchain/internal/app/app.go`. GPL sidecar. Editor only spawns the binary.

## Global

```text
blazium-toolchain [--json] [--prefix DIR] version
blazium-toolchain [--json] list
blazium-toolchain settings
blazium-toolchain [--prefix DIR] ps1|ps2|n64|interdvd setup [--offline]
blazium-toolchain [--prefix DIR] ps1|ps2|n64|interdvd env|status
```

`ps3` and `ps4` are reserved and exit `2`.

## Per-target extras

| Target | Extra verbs |
|--------|-------------|
| any guest | `build`, `run`, `export-guest` |
| ps1 / ps2 / interdvd | `iso` |
| n64 | `rom` (no `iso` — product is big-endian `.z64`) |
| ps2 | `elf-info`, `chd` |
| ps1 | `fmv` |
| interdvd | `ffmpeg`, `ffprobe`, `meta init`, `meta validate` |

```text
blazium-toolchain [--prefix DIR] ps1 build --out FILE [--src DIR | --sample template|gte]
blazium-toolchain [--prefix DIR] ps1 run [--iso CUE] GAME.EXE
blazium-toolchain [--prefix DIR] ps1 iso --xml FILE [--out PATH]
blazium-toolchain [--prefix DIR] ps2 build --out FILE.elf
blazium-toolchain [--prefix DIR] ps2 iso --dir TREE --out FILE.iso
blazium-toolchain [--prefix DIR] ps2 elf-info FILE.elf
blazium-toolchain [--prefix DIR] n64 build --out FILE.z64
blazium-toolchain [--prefix DIR] n64 rom …
blazium-toolchain [--prefix DIR] n64 run [--emu ares|project64|both] GAME.z64
blazium-toolchain interdvd iso --dir DIR --out FILE
blazium-toolchain interdvd ffmpeg|ffprobe …
blazium-toolchain interdvd meta init --out disc.interdvd.json
blazium-toolchain interdvd meta validate …
```

Install the binary: `blazium-cli update apply --product toolchain`.
Settings: `.blazium-toolchain.yml` or `blazium-toolchain.yml` (or `--settings` / `$BLAZIUM_TOOLCHAIN_SETTINGS`). Dump resolved: `blazium-toolchain settings`.
