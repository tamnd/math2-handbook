"""mh: build The Math 2.0 Handbook from the math2 project.

    python -m mh survey  [--content ../math2]
    python -m mh check   [--content ../math2] [--volume N]
    python -m mh brief   [--content ../math2] --volume N [--chapter K] [--sections]
    python -m mh build   [--content ../math2] [--volume N|all] [--formats tex,pdf,epub]
"""

from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import sys
import time

from .book import Book
from .corpus import LINK, Corpus

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAGLINK = re.compile(r"\]\(/([0-9A-Z]{6}|[0-9A-Z]{10})/(?:#[^)]*)?\)")


def _edition() -> dict:
    """The file EDITION: 'version 0.1.1' and 'content <commit of tamnd/math2>'."""
    out = {"version": "0.1", "content": ""}
    path = os.path.join(ROOT, "EDITION")
    if os.path.exists(path):
        for line in open(path):
            k, _, v = line.strip().partition(" ")
            if k:
                out[k] = v.strip()
    return out


EDITION = _edition()["version"]


def load(args) -> Book:
    t = time.time()
    corpus = Corpus(os.path.abspath(os.path.expanduser(args.content)))
    book = Book(corpus, os.path.join(ROOT, "content"))
    commit = corpus.commit()
    print(f"corpus {commit[:8]}: {len(corpus.nodes)} nodes, loaded in {time.time() - t:.1f}s", file=sys.stderr)
    pinned = _edition()["content"]
    if pinned and commit and not pinned.startswith(commit[:8]):
        print(f"note: EDITION pins content {pinned[:8]}, but the content is at {commit[:8]}", file=sys.stderr)
    return book


def volumes(book: Book, which: str):
    if which == "all":
        return [v for v in book.volumes if v.built]
    nums = {int(x) for x in which.split(",")}
    return [v for v in book.volumes if v.number in nums]


def cmd_survey(args):
    book = load(args)
    for v in book.volumes:
        e = len(v.entries)
        a = sum(len(book.attached[x.tag]) for x in v.entries)
        w = sum(n.words for n in v.entries) + sum(n.words for x in v.entries for n in book.attached[x.tag])
        empty = sum(1 for c in v.chapters if not c.entries)
        print(f"{v.number:>2} {v.name:<28} chapters {len(v.chapters):>3} (unwritten {empty:>2})  entries {e:>4}  "
              f"attached {a:>4}  words {w:>9,}")


BANNED = (r"\b(leverag(?:e|es|ed|ing)|showcas(?:e|es|ed|ing)|powerful|elegant(?:ly)?|seamless(?:ly)?|crucial(?:ly)?|"
          r"delv(?:e|es|ed|ing)|journey|landscape)\b")


