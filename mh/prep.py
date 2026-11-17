"""Make the pandoc Markdown of a volume from the nodes and the learner layer.

One Markdown file serves both targets. Raw blocks carry what differs: ```{=latex}``` blocks are dropped by the EPUB
writer, and elements with the class `html-only` are dropped from the LaTeX output by filters/mh.lua.
"""

from __future__ import annotations

import os
import re

import yaml

from .book import Book, Chapter, Volume
from .corpus import LINK, SITE, Node

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIENCE = {"school": "School", "ug1": "Undergraduate", "ug2": "Undergraduate", "ug3": "Undergraduate",
            "grad": "Graduate", "research": "Research"}
EXPLANATIONS = {"L1 human": "In plain words", "L2 human": "In detail", "L3 human": "For the specialist"}

# --------------------------------------------------------------------------- escaping

_TEX_SPECIAL = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
                "#": r"\#", "^": r"\textasciicircum{}", "_": r"\_", "%": r"\%", "~": r"\textasciitilde{}"}


def tex(s: str) -> str:
    """Escape plain text for LaTeX; $…$ stays mathematics."""
    out = []
    for i, part in enumerate(re.split(r"(\$[^$]+\$)", s)):
        if i % 2:
            out.append(r"\(" + part[1:-1] + r"\)")
        else:
            out.append("".join(_TEX_SPECIAL.get(c, c) for c in part))
    return "".join(out)


def md_plain(s: str) -> str:
    """Escape plain text for a Markdown heading or link text; $…$ stays mathematics."""
    parts = re.split(r"(\$[^$]+\$)", s)
    return "".join(p if i % 2 else re.sub(r"([*_`\[\]<>#\\])", r"\\\1", p) for i, p in enumerate(parts))


# `$x $`: KaTeX accepts a space before the closing dollar; pandoc does not.
_MATH_TRAIL = re.compile(r"(?<![\\$\w])\$([^\s$][^$\n]{0,60}?)\s+\$(?![\w$])")


def fix_math(md: str) -> str:
    def line(ln: str) -> str:
        if "$" not in ln or "$$" in ln:
            return ln
        i = 0
        while (m := _MATH_TRAIL.search(ln, i)):
            if ln[:m.start()].replace("\\$", "").count("$") % 2:
                i = m.start() + 1
                continue
            ln = ln[:m.start()] + "$" + m.group(1) + "$" + ln[m.end():]
            i = m.start() + len(m.group(1)) + 2
        return ln
    return "\n".join(line(x) for x in md.split("\n"))

# --------------------------------------------------------------------------- references


class Refs:
    """Turn a tag into a link: to its place in this volume, or to the site, with the number of an entry."""

    def __init__(self, book: Book, volume: Volume):
        self.book, self.volume = book, volume

    def target(self, tag: str) -> str:
        n = self.book.corpus.nodes.get(tag)
        if n is None:
            return SITE + "/"
        if self.book.volume_of.get(tag) == self.volume.number:
            return "#" + n.slug
        return n.url

    def num(self, tag: str) -> str:
        num = self.book.ref(tag)
        return f" [{num}]{{.ref}}" if num else ""

    def link(self, tag: str, text: str | None = None) -> str:
        n = self.book.corpus.nodes.get(tag)
        name = text if text is not None else md_plain(n.name if n else tag)
        return f"[{name}]({self.target(tag)})" + self.num(tag)

    def wiki(self, md: str, self_tag: str = "") -> str:
        """[[text|TAG]] → [text](target) [number]."""
        def repl(m):
            text, tag = m.group(1), m.group(2)
            if tag not in self.book.corpus.nodes:
                return text
            if tag == self_tag:
                return text
            return self.link(tag, text)
        return LINK.sub(repl, md)

    def slashes(self, md: str) -> str:
        """[text](/TAG/) of the learner layer → [text](target) [number]."""
        def repl(m):
            text, tag = m.group(1), m.group(2)
            if tag not in self.book.corpus.nodes:
                return text
            return self.link(tag, text)
        return re.sub(r"(?<!!)\[([^\]]+)\]\(/([0-9A-Z]{6}|[0-9A-Z]{10})/\)", repl, md)

# --------------------------------------------------------------------------- sections of a body


