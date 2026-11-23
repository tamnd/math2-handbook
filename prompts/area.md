# Brief: write the learner layer of one volume (or part of one)

You are writing pages of **The Math 2.0 Handbook**, a book built from the pages of the site
<https://math2.tamnd.com> (project Math 2.0, content repo tamnd/math2, edition v0.4.0). The builder turns each area
of the site into a volume and each sub-area into a chapter; the entries (nodes) are already written, with their
proofs and examples. Your job is the *learner layer*: the pages that turn a run of entries into a textbook a person
can learn from alone.

Read this whole brief before you write anything. Then read the gold sample (below) closely.

## Where things are

- The handbook repo: `~/github/tamnd/math2-handbook`. Work only in `content/<area-id>/` for the chapters you are
  given. Do not edit anything else: not `mh/`, not `tex/`, not other chapters, not `prompts/`.
- The content, read-only: `~/hb-work/math2-0.4.0`. A node is the file
  `~/hb-work/math2-0.4.0/nodes/<first three characters of the tag>/<TAG>.md` (YAML front matter, then the body),
  e.g. `nodes/0NT/0NTF6DMVAP.md`. Never edit these files. Never touch `~/github/tamnd/math2` or
  `~/github/tamnd/math2-agent`.
- Do not run `git` anywhere. Do not commit. Do not build PDFs. Do not delete files you did not write.

## Tools

Run these from `~/github/tamnd/math2-handbook` (each takes a few seconds):

    python3 -m mh brief --content ~/hb-work/math2-0.4.0 --volume N                  # every chapter
    python3 -m mh brief --content ~/hb-work/math2-0.4.0 --volume N --chapter K      # one chapter
    python3 -m mh brief --content ~/hb-work/math2-0.4.0 --volume N --chapter K --sections
    python3 -m mh check --content ~/hb-work/math2-0.4.0 --volume N                  # must be clean for your chapters

The brief prints the chapter's sub-area page (summary and prerequisites), then each entry as
`1.5.2 Direct proof` with its tag, kind, length and the one-line description from the reading order, and under it
the proofs and examples that the book prints with that entry. The order of the entries is the site's reading
order, and **the book keeps that order**. Never write an entry number by hand. Write links only, as
`[direct proof](/0NTF6DMVAP/)` (the tag between slashes), and the builder adds the number or, for a page that is
not in the book, a link to the site.

## The files, per chapter

For a volume with area id `A` and a chapter (sub-area) with id `S` (both are printed by the brief, in backticks),
write in `content/A/S/`:

| File | What it is | Size |
|---|---|---|
| `outline.yaml` | The groups of the chapter: a title, a short intro and the entry tags | every entry, once, in reading order |
| `opening.md` | The chapter's opening pages | 450–900 words |
| `summary.md` | What to remember, a table where one makes sense, guidance | 300–800 words |
| `exercises.md` | Numbered exercises in three bands | 15–30 exercises |
| `hints.md` | Hints and short answers for about half the exercises | as needed |
| `notes.md` | History and further reading | 300–700 words |

And once per volume, `content/A/volume.md`: the volume introduction, 900–1500 words. Write it only if your
assignment says you own it.

A chapter with **no entries** (the brief says "0 entries") gets only `opening.md` (250–450 words: what the topic
is, why it matters, what the planned pages will cover, what to read meanwhile, with links to related entries that
do exist) and no other file. Its sub-area page (`nodes/<3>/<TAG>.md` of the sub-area tag) describes the topic.

## Gold sample: read it first

The model for voice, structure and density is the learner layer of a sister book, The Handbook of Algorithms:
`~/github/tamnd/algorithm-handbook/content/sorting/volume.md` and the six files in
`~/github/tamnd/algorithm-handbook/content/sorting/comparison-sorts/`. Read all of them before writing (they are
about algorithms; you write about mathematics, so theorems and proofs take the place of algorithms and costs, but
the shape and the care are the same). Their links have the form `(/slug/)`; yours have the form `(/TAG/)`.

## The outline (`outline.yaml`)

```yaml
groups:
  - title: Direct proof and its relatives      # a short title in sentence case
    intro: >                                   # 2–4 sentences: what the group is about, how its entries relate
      Most proofs of an implication assume the hypothesis and reason forward. ...
    entries:                                   # tags, in the reading order
      - G9JFJGY4TQ
      - 0NTF6DMVAP
```

- List **every entry of the chapter exactly once, in the order of the brief**. You choose only where the group
  boundaries fall. `mh check` warns about missing, doubled or unknown tags and about any change of order; fix
  every warning for your chapters.
- Make 3 to 8 groups of consecutive entries (a chapter of fewer than 9 entries may have 2 or 3 groups).
- Group intros may contain links and `$math$`.
- Do not list the attached proofs and examples (indented under an entry in the brief); they print with their entry.

## The opening (`opening.md`)

The reader has just turned to the chapter. Tell them, in this order:

1. What the chapter is about, concretely, with one or two mathematical examples of where it matters. No
   throat-clearing.
2. `## What the chapter covers`: the groups in order, as a numbered list, one or two sentences each, with links to
   the key entries.
