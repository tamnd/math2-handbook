The Math 2.0 Handbook, edition 0.4.0: the first four areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.4.0 (`18d8d2d9e4707a68f1658e0815c59b09d8b9aae8`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Proofs | Worked examples | Exercises | Pages |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 7 | 398 | 362 | 1,198 |
| 2 | Mathematical logic | 28 | 493 | 142 | 876 | 687 | 2,753 |
| 3 | Linear algebra | 21 | 398 | 197 | 493 | 533 | 2,081 |
| 4 | Model theory | 27 | 126 | 45 | 178 | 238 | 680 |
| | **All** | **90** | **1,197** | **391** | **1,945** | **1,820** | **6,712** |

- **Volume 3, Linear algebra**, is rewritten for learners. The site rewrote all 21 sub-areas of linear algebra
  in textbook prose for its v0.4.0, and the learner pages of the volume are written again to match. These are the
  volume introduction, and for each of the 21 chapters an opening, groups, a summary, exercises, hints and notes.
  - **Openings.** Each opening starts from a computation done by hand, such as a least-squares fit of three
    equations, a 2 × 2 system whose determinant is also an area, or a rotation of space found from its matrix. It
    then says what the chapter proves.
  - **Groups.** The introduction of each group states its main theorem with all of its hypotheses.
  - **Summaries.** Each summary repeats the hypotheses of every result and ends with common errors.
  - **Exercises.** There are 533 exercises in three bands (◦ check, • practice, ★ challenge), with hints for every
    ★. They mix computation, proof, counterexample and find-the-error items, and none repeats an example printed
    in the entries. Every numerical answer was checked in exact rational arithmetic, and every count over a finite
    field by brute force.
  - **Introduction.** The volume introduction gives two routes through the volume, computations first or structure
    first, which meet at Chapter 3.8, and a first course of 19 entries.
- **Volume 4, Model theory**, now has 126 entries (86 in 0.3.1) and learner pages for Chapters 4.1 to 4.11. The
  four new chapters are:
  - *Quantifier elimination and model completeness* (4.8);
  - *Preservation and definability theorems* (4.9);
  - *Interpretations and imaginaries* (4.10);
  - *Indiscernibles and two-cardinal theorems* (4.11).

  They add 86 new exercises. The introduction of the volume is revised. Chapters 4.12 to 4.27 have no entries on
  the site yet, and the book prints their openings only.
- **Volume 1, Reasoning and proof**, has new learner pages for Chapters 1.1 to 1.3, whose entries the site
  rewrote in textbook prose. The three chapters are *Proof, theorems and mathematical method*, *The language of
  mathematical statements* and *Definitions in mathematics*, and they have 84 exercises. The introduction of the
  volume now describes these chapters in full.
- **Volume 2, Mathematical logic**, has the same learner pages as in 0.3.1. It is built again from the entries of
  v0.4.0, with its proofs now printed (see below).
- **Proofs are printed.** The proof pages of the site are now printed after the theorems they prove, together with
  the worked examples: 391 proofs in all. In earlier editions the builder read a proof's single target as a list of
  characters, so no proof was ever attached.
- **Builder.** Three more changes to how the books are built:
  - **Proof titles.** A proof named "Proof of …" is no longer printed as "Proof: Proof of …".
  - **Sans-serif Greek.** A Greek letter inside `\mathsf{…}`, as in the theory IΣ₁, is set upright from the math
    font. The sans-serif font has no math Greek, so the Σ was lost.
  - **Macros after accents.** A macro after a bare accent, as in `\overline \Q`, is expanded inside braces, so the
    bar covers the whole of ℚ and the EPUB can convert the formula.
  - **New headings.** The builder reads the site's new headings for the reading order of a sub-area (`### Reading
    order: …`, `### Reading order, continued: …`) and for the list of sub-areas of an area.
- **Corrections.** Four errors were found in four entries while writing:
  - the field $\overline{\Q}$;
  - a doubled word;
  - the year of Wiles's proof of Fermat's Last Theorem;
  - the sign of the homogeneous system behind an augmented matrix.

  They were corrected on the site after v0.4.0 in [tamnd/math2#465](https://github.com/tamnd/math2/pull/465).
  This edition prints the entries of v0.4.0. The corrections of
  [tamnd/math2#410](https://github.com/tamnd/math2/pull/410) and
  [tamnd/math2#412](https://github.com/tamnd/math2/pull/412), from the writing of editions 0.3.0 and 0.3.1, are in
  v0.4.0 and so in this edition.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