def split_h2(body: str):
    """Split a body into [(heading or None, text)], ignoring headings inside code fences."""
    parts, cur_h, buf, fence = [], None, [], None
    for line in body.split("\n"):
        f = re.match(r"^(`{3,}|~{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)
            elif re.match(r"^" + re.escape(fence) + r"\s*$", line):
                fence = None
        if fence is None and line.startswith("## "):
            parts.append((cur_h, "\n".join(buf)))
            cur_h, buf = line[3:].strip(), []
        else:
            buf.append(line)
    parts.append((cur_h, "\n".join(buf)))
    return parts


def shift_headings(md: str, by: int) -> str:
    """Move every ATX heading down by `by` levels, outside code fences; mark them unnumbered."""
    out, fence = [], None
    for line in md.split("\n"):
        f = re.match(r"^(`{3,}|~{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)
            elif re.match(r"^" + re.escape(fence) + r"\s*$", line):
                fence = None
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line) if fence is None else None
        if m:
            lvl = min(6, len(m.group(1)) + by)
            text = m.group(2)
            if not text.endswith("}"):
                text += " {.unnumbered}"
            line = "#" * lvl + " " + text
        out.append(line)
    return "\n".join(out)


def rename_explanations(md: str) -> str:
    return re.sub(r"^(#{3,6}) (L[123] human)\s*$", lambda m: f"{m[1]} {EXPLANATIONS[m[2]]}", md, flags=re.M)


def _anchor(text: str) -> str:
    t = re.sub(r"\{[^{}]*\}\s*$", "", text).strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t).strip("-")


def scope_anchors(md: str, slug: str) -> str:
    """Give the section headings of an entry identifiers of their own (`direct-proof--remarks`)."""
    out, fence, ids = [], None, set(re.findall(r"\{#(" + re.escape(slug) + r"--[^\s}]+)", md))
    for line in md.split("\n"):
        f = re.match(r"^(`{3,}|~{3,})", line)
        if f:
            if fence is None:
                fence = f.group(1)[0]
            elif f.group(1)[0] == fence:
                fence = None
        elif fence is None and (m := re.match(r"^(#{4,6} )(.*?)(?:\s*\{([^{}]*)\})?\s*$", line)):
            attrs = m.group(3) or ""
            if "#" not in attrs and (a := _anchor(m.group(2))):
                ident, k = f"{slug}--{a}", 1
                while ident in ids:
                    k += 1
                    ident = f"{slug}--{a}-{k}"
                ids.add(ident)
                line = f"{m.group(1)}{m.group(2)} {{#{ident}{' ' + attrs if attrs else ''}}}"
        out.append(line)
    return "\n".join(out)

# --------------------------------------------------------------------------- sources


def _load_yaml(name: str) -> dict:
    p = os.path.join(ROOT, "data", name)
    return (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}


BOOKS = _load_yaml("books.yaml")     # isbn → {author, title, publisher, year}
DOIS = _load_yaml("dois.yaml")       # doi → {author, title, container, year}
ARXIV = _load_yaml("arxiv.yaml")     # arXiv id → {author, title, year}


def book_md(isbn: str) -> str:
    b = BOOKS.get(isbn)
    if not b:
        return f"ISBN {isbn}"
    return f"{b['author']}, *{b['title']}*, {b['publisher']}, {b['year']}"


def doi_md(doi: str) -> str:
    d = DOIS.get(doi.lower())
    link = f"<https://doi.org/{doi}>"
    if not d:
        return f"DOI {link}"
    parts = [d.get("author") or "", f"“{d['title']}”" if d.get("title") else "",
             f"*{d['container']}*" if d.get("container") else "", str(d.get("year") or "")]
    return ", ".join(p for p in parts if p) + f". {link}"


def _wiki_title(url: str) -> str:
    from urllib.parse import unquote
    t = unquote(url.split("/wiki/", 1)[1]).split("#")[0].replace("_", " ")
    return t


def source_key(s: dict) -> tuple[str, str]:
    """(kind, key) of a source: book, doi, arxiv, wikipedia or web."""
    if s.get("book"):
        return "book", str(s["book"]).removeprefix("isbn:")
    if s.get("doi"):
        return "doi", str(s["doi"]).lower()
    if s.get("arxiv"):
        return "arxiv", str(s["arxiv"])
    if s.get("wikipedia"):
        return "wikipedia", str(s["wikipedia"])
    url = str(s.get("url") or "")
    if re.match(r"https?://doi\.org/", url):
        return "doi", re.sub(r"https?://doi\.org/", "", url).lower()
    if re.match(r"https?://arxiv\.org/abs/", url):
        return "arxiv", re.sub(r"https?://arxiv\.org/abs/", "", url)
    if "wikipedia.org/wiki/" in url:
        return "wikipedia", _wiki_title(url)
    return "web", url


def source_md(kind: str, key: str) -> str:
    if kind == "book":
        return book_md(key)
    if kind == "doi":
        return doi_md(key)
    if kind == "arxiv":
        a = ARXIV.get(key)
        head = f"{a['author']}, “{a['title']}”, preprint, {a['year']}. " if a else ""
        return f"{head}arXiv:{key} <https://arxiv.org/abs/{key}>"
    if kind == "wikipedia":
        return f"Wikipedia, “{md_plain(key)}”"
    return f"<{key}>"


