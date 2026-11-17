## What to remember

- **A fallacy** is an argument with the form of a proof and at least one invalid step that looks valid. A howler is a fallacy whose conclusion happens to be true, as in cancelling the $6$s in $\frac{16}{64} = \frac{1}{4}$.
- **Cancellation needs a non-zero factor.** From $ac = bc$ one may conclude $a = b$ only when $c \ne 0$. Dividing an equation by an expression in $x$ loses the solutions where it vanishes.
- **Roots and powers have hypotheses.** $\sqrt{ab} = \sqrt a \, \sqrt b$ needs $a, b \ge 0$; $\sqrt{a^2} = \abs{a}$, not $a$; and $(a^b)^c = a^{bc}$ can fail for complex $a$ or non-integer exponents.
- **Infinite sums are not finite sums.** Rearranging a conditionally convergent series can change its sum, and $\int_a^b f = F(b) - F(a)$ needs $f$ continuous on $[a, b]$. Iterated limits need not be equal.
- **Implication runs one way.** From $P \Rightarrow Q$ and $Q$ nothing follows about $P$, and from $P \Rightarrow Q$ and $\neg P$ nothing follows about $Q$. The valid forms are modus ponens and modus tollens.
- **Examples prove existence, not generality.** A universal claim needs a proof; one counterexample refutes it.
- **Quantifiers do not commute.** $\exists y \, \forall x \, P(x, y)$ implies $\forall x \, \exists y \, P(x, y)$, and the converse fails in general.
- **Squaring and similar steps do not reverse.** A solution found through a non-reversible step must be checked in the original equation.
- **Published proofs can be wrong.** An incorrect proof does not make its result false: Kempe's argument for four colours failed, and the theorem was later proved.

| Error | Invalid step | Valid form nearby |
|---|---|---|
| Division by zero | $ac = bc \Rightarrow a = b$ | Same, when $c \ne 0$ |
| Roots of negatives | $\sqrt{ab} = \sqrt a \, \sqrt b$ for all $a, b$ | Same, when $a, b \ge 0$ |
| Rearranging a series | Any order gives the same sum | Same, for absolutely convergent series |
| Improper integral | $\int_{-1}^{1} x^{-2} \, dx = [-x^{-1}]_{-1}^{1}$ | The formula, when the integrand is continuous on the interval |
| Circular reasoning | The conclusion is used as a premise | Use only earlier results whose proofs do not use the conclusion |
| Affirming the consequent | $P \Rightarrow Q$ and $Q$, so $P$ | Modus ponens: $P \Rightarrow Q$ and $P$, so $Q$ |
| Denying the antecedent | $P \Rightarrow Q$ and $\neg P$, so $\neg Q$ | Modus tollens: $P \Rightarrow Q$ and $\neg Q$, so $\neg P$ |
| Proof by example | $P(a)$ for some $a$, so $\forall x \, P(x)$ | $P(a)$ for some $a$, so $\exists x \, P(x)$ |
| Quantifier shift | $\forall x \, \exists y \, P$, so $\exists y \, \forall x \, P$ | $\exists y \, \forall x \, P$, so $\forall x \, \exists y \, P$ |
| Non-reversible step | Squaring treated as an equivalence | Check every candidate in the original equation |

: The common errors of the chapter, the step that fails, and the correct rule closest to it.

## Finding the error

- **Test the conclusion first.** If the conclusion is false, the argument has a wrong step; check each step on the specific numbers until one fails.
- **Ask each rule for its hypothesis.** For every cancellation, root, exponent law, interchange of limits or use of a figure, state the condition under which the rule holds and check it.
- **Write the logical form.** Many errors of logic disappear once the quantifiers and implications are written out: a reversed arrow or a swapped $\forall\exists$ becomes visible.
- **Check the direction of each step.** In solving an equation, mark each step as "implies" or "is equivalent to", and check the candidates when any step is one-way.
- **Do not trust the figure.** Redraw it accurately, or replace each fact read off it by a proof from the axioms.
- **Treat "obviously" as a request for a reason.** A step that is only asserted, or justified by who asserted it, is a gap until it is proved.
