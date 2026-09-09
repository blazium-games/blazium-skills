# Agent invocation (blazium-cli)

First-party contract for Claude, Cursor, and Codex. Written from the Go
binary in `blazium-cli/`. Do not invent verbs or flags.

## Flags that exist

| Flag | Role |
|------|------|
| `--json` | Persistent. JSON on stdout; implies `--quiet`. Shorthand for `--format json`. |
| `--format human\|json\|tsv` | Persistent. `--json` wins if both are set. |
| `--quiet` | Persistent. Suppress warnings. |
| `--dry-run` | **Only** on `upgrade` and `update apply`. Not a global flag. |

Every input is a flag or argument. Do not wait for an interactive menu.

## Discover incrementally

```text
blazium-cli --help
blazium-cli install --help
blazium-cli templates list --help
blazium-cli update apply --help
```

Do not dump this catalog into a tool call. Prefer `--json` for agents.

## Proven examples

```text
blazium-cli install 0.6.714 --json
blazium-cli install nightly --templates --json
blazium-cli templates list nightly --platform web --format json
blazium-cli templates download nightly --tpz --json
blazium-cli templates download 0.6.748 --platform android --json
blazium-cli templates download nightly --runtime --variant release --json
blazium-cli update check --product editor --json
blazium-cli update apply --product cli --dry-run --json
blazium-cli upgrade --dry-run --json
blazium-cli hub-remote ensure --json
```

`hub-remote ensure` never rotates a valid token. `install` / `templates
download` are safe to retry (already-installed is success).

## Do not invent

- `blazium-cli hub install`
- `update apply --product editor` or `--product templates`
- Global `--dry-run` on `install` / `open` / `remote`

On missing required args, the binary exits immediately. Re-run with the
example from `--help`, not a prompt.