def fmt_sources(sources) -> list[str]:
    items = []
    for s in sources or []:
        if not isinstance(s, dict):
            continue
        kind, key = source_key(s)
        if not key:
            continue
        txt = source_md(kind, key)
        loc = str(s.get("locator") or s.get("sections") or "").strip().rstrip(".")
        if isinstance(s.get("sections"), list):
            loc = "sections " + ", ".join(map(str, s["sections"]))
        if loc:
            txt += ". " + md_plain(loc[0].upper() + loc[1:])
        items.append(txt.rstrip(".") + ".")
    return items

# --------------------------------------------------------------------------- an entry


def facts(node: Node, refs: Refs) -> str:
    fm = node.fm
    rows = []
    al = [str(a) for a in fm.get("aliases") or []
          if str(a).strip() and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", str(a))]   # not the site's slugs
    if al:
        rows.append(("Also called", ", ".join(md_plain(a) for a in al)))
    sp = [t for t in fm.get("specializes") or [] if isinstance(t, str) and t in refs.book.corpus.nodes]
    if sp:
        rows.append(("Special case of", ", ".join(refs.link(t) for t in sp)))
    uses = [t for t in fm.get("uses") or [] if isinstance(t, str) and t in refs.book.corpus.nodes]
    if uses:
        rows.append(("Uses", ", ".join(refs.link(t) for t in uses)))
    h = fm.get("history")
    if isinstance(h, dict):
        for k, label in (("first_stated", "First stated"), ("posed_by", "Posed by"), ("proved_by", "Proved by")):
            if h.get(k):
                rows.append((label, md_plain(str(h[k]))))
    msc = fm.get("msc") or []
    if msc:
        rows.append(("MSC", ", ".join(map(str, msc))))
    if not rows:
        return ""
    lines = ['::: {.facts latex-env="hbfacts"}']
    for k, v in rows:
        lines.append(f'[{k}]{{.fk latex-cmd="hbfk"}} {v}\n')
    lines.append(":::")
    return "\n".join(lines)


def body_md(node: Node, refs: Refs, drop_first: bool) -> tuple[str, str]:
    """(lead, rest) of a node body, with links rewritten."""
    body = fix_math(refs.wiki(node.body, node.tag))
    secs = split_h2(body)
    lead, out = "", []
    for i, (h, text) in enumerate(secs):
        if h is None:
            if text.strip():
                out.append(text.strip())
            continue
        if drop_first and not lead:
            lead = text.strip()
            continue
        out.append(f"## {h}\n\n{text.strip()}")
    return lead, rename_explanations("\n\n".join(out))


def attached_md(node: Node, host: Node, refs: Refs) -> str:
    lead, rest = body_md(node, refs, drop_first=True)
    title = f"{node.label}: {node.name}"
    rest = shift_headings(rest, 4)
    out = [f'::: {{#{node.slug} .proof latex-env="hbproof"}}',
           f'[{md_plain(title)}]{{.prooftitle latex-cmd="hbprooftitle"}}', "", lead, "", rest]
    items = fmt_sources(node.fm.get("sources"))
    if items:
        out += ["", "###### Sources {.unnumbered}", "", "\n".join(f"- {i}" for i in items)]
    out.append(":::")
    return "\n".join(out)


def entry_md(node: Node, num: str, refs: Refs) -> str:
    book = refs.book
    kind = node.label
    level = AUDIENCE.get(node.fm.get("audience") or "", "")
    lead, rest = body_md(node, refs, drop_first=True)
    head = [
        "```{=latex}",
        r"\hbentry{%s}{%s}{%s}{%s}{%s}" % (num, tex(node.name), node.slug, kind, level),
        "```",
        "",
        f"### [{num}]{{.num}} {md_plain(node.name)} {{#{node.slug} .html-only}}",
        "",
        f"[{kind}{' · ' + level if level else ''}]{{.badge .html-only}}",
        "",
        f'::: {{.lead latex-env="hblead"}}\n{lead}\n:::',
        "",
        facts(node, refs),
        "",
    ]
    parts = [rest]
    att = book.attached.get(node.tag, [])
    if att:
        names = {"example": "Examples", "counterexample": "Examples", "proof": "Proofs"}
        heading = " and ".join(sorted({names.get(n.kind, "Examples") for n in att}, reverse=True))
        parts.append(f"## {heading}\n\n" + "\n\n".join(attached_md(n, node, refs) for n in att))
    items = fmt_sources(node.fm.get("sources"))
    if items:
        parts.append("## Sources\n\n" + '::: {.refs latex-env="hbrefs"}\n' +
                     "\n".join(f"1. {i}" for i in items) + "\n:::")
    parts.append(f'[On the site: <{node.url}>]{{.siteline latex-cmd="hbsiteline"}}')
    md = "\n\n".join(p for p in parts if p and p.strip())
    md = shift_headings(md, 2)     # ## → ####, ### → #####
    md = scope_anchors(md, node.slug)
    return "\n".join(head) + "\n" + md + "\n"

# --------------------------------------------------------------------------- learner layer


def glue(book: Book, refs: Refs, *parts, shift: int = 2) -> str:
    """A page of the learner layer, with its links rewritten and its headings moved down."""
    t = book.text(*parts)
    if not t.strip():
        return ""
    t = fix_math(re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S))
    t = refs.slashes(t)
    return shift_headings(t, shift)


