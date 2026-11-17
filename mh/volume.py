"""The Markdown of a whole volume: introduction, chapters, appendices.

The same text feeds the LaTeX and the EPUB writers. Headings that LaTeX makes with its own macros
(\\hbchapter, \\hbintro, \\hbentry) are repeated as `html-only` Markdown headings for the EPUB.
"""

from __future__ import annotations

from . import apparatus
from .book import Book, Volume
from .corpus import SITE
from .prep import Refs, chapter_md, glue, hints_md, md_plain, tex


def _intro_head(title: str, label: str) -> str:
    return (f"```{{=latex}}\n\\hbintro{{{tex(title)}}}{{{label}}}\n```\n\n"
            f"# {md_plain(title)} {{#{label} .html-only .unnumbered}}\n")


def chapter_table(book: Book, vol: Volume) -> str:
    rows = ["| | Chapter | Entries | Examples |", "|--|------------------------|-----:|-----:|"]
    for ch in vol.chapters:
        name = f"[{md_plain(ch.name)}](#ch-{ch.id})"
        ex = sum(len(book.attached.get(e.tag, [])) for e in ch.entries)
        rows.append(f"| {ch.num} | {name} | {len(ch.entries) or '–'} | {ex or '–'} |")
    return "\n".join(rows) + f"\n\n: The chapters of Volume {vol.number}.\n"


def introduction(book: Book, vol: Volume, refs: Refs) -> str:
    out = [_intro_head("Introduction", f"intro-{vol.id}")]
    t = glue(book, refs, vol.id, "volume.md")
    out.append(t if t else refs.wiki(vol.summary.strip()) + "\n")
    n_e = len(vol.entries)
    n_a = sum(len(book.attached.get(e.tag, [])) for e in vol.entries)
    empty = [c for c in vol.chapters if not c.entries]
    out.append("```{=latex}\n\\hbgroup{The volume at a glance}\n```\n\n"
               f"## The volume at a glance {{#intro-{vol.id}-glance .html-only}}\n")
    more = (f" The pages of {len(empty)} chapters are not written yet; the book gives their openings."
            if empty else "")
    out.append(f"This edition of the volume has {len(vol.chapters)} chapters with {n_e} entries and "
               f"{n_a} worked examples.{more}\n")
    out.append(chapter_table(book, vol))
    out.append("```{=latex}\n\\hbgroup{How to use the entries}\n```\n\n"
               f"## How to use the entries {{#intro-{vol.id}-entries .html-only}}\n\n"
               "Each entry is a page of the site. It opens with a short statement of what the page is about and a "
               "box of facts: other names, the pages it uses, and its classification in the Mathematics Subject "
               "Classification (MSC). The body follows the plan of the site: motivation and notation, then remarks "
               "with examples, non-examples, basic properties, history and common errors, and last three "
               "explanations at rising levels: *in plain words*, *in detail* and *for the specialist*. The worked "
               "examples of an entry follow it, each in a box. A number such as 1.5.2 after a link is the number "
               "of an entry of this book; a link without a number goes to a page of the site, "
               f"<{SITE}>, where every other area of mathematics has its pages.\n")
    return "\n".join(out)


def volume_md(book: Book, vol: Volume) -> tuple[str, dict]:
    """The Markdown of the volume, and some numbers about it."""
    refs = Refs(book, vol)
    chapters = [chapter_md(book, vol, ch, refs) for ch in vol.chapters]
    parts = [introduction(book, vol, refs)] + chapters
    parts.append("```{=latex}\n\\hbbackmatter\n```\n")
    appx = [
        ("Hints to the exercises", "hints", lambda: hints_md(book, vol, refs)),
        ("Bibliography", "bibliography", lambda: apparatus.bibliography(book, vol, refs)),
        ("Index", "index", lambda: apparatus.subject_index(book, vol, refs)),
    ]
    for title, label, make in appx:
        body = make()
        if body and body.strip():
            parts.append(_intro_head(title, label) + "\n" + body + "\n")
    att = [n for e in vol.entries for n in book.attached.get(e.tag, [])]
    stats = {"chapters": len(vol.chapters), "entries": len(vol.entries), "attached": len(att),
             "words": sum(e.words for e in vol.entries) + sum(n.words for n in att),
             "warnings": [w for c in vol.chapters for w in c.warnings]}
    return "\n\n".join(parts), stats


def volume_hue(n: int) -> str:
    """One hue per volume, spread round the wheel with the golden angle, at an even darkness."""
    import colorsys
    h = ((n * 137.508 + 200) % 360) / 360
    r, g, b = colorsys.hls_to_rgb(h, 0.38, 0.55)
    return "%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))


__all__ = ["volume_md", "volume_hue", "SITE"]
