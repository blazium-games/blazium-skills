# Verify LoginClient / LobbyClient on nightly

`LoginClient`, `LobbyClient`, `MasterServerClient`, and `ScriptedLobbyClient`
are **script templates** plus https://docs.blazium.app — not C++/xml class
docs in a default installed editor.

## Before calling a method

1. Open `script_templates/LoginClient/default.gd` (and Lobby siblings) in
   the **installed** editor or engine tree.
2. Confirm the method exists on that template (`request_login_info`,
   `received_jwt`, `connect_to_server`, reconnect-token handlers).
3. Check https://docs.blazium.app for the same nightly. If the page and
   the template disagree, **trust the installed template**.
4. `ClassDB.class_exists` may be false for template-only types. Do not
   invent a C++ client.

## Copy only

- `request_login_info("discord")` / Steam ticket path
- `received_jwt`
- `connect_to_server`
- `connected_to_server` / `disconnected_from_server`
- `reconnection_token` in `user://blazium.cfg`

Do not invent extra LoginClient / LobbyClient methods, cloud URLs, or
IAP / ads helpers.
