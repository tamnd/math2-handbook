The Math 2.0 Handbook, edition 0.5.4: the first four areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.5.4 (`71fe75b8f58451e20c95c0565d5a06b4d94ab0c1`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Proofs | Worked examples | Exercises | Pages |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 7 | 398 | 367 | 1,234 |
| 2 | Mathematical logic | 28 | 493 | 142 | 885 | 687 | 2,858 |
| 3 | Linear algebra | 21 | 398 | 197 | 493 | 533 | 2,081 |
| 4 | Model theory | 27 | 126 | 45 | 178 | 238 | 682 |
| | **All** | **90** | **1,197** | **391** | **1,954** | **1,825** | **6,855** |

- **Volume 2, Mathematical logic**, prints the new entries of chapters 2.1 to 2.19. The site rewrote these
  nineteen chapters in textbook prose in its releases v0.5.1 to v0.5.4 and fixed many mathematical slips on the way.
  The learner pages of those chapters were revised to match:
  - **Agreement with the new entries.** The pages were checked claim by claim against the change of every entry.
    Some corrections: validity is undecidable in general, but monadic validity is decidable. Resolution is
    refutation complete only, so it no longer appears in the list of equivalent proof systems. The compactness
    example adds the new constant to the true sentences of ℕ. Harmony is local, and a separate proof is needed
    that reduction ends. The subformula property is no longer claimed for deep inference. The A-translation names
    ex falso as the rule that fails. Δ¹₂-CA₀ is no longer paired with an ordinal that the entries do not give.
  - **Exercises.** Where a new entry now works an old exercise as its own example, the exercise was replaced in
    the same band. Answers that rest on changed definitions were computed again by script, among them the
    Kanamori–McAloon regressive colorings (now on positive integers), the worm and hydra battles, the weak tree
    function, now indexed as in the entry, and the bad sequences of Friedman's finite Kruskal theorem.
  - **Reading order.** Chapter 2.12, natural independence results, follows the site's new order in six groups, from
    Goodstein's theorem to concrete incompleteness. The introduction of the volume was revised to match.
- **Volumes 1, 3 and 4** have the same learner pages as in edition 0.5.0. They are built again, because some of
  their entries changed, among them the corrections of [tamnd/math2#465](https://github.com/tamnd/math2/pull/465)
  (the year of Wiles's proof, the sign of the homogeneous system behind an augmented matrix). Their
  cross-references also follow the new numbering of Volume 2.
- **Builder.** `mh` reads an area whose sub-areas are listed as its reading order. It also reads a reading order
  continued under a heading without a colon.
- **Corrections.** Four errors were found in four entries while revising:
  - a decidable set of axioms where a primitive recursive one is needed;
  - a pairing function that is not onto, so some stages of a construction were left undefined;
  - a link to the propositional Hilbert system in place of the predicate calculus;
  - a count of evaluations off by one.

  They were corrected on the site after v0.5.4 in [tamnd/math2#482](https://github.com/tamnd/math2/pull/482).
  This edition prints the entries of v0.5.4.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