def check_content(book: Book, which) -> list[str]:
    """Problems in the learner layer: links to unknown tags, files in unknown places, bad exercise numbers."""
    probs = []
    areas = {v.id: {c.id: c for c in v.chapters} for v in book.volumes}
    for f in sorted(glob.glob(os.path.join(book.content, "**", "*.*"), recursive=True)):
        rel = os.path.relpath(f, book.content)
        parts = rel.split(os.sep)
        if len(parts) == 1:
            continue   # PROVENANCE.md and other notes about the directory
        if parts[0] not in areas:
            probs.append(f"{rel}: unknown area {parts[0]}")
            continue
        if len(parts) == 3 and parts[1] not in areas[parts[0]]:
            probs.append(f"{rel}: unknown chapter {parts[1]}")
        t = open(f, encoding="utf-8").read()
        for tag in TAGLINK.findall(t):
            if tag not in book.corpus.nodes:
                probs.append(f"{rel}: link to unknown tag /{tag}/")
        if re.search(r"\]\(/[a-z0-9-]+/\)", t):
            probs.append(f"{rel}: link by slug; write links as [text](/TAG/)")
        if LINK.search(t):
            probs.append(f"{rel}: wiki link [[…|TAG]]; write links as [text](/TAG/)")
        prose = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$|`[^`\n]*`|```.*?```", " ", t, flags=re.S)
        prose = re.sub(r"\]\(/[^)]*\)", "]", prose)
        prose = re.sub(r"\bmost powerful\b", " ", prose, flags=re.I)
        for w in sorted(set(re.findall(BANNED, prose, flags=re.I))):
            probs.append(f"{rel}: style: '{w}' (see the writing standard in prompts/area.md)")
        if re.search(r"[A-Za-z)]!(\s|$)", prose):
            probs.append(f"{rel}: style: exclamation mark")
        if re.search(r"\bIn this chapter,? we will\b", prose):
            probs.append(f"{rel}: style: 'In this chapter, we will'")
        if re.search(r"\b(AI|language model|LLM)\b", prose):
            probs.append(f"{rel}: style: mentions AI")
        if f.endswith("exercises.md"):
            nums = [int(x) for x in re.findall(r"^(\d+)\.\s", t, flags=re.M)]
            if nums != list(range(1, len(nums) + 1)):
                probs.append(f"{rel}: exercises are not numbered 1..{len(nums)}")
            for n, band in re.findall(r"^(\d+)\.\s+(\S)", t, flags=re.M):
                if band not in "◦•★":
                    probs.append(f"{rel}: exercise {n} has no band mark")
            hp = f.replace("exercises.md", "hints.md")
            if os.path.exists(hp):
                hn = [int(x) for x in re.findall(r"^(\d+)\.\s", open(hp).read(), flags=re.M)]
                bad = [h for h in hn if h > len(nums)]
                if bad:
                    probs.append(f"{rel}: hints for missing exercises {bad}")
    return probs


def cmd_check(args):
    book = load(args)
    for v in volumes(book, args.volume):
        for c in v.chapters:
            for w in c.warnings:
                print(f"{c.num} {c.id}: {w}")
    for p in check_content(book, args.volume):
        print(p)


def _reading_notes(book: Book, ch) -> dict:
    """The description after each item of the reading order: '3. [[Name|TAG]]: what it is'."""
    out = {}
    for line in ch.node.subsection("Reading order").split("\n"):
        m = LINK.search(line)
        if m:
            out.setdefault(m[2], line[m.end():].lstrip(" :—-").strip())
    return out


def cmd_brief(args):
    """A brief of a volume or chapter for writers of the learner layer."""
    book = load(args)
    v = book.volume(args.volume)
    print(f"# Volume {v.number} `{v.id}`: {v.name} (area {v.tag})\n")
    if not args.chapter:
        print(v.node.body.strip() + "\n")
    for ch in v.chapters:
        if args.chapter and str(ch.number) != str(args.chapter):
            continue
        att = sum(len(book.attached[e.tag]) for e in ch.entries)
        print(f"## Chapter {ch.num} `{ch.id}`: {ch.name} (sub-area {ch.tag}; {len(ch.entries)} entries, "
              f"{att} attached proofs and examples)\n")
        print(ch.node.section("Summary") + "\n")
        pre = ch.node.subsection("Prerequisites")
        if pre:
            print("Prerequisites (from the sub-area page):\n\n" + pre + "\n")
        notes = _reading_notes(book, ch)
        for e in ch.entries:
            heads = [l[3:].strip() for l in e.body.split("\n") if l.startswith("## ")]
            line = (f"- **{book.ref(e.tag)} {e.name}** `{e.tag}` [{e.label}, {e.words} words]. "
                    f"{notes.get(e.tag) or e.short(2)}")
            if args.sections:
                line += f" Sections: {' / '.join(heads)}."
            print(line)
            for n in book.attached[e.tag]:
                print(f"    - with {n.label.lower()} *{n.name}* `{n.tag}` ({n.words} words)")
        print()


def slugname(v) -> str:
    return f"{v.number:02d}-{v.id}"


def cmd_build(args):
    from . import latex
    from .volume import volume_md
    book = load(args)
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    date = (datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).date() if epoch
            else datetime.date.today()).isoformat()
    formats = set(args.formats.split(","))
    report, failed = {}, []
    for v in volumes(book, args.volume):
        t = time.time()
        out = os.path.join(ROOT, "build", slugname(v))
        md, stats = volume_md(book, v)
        info = dict(stats, warnings=len(stats["warnings"]))
        if formats & {"tex", "pdf"}:
            info.update(latex.build(book, v, md, out, EDITION, date, pdf="pdf" in formats))
            if "pdf" in formats and not info.get("ok"):
                failed.append(v.number)
        if "epub" in formats:
            from . import epub
            info.update(epub.build(book, v, md, out, EDITION, date))
        info["seconds"] = round(time.time() - t, 1)
        report[v.number] = info
        err = info.pop("error", None)
        print(f"vol {v.number} {v.name}: " + json.dumps({k: x for k, x in info.items() if k != "missing_glyphs"}))
        if info.get("missing_glyphs"):
            print("  missing glyphs:", "".join(list(info["missing_glyphs"])[:60]))
        for w in stats["warnings"][:20]:
            print("  warning:", w)
        if err:
            print(err)
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    json.dump(report, open(os.path.join(ROOT, "build", "report.json"), "w"), indent=1, ensure_ascii=False)
    if failed:
        sys.exit(f"LaTeX failed for volume(s) {', '.join(map(str, failed))}")


def main():
    ap = argparse.ArgumentParser(prog="mh")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("survey", "check", "build", "brief"):
        p = sub.add_parser(name)
        p.add_argument("--content", default=os.path.join(ROOT, "..", "math2"))
        if name != "survey":
            p.add_argument("--volume", default="all")
        if name == "build":
            p.add_argument("--formats", default="tex,pdf")
        if name == "brief":
            p.add_argument("--chapter", default="")
            p.add_argument("--sections", action="store_true")
    args = ap.parse_args()
    {"survey": cmd_survey, "check": cmd_check, "build": cmd_build, "brief": cmd_brief}[args.cmd](args)


if __name__ == "__main__":
    main()
