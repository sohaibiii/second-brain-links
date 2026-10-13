# second-brain-links

The pages Second Brain's App Store listing points at, hosted with GitHub Pages at
https://sohaibiii.github.io/second-brain-links/

| Page | URL | App Store Connect field |
|---|---|---|
| Support | https://sohaibiii.github.io/second-brain-links/ | Support URL |
| About | https://sohaibiii.github.io/second-brain-links/about/ | Marketing URL |
| Privacy Policy | https://sohaibiii.github.io/second-brain-links/privacy/ | Privacy Policy URL (App Privacy) |
| Terms of Use (EULA) | https://sohaibiii.github.io/second-brain-links/terms/ | Linked from the app description and the paywall; optional custom EULA |
| Delete your data | https://sohaibiii.github.io/second-brain-links/delete-data/ | Linked from Privacy and Support; account-deletion help |

## Languages

Every page exists in the **eight languages Second Brain ships in**. A row of tabs under the
navigation switches between them without leaving the page you are on. English lives at the root and
each other language under its own code, so `/de/privacy/` is the German privacy policy:

`en` · `/de` · `/es` · `/fr` · `/ja` · `/ko` · `/pt-BR` · `/zh-Hans`

The App Store fields above should point at the **English** URLs. Apple shows the listing in
the reader's own language, and the tabs let them carry that through to these pages. A hard-coded
`/de/` URL would trap an English reader in German. Translated Privacy and Terms pages say that the
English version applies if a translation differs.

Each page declares `hreflang` alternates for all eight plus `x-default`, and `sitemap.xml` repeats
them, so search engines see one page in eight languages rather than eight competing pages.

Wording that names a screen in the app, such as <kbd>Settings</kbd> → <kbd>Cloud sync and AI choices</kbd> →
<kbd>Delete account and library</kbd>, is the `k.*` keys in each words file. Those are copied from the
app's own catalogue (`SecondBrain/Localizable.xcstrings` in the app repo), so a page never tells
somebody to tap a button whose label is written differently on their screen. If the app renames a
label, update the `k.*` value in every language.

## What the pages say, and where it comes from

The privacy policy, terms and data page describe what the app and its Cloudflare Worker actually do,
as of the date at the top of each page. That covers on-device AI first, Luna via our server only
with consent, the iCloud private database, Sign in with Apple with no name or email, App Attest, the
24-hour AI result window and the content-free deletion marker. The sources are the app's
`SettingsView.swift` → *Your privacy* screen, `Backend/src`, and `docs/` in the app repo. **When
the app's data handling changes, change these pages in the same release.**

## Editing

`_src/gen.py` owns the markup and styling. `_src/words/<lang>.py` owns the words. English is the
fallback behind all seven others, so a key that has not been translated yet renders as English,
never as an identifier.

```
python3 _src/check.py     # the eight catalogues agree
python3 _src/gen.py       # rewrite every page
```

Run **both**, and commit the regenerated HTML alongside the source. `check.py` holds every
catalogue to the same key set, the same `{placeholders}`, the same link targets and balanced tags,
and checks that "Second Brain" is spelled as the app spells it. A translation that quietly drops
a link is a defect nobody reading only English would ever see.

To change the effective date, edit `ui.date` in every words file. To add a language, add it to
`LANGUAGES` and `NATIVE_NAME` in `_src/gen.py`, add `_src/words/<code>.py` (underscores for a
hyphen: `pt_BR.py`), translate, then run the two commands above. Keep the list and its order in
step with `AppLanguage` in the app.

The colours, radii and type follow the app's own tokens (`SecondBrain/DesignSystem/BrainTheme.swift`):
warm paper with a faint notebook grid, white cards, #056BFF blue, and the sky-blue brain mascot.
Light and dark both follow the reader's system setting. The pages load nothing from anywhere else:
no web fonts, scripts or analytics.

Once Second Brain is live on the App Store, set `APP_STORE_URL` at the top of `_src/gen.py`
(the app's Apple ID is 6821703799) and regenerate. Every "Coming soon" label then becomes a
"Download on the App Store" link.

## Hosting

GitHub Pages serves the `main` branch from the repository root. `.nojekyll` turns off Jekyll so
`_src/` is published as-is and nothing is rewritten. `_src/` is public but harmless: it's the
source of these pages, with no keys or private data. `404.html` is served for any missing path.
