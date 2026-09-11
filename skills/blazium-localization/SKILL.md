---
name: blazium-localization
description: >
  Sets up Blazium 0.6.x localization with TranslationServer, tr() keys, and
  CSV/PO translation files on Godot 4.3.2. Use when adding locales, wrapping
  UI strings, or switching locale in play mode. Large CSV pipelines pair with
  blazium-csv. Not Theme/layout and not raw table queries.
when-to-use: >
  TranslationServer, tr(), locale, CSV translations, PO file, set_locale,
  MENU_START key, localization
metadata:
  author: blazium-games
  short-description: TranslationServer, tr() keys, and CSV/PO locales
---

# Blazium localization

Use `TranslationServer` + translation CSVs / PO. Baseline: **Blazium 0.6.x
(Godot 4.3.2 fork)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep 4.3.2-safe APIs unless the user asks to migrate.

## When to use

- Use when adding locales, `tr()`, or locale-specific assets.

**When not to use:** Theme/layout → `blazium-ui`. Raw CSV query engine →
`blazium-csv` for huge tables.

## Grok host

Read this file only. Spawn `ui-programmer` for `tr()` wraps and `qa-tester`
for locale asserts. Child prompts must include locale codes and translation
file paths. Evidence is Autowork `assert_eq(tr("KEY"), expected)` after
`set_locale` — not a screenshot of the English HUD.

## Workflow

1. **Inspect.** Existing `translations` in project settings.
2. **Add** CSV/PO; register in Project Settings.
3. **Wrap** UI with `tr("KEY")` — not concatenated sentences.
4. **Verify.** `TranslationServer.set_locale` then Autowork
   `assert_eq(tr("KEY"), expected)`.
5. **Handoff.** Locale codes + translation file paths.

## Patterns

```gdscript
TranslationServer.set_locale("es")
label.text = tr("MENU_START")
```

Keys are stable IDs. Whole sentences in one key so translators can reorder.

## Output contract

- Locale codes enabled
- Translation file paths
- Keys wrapped with `tr()`
- Autowork `set_locale` + `tr()` assert

## Pitfalls

- **Hardcoded English in Controls** → wrap every player-facing string.
- **Invented Unity Localization table C#** → TranslationServer + CSV/PO.
- **Split sentences for concat** → one `tr()` per sentence.
- **CSV not registered in Project Settings** → `tr()` returns the key.

## Related skills

- `blazium-ui`, `blazium-csv`, `blazium-audio`, `blazium-autowork`
