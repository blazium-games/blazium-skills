---
name: blazium-specialty-export
description: >
  Exports Blazium novelty targets: LiveWallpaper, Screensaver (.scr), USB
  autorun.inf, and InterDVD happy-path bake. Use when the product is not a
  normal player. Compiler install stays on blazium-toolchain.
---

# Blazium specialty export

Windows novelty + Interactive DVD. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Ship a **normal player** with `blazium-export` unless the user asked for one
of these targets. PS1/PS2/N64 compiler install → `blazium-toolchain`.

InterDVD has **19 classes**. This skill covers the happy path only, then
hands off to engine docs.

## When to use

- Use when exporting a live wallpaper, `.scr` screensaver, USB/disc
  `autorun.inf`, or an InterDVD VIDEO_TS bake.

**When not to use:** desktop/mobile/web store builds → `blazium-export` /
`blazium-export-web`. `blazium-toolchain ps1|ps2|n64 setup` → toolchain.
Deep InterDVD IFO/PGC authoring beyond bake → class docs, not this file.

## Workflow

1. **Inspect.** Which target? Module compiled? `ClassDB.class_exists`.
2. **Choose.** One novelty platform. Do not stack wallpaper + .scr + DVD.
3. **Implement.** Enable the matching project setting / export platform.
   InterDVD: scene tree → bake → toolchain ffmpeg/iso.
4. **Verify.** Launch with the real host switches (`/s`, WorkerW, USB
   insert, or a DVD player / ISO). Not a screenshot alone.
5. **Handoff.** Artifact path. Compilers → toolchain.

## Patterns

### Per-target

| Target | Classes / setting | Notes |
|--------|-------------------|--------|
| Live wallpaper | `LiveWallpaper`, `EditorExportPlatformWindowsLiveWallpaper`; `blazium/livewallpaper/enabled` | WorkerW parent. Preview: `--livewallpaper-preview` or `/p`. Quit: `--livewallpaper-quit`. `get_mode()` / `is_attached()` / `get_workerw()` / `request_exit()`. Modes: `MODE_DISABLED`, `MODE_RUN`, `MODE_PREVIEW`, `MODE_QUIT`. Disabled runtime: `get_workerw() == 0`. |
| Screensaver | `Screensaver`, `EditorExportPlatformWindowsScreensaver`; `blazium/screensaver/enabled` | Windows `/s` `/p` `/c` `/a`. `application/run/main_scene` is the animation — **not** `unlock_scene`. Password: `has_password()`, `set_password(old, new)`, `verify_password()`, `clear_password()`, `set_password_enabled()`, `is_password_enabled()`. Hash is per-user, never plaintext in the PCK. |
| USB / disc autorun | `AutorunInf`, `EditorExportDeviceAutorun` | Properties: `open`, `icon`, `action`, `label`, `shell`, `shell_verbs`; `build()`, `AutorunInf.usb_note_text()`. Preset keys: `autorun/enable`, `autorun/icon`, `autorun/action`, `autorun/shell`, `autorun/shell_verbs`, `autorun/write_usb_note`. Empty fields omitted from `build()`. Win7+ USB **ignores** `OPEN=` / `ACTION=`. |
| InterDVD | `InterDVDDisc`, `InterDVDProject`, `InterDVDSceneBaker` | Prefer a Disc scene; export calls `InterDVDDisc.build_project`. Bake: `InterDVDSceneBaker.bake_cell` → `blazium-toolchain interdvd ffmpeg`. Then `interdvd iso`. Tests also register `InterDVDStream`, `InterDVDCell`, `InterDVDInstruction`, `InterDVDMachine`, `InterDVDPGC`, `InterDVDMenu`, `InterDVDButton`, `InterDVDExportProgress`, `InterDVDIfoWriter`, `EditorExportPlatformWindowsInterDVD`. Happy path only — do not invent IFO authoring. |

### InterDVD happy path

1. Author an `InterDVDDisc` tree (or `blazium/inter_dvd/project` `.tres`).
2. Bake cells (720×480 NTSC). Packed `Node3D` on dummy/headless →
   `ERR_UNAVAILABLE`.
3. Mux / ISO via toolchain (`interdvd iso --dir … --out …`).
4. Stop. Title-set / IFO / hotspot details →
   `blazium/modules/inter_dvd/doc_classes/`.

## Pitfalls

- **Used this for a Steam/desktop player** → `blazium-export`.
- **Vendored compilers here** → `blazium-toolchain`.
- **Set main_scene to unlock_scene** → unlock is only for `/s` dismiss.
- **Assumed USB AutoRun still opens EXE** → policy ignores OPEN/ACTION.

## Resources

- Tests: https://github.com/blazium-games/livewallpaper_module_tests
- Tests: https://github.com/blazium-games/screensaver_module_tests
- Tests: https://github.com/blazium-games/device_autorun_module_tests
- Tests: https://github.com/blazium-games/inter_dvd_module_tests

- Gates: `BLAZIUM_EXE` + flavored `BLAZIUM_TEMPLATE`; `validate_all.ps1`
- Modules: `livewallpaper`, `screensaver`, `device_autorun`, `inter_dvd`
- Toolchain ffmpeg/iso: `blazium-toolchain`

## Related skills

- `blazium-export` — normal players
- `blazium-toolchain` — compilers + InterDVD ISO
- `blazium-export-web` — browser hosts
