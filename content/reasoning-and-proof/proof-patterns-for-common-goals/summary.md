## What to remember

- **Double inclusion.** $A = B$ if and only if $A \subseteq B$ and $B \subseteq A$.
- **Maps.** $f \colon X \to Y$ is injective when $f(a) = f(b)$ implies $a = b$, and surjective when every $y \in Y$ equals $f(x)$ for some $x \in X$. A surjectivity proof must produce the $x$ and then check that $f(x) = y$. Between finite sets of the same size, injective and surjective are equivalent.
- **Equivalence relations.** A relation is an equivalence relation when it is reflexive, symmetric and transitive; no two of the three imply the third. A relation of the form $x \sim y \iff f(x) = f(y)$ is always one.
- **Two inequalities.** $a \le b$ and $b \le a$ give $a = b$ in any partial order. In $\R$, if $a \le b + \varepsilon$ for every $\varepsilon > 0$, then $a \le b$.
- **Identities.** Transform one side into the other, or both into a common form, or show that the difference is $0$. A chain of equivalences works only when every step reverses. Two polynomials of degree at most $d$ that agree at $d + 1$ points are equal.
- **Epsilon over three.** If $f_n \to f$ uniformly, then
  $$\abs{f(x) - f(y)} \le \abs{f(x) - f_n(x)} + \abs{f_n(x) - f_n(y)} + \abs{f_n(y) - f(y)},$$
  and a property of the $f_n$ such as continuity passes to $f$ when each term is made smaller than $\varepsilon/3$.
- **Density.** Two continuous maps into a metric space that agree on a dense set agree everywhere. An estimate proved on a dense set extends by continuity.
- **Open-closed.** In a connected space, a non-empty set that is both open and closed is the whole space. Show that the set where the property holds is non-empty, open and closed.
- **Algorithms.** A procedure proves existence when it terminates, because a natural number decreases at each step, and when an invariant holds at every step and gives the required property at the end.

| Goal | Pattern | What the proof checks |
|---|---|---|
| $A = B$ for sets | Double inclusion | $x \in A \Rightarrow x \in B$ and $x \in B \Rightarrow x \in A$ |
| $f$ injective | Equal outputs | $f(a) = f(b) \Rightarrow a = b$ |
| $f$ surjective | Solve for a preimage | For each $y$, an $x$ in the domain with $f(x) = y$ |
| $\sim$ an equivalence relation | Three checks, or a map $f$ | Reflexive, symmetric, transitive |
| $a = b$ for numbers | Two inequalities | $a \le b$ and $b \le a$, or $a \le b + \varepsilon$ for all $\varepsilon > 0$ |
| Identity in $x$ | Rewrite, or difference is zero | Every step valid for every $x$ in the domain |
| Limit or continuity | Epsilon-delta | A $\delta$ for every $\varepsilon$, often $\delta = \min(1, c\varepsilon)$ |
| Property of a uniform limit | $\varepsilon/3$ | Three terms, each below $\varepsilon/3$ |
| Statement on all of a space | Density | The statement on a dense set, and continuity |
| Property on a connected space | Open-closed | Non-empty, open, closed |
| A strong a priori bound | Bootstrapping | A weak bound that improves itself, and continuity |
| Existence of an object | Algorithm | Termination and an invariant |

: The common goals of the chapter and the pattern that proves each.

## Choosing a pattern

- **Read the goal first.** Write the goal in logical form. The outermost connective or quantifier usually fixes the pattern.
- **Prefer the difference for identities.** Showing that the difference of the two sides is $0$ avoids steps that do not reverse, such as squaring both sides.
- **Bound before solving.** In an epsilon-delta proof, first restrict to $\abs{x - a} < 1$ to bound the other factors, then choose $\delta = \min(1, c\varepsilon)$.
- **Look for uniformity.** The $\varepsilon/3$ argument needs one $n$ that works for all points at once. With only pointwise convergence it fails, as the functions $x^n$ on $[0, 1]$ show.
- **Look for a symmetry or a normalization.** If the statement is unchanged by swapping variables or by scaling, use that before computing.
- **For local-to-global claims, check connectedness.** If the space is connected, the open-closed argument is often the shortest route.
- **Check the domain.** A surjectivity proof that solves $f(x) = y$ must check that the $x$ found lies in the domain, and an absorption step $x \le A + x/2 \Rightarrow x \le 2A$ needs $x$ finite.

