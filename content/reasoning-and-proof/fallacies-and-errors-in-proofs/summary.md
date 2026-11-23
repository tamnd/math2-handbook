## What to remember

- A **fallacy** is an argument that looks valid and has an invalid step. Its conclusion is usually false, but a wrong method can give a right answer (a howler), and a true but surprising result, such as $0.999\ldots = 1$, is not a fallacy. To find the error, test each step against the exact rule it uses, hypotheses included.
- **Cancellation.** For real or complex numbers, $ac = bc$ holds exactly when $c = 0$ or $a = b$. So $ac = bc \Rightarrow a = b$ needs $c \ne 0$.
- **Roots and powers.** For real $a, b \ge 0$, $\sqrt{ab} = \sqrt{a}\sqrt{b}$; for real $x$, $\sqrt{x^2} = \abs{x}$. The rule $(a^m)^n = a^{mn}$ holds for $a > 0$ and all real $m, n$, and for $a \ne 0$ when $m$ and $n$ are integers. For complex $w$, $\operatorname{Log}(e^w) = w$ only when the imaginary part of $w$ lies in $(-\pi, \pi]$.
- **Infinite processes.** Grouping and rearranging the terms of a series are safe when the series converges absolutely; by [Riemann's rearrangement theorem](/0E7VBYGFF7/) a conditionally convergent series can be rearranged to any real sum. The formula $\int_a^b f = F(b) - F(a)$ needs $F' = f$ on all of $[a, b]$, which fails when $f$ is unbounded inside the interval. Limits, sums and integrals may be exchanged only under a hypothesis such as uniform convergence or domination.
- **Valid and invalid forms.** Modus ponens and modus tollens are valid. Affirming the consequent and denying the antecedent are invalid: one case with true premises and a false conclusion shows it.
- **Examples.** One example proves an existential statement and one counterexample refutes a universal one. No number of checked cases proves a statement about infinitely many cases; checking every case proves a statement about finitely many.
- **Order of quantifiers.** $\exists y\, \forall x\, P(x, y)$ implies $\forall x\, \exists y\, P(x, y)$, and the converse fails: every real number has a larger one, and no real number is larger than all of them.
- **Solving equations.** Squaring both sides, multiplying by an expression that may vanish, or applying a function that is not injective gives an implication, not an equivalence: the new equation may have extra solutions, so check every candidate in the original. Dividing by an expression that may vanish can lose solutions.
- **Circularity and intimidation.** A proof is circular if it uses its conclusion, or a result proved from it, as a premise; trace where each premise comes from. A "clearly" in place of an argument marks a step to check.

## Four forms with a conditional

| Name | Premises | Conclusion | Valid? |
|---|---|---|---|
| Modus ponens | $P \Rightarrow Q$ and $P$ | $Q$ | yes |
| Modus tollens | $P \Rightarrow Q$ and $\neg Q$ | $\neg P$ | yes |
| Affirming the consequent | $P \Rightarrow Q$ and $Q$ | $P$ | no |
| Denying the antecedent | $P \Rightarrow Q$ and $\neg P$ | $\neg Q$ | no |

: The two invalid forms are the valid ones applied to the converse $Q \Rightarrow P$. With $P$ "$6$ divides $n$", $Q$ "$3$ divides $n$" and $n = 9$, both invalid forms have true premises and a false conclusion.

## Common errors

- **Cancelling a factor that can be zero.** Before dividing by $x - 2$ or $a - b$, ask whether it can vanish. In the classic "proofs" of $2 = 1$ it vanishes by construction.
- **Squaring without checking.** After squaring, or after multiplying by an expression in the unknown, every candidate must be put back into the original equation.
- **Reasoning from the converse.** A proof of "if $P$ then $Q$" that starts from $Q$ and ends with $P$ proves the converse. Check the direction of each implication, and reverse the chain only where every step is an equivalence.
- **Proof by example.** Forty checked values of $n$ prove nothing about all $n$.
- **Shifting a quantifier.** "For each $x$ there is a $\delta$" does not give one $\delta$ for all $x$. Write the quantifiers out and keep their order.
- **Trusting the figure.** Recompute the key facts of a figure with coordinates, or derive the position of each point from the axioms.
- **Using the result to prove itself.** When a proof cites a theorem, check that the theorem was not proved from the statement now being proved.

Two tests find most errors. If the conclusion is false, put a value into each line and stop at the first false line. If the same steps prove something false in another case, the argument proves too much.
