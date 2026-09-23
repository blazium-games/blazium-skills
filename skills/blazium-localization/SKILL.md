---
name: blazium-localization
description: >
  Sets up Blazium 0.8.x localization with TranslationServer, tr() keys, and
  CSV/PO translation files on Godot 4.8.x. Use when adding locales, wrapping
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

Use `TranslationServer` + translation CSVs / PO. Baseline: **Blazium 0.8.x
(Godot 4.8.x fork, branch `blazium_4.8`)**.

**Version drift:** inspect `config_version` / `features` in `project.blazium`
(or `project.godot`). Keep `blazium_4.8`-safe APIs unless the user asks to migrate.

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

### Batch string pass

Walk player-facing Control text. Each literal becomes one CSV row: key,
source, then one column per locale. Register the CSV in Project Settings.
Autowork `set_locale` on two keys, not one. Large files → `blazium-csv`.

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
