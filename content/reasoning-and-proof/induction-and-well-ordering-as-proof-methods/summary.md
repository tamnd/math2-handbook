## What to remember

- **Induction.** If $P(n_0)$ holds, and $P(n)$ implies $P(n + 1)$ for every $n \ge n_0$, then $P(n)$ holds for every $n \ge n_0$. The step is proved for an arbitrary $n$, and the assumption $P(n)$ is the induction hypothesis.
- **Strong induction.** If, for each $n$, the truth of $P(k)$ for every $k < n$ implies $P(n)$, then $P(n)$ holds for every natural number $n$. A step that uses the cases $n - 1, \ldots, n - j$ needs $j$ base cases, or must treat the small $n$ separately.
- **Well-ordering.** Every nonempty subset of $\N$ has a least element. Over the base theory of a linear order with $0$ and a successor, induction, strong induction and well-ordering are equivalent.
- **Minimal counterexample and descent.** To prove that no object of size in $\N$ fails $P$, take a counterexample of least size and derive a contradiction. To prove that a set $S$ is empty, show that each element of $S$ gives an element of $S$ of smaller size.
- **Strengthening.** If the step from $P(n)$ to $P(n + 1)$ fails, prove a statement $Q(n)$ that implies $P(n)$ and has a provable step. Proving $\sum_{k=1}^n 1/k^2 \le 2 - 1/n$ proves the bound $2$.
- **Two variables and doubling.** A claim $P(m, n)$ can be proved by nested induction, by induction on $m + n$, or in lexicographic order. Forward-backward induction proves $P(n)$ for an infinite set of $n$, usually the powers of $2$, and then $P(n) \Rightarrow P(n - 1)$ for every $n \ge 2$.
- **Structure and size.** For an inductively defined set, the smallest set that contains the base objects and is closed under the rules, a property holds for every element if it holds for the base objects and each rule keeps it. For graphs, sets or polynomials, choose a size function and induct on it, breaking an object of size $n + 1$ down into smaller ones.
- **Errors.** A step must hold for every $n$ from the base case on, including the smallest, and must stay inside the domain of the claim. The false proof that all horses have the same colour fails only at the step from $1$ to $2$.

| Method | What the proof assumes | What it must show | Typical use |
|---|---|---|---|
| Induction | $P(n)$ | $P(n_0)$ and $P(n + 1)$ | sums, divisibility, inequalities in $n$ |
| Strong induction | $P(k)$ for all $k < n$ | $P(n)$, with enough base cases | factorization, recursions of order $2$ or more |
| Minimal counterexample | a counterexample of least size | a smaller counterexample, or a contradiction | existence of prime factors, colourings |
| Infinite descent | an element of $S$ | an element of $S$ of smaller size | Diophantine equations without solutions |
| Double induction | smaller pairs $(m', n')$ | $P(m, n)$ | binomial coefficients, the Ackermann function |
| Forward-backward induction | $P(n)$ | $P(2n)$ and $P(n - 1)$ | the inequality of arithmetic and geometric means |
| Structural induction | $P$ for the parts | $P$ for each base object and each rule | lists, trees, formulas |
| Induction on size | the claim for smaller objects | the claim for an object of size $n + 1$ | graphs, finite sets, polynomials |

: The forms of induction in this chapter, with the hypothesis each one gives and what remains to be proved.

## Checking an induction proof

Read the claim $P(n)$ first and write it out as a sentence with $n$ free; many errors come from a claim that changes meaning between the base case and the step. Then check four things. The base cases are proved, and there are as many as the step needs. The step is proved for an arbitrary $n$ at or above the base, with no hidden condition such as $n \ge 2$. The step uses only the cases the method allows, and they lie inside the domain: no $n - 1$ when $n = 0$, no $a - 1$ when $a$ may be $0$. And the step breaks an arbitrary object of size $n + 1$ down; building a large object up from a small one covers only the objects that the construction happens to reach.

When the step stalls, try a stronger claim before a different method. A bound that the step cannot keep, such as $\sum 1/k^2 \le 2$, often becomes provable as a sharper bound that depends on $n$. When the step needs more than one earlier case, switch to strong induction or to a minimal counterexample, which is the same argument written from the other end.
