## What to remember

- **Read the conventions first.** A symbol means what its book has declared, and the common conflicts are known: whether $0 \in \N$, whether $A \subset B$ allows $A = B$, whether "increasing" is strict, whether $f^2$ is $f \circ f$ or $x \mapsto f(x)^2$, and which base $\log$ has. A letter bound by $\sum$, $\int$ or a quantifier may be renamed; the value of the expression depends only on its free letters.
- **Equality signs are different relations.** $a = b$ says that two names denote one object; $a := b$ defines the new name $a$; $a \equiv b \pmod n$ is congruence; $\approx$ is approximate equality and is not transitive; $\cong$ is isomorphism. In $f(n) = O(g(n))$ the sign is read in one direction only.
- **An abuse of notation is safe when the hidden map is well defined.** Writing $a$ for the class $[a] \in \Z/n$ is harmless for $+$ and $\cdot$, because the result does not depend on the representative; a rule such as $[a] \mapsto [2^a]$ from $\Z/4$ to $\Z/7$ fails that test.
- **Abbreviations carry logic.** "i.e." joins two equivalent statements, "e.g." gives one instance, "resp." pairs two lists term by term, and "wlog" is valid only after a symmetry of the statement has been named.
- **Canonical means "free of choices".** A canonical form for an equivalence relation $\sim$ on $X$ is a map $c$ with $c(x) \sim x$ and $x \sim y \Rightarrow c(x) = c(y)$; then $x \sim y \iff c(x) = c(y)$, so computing forms decides equivalence.
- **"Almost all" needs a sense.** The exceptions may be required to be finite, of density zero, countable, of measure zero, or meagre. On $\N$, "all but finitely many" implies "all but a set of density zero", and not conversely. Finite unions of negligible sets are negligible in every sense; countable unions only in the countable, measure and category senses.
- **Eventually and frequently are quantifier patterns.** "$P(n)$ for all sufficiently large $n$" is $\exists N \, \forall n \ge N \, P(n)$; "$P(n)$ frequently" is $\forall N \, \exists n \ge N \, P(n)$. The negation of "eventually $P$" is "frequently not $P$".
- **Stronger, sharp, elementary.** $A$ is stronger than $B$ when $A \Rightarrow B$. A constant $C$ in $f(x) \le C g(x)$ (with $g > 0$ on the class $X$) is sharp when $C = \sup_X f/g$; it is attained when some $x_0$ gives equality. An elementary proof uses only an agreed list of tools; "deep" means that every known proof uses ideas far beyond the statement.

## How often a property holds

| Statement about $P(n)$, $n \in \N$ | Formal meaning | $n \ge 5$ | $n$ not a square | $n$ odd | $n = 3$ |
|---|---|---|---|---|---|
| for all $n$ | $\forall n \, P(n)$ | no | no | no | no |
| for all sufficiently large $n$ | $\exists N \, \forall n \ge N \, P(n)$ | yes | no | no | no |
| for almost all $n$ (density) | the exceptions have density $0$ | yes | yes | no | no |
| frequently | $\forall N \, \exists n \ge N \, P(n)$ | yes | yes | yes | no |
| for some $n$ | $\exists n \, P(n)$ | yes | yes | yes | yes |

: Each row implies every row below it, and each column shows a property that separates two adjacent rows, so none of the implications can be reversed.

## Common errors

- **Using a definition from another book.** A theorem may be true under its own conventions and false under yours.
- **Chaining $\approx$.** Each step of $a \approx b \approx c$ may be within the tolerance while $a$ and $c$ are not.
- **Treating a class as a number.** An operation on $\Z/n$ written with representatives must be checked for independence of the representative before it is used.
- **"i.e." for a one-way implication.** "$x > 2$, i.e. $x^2 > 4$" is wrong, since $x = -3$ satisfies the second and not the first.
- **Reading "almost all" in the wrong sense.** The squares are infinite, so "almost all $n$ are not squares" is false in the cofinite sense, although it is true in the density sense.
- **Confusing sharp with attained.** The bound $x^2 < 1$ on $(-1, 1)$ is sharp, since no smaller constant works, but it is never an equality.
- **Hiding a gap behind "clearly".** "Clearly" claims that the step is routine; it does not replace the step.
- **Reading $\therefore$ as the end of a proof.** It marks a consequence inside the argument; only $\blacksquare$, $\square$ or Q.E.D. marks the end.
