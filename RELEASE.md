The Math 2.0 Handbook, edition 0.3.1: the first four areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.3.1 (`dff5d8ee7db135a5ff5721b52c0982b49785be8a`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Worked examples | Pages |
|---|---|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 398 | 1,176 |
| 2 | Mathematical logic | 28 | 493 | 876 | 2,515 |
| 3 | Linear algebra | 21 | 397 | 483 | 1,488 |
| 4 | Model theory | 27 | 86 | 125 | 436 |
| | **All** | **90** | **1,156** | **1,882** | **5,615** |

- **Volume 4, Model theory**, now has 86 entries (42 in 0.3.0) and learner pages for chapters 4.1 to 4.7. New in
  this edition: types and saturated models (types and the Stone space of types, realizing and omitting types,
  isolated types, algebraic and definable closure, saturated, homogeneous, universal, special and recursively
  saturated models, the monster model, rigid structures, types as orbits); countable models and categoricity
  (categorical theories and the Łoś–Vaught test, atomic and prime models, small theories, the Ryll-Nardzewski
  theorem, Vaught's never-two theorem, Ehrenfeucht's theory with three countable models, the Vaught conjecture and
  Morley's theorem on the number of countable models); and Fraïssé theory and homogeneous structures (ages,
  amalgamation and Fraïssé limits, the Rado and Henson graphs, the Lachlan–Woodrow theorem, Hrushovski's extension
  property, the small index property, Ramsey classes and the Kechris–Pestov–Todorcevic correspondence, Hrushovski
  amalgamation). 73 new exercises. The introduction of the volume is revised, and its first course now runs
  through Chapter 4.6. Chapters 4.8 to 4.27 still have an opening each.
- **Volume 2, Mathematical logic**, has the same learner pages as in 0.3.0; it is built again because its entries
  now refer to new entries of Chapters 4.5 to 4.7 (saturated model, categorical theory, the Łoś–Vaught test, dense
  linear orders, the amalgamation property), and it prints the corrections of
  [tamnd/math2#408](https://github.com/tamnd/math2/pull/408) to its entries (the modalities of S5, the history of
  dynamic logic, links to the Buchholz hydra).
- **Volume 3, Linear algebra**, has the same learner pages as in 0.2.0; it is built again for the corrections of
  [tamnd/math2#408](https://github.com/tamnd/math2/pull/408) to its entries (the Desnanot–Jacobi identity, the
  Cayley–Hamilton theorem and others).
- **Volume 1, Reasoning and proof**, has the same text as in 0.3.0, and its files are those of 0.3.0 under the new
  names, so its cover, title page and copyright page say edition 0.3.0.
- **Entries** are the pages of each sub-area's reading order on the site, numbered (4.6.8), each with its summary,
  a box of facts, motivation, notation, remarks, and three explanations at rising levels. The worked examples and
  counterexamples of an entry follow it in boxes, and each entry ends with its sources.
- **Learner pages** around the entries: a volume introduction with a first-course path, and for each chapter an
  opening, groups with short introductions, a summary with tables, 19 to 28 exercises in three bands (◦ check,
  • practice, ★ challenge) with hints, and notes on history and further reading.
- **Apparatus**: a bibliography of the works the entries cite, and an index of entries, other names, and the pages
  of other areas that the entries use, with links to the site.
- **Builder**: the character ᗮ, which Mathlib uses for the orthogonal complement (`Uᗮ`), is in no font of the
  book; the PDF now prints it as a raised ⊥.
- **Corrections**: seven statements found in seven entries while writing (four missing the hypothesis of a
  countable signature or an uncountable cardinal, among others) were corrected on the site after v0.3.1
  ([tamnd/math2#412](https://github.com/tamnd/math2/pull/412)); this edition prints the entries of v0.3.1. The
  corrections of [tamnd/math2#410](https://github.com/tamnd/math2/pull/410), from the writing of edition 0.3.0, are
  not yet in a release of the site.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
