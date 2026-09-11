---
name: blazium-audio
description: >
  Routes Blazium audio (AudioStreamPlayer, buses, ducking) on 0.6.x / Godot
  4.3.2. Use when adding SFX/music or mixer-style routing. Prefer JustAMCP
  audio_tools. Not interactive_music internals.
when-to-use: >
  AudioStreamPlayer, audio bus, linear_to_db, add_audio_bus, ducking, SFX
metadata:
  author: blazium-games
  short-description: Audio players, buses, and mixer routing
---

# Blazium audio

Volume is in dB. Baseline: **Blazium 0.6.x (Godot 4.3.2 fork)**. JustAMCP:
`get_audio_bus_layout`, `add_audio_bus`, `add_audio_player`.

**Version drift:** inspect `config_version` / `features` in `project.blazium` (or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding players, buses, or music/SFX split.

**When not to use:** interactive_music module internals (vanilla — skip).
Localization of voice lines → `blazium-localization`.

## Grok host

Load this file plus at most one pin (`blazium-ui` for volume sliders).
Spawn `audio-director` for bus layout and `sound-designer` for event lists.
Child prompts must include bus names (Master / Music / SFX) and player paths.
Do not dump the catalog.

Grok `code_execution` is not mixer evidence. Quote `get_audio_bus_layout`,
Autowork `assert_eq` on `bus`, play-mode MCP, or `INCONCLUSIVE`.

## Workflow

1. **Inspect.** Bus layout via `get_audio_bus_layout` (Master / Music / SFX).
2. **Route** players to buses; set dB, not 0–1 linear as “percent” without
   `linear_to_db`.
3. **Verify.** `get_audio_bus_layout` shows Music/SFX. Play mode: player has a
   stream and is routed off Master. Autowork `assert_eq` on `bus`. Not a
   screenshot of the mixer.
4. **Handoff.** Bus names + player paths.

## Patterns

Music and SFX on separate buses; duck music on dialogue.
`AudioStreamPlayer` (2D/3D variants for spatial).

```gdscript
extends AudioStreamPlayer

func _ready() -> void:
	bus = "SFX"
	volume_db = linear_to_db(0.5)
```

JustAMCP: `add_audio_bus` then `add_audio_player` onto that bus.

## Output contract

- Bus names (Master / Music / SFX)
- Player paths and assigned streams
- Evidence: `get_audio_bus_layout`, Autowork bus assert, play-mode MCP, or `INCONCLUSIVE`
- Next skill (`blazium-ui`, `blazium-localization`)

## Pitfalls

- **Linear 0.5 as “half volume”** → use `linear_to_db`.
- **Everything on Master** → cannot mute SFX independently. Add an SFX bus.
- **Polyphony explosion** → limit simultaneous players.
- **Player with no stream** → silence. Assign an AudioStream before play.

## Resources

- JustAMCP: `audio_tools`

## Related skills

- `blazium-ui` — volume sliders
- `blazium-localization` — voiced lines
- `blazium-autowork` — bus asserts
