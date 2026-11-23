"""The content of tamnd/math2: the node files, read once.

A node is `nodes/<first three characters of the tag>/<tag>.md`: YAML front matter and a Markdown body. Links in a
body have the form [[text|TAG]]. An area is a topic node with no parent topic; its body lists the sub-areas under
`### Sub-areas`, and the body of each sub-area lists its pages under `### Reading order`.
"""

from __future__ import annotations

import glob
import os
import pickle
import re
import subprocess
import unicodedata

import yaml

try:
    from yaml import CSafeLoader as _Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as _Loader

SITE = "https://math2.tamnd.com"
LINK = re.compile(r"\[\[([^\]|]*)\|([0-9A-Z]{6}|[0-9A-Z]{10})\]\]")

KIND_LABEL = {"concept": "Concept", "definition": "Definition", "statement": "Theorem", "conjecture": "Conjecture",
              "problem": "Problem", "example": "Example", "counterexample": "Counterexample", "object": "Object",
              "proof": "Proof", "computation": "Computation", "topic": "Topic"}
ROLE_LABEL = {"theorem": "Theorem", "lemma": "Lemma", "proposition": "Proposition", "corollary": "Corollary",
              "principle": "Principle", "axiom": "Axiom", "fact": "Fact", "formula": "Formula",
              "identity": "Identity", "inequality": "Inequality", "criterion": "Criterion", "law": "Law",
              "rule": "Rule", "schema": "Schema", "test": "Test", "conjecture": "Conjecture"}


def slugify(name: str) -> str:
    """The slug of a name, as the site makes it (math2-agent site/slug.go)."""
    out, hyphen = [], False
    for r in unicodedata.normalize("NFD", name):
        if unicodedata.category(r) == "Mn" or r in "'’":
            continue
        if "a" <= r <= "z" or "0" <= r <= "9":
            pass
        elif "A" <= r <= "Z":
            r = r.lower()
        else:
            hyphen = bool(out)
            continue
        if hyphen:
            out.append("-")
            hyphen = False
        out.append(r)
    return "".join(out)


SLUG_KINDS = ["topic", "concept", "definition", "statement", "conjecture", "problem", "object", "example",
              "counterexample", "proof", "computation", "exercise"]


def _targets(v) -> list[str]:
    # A field holds one target or a list of them; a single target (`proves: 0R7SVNYTJS`) is a plain string.
    if isinstance(v, (str, dict)):
        v = [v]
    out = []
    for x in v or []:
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, dict) and x.get("target"):
            out.append(x["target"])
    return out


class Node:
    __slots__ = ("tag", "fm", "body", "slug", "path")

    def __init__(self, tag, fm, body, path):
        self.tag, self.fm, self.body, self.path = tag, fm, body, path
        self.slug = tag.lower()

    @property
    def name(self) -> str: return self.fm.get("name") or self.tag
    @property
    def kind(self) -> str: return self.fm.get("kind", "concept")
    @property
    def role(self) -> str: return self.fm.get("role") or ""
    @property
    def words(self) -> int: return len(self.body.split())
    @property
    def url(self) -> str: return f"{SITE}/wiki/{self.slug}/"

    @property
    def label(self) -> str:
        """Theorem, Lemma, Definition, Concept …"""
        if self.kind == "statement":
            return ROLE_LABEL.get(self.role, self.role.title() or "Theorem")
        return KIND_LABEL.get(self.kind, self.kind.title())

    def section(self, title: str) -> str:
        m = re.search(r"^## " + re.escape(title) + r"[ \t]*\n(.*?)(?=^## |\Z)", self.body, re.S | re.M)
        return m.group(1).strip() if m else ""

    def subsection(self, title: str) -> str:
        m = re.search(r"^### " + re.escape(title) + r"[ \t]*\n(.*?)(?=^##+ |\Z)", self.body, re.S | re.M)
        return m.group(1).strip() if m else ""

    @property
    def summary(self) -> str:
        """The first section of the body (Summary, Definition, Statement, Example …), the lead of the entry."""
        m = re.search(r"^## [^\n]*\n(.*?)(?=^## |\Z)", self.body, re.S | re.M)
        return m.group(1).strip() if m else self.body.strip()

    def short(self, n: int = 1) -> str:
        """The first n sentences of the summary, links as plain text."""
        t = LINK.sub(lambda m: m[1], self.summary)
        sents = re.split(r"(?<=[.!?])\s+(?=[A-Z$])", t.replace("\n", " "))
        return " ".join(sents[:n]).strip()

    def links(self) -> list[str]:
        return [m[2] for m in LINK.finditer(self.body)]

    def targets(self, field: str) -> list[str]:
        return _targets(self.fm.get(field))


