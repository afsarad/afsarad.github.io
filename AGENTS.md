# Publishing in Turkish and English

The author requires full content parity between Turkish and English editions.

- Treat every request to publish or revise a Turkish page as a request to publish or revise its full English translation in the same change.
- Turkish pages remain at their existing URLs. Their English counterparts use the same relative paths under `en/`. The old `index-english.html` URL redirects to `en/index.html`.
- Translate the complete text, headings, UI, accessible labels, metadata and interactive text. A summary, browser translation button or link to Turkish text does not satisfy this requirement.
- Preserve meanings, dates, uncertainty, references and original media. Keep original bibliographic titles; do not invent English editions of cited sources.
- Add reciprocal language navigation, canonical URLs, hreflang metadata and both URLs to sitemap.xml.
- Update the matching SHA-256 entries in translations.json only after reviewing the two editions. The manifest records checked content; changing hashes alone is not translation.
- Run `python3 scripts/check_translations.py` before publishing. The Pages workflow runs it before deployment and must remain gated by this check.
- Do not add editorial coaching, implementation details or conversation notes to the author's published articles.
