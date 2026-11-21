The Math 2.0 Handbook, edition 0.3.0: the first four areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.3.0 (`07dd7dababb4edd76ea78220bd3ce8ade0bfe095`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Worked examples | Pages |
|---|---|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 398 | 1,176 |
| 2 | Mathematical logic | 28 | 493 | 876 | 2,515 |
| 3 | Linear algebra | 21 | 397 | 483 | 1,488 |
| 4 | Model theory | 27 | 42 | 66 | 260 |
| | **All** | **90** | **1,112** | **1,823** | **5,439** |

- **Volume 2, Mathematical logic**, is complete: all 28 chapters have entries and learner pages, 493 entries in
  all (392 in 0.2.0). New in this edition: many-valued and fuzzy logics (the three-valued logics of Łukasiewicz
  and Kleene, first-degree entailment, Post's logics, Łukasiewicz infinite-valued logic with Chang's completeness
  theorem and McNaughton's theorem, t-norms, BL, MTL, product and Gödel logics); substructural, linear and
  relevance logics (the Lambek calculus, linear logic with proof nets, phase semantics and coherence spaces,
  Routley–Meyer semantics, Urquhart's undecidability theorem); paraconsistent, free, non-monotonic and other
  non-classical logics (explosion, the logic of paradox, da Costa's systems, free and partial logics, default
  logic and preferential consequence, quantum and computability logics); algebraic logic (Lindenbaum–Tarski
  algebras, modal and interior algebras, MV- and BL-algebras, cylindric and relation algebras, algebraizable
  logics and the Leibniz hierarchy); and truth and the semantic paradoxes (the liar and its relatives, Tarski's
  conception of truth, Kripke's theory of truth, revision theory, axiomatic theories of truth and McGee's
  theorem). 131 new exercises. The introduction of the volume is revised for the complete volume, with a reading
  path into non-classical logics and truth.
- **Volume 4, Model theory**, new, with chapters 4.1 to 4.4 written: basic notions of model theory (substructures
  and embeddings, theories, elementary equivalence and elementary classes, definable sets); elementary extensions
  and the Löwenheim–Skolem theorems (the Tarski–Vaught test, diagrams, Skolem hulls, elementary chains);
  ultraproducts and product constructions (Łoś's theorem, ultrapowers, the Keisler–Shelah theorem, the
  Feferman–Vaught theorem); and back-and-forth methods and Ehrenfeucht–Fraïssé games. 79 exercises. The other 23
  chapters, from types and saturated models to finite model theory, have an opening each, and the volume has its
  introduction.
- **Volume 3, Linear algebra**, has the same text as in 0.2.0, and its files are those of 0.2.0 under the new names,
  so its cover, title page and copyright page say edition 0.2.0.
- **Volume 1, Reasoning and proof**, has the same learner pages as in 0.2.0; it is built again because its entries
  now refer to entries of the new chapters (the liar paradox, 2.28.1; explosion, 2.26.2; model theory, 4.1.1).
- **Entries** are the pages of each sub-area's reading order on the site, numbered (4.3.2), each with its summary,
  a box of facts, motivation, notation, remarks, and three explanations at rising levels. The worked examples and
  counterexamples of an entry follow it in boxes, and each entry ends with its sources.
- **Learner pages** around the entries: a volume introduction with a first-course path, and for each chapter an
  opening, groups with short introductions, a summary with tables, 19 to 28 exercises in three bands (◦ check,
  • practice, ★ challenge) with hints, and notes on history and further reading.
- **Apparatus**: a bibliography of the works the entries cite, and an index of entries, other names, and the pages
  of other areas that the entries use, with links to the site.
- **Builder**: a Ł in a subscript (`x \to_{Ł} y`, the Łukasiewicz conditional) now prints in the PDF, and the
  section sign of light linear logic (`\S`) in the EPUB.
- **Corrections**: a link in the summary of chapter 2.7 that pointed to the wrong entry now points to *True
  arithmetic* (2.10.13). Twelve errors found in eleven entries while writing were corrected on the site after
  v0.3.0 ([tamnd/math2#410](https://github.com/tamnd/math2/pull/410)); this edition prints the entries of v0.3.0.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