def split_front(text: str):
    if not text.startswith("---"):
        return {}, text
    fm, _, body = text[3:].partition("\n---")
    return yaml.load(fm, Loader=_Loader) or {}, body.lstrip("\n")


class Corpus:
    def __init__(self, root: str):
        self.root = root
        self.nodes: dict[str, Node] = {}
        commit = self.commit()
        cache = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build",
                             f".corpus-{commit[:12]}.pickle")
        if commit and os.path.exists(cache):
            with open(cache, "rb") as f:
                for tag, fm, body, p in pickle.load(f):
                    self.nodes[tag] = Node(tag, fm, body, p)
        else:
            for p in glob.glob(os.path.join(root, "nodes", "*", "*.md")):
                fm, body = split_front(open(p, encoding="utf-8").read())
                tag = fm.get("tag")
                if not tag or fm.get("retired"):
                    continue
                self.nodes[tag] = Node(tag, fm, body, p)
            if commit:
                os.makedirs(os.path.dirname(cache), exist_ok=True)
                with open(cache + ".tmp", "wb") as f:
                    pickle.dump([(n.tag, n.fm, n.body, n.path) for n in self.nodes.values()], f, protocol=5)
                os.replace(cache + ".tmp", cache)
        self._slugs()
        self.macros = self._macros()

    def _slugs(self):
        """Slugs as the site assigns them: by kind, then tag; the name, else name-kind, else name-tag."""
        rank = {k: i for i, k in enumerate(SLUG_KINDS)}
        used = set()
        for n in sorted(self.nodes.values(), key=lambda n: (rank.get(n.kind, len(SLUG_KINDS)), n.tag)):
            n.slug = n.tag.lower()
            base = slugify(n.name)
            if base:
                for s in (base, base + "-" + n.kind, base + "-" + n.slug):
                    if s not in used:
                        n.slug = s
                        break
            used.add(n.slug)

    def _macros(self) -> str:
        p = os.path.join(self.root, "macros", "m2.sty")
        if not os.path.exists(p):
            return ""
        return "\n".join(l for l in open(p) if l.startswith("\\newcommand"))

    def commit(self) -> str:
        try:
            return subprocess.run(["git", "-C", self.root, "rev-parse", "HEAD"], capture_output=True,
                                  text=True).stdout.strip()
        except Exception:
            return ""

    def listed(self, tag: str, heading: str) -> list[str]:
        """The tags linked in the list under `### heading` of a topic body, in order, once each."""
        n = self.nodes.get(tag)
        if not n:
            return []
        # The list may be split into several sections `### heading: part` or `### heading, continued: part`, read
        # in order. An area whose list of sub-areas has no section of its own keeps it as the numbered list under
        # `### How to read the area`.
        ms = list(re.finditer(r"^### " + re.escape(heading) + r"(?:(?::|, continued:)[^\n]*)?[ \t]*\n(.*?)(?=^#|\Z)", n.body,
                              re.S | re.M))
        if not ms and heading == "Sub-areas":
            ms = list(re.finditer(r"^### How to read the area[ \t]*\n(.*?)(?=^#|\Z)", n.body, re.S | re.M))
        out = []
        for m in ms:
            for line in m.group(1).split("\n"):
                if re.match(r"^\s*(\d+\.|[-*])\s", line):
                    k = LINK.search(line)
                    if k and k[2] not in out:
                        out.append(k[2])
        return out
