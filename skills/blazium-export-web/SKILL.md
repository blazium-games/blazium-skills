---
name: blazium-export-web
description: >
  Exports Blazium to HTML5 with COOP/COEP, YouTube Playables
  (YoutubePlayablesClient), and Discord Embedded Apps host/Docker webbuild.
  Use for browser, Playables, or *.discordsays.com. Not native Discord SDK.
when-to-use: >
  HTML5 export, COOP COEP, SharedArrayBuffer, YouTube Playables,
  YoutubePlayablesClient, Discord Embedded Apps, discordsays.com
metadata:
  author: blazium-games
  short-description: Web export with COOP/COEP, Playables, and Discord embed host
---

# Blazium export web

Web is where Blazium diverges from a vanilla Godot desktop export. Baseline:
**Blazium 0.6.x (Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

Native Discord Social SDK stays on `blazium-discord`. This skill owns the
**host**: web export, headers, Playables node, Embedded Apps iframe.

Size/shader stripping is text `.gdshader` + export filters only.

## When to use

- Use when exporting HTML5, fixing SharedArrayBuffer / COOP/COEP, or shipping
  YouTube Playables / Discord Embedded Apps.

**When not to use:** desktop/Android player → `blazium-export`. Native
presence/OAuth → `blazium-discord`. Generic preset install → `blazium-cli`.

## Grok host

Read this skill, then `blazium-export` if no web preset exists. Spawn
`tools-programmer` for headers/Docker and `qa-tester` for the load check.
Child prompts must include threads vs no-threads and the host URL. Do not
dump the catalog.

Evidence is export success + `window.crossOriginIsolated` when threads are
on — not a screenshot of the canvas. Grok `code_execution` is not evidence.

## Workflow

1. **Inspect.** Web preset in `export_presets.cfg`. Threads vs no-threads
   template (`blazium-cli templates list … --platform web`).
2. **Choose.** Plain web vs Playables vs Discord embed. Threads need COOP/COEP.
3. **Implement.** Export via `export_tools`. Add host headers. Playables:
   `YoutubePlayablesClient`. Embed: `DiscordEmbeddedAppClient` / `ReactClient`
   + Docker webbuild for `*.discordsays.com`.
4. **Verify.** Load in a browser (or Playables test suite / Discord iframe).
   Confirm `window.crossOriginIsolated` when threads are on.
5. **Handoff.** URL, header requirements, which client node was added.

## Patterns

### COOP/COEP checklist (threads / SharedArrayBuffer)

Serve (or set on the CDN):

- `Cross-Origin-Opener-Policy: same-origin`
- `Cross-Origin-Embedder-Policy: require-corp`

Also: correct MIME for `.wasm` / `.pck`; HTTPS (or localhost). Without these,
threaded web builds fail or silently fall back.

No-threads export if the host cannot set headers.

### YouTube Playables

`YoutubePlayablesClient` (`socialexports`). Official SDK:
developers.google.com/youtube/gaming/playables. Test suite:
developers.google.com/youtube/gaming/playables/test_suite.

Keep payload small. `get_language()` is YouTube locale, not `OS` locale.
Calls outside the Playables shell return empty / error — do not invent extra
SDK methods.

### Discord Embedded Apps host

- Game: `DiscordEmbeddedAppClient` (wait `is_ready`, then authorize).
- Host: web export + Docker webbuild targeting `*.discordsays.com`.
- Native desktop SDK → `blazium-discord`, not this skill.

## Output contract

- Export preset / artifact path
- Threads vs no-threads
- Host headers (COOP/COEP) or `INCONCLUSIVE`
- Client node added (`YoutubePlayablesClient` / `DiscordEmbeddedAppClient` / none)

## Pitfalls

- **Skipped COOP/COEP on a threads build** → SharedArrayBuffer missing.
- **Taught native `Discord.initialize` here** → `blazium-discord`.
- **Copied Godot 4.7 web-only APIs** → pin 4.3.2 export options.

## Resources

- JustAMCP: `export_tools`
- Classes: `YoutubePlayablesClient`, `DiscordEmbeddedAppClient`, `ReactClient`
- Template: `script_templates/DiscordEmbeddedAppClient/`

## Related skills

- `blazium-export` — desktop/mobile presets
- `blazium-discord` — native vs embedded
- `blazium-ci-export` — web artifact in GHA
