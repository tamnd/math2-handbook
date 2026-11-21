The Math 2.0 Handbook, edition 0.2.0: the first three areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.2.0 (`76ed8d8f5aa5bb5dacb5796b77e3cf1cb656cd49`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Worked examples | Pages |
|---|---|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 398 | 1,176 |
| 2 | Mathematical logic | 28 | 392 | 670 | 2,047 |
| 3 | Linear algebra | 21 | 397 | 483 | 1,488 |
| | **All** | **63** | **969** | **1,551** | **4,711** |

- **Volume 3, Linear algebra**, new, all 21 chapters written: vectors in the plane and in space; systems of linear
  equations and row reduction; matrices and their operations; invertible matrices, the LU decomposition and Schur
  complements; vector spaces, span, independence, bases and dimension; linear maps; direct sums, complements and
  quotients; matrices of linear maps, rank and change of basis; dual spaces; determinants; eigenvalues and the
  characteristic and minimal polynomials; diagonalization, triangularization and invariant subspaces; canonical
  forms under similarity (Jordan and rational forms); inner product spaces; orthogonal projections and least
  squares; adjoints, normal operators and the spectral theorems; isometries and the orthogonal and unitary groups;
  positive definite matrices and the singular value decomposition; bilinear and sesquilinear forms; quadratic
  forms and the principal axis theorem; and applications (networks and input-output models, interpolation and least
  squares fits, recurrences, Markov chains and PageRank, differential equations, graphics, signals and images,
  Lights Out, graphs). 503 exercises.
- **Volume 2, Mathematical logic**, now has 392 entries (198 in 0.1.1) and learner pages for chapters 2.1 to 2.23.
  New in this edition: natural independence results and fast-growing functions; structural proof theory; ordinal
  analysis and ordinal notations; proof interpretations and conservation results; provability and
  interpretability logics; reverse mathematics; bounded arithmetic; propositional proof complexity; the syntax,
  Kripke semantics and completeness of modal logic; correspondence, bisimulation and extended modal logics; applied
  modal logics; and intuitionistic and intermediate logics. The introduction of the volume is rewritten, with
  reading paths into proof theory and into modal and intuitionistic logic. Chapters 2.24 to 2.28 (many-valued,
  substructural, paraconsistent and other non-classical logics, algebraic logic, truth and the paradoxes) still
  have an opening each.
- **Volume 1, Reasoning and proof**, has the same learner pages as in 0.1.1, with the entries as they are in
  release v0.2.0 of the site.
- **Entries** are the pages of each sub-area's reading order on the site, numbered (3.11.4), each with its summary,
  a box of facts, motivation, notation, remarks, and three explanations at rising levels. The worked examples and
  counterexamples of an entry follow it in boxes, and each entry ends with its sources.
- **Learner pages** around the entries: a volume introduction with a first-course path, and for each chapter an
  opening, groups with short introductions, a summary with tables, 20 to 28 exercises in three bands (◦ check,
  • practice, ★ challenge) with hints, and notes on history and further reading.
- **Apparatus**: a bibliography of the works the entries cite, and an index of entries, other names, and the pages
  of other areas that the entries use, with links to the site.
- **Builder**: a macro with arguments followed by a letter (`\ip{x}{u}u`) now expands with a space in the EPUB;
  math that contains an escaped dollar (`$\$_w$`, the spheres of Lewis) has its macros expanded; a negated ⊳
  (`\not\rhd`, "does not interpret") prints in the PDF and the EPUB; the index lists every page of another area
  that the entries use, also when two of them have the same name (a definition and a concept), and no longer
  changes from build to build; and `mh check` reports a table caption that contains a line break. Nine errors
  found in ten entries while writing were corrected on the site after v0.2.0
  ([tamnd/math2#408](https://github.com/tamnd/math2/pull/408)); this edition prints the entries of v0.2.0.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
