# Provenance of the learner pages

This file says how the pages in `content/` were made, so that readers and anyone who reuses them know what they
are. It is not part of any volume.

## What is here

Each `content/<area>/` holds the learner pages of one volume: the volume introduction (`volume.md`), and for each
chapter an outline (the groups of its entries, in the site's reading order), an opening, a summary, exercises,
hints and notes. A chapter whose sub-area has no pages yet has an opening only. None of these pages is on the site;
the entries themselves are the text of the site and are not stored here.

## How the pages were written

The pages of edition 0.1.1 were drafted by AI agents in November 2026:

1. A brief, [`prompts/area.md`](../prompts/area.md), fixes the files, their sizes, the voice, the exercise bands,
   the rules for hints and notes, and the checks. The learner layer of a sister book, The Handbook of Algorithms,
   served as the model of voice and structure.
2. Nine writers shared the two volumes: four for the fourteen chapters of Volume 1, four for chapters 2.1 to 2.11
   of Volume 2, and one for the two volume introductions and the openings of chapters 2.12 to 2.28, whose
   sub-areas have no pages yet. Each writer read the entries of its chapters (the summary and section headings of
   all of them, the full text of the key entries and of any entry whose fact it states).
3. Each writer worked the exercises it set; numerical answers were checked with short scripts.
4. `python -m mh check` verifies every link, the outline of every chapter, the numbering and bands of exercises,
   the hints, and a list of banned words.
5. The writers listed the names, years and titles they were not sure of; these were checked by hand, and where a
   fact could not be settled, the text leaves it out.

For edition 0.2.0 (November 2026, built from release v0.2.0 of the site), the same brief, with the paths of the
new content, was used for the new pages: the volume introduction and the 21 chapters of Volume 3, *Linear algebra*,
and chapters 2.12 to 2.23 of Volume 2, whose sub-areas now have entries (their openings were rewritten, and the
other five files written). Eleven writers shared the 33 chapters, three or four chapters each; the introduction of
Volume 3 was written after its chapters, and that of Volume 2 was rewritten for the chapters it now has. The
exercises were again worked and their numerical answers checked with short scripts, and `mh check` is clean for
all three volumes. Nine errors that the writers found in ten entries (a wrong link, a misstated position of matrix
entries, two dates and attributions in history sections, a misnumbered list, links to a retired page) were
corrected on the site after its release v0.2.0, in [tamnd/math2#408](https://github.com/tamnd/math2/pull/408);
this edition prints the entries as they are in v0.2.0. The pages of Volume 1 and chapters 2.1 to 2.11 are those of
edition 0.1.1.

For edition 0.3.0 (November 2026, built from release v0.3.0 of the site), the same brief was used for the new pages:
chapters 2.24 to 2.28, which complete Volume 2, and Volume 4, *Model theory*, new in this edition, whose first four
chapters have entries. Nine writers shared the work: one for each of the five chapters of Volume 2 (the writer of
2.28 also revised the introduction of Volume 2 for the complete volume), two for chapters 4.1 to 4.4, and two for
the openings of the 23 chapters of Volume 4 that have no entries yet, one of whom wrote the introduction of
Volume 4. The exercises were again worked and their answers checked with short scripts, and `mh check` is clean for all
four volumes. Twelve errors that the writers found in eleven entries (a false equivalence between FDE and the pair
LP, K3; a wrong example for the Tarski–Vaught test; an axiom pair called inconsistent without the axioms that make
it so; a fragment of $R$ called decidable; a misattributed name, a wrong year and an overstated attribution in
history sections; a wrong case and a wrong subscript in one remark; and three loose or incomplete statements) were
corrected on the site after its release v0.3.0, in [tamnd/math2#410](https://github.com/tamnd/math2/pull/410); this
edition prints the entries as they are in v0.3.0. A link in the summary of chapter 2.7 that pointed to the wrong
entry now points to *True arithmetic*. The other pages of Volumes 1 to 3 are those of edition 0.2.0.

For edition 0.3.1 (November 2026, built from release v0.3.1 of the site), the same brief was used for chapters 4.5
to 4.7 of Volume 4 (types and saturated models; countable models and categoricity; Fraïssé theory and homogeneous
structures), which have entries in this release. Three writers shared the work, one for each chapter, and the
introduction of Volume 4 was revised for the seven written chapters. The exercises were again worked and their
answers checked with short scripts, and `mh check` is clean for all four volumes. Seven loose or incomplete
statements that the writers found in seven entries (four missing the hypothesis of a countable signature or an
uncountable cardinal, a list of the homogeneous graphs without the complete multipartite graphs, a form of the
Vaught conjecture called both stronger and equivalent, and an example that read a definition differently from its
entry) were corrected on the site after its release v0.3.1, in
[tamnd/math2#412](https://github.com/tamnd/math2/pull/412); this edition prints the entries as they are in v0.3.1.
The other pages of Volumes 1 to 3 are those of edition 0.3.0.

For edition 0.4.0 (November 2026, built from release v0.4.0 of the site), the site had rewritten the entries of
Volume 3, *Linear algebra*, and of chapters 1.1 to 1.3 in textbook prose, so the learner pages of those chapters
were written again from scratch, with a brief that asked for more than before. Each opening starts from a
computation done by hand; each group introduction states its main theorem with all its hypotheses; each summary
repeats the hypotheses and ends with common errors. There are 18 to 30 exercises per chapter, in bands of about
35, 45 and 20 per cent, and none repeats an example printed in the entries. Every numerical answer was checked in
exact rational arithmetic, and every count over a finite field by brute force. Nine writers shared the 21 chapters
of Volume 3, its introduction, and chapters 1.1 to 1.3, two or three chapters each. The writer of chapters 1.1 to
1.3 also reported three gaps in the introduction of Volume 1, which was corrected. Chapters 4.8 to 4.11 of Volume 4
(quantifier elimination and model completeness; preservation and definability theorems; interpretations and
imaginaries; indiscernibles and two-cardinal theorems), which have entries in this release, were written with the
same brief, and the introduction of Volume 4 was revised for the eleven written chapters. `mh check` is clean for
all four volumes. Four errors that the writers found in four entries (a missing pair of braces, a doubled word, the
year of Wiles's proof, and the sign of the homogeneous system behind an augmented matrix) were corrected on the
site after its release v0.4.0, in [tamnd/math2#465](https://github.com/tamnd/math2/pull/465); this edition prints
the entries as they are in v0.4.0. The pages of chapters 1.4 to 1.14 and of Volume 2 are those of edition 0.3.1.

For edition 0.5.0 (November 2026, built from release v0.5.0 of the site), the site had rewritten the entries of
chapters 1.4 to 1.14 of Volume 1, *Reasoning and proof*, in textbook prose, so the learner pages of those eleven
chapters were written again from scratch with the brief of edition 0.4.0, adapted to proofs. Each opening starts
from a puzzle, a claim or a flawed argument that a student can check by hand; each summary gives, for every method,
the form of statement it proves, the skeleton of its proof and when to use it, and ends with common errors. Every
numerical answer and every parity, invariant and pigeonhole claim was checked by script or by brute force, and no
exercise repeats an example printed in the entries. Six writers shared the eleven chapters and the introduction of
Volume 1. `mh check` is clean for all four volumes. Three errors that the writers found in three
entries (a student's argument that described the opposite of the belief the entry explains, a strict inequality that
is an equality in a case the setup allows, and a missing hypothesis in the improved Euler theorem of Lakatos) were
corrected on the site after its release v0.5.0, in [tamnd/math2#469](https://github.com/tamnd/math2/pull/469); this
edition prints the entries as they are in v0.5.0. The entries of Volumes 2 to 4 did not change between v0.4.0 and
v0.5.0, so their books are those of edition 0.4.0.

## Known limits

- The history in the notes rests on the `### History` sections and the sources of the entries, and on general
  knowledge; years that could not be confirmed were left out rather than guessed.
- Exercises are new, not copied; a few classic facts (such as the irrationality of $\sqrt 2$) are asked in new
  words.
- The entries of the site can disagree with each other on small points (a date, the number of an axiom). The
  learner pages follow the entry nearest to the point, and such disagreements are reported upstream.
