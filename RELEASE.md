The Math 2.0 Handbook, edition 0.5.0: the first four areas of [math2.tamnd.com](https://math2.tamnd.com) as
books, one volume per area, in PDF (7 × 10 in, with bookmarks and links), EPUB 3 and LaTeX source. Built from
[`tamnd/math2`](https://github.com/tamnd/math2) release v0.5.0 (`70a7e61bc19e573a487d206469309d52c1f092f9`); the
edition number follows the release of the site.

| | Volume | Chapters | Entries | Proofs | Worked examples | Exercises | Pages |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Reasoning and proof | 14 | 180 | 7 | 398 | 367 | 1,234 |
| 2 | Mathematical logic | 28 | 493 | 142 | 876 | 687 | 2,753 |
| 3 | Linear algebra | 21 | 398 | 197 | 493 | 533 | 2,081 |
| 4 | Model theory | 27 | 126 | 45 | 178 | 238 | 680 |
| | **All** | **90** | **1,197** | **391** | **1,945** | **1,825** | **6,748** |

- **Volume 1, Reasoning and proof**, is rewritten for learners. The site rewrote all 14 sub-areas of reasoning and
  proof in textbook prose for its v0.5.0. Chapters 1.1 to 1.3 were written again in edition 0.4.0. In this edition
  the learner pages of the other eleven chapters, 1.4 to 1.14, are written again to match, and so is the volume
  introduction. For each chapter that means an opening, groups, a summary, exercises, hints and notes.
  - **Openings.** Each opening starts from something a student can check by hand. Examples are a flawed proof
    that $3 \mid n^2$ implies $3 \mid n$ (which in fact proves the converse), a false "proof" that $2 = 1$, the
    sum $1 - 4 + 9 - \dots$, and two textbooks that disagree about whether every increasing function is injective.
    It then says what the chapter covers and which entries to read first.
  - **Summaries.** For each proof method, the summary gives the form of statement it proves, the skeleton of its
    proof and when to use it. Each ends with common errors.
  - **Exercises.** There are 283 new exercises in three bands (◦ check, • practice, ★ challenge), with hints for
    every ★. They mix proofs, counterexamples, find-the-error items and referee reports, and none repeats an
    example printed in the entries. Every number and every parity, invariant and pigeonhole claim was checked by
    script or by brute force.
  - **Introduction.** The volume introduction describes all 14 chapters. It names induction, strong induction and
    well-ordering as three equivalent forms of one principle. It gives a first course of 19 entries and routes for
    students preparing for competitions, students starting analysis, and teachers.
- **Volumes 2 to 4** are unchanged. Their entries are the same in v0.4.0 and v0.5.0, and the books built from them
  are identical apart from the edition number. Their files are those of edition 0.4.0 under the names of this
  edition, so their title pages still say 0.4.0.
- **Corrections.** Three errors were found in three entries while writing:
  - a student's argument that described the opposite of the belief the entry goes on to explain;
  - a strict inequality in Kelly's proof of the Sylvester–Gallai theorem that is an equality in a case the setup
    allows;
  - a missing hypothesis, that every face is a disc, in the improved Euler theorem of Lakatos.

  They were corrected on the site after v0.5.0 in [tamnd/math2#469](https://github.com/tamnd/math2/pull/469).
  This edition prints the entries of v0.5.0.

Assets: per volume, the PDF, the EPUB and the LaTeX source (`-tex.tar.gz`: `main.tex`, `body.tex`,
`handbook.sty`, built with tectonic); all PDFs and all EPUBs as two zips; and `SHA256SUMS`.

The learner pages were drafted by AI agents from a written brief and checked; see
[`content/PROVENANCE.md`](https://github.com/tamnd/math2-handbook/blob/main/content/PROVENANCE.md). Text
CC BY-SA 4.0; builder MIT. Report errors in an entry at [tamnd/math2](https://github.com/tamnd/math2/issues) and
errors in the books [here](https://github.com/tamnd/math2-handbook/issues).
