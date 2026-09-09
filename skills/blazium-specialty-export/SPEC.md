---
name: blazium-specialty-export
pack: ship
---

# blazium-specialty-export

Engine baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. Do not apply Godot 4.7-only APIs.

## Why

Live wallpaper, screensaver, USB autorun, and Interactive DVD are Blazium-only export targets.

## What

`LiveWallpaper`, `Screensaver`, `AutorunInf`, InterDVD (`InterDVDDisc`, `InterDVDProject`, `InterDVDSceneBaker`).

**Non-goals:** Do not own PS1/PS2/N64 compiler install (toolchain).

## How

- Modules: livewallpaper, screensaver, device_autorun, inter_dvd (19 classes).
- InterDVD authoring is large — skill should route heavy authoring to engine docs after a happy-path bake.

## Reasoning

One 'novelty + DVD' export skill so ship pack stays navigable.

## Sources

- blazium/modules/{livewallpaper,screensaver,device_autorun,inter_dvd}/

## Limits

Do not invent classes, flags, or CLI verbs. Pin Blazium 0.6.x (Godot 4.3.2 fork). Prefer JustAMCP, Autowork, or `blazium-cli` over unverified editor clicks.

## Related skills

- `blazium-toolchain` — DVD/console compilers
- `blazium-export` — normal players
