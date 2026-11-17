"""The structure of the set: volumes, chapters, groups and entries, with their numbers.

A volume is an area of math2 (a root topic), a chapter is one of its sub-areas, and the entries of a chapter are the
pages of the sub-area's reading order, in that order. Proofs, examples and counterexamples of an entry are printed
with it and take no number of their own.
"""

from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass, field

import yaml

from .corpus import Corpus, Node, slugify

# The volumes of this edition: number -> tag of the area.
VOLUMES = {1: "SGSVYFDSYK", 2: "DYJ0KGTPMR"}


@dataclass
class Group:
    title: str
    intro: str = ""
    entries: list = field(default_factory=list)   # [Node]


@dataclass
class Chapter:
    volume: int
    number: int
    id: str
    name: str
    node: Node
    groups: list = field(default_factory=list)    # [Group]
    warnings: list = field(default_factory=list)

    @property
    def num(self): return f"{self.volume}.{self.number}"
    @property
    def entries(self): return [e for g in self.groups for e in g.entries]
    @property
    def tag(self): return self.node.tag


@dataclass
class Volume:
    number: int
    id: str
    name: str
    node: Node
    chapters: list = field(default_factory=list)

    @property
    def entries(self): return [e for c in self.chapters for e in c.entries]
    @property
    def built(self): return True
    @property
    def summary(self): return self.node.summary
    @property
    def tag(self): return self.node.tag


class Book:
    def __init__(self, corpus: Corpus, content_dir: str, numbers: dict | None = None):
        self.corpus = corpus
        self.content = content_dir
        self.volumes: list[Volume] = []
        self.number: dict[str, str] = {}      # tag -> "1.2.3" for entries
        self.volume_of: dict[str, int] = {}   # tag -> volume number, for entries and attached nodes
        self.chapter_of: dict[str, Chapter] = {}
        self.host: dict[str, str] = {}        # tag of an attached proof or example -> tag of its entry
        self.attached: dict[str, list[Node]] = defaultdict(list)   # entry tag -> proofs, examples
        self._attachments()
        self._build(numbers or VOLUMES)

    # -- files of the learner layer --------------------------------------------------------
    def path(self, *parts) -> str:
        return os.path.join(self.content, *parts)

    def text(self, *parts) -> str:
        p = self.path(*parts)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

    # -- structure --------------------------------------------------------------------------
    def _attachments(self):
        self.of: dict[str, list[Node]] = defaultdict(list)   # target tag -> nodes that attach to it
        for n in sorted(self.corpus.nodes.values(), key=lambda n: (n.kind != "proof", n.name.lower(), n.tag)):
            if n.kind == "proof":
                for t in n.targets("proves"):
                    self.of[t].append(n)
            elif n.kind in ("example", "counterexample"):
                for f in ("instance_of", "not_instance_of", "illustrates"):
                    for t in n.targets(f):
                        if n not in self.of[t]:
                            self.of[t].append(n)

    def _build(self, numbers: dict):
        nodes = self.corpus.nodes
        for vn, atag in sorted(numbers.items()):
            a = nodes[atag]
            v = Volume(vn, slugify(a.name), a.name, a)
            for cn, stag in enumerate(self.corpus.listed(atag, "Sub-areas"), 1):
                s = nodes[stag]
                ch = Chapter(vn, cn, slugify(s.name), s.name, s)
                order = []
                for t in self.corpus.listed(stag, "Reading order"):
                    if t not in nodes:
                        ch.warnings.append(f"reading order lists {t}, which is not a node; dropped")
                    elif t in self.number:
                        ch.warnings.append(f"{t} {nodes[t].name} is entry {self.number[t]} already; dropped")
                    else:
                        order.append(nodes[t])
                ch.groups = self._groups(v, ch, order)
                for k, e in enumerate(ch.entries, 1):
                    self.number[e.tag] = f"{vn}.{cn}.{k}"
                    self.volume_of[e.tag] = vn
                    self.chapter_of[e.tag] = ch
                v.chapters.append(ch)
            self.volumes.append(v)
        # attach proofs and examples to the first entry they serve, unless they are entries themselves
        for v in self.volumes:
            for e in v.entries:
                for n in self.of.get(e.tag, []):
                    if n.tag in self.number or n.tag in self.host:
                        continue
                    self.host[n.tag] = e.tag
                    self.volume_of[n.tag] = v.number
                    self.attached[e.tag].append(n)

    def _groups(self, v: Volume, ch: Chapter, order: list[Node]) -> list[Group]:
        p = self.path(v.id, ch.id, "outline.yaml")
        if not order:
            return []
        if not os.path.exists(p):
            return [Group("", "", order)]
        spec = yaml.safe_load(open(p, encoding="utf-8")) or {}
        by_tag = {n.tag: n for n in order}
        groups, seen = [], []
        for g in spec.get("groups", []):
            grp = Group(g.get("title", ""), (g.get("intro") or "").strip())
            for t in g.get("entries", []):
                t = str(t)
                if t in seen:
                    ch.warnings.append(f"outline lists {t} twice")
                elif t not in by_tag:
                    ch.warnings.append(f"outline entry {t} is not in the reading order of {ch.name}; dropped")
                else:
                    seen.append(t)
                    grp.entries.append(by_tag[t])
            if grp.entries:
                groups.append(grp)
        rest = [n for n in order if n.tag not in seen]
        if rest:
            ch.warnings.append("not in the outline: " + ", ".join(n.tag for n in rest))
            groups.append(Group("Other entries", "", rest))
        if [n.tag for n in order if n.tag in seen] != seen:
            ch.warnings.append("the outline changes the reading order")
        return groups

    def volume(self, n) -> Volume:
        for v in self.volumes:
            if str(v.number) == str(n) or v.id == n:
                return v
        raise KeyError(n)

    def ref(self, tag: str) -> str | None:
        return self.number.get(tag)
