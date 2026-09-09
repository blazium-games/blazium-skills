# Verify LobbyClient on nightly

Same rule as `blazium-services`: `LobbyClient` / `ScriptedLobbyClient` /
`MasterServerClient` are **templates** + https://docs.blazium.app.

## Before calling a method

1. Open `script_templates/LobbyClient/default.gd` and
   `script_templates/ScriptedLobbyClient/default.gd` in the installed tree.
2. Copy only methods that file actually defines.
3. Verify names on https://docs.blazium.app for this nightly. Template
   wins if they drift.
4. Persist `reconnection_token` under the matching ConfigFile section
   (`LobbyClient` vs `ScriptedLobbyClient`).

Do not invent room RPCs, WebRTC setup (that is `blazium-enet-webrtc`), or
`@rpc` spawners (`blazium-multiplayer-core`).
