# The Math 2.0 Handbook

The content of [math2.tamnd.com](https://math2.tamnd.com) as a set of books that a person can learn from, from the
first page to the last: one volume per area of the site, in PDF, EPUB and LaTeX.

Each area of the site is a volume, each sub-area a chapter, and each page of a sub-area's reading order an entry
with a fixed number (2.7.3 is the third entry of chapter 7 of Volume 2, *Mathematical logic*). The proofs, worked
examples and counterexamples of an entry are printed with it, each in a box. Around the entries, the handbook adds the pages
a reference site does not need and a textbook does: an introduction to each volume, an opening, groups and a
reading order for each chapter, summaries, exercises in three bands with hints, notes on history and further
reading, a bibliography and an index.

## Volumes in edition 0.5.4

Built from [`tamnd/math2`](https://github.com/tamnd/math2) at the commit named in [`EDITION`](EDITION), the content
of release v0.5.4. The edition number of the handbook follows the release of the site it is built from; a larger
fourth number would mark a new build of the same release. The books are on the
[releases page](https://github.com/tamnd/math2-handbook/releases).

| | Volume | Chapters | Entries | Proofs | Worked examples | Learner pages |
|---|---|---:|---:|---:|---:|---|
| 1 | Reasoning and proof | 14 | 180 | 7 | 398 | written |
| 2 | Mathematical logic | 28 | 493 | 142 | 885 | written |
| 3 | Linear algebra | 21 | 398 | 197 | 493 | written |
| 4 | Model theory | 27 | 126 | 45 | 178 | written for chapters 4.1–4.11; openings for the other 16 |

The other areas of the site join as their reading orders are written.

## Building

Requirements: Python 3.11+, [pandoc](https://pandoc.org) 3.8 or later, [tectonic](https://tectonic-typesetting.github.io)
and poppler (`pdfinfo`). Fonts come from tectonic's TeX Live bundle; nothing else is installed.

```sh
git clone https://github.com/tamnd/math2 ../math2              # the content, next to this repository
pip install .
python -m mh survey                                            # the volumes, chapters and entries
python -m mh check --volume all                                # the learner pages: links, outlines, exercises, style
python -m mh brief --volume 2 --chapter 7                      # what a writer of a chapter's pages works from
python -m mh build --volume 2 --formats tex,pdf,epub           # build/02-mathematical-logic/main.pdf, main.epub
```

`--content` points at another checkout of the content. A volume takes about ten minutes, most of it in tectonic.

## Layout

| Path | What |
|---|---|
| `mh/` | the builder: corpus, book structure, Markdown assembly, macros, apparatus, LaTeX, EPUB, covers |
| `filters/mh.lua` | the pandoc filter that lets one Markdown file serve LaTeX and EPUB |
| `tex/handbook.sty`, `tex/epub.css` | the design of the PDF and the EPUB |
| `data/` | the books and articles that the entries cite by ISBN and DOI, for the bibliography |
| `content/<area>/` | the learner pages of a volume: `volume.md`, and per chapter `outline.yaml`, `opening.md`, `summary.md`, `exercises.md`, `hints.md`, `notes.md` |
| `prompts/area.md` | the brief the learner pages are written from |

## How the text was made

The entries are the text of the site. The learner pages were drafted by AI agents from a written brief and a sample
chapter, checked by `mh check`, and spot-checked; see [`content/PROVENANCE.md`](content/PROVENANCE.md). Report
errors in an entry at [tamnd/math2 issues](https://github.com/tamnd/math2/issues) and errors in the learner pages
or the books here.

## Licences

The text of the books and of `content/` is licensed under [CC BY-SA 4.0](LICENSE-CONTENT), as on the site. The
builder is [MIT](LICENSE).
