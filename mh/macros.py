"""The macros of the site (macros/m2.sty of tamnd/math2).

The LaTeX gets them in the preamble of main.tex. The EPUB's MathML writer knows none of them, so they are
expanded here, inside the mathematics of the Markdown. Pandoc reads the Markdown with `-latex_macros`: given the
definitions in the text it would expand them itself, but it is slow at that on a volume of this size."""

from __future__ import annotations

import re

_DEF = re.compile(r"\\newcommand\{\\([A-Za-z]+)\}(?:\[(\d)\])?\{(.*)\}\s*$")


def parse(lines: str) -> dict[str, tuple[int, str]]:
    out = {}
    for ln in lines.splitlines():
        m = _DEF.match(ln.strip())
        if m:
            out[m[1]] = (int(m[2] or 0), m[3])
    return out


def preamble(lines: str) -> str:
    """The definitions for main.tex: \\providecommand then \\renewcommand, so a name that a package already
    defines takes the site's meaning, as on the site."""
    out = []
    for name, (n, body) in parse(lines).items():
        arg = f"[{n}]" if n else ""
        out.append(f"\\providecommand{{\\{name}}}{{}}\\renewcommand{{\\{name}}}{arg}{{{body}}}")
    return "\n".join(out)


def _arg(s: str, i: int) -> tuple[str, int] | None:
    """The argument of a macro at s[i:]: a balanced {group}, a control word, or one character."""
    while i < len(s) and s[i] in " \t\n":
        i += 1
    if i >= len(s):
        return None
    if s[i] == "{":
        depth, j = 0, i
        while j < len(s):
            c = s[j]
            if c == "\\":
                j += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
            j += 1
        return None
    if s[i] == "\\":
        m = re.match(r"\\([A-Za-z]+|.)", s[i:])
        return m.group(0), i + m.end()
    return s[i], i + 1


def expand(math: str, defs: dict[str, tuple[int, str]], depth: int = 0) -> str:
    if depth > 8 or "\\" not in math:
        return math
    rx = re.compile(r"\\(" + "|".join(sorted(defs, key=len, reverse=True)) + r")(?![A-Za-z])")
    out, i = [], 0
    while True:
        m = rx.search(math, i)
        if not m:
            out.append(math[i:])
            break
        # an escaped backslash before it (`\\N` is a line break and an N)
        k, bs = m.start() - 1, 0
        while k >= 0 and math[k] == "\\":
            bs, k = bs + 1, k - 1
        if bs % 2:
            out.append(math[i:m.end()])
            i = m.end()
            continue
        n, body = defs[m[1]]
        j, args = m.end(), []
        for _ in range(n):
            a = _arg(math, j)
            if a is None:
                break
            args.append(expand(a[0], defs, depth + 1))
            j = a[1]
        if len(args) < n:
            out.append(math[i:m.end()])
            i = m.end()
            continue
        rep = body
        for k2, a in enumerate(args, 1):
            rep = rep.replace(f"#{k2}", a)
        # a control word right after the expansion must stay apart from it: `\R x` → `\mathbb{R} x`
        if not n and rep[-1:].isalpha() and math[j:j + 1].isalpha():
            rep += " "
        if math[:m.start()].rstrip()[-1:] in ("_", "^"):   # a bare script, `S_\N`: it needs its braces
            rep = "{" + rep + "}"
        out.append(math[i:m.start()] + rep)
        i = j
    return "".join(out)


_MATH = re.compile(r"\$\$.*?\$\$|(?<![\\$])\$[^$\n]+\$", re.S)


def expand_md(md: str, lines: str) -> str:
    defs = parse(lines)
    if not defs:
        return md
    return _MATH.sub(lambda m: expand(m.group(0), defs), md)
