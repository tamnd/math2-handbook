"""The apparatus of a volume: the bibliography and the index."""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

from .book import Book, Volume
from .prep import Refs, md_plain, source_key, source_md

MAX_REFS = 24


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\$[^$]*\$", "", s)
    return re.sub(r"^[^A-Za-z0-9]+", "", s.lower())


def numkey(num: str):
    return [int(x) for x in num.split(".")]


def _letter(term: str) -> str:
    f = fold(term)
    if f and f[0].isalpha():
        return f[0].upper()
    return "0–9" if f and f[0].isdigit() else "Symbols"


def _entry_of(book: Book, tag: str) -> str:
    """The entry a tag belongs to: itself, or the entry an example is printed with."""
    return book.host.get(tag, tag)


def _links(book: Book, refs: Refs, tags, main: str | None = None) -> str:
    ents = {_entry_of(book, t) for t in tags}
    nums = sorted({t for t in ents if book.ref(t)}, key=lambda t: numkey(book.ref(t)))
    more = 0
    if len(nums) > MAX_REFS:
        more = len(nums) - MAX_REFS
        nums = nums[:MAX_REFS]
    parts = []
    for t in nums:
        s = f"[{book.ref(t)}]({refs.target(t)})"
        parts.append(f"**{s}**" if t == main else s)
    if more:
        parts.append(f"and {more} more")
    return ", ".join(parts)


def _render(groups: dict[str, list[str]]) -> str:
    out = ['::: {.index latex-env="hbindex"}']
    for letter in sorted(groups, key=lambda x: (len(x) > 1, x)):
        out.append(f"```{{=latex}}\n\\hbidxletter{{{letter}}}\n```\n")
        out.append(f"[{letter}]{{.idxletter .html-only}}\n")
        out += groups[letter]
    out.append(":::")
    return "\n".join(out)


def _pages(book: Book, vol: Volume):
    """Every node printed in the volume: the entries and their examples."""
    for e in vol.entries:
        yield e
        yield from book.attached.get(e.tag, [])


def subject_index(book: Book, vol: Volume, refs: Refs) -> str:
    nodes = book.corpus.nodes
    mentioned = defaultdict(set)   # tag -> printed nodes of this volume that link to it
    for p in _pages(book, vol):
        for t in set(p.links()) | {t for t in p.fm.get("uses") or [] if isinstance(t, str)}:
            if t != p.tag and t in nodes:
                mentioned[t].add(p.tag)
    terms = {}   # display -> markdown line
    for e in vol.entries:
        terms[e.name] = f"{md_plain(e.name)}, {_links(book, refs, {e.tag} | mentioned.get(e.tag, set()), main=e.tag)}\n"
        for a in e.fm.get("aliases") or []:
            a = str(a)
            if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", a):
                continue   # a slug of the site, not a name
            if fold(a) != fold(e.name) and a not in terms:
                terms[a] = f"{md_plain(a)}, *see* [{md_plain(e.name)}]({refs.target(e.tag)})\n"
    # pages outside the volume that its entries use: the site has them
    for t, users in mentioned.items():
        if book.volume_of.get(t) == vol.number:
            continue
        n = nodes[t]
        if n.name in terms or n.kind in ("example", "counterexample", "proof"):
            continue
        where = f"[{book.ref(t)}]({refs.target(t)})" if book.ref(t) else f"[site]({refs.target(t)})"
        terms[n.name] = f"{md_plain(n.name)} ({where}), used in {_links(book, refs, users)}\n"
    groups = defaultdict(list)
    for t in sorted(terms, key=fold):
        groups[_letter(t)].append(terms[t])
    return _render(groups)


def bibliography(book: Book, vol: Volume, refs: Refs) -> str:
    where = defaultdict(set)
    for p in _pages(book, vol):
        for s in p.fm.get("sources") or []:
            if isinstance(s, dict):
                k = source_key(s)
                if k[1]:
                    where[k].add(p.tag)
    by_kind = defaultdict(list)
    for k in where:
        by_kind[k[0]].append(k)
    out = []
    sections = [("book", "Books"), ("doi", "Articles and chapters"), ("arxiv", "Preprints")]
    for kind, title in sections:
        ks = by_kind.get(kind)
        if not ks:
            continue
        out.append(f"#### {title} {{.unnumbered}}\n")
        out.append('::: {.bibliography latex-env="hbbib"}')
        for k in sorted(ks, key=lambda k: fold(re.sub(r"[*“”<>]", "", source_md(*k)))):
            txt = source_md(*k).rstrip(".")
            out.append(f"{txt}. Cited in {_links(book, refs, where[k])}.\n")
        out.append(":::\n")
    nw, nweb = len(by_kind.get("wikipedia", [])), len(by_kind.get("web", []))
    if nw or nweb:
        arts = "article" if nw == 1 else "articles"
        pages = "page" if nweb == 1 else "pages"
        out.append(f"The entries of this volume also cite {nw} {arts} of Wikipedia and {nweb} other web {pages}. "
                   "Each entry lists its own sources at its end, with the section or page cited.\n")
    return "\n".join(out)
