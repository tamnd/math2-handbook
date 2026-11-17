# Provenance of the learner pages

This file says how the pages in `content/` were made, so that readers and anyone who reuses them know what they
are. It is not part of any volume.

## What is here

Each `content/<area>/` holds the learner pages of one volume: the volume introduction (`volume.md`), and for each
chapter an outline (the groups of its entries, in the site's reading order), an opening, a summary, exercises,
hints and notes. A chapter whose sub-area has no pages yet has an opening only. None of these pages is on the site;
the entries themselves are the text of the site and are not stored here.

## How the pages were written

All pages in this directory were drafted by AI agents in November 2026, for edition 0.1.1:

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

## Known limits

- The history in the notes rests on the `### History` sections and the sources of the entries, and on general
  knowledge; years that could not be confirmed were left out rather than guessed.
- Exercises are new, not copied; a few classic facts (such as the irrationality of $\sqrt 2$) are asked in new
  words.
- The entries of the site can disagree with each other on small points (a date, the number of an axiom). The
  learner pages follow the entry nearest to the point, and such disagreements are reported upstream.
