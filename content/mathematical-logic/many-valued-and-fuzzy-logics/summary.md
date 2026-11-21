## What to remember

- **A logic is a matrix, not a table.** A [logical matrix](/P7E926JK13/) is an algebra with a set $D$ of designated values, and $\Gamma \models \varphi$ means that every valuation that designates all of $\Gamma$ designates $\varphi$.
- **One entry separates Ł3 from K3.** [Łukasiewicz three-valued logic](/1CE2TGM6MQ/) differs from [strong Kleene logic](/SZHA10A9X7/) only at $\tfrac12 \to \tfrac12$, which is $1$ in $\mathrm{Ł}_3$ and $\tfrac12$ in $\mathsf{K}_3$. This one entry makes $p \to p$ a tautology of $\mathrm{Ł}_3$.
- **Weak Kleene values are infectious.** A formula has value $\tfrac12$ exactly when one of its variables has it. So $\mathrm{B}_3$ loses addition $p \models p \lor q$, and $\mathsf{PWK}$ has exactly the classical tautologies.
- **FDE has four values and no tautologies.** In [first-degree entailment](/KXTP4P3GHT/) the values are the subsets of $\set{T, F}$, and the designated ones contain $T$. Every FDE inference holds in $\mathsf{K}_3$ and in $\mathsf{LP}$.
- **Completeness of connectives.** [Post's cyclic negation](/YHYSGRE7JV/) with $\max$ defines every function on $m$ values. A [Sheffer function](/1K829SJG3K/) preserves no proper nonempty subset of values, so $f(a, \dots, a) \ne a$ for every $a$.
- **Łukasiewicz logic on $[0, 1]$** has $x \to y = \min(1, 1 - x + y)$ and $x \odot y = \max(0, x + y - 1)$. Its axioms are complete for finite premise sets but not for infinite ones. [Chang's theorem](/QM0F33QE9P/) proves completeness through MV-algebras, and by [McNaughton's theorem](/E11A9H8Z7Q/) the formulas define exactly the continuous piecewise linear functions with integer coefficients.
- **t-norms and residua.** A [t-norm](/VR6D8JXX1W/) has a residuum $x \Rightarrow y = \max \set{z : z * x \le y}$ exactly when it is left-continuous, and then $x \Rightarrow y = 1$ iff $x \le y$. MTL is the logic of all left-continuous t-norms and [BL](/3AQ5GHTXA4/) that of the continuous ones; Łukasiewicz, Gödel and [product logic](/YTHRDT9PDR/) extend BL by double negation, idempotence and cancellation.
- **Quantifiers are infima and suprema.** [First-order Gödel logics](/H8C323CV3T/) depend on the order type of the value set $V$. Standard validity in first-order Łukasiewicz logic is [$\Pi^0_2$-complete](/VAHH1505Z0/), so no computably enumerable axiom system captures it.
- **Probabilities are not truth values.** In [probability logic](/Z2WRGJDRQT/), $P(\varphi \land \psi)$ is not a function of $P(\varphi)$ and $P(\psi)$. From $P(p) = a$ and $P(p \to q) = b$ one gets only $a + b - 1 \le P(q) \le b$.

## Small logics side by side

| Logic | Values | Designated | Has tautologies | $p \to p$ | $p \lor \neg p$ | $p \land \neg p \models q$ |
|---|---|---|---|---|---|---|
| Classical | $0, 1$ | $1$ | yes | yes | yes | yes |
| [Ł3](/1CE2TGM6MQ/) | $0, \tfrac12, 1$ | $1$ | yes | yes | no | yes |
| [K3](/SZHA10A9X7/) | $0, \tfrac12, 1$ | $1$ | no | no | no | yes |
| LP | $0, \tfrac12, 1$ | $\tfrac12, 1$ | yes | yes | yes | no |
| [B3](/BCK5QXQXA6/) | $0, \tfrac12, 1$ | $1$ | no | no | no | yes |
| PWK | $0, \tfrac12, 1$ | $\tfrac12, 1$ | yes | yes | yes | no |
| [FDE](/KXTP4P3GHT/) | $\mathbf{T}, \mathbf{F}, \mathbf{B}, \mathbf{N}$ | $\mathbf{T}, \mathbf{B}$ | no | no | no | no |
| [Łukasiewicz](/NFCEM44XYH/) | $[0, 1]$ | $1$ | yes | yes | no | yes |
| Gödel | $[0, 1]$ | $1$ | yes | yes | no | yes |
| [Product](/YTHRDT9PDR/) | $[0, 1]$ | $1$ | yes | yes | no | yes |

: Ten logics. In the last three columns "yes" means a tautology or a valid inference. In the Kleene logics, the weak Kleene logics and FDE, $p \to p$ stands for $\neg p \lor p$; in the last three rows $\land$ is the minimum.

## Common errors

- **Forgetting the designated set.** $\mathsf{K}_3$ and $\mathsf{LP}$, and $\mathrm{B}_3$ and $\mathsf{PWK}$, share their tables and differ only in $D$, and their laws differ.
- **Using the wrong disjunction.** In Łukasiewicz logic $\neg x \to y$ is the strong disjunction $\min(1, x + y)$, not $\max(x, y)$. The weak disjunction is $(x \to y) \to y$.
- **Combining degrees by the minimum.** Modus ponens in degrees uses the t-norm: $x \odot (x \to y) \le y$ holds, but $\min(x, x \to y) \le y$ fails. In Pavelka logic the degrees $r$ and $s$ combine to $r \odot s$.
- **Taking $1 - x$ as the negation of every fuzzy logic.** In Gödel and product logic, $\neg x = x \Rightarrow 0$ is $1$ at $0$ and $0$ elsewhere, so $\neg\neg p \to p$ fails.
- **Expecting strong completeness.** The Łukasiewicz axioms are complete for finite premise sets only, and first-order Łukasiewicz logic is complete for general but not for standard semantics.