def glue_inline(refs: Refs, text: str) -> str:
    return refs.slashes(text)


def roadmap(book: Book, ch: Chapter, refs: Refs) -> str:
    rows = ["| | Entry | Kind | Examples |", "|---|---|---|--:|"]
    for e in ch.entries:
        n = len(book.attached.get(e.tag, []))
        rows.append(f"| {book.ref(e.tag)} | [{md_plain(e.name)}](#{e.slug}) | {e.label} | {n or '–'} |")
    return ('::: {.roadmap latex-env="hbroadmap"}\n' + "\n".join(rows) +
            f"\n\n: The entries of chapter {ch.num}.\n:::\n")


def chapter_md(book: Book, vol: Volume, ch: Chapter, refs: Refs) -> str:
    out = [
        "```{=latex}",
        r"\hbchapter{%s}{%s}{ch-%s}" % (ch.num, tex(ch.name), ch.id),
        "```",
        "",
        f"# [{ch.num}]{{.num}} {md_plain(ch.name)} {{#ch-{ch.id} .html-only}}",
        "",
    ]
    opening = glue(book, refs, vol.id, ch.id, "opening.md")
    if opening:
        out.append(opening)
    if ch.entries:
        out.append(roadmap(book, ch, refs))
    else:
        if not opening:
            out.append(refs.wiki(ch.node.section("Summary")) + "\n")
        out.append(f"The pages of this chapter are not written yet. The site keeps the plan of the topic: "
                   f"<{ch.node.url}>.\n")
    cid = "ch-" + ch.num.replace(".", "-")
    for gi, g in enumerate(ch.groups, 1):
        if g.title:
            out += ["```{=latex}", r"\hbgroup{%s}" % tex(g.title), "```", "",
                    f"## {md_plain(g.title)} {{#{cid}-g{gi} .html-only}}", ""]
            if g.intro:
                out.append(f'::: {{.groupintro latex-env="hbgroupintro"}}\n{glue_inline(refs, g.intro)}\n:::\n')
        for e in g.entries:
            out.append(entry_md(e, book.ref(e.tag), refs))
    for fname, title in [("summary.md", "Summary"), ("exercises.md", "Exercises"),
                         ("notes.md", "Notes and further reading")]:
        t = glue(book, refs, vol.id, ch.id, fname)
        if not t:
            continue
        if fname == "exercises.md":
            t = number_exercises(t, ch.num)
        out += ["```{=latex}", r"\hbgroup{%s}" % title, "```", "", f"## {title} {{#{cid}-{fname[:-3]} .html-only}}", "", t]
    return "\n".join(out) + "\n"


def number_exercises(md: str, chnum: str) -> str:
    """Give each exercise the number <chapter>.<k>: an item `7.` at the start of a line becomes **1.5.7**."""
    out = []
    for line in md.split("\n"):
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            k = m.group(1)
            out.append("§§OPEN")
            out.append(f'::: {{.exercise #ex-{chnum.replace(".", "-")}-{k} latex-env="hbexercise"}}\n'
                       f'**{chnum}.{k}** {m.group(2)}')
        else:
            out.append(line)
    res, open_ = [], False
    for line in out:
        if line == "§§OPEN":
            if open_:
                res.append(":::\n")
            open_ = True
            continue
        if open_ and re.match(r"^#{1,6} ", line):
            res.append(":::\n")
            open_ = False
        res.append(line)
    if open_:
        res.append(":::")
    return "\n".join(res)


def hints_md(book: Book, vol: Volume, refs: Refs) -> str:
    out = []
    for ch in vol.chapters:
        t = glue(book, refs, vol.id, ch.id, "hints.md")
        if not t:
            continue
        t = re.sub(r"^(\d+)\.\s+", lambda m: f"**[{ch.num}.{m.group(1)}](#ex-{ch.num.replace('.', '-')}-{m.group(1)})** ",
                   t, flags=re.M)
        out.append(f"#### Chapter {ch.num}: {md_plain(ch.name)} {{.unnumbered}}\n\n"
                   f'::: {{.hints latex-env="hbhints"}}\n{t}\n:::')
    return "\n\n".join(out)
