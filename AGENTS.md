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

# Referring to the author of Risale-i Nur

- In Turkish text, refer to the author as “Bediüzzaman Said Nursi” or “Bediüzzaman hazretleri”, never by the surname alone or as “Said Nursi” alone.
- Use “Bediüzzaman Said Nursi” in the English editions and source credits as well.
- Preserve verbatim historical quotations; apply this convention to authored prose, commentary and source attributions.

# Pinned Risale essay

- Keep risale-i-nur-ilham-vahiy-kainati-okumak.html pinned first ONLY on risale-i-nur-kulliyati-sosyolojisi.html and en/risale-i-nur-kulliyati-sosyolojisi.html when adding new writing. Do not pin it on index.html or en/index.html. Use the dedicated Risale section URLs when sharing its pinned position.
- Introduce it with “Risale-i Nur Külliyatı vahiy mi, ilham mı?” in Turkish and “Is the Risale-i Nur Collection revelation or inspiration?” in English. Preserve its existing article title and URL.

# Separate Risale publication area

- The general homepages index.html and en/index.html may contain only links to their dedicated Risale-i Nur Külliyatı Sosyolojisi page. Do not include Risale article cards, previews, excerpts, summaries or pinned essays on those general homepages.
- List and feature Risale essays only on risale-i-nur-kulliyati-sosyolojisi.html and en/risale-i-nur-kulliyati-sosyolojisi.html. Preserve the existing article URLs.

# Glossary for retained Turkish terms

- When retaining Turkish or Ottoman terms in English Risale essays, provide an English equivalent and a short English explanation through the accessible on-click glossary, including terms in authored prose as well as source excerpts. Maintain the corresponding Turkish glossary support.

# Pinned homepage section links

- Keep the three decorative section links immediately after the complete author biography section (`section#hakkinda`) on both `index.html` and `en/index.html`.
- Preserve this order: `risale-i-nur-sosyolojisi`, `sorularla-islamiyet-projesi`, `cevabul-ahmak-baglantisi`.
- These are links to independent pages. Keep their existing fonts, colors, borders and destinations when adding other homepage content. Do not move them below the books section.