3. `## A first reading`: the 5–12 entries to read first, in order, as links. Say what can be skipped at first.
4. `## Before you start`: what is assumed, with links to entries in other chapters or volumes where they exist (the
   sub-area page's `### Prerequisites` is a good base).

## The summary (`summary.md`)

- `## What to remember`: 5–9 bullets, each a fact, definition or theorem stated precisely, in math where math is
  clearer.
- A table when the chapter has things to compare (methods of proof and the goals they fit; logics and their
  properties such as soundness, completeness, compactness, decidability; theories and what they prove). Give it a
  caption line `: …` after the table. Every claim in it must match the entries; check them.
- A short section of practical guidance (`## Choosing a method`, `## Common errors`, or what fits the chapter).

## The exercises (`exercises.md`)

- A plain numbered list `1.`, `2.`, … with one blank line between exercises. The builder renumbers them as
  `1.5.7` and links hints to them.
- Each exercise starts with its band mark: `◦` (check: a few minutes, tests close reading: negate a statement,
  identify a hypothesis, spot the error in a short argument, compute a small case), `•` (practice: prove a small
  claim with a method of the chapter, build a counterexample, formalize a sentence) or `★` (challenge: a real proof,
  a known result in your own words, a construction). Aim for about 35% ◦, 45% •, 20% ★, ordered by band.
- Concrete statements, exact questions. Every exercise must have a definite answer you know. Work each one out
  yourself before you write it. Do not pose open problems as exercises.
- Do not copy exercises from textbooks. Classic facts (such as "$\sqrt 2$ is irrational") are fine to ask about in
  your own words.
- Do not repeat a worked example that the book prints in the chapter (the attached examples in the brief): ask for
  a variation instead.
- Link to entries where it helps: `Use [proof by contrapositive](/0BB5TPGQ1N/) to show …`.

## The hints (`hints.md`)

- A numbered list whose numbers are the numbers of the exercises they belong to (not 1, 2, 3 … in order; skip
  exercises with no hint). Give hints to about half the exercises, including most ★ ones.
- For ◦ exercises, give the answer. For • and ★, give the key idea in one to four sentences, and the answer when it
  is short.

## The notes (`notes.md`)

- `## History`: who found the main ideas, when, and how the topic grew. Three to five paragraphs of plain narrative.
  Use the `### History` sections and the `sources` of the entries as your base; every name, year and title must be
  one you are sure of. If you are not sure of a year, leave the year out. Never invent a paper or a book.
- `## Further reading`: 3–6 items, books and survey articles, each with one sentence on what it is good for. Prefer
  works cited in the entries' sources (`book: isbn:…` items: look the title up from what you know only if you are
  sure of it). Use full, correct titles and authors.

## The volume introduction (`volume.md`), when assigned

Follow `~/github/tamnd/algorithm-handbook/content/sorting/volume.md`: what the area is and where it shows up; a
section on the big ideas the volume teaches; `## The chapters`, one paragraph per chapter with key links (for a
chapter with no entries yet, one sentence saying what it will cover; the book prints its opening only);
`## How to read this volume` with a first-course path through 10–20 key entries; `## What you need first`;
`## The exercises` (adapt the band explanation from the sample to mathematics). The area page (the volume's tag,
printed by the brief without `--chapter`) is your base.

## The writing standard

- **Plain words and short sentences**, like the pages of the site. Explain; do not decorate. Write "uses", not
  "leverages"; "shows", not "showcases". No marketing words (powerful, elegant, seamless, crucial, robust, delve,
  landscape, journey). No rhetorical questions as section openers. No exclamation marks (factorials such as $n!$
  go in math).
- Active voice, present tense. Address the reader as "you" sparingly, in guidance.
- Every claim must agree with the entries. Read the key entries of each group in full (front matter and body); for
  the rest, the brief and the section headings are usually enough, but open the entry whenever you state a specific
  fact from it.
- Mathematics in `$…$` or `$$…$$` (KaTeX syntax, as on the site). You may use the site's macros `\N \Z \Q \R \C \F`,
  `\abs{x} \norm{x} \set{x} \floor{x} \ceil{x}`; nothing else that is not standard LaTeX math. Do not use
  `\begin{align}`; use `\begin{aligned}` inside `$$…$$`. Never put a `$` inside a link's text unless it is math.
- Links: only `[text](/TAG/)` with a tag that exists (`mh check` verifies). Link an entry the first time a page
  mentions it; do not link every mention. A link may point to any node of math2, also outside the book (the builder
  turns it into a link to the site), but prefer entries of the book. Do not link to external sites in the body text
  (notes may name papers and books without URLs). Never write the site's `[[text|TAG]]` form.
- Spelling: British, as on the site ("colour", "rigour", "practise" as a verb; "-ize" endings such as
  "formalize"). Be consistent within a file.
- Do not write "In this chapter, we will…". Do not end with a summary of what you just said.
- Do not mention AI, agents or how the text was made.

## Finish

1. Run `python3 -m mh check --content ~/hb-work/math2-0.4.0 --volume N` and fix every problem it reports for your
   chapters (problems in other chapters are not yours).
2. Re-read each file once against this brief.
3. Report back: the files written (with word counts, `wc -w`), the number of exercises per chapter, and any factual
   doubt you could not settle.
