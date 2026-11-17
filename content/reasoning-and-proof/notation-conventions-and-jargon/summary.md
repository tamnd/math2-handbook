## What to remember

- **Conventions** are choices, not facts. This book takes $0 \in \N$, writes $A \subseteq B$ for subset and $A \subsetneq B$ for proper subset, reads "increasing" as $x \leq y \Rightarrow f(x) \leq f(y)$, "positive" as $> 0$, $\log$ as the natural logarithm, and sets $0^0 = 1$. Check the conventions of any other source before you use its results.
- An **abuse of notation**, such as $3 \in \Z/7$ for the class $[3]$ or $G$ for a group $(G, \cdot)$, is acceptable only when the context fixes one correct expansion. A step that depends on the representative, such as $[a] \mapsto a$, is an error, not an abuse.
- Only $=$ lets you **replace** one side by the other everywhere. $:=$ defines; $a \equiv b \pmod n$ survives sums and products but not exponents ($2 \equiv 7 \pmod 5$, yet $2^2 = 4$ and $2^7 \equiv 3$); $\approx$ is not transitive; and $f = O(g)$ is a one-way statement, so $n = O(n^2)$ does not give $n^2 = O(n)$.
- **"Trivial"** is exact for objects (the zero solution, the one-element group) and a judgement for steps. A step called "clearly" true still needs an argument that the reader can supply.
- A construction is **canonical** when it uses no arbitrary choice. A canonical form for $\sim$ is a map $c$ with $c(x) \sim x$ and $c(x) = c(y)$ whenever $x \sim y$. The map from a vector space to its [double dual](/0ZJM9D7NPS/) is canonical; an isomorphism with the dual space needs a basis.
- **"Eventually $P(n)$"** is $\exists N \, \forall n \geq N \, P(n)$; **"frequently $P(n)$"** is $\forall N \, \exists n \geq N \, P(n)$. "Not eventually $P$" is "frequently not $P$". **"Almost all"** means that the exceptions are negligible, and a text must say in which sense.
- $A$ is **stronger** than $B$ when $A \Rightarrow B$. A theorem with a weaker hypothesis or a stronger conclusion is a stronger theorem.
- A constant $C$ in $f \leq C g$ is **sharp** when no smaller constant works; it is the supremum of $f/g$. An equality case proves sharpness, but a sharp bound need not be attained.
- **"Elementary"** restricts the tools of a proof, not its length; **"pathological"** and **"deep"** are judgements relative to a class and a time; and an end mark such as $\blacksquare$ is the author's claim that the proof is complete, not a proof.

## Phrases that hide quantifiers

| Phrase | Meaning | Example |
|---|---|---|
| for all sufficiently large $n$; eventually | $\exists N \; \forall n \geq N \; P(n)$ | $n! > 2^n$ for all $n \geq 4$ |
| frequently; for infinitely many $n$ | $\forall N \; \exists n \geq N \; P(n)$ | $n$ is prime |
| for all but finitely many $n$ | the exceptions form a finite set | primes are odd, except $2$ |
| for almost all $n$, in density | the exceptions have density $0$ | $n$ is not a perfect square |
| for almost every $x \in \R$ | the exceptions have measure $0$ | $x$ is irrational |
| for generic $x \in \R$ | the exceptions form a meagre set | $x$ is a Liouville number |
| $C$ is sharp in $f \leq C g$ | $f \leq Cg$ on $X$, and no $C' < C$ works | $\sqrt{ab} \leq \frac12 (a + b)$ |

: Each phrase as a statement with explicit quantifiers. On $\N$, "for all but finitely many" is the same as "eventually". Liouville numbers are generic but have measure zero, so the measure and category senses of "almost all" can disagree.

## Common errors

- **Mixing conventions.** A result about "positive" numbers from a French source may include $0$; a formula with $\log$ from an engineering source uses base $10$.
- **Hiding a dependence.** In "for each $\varepsilon > 0$, eventually $\abs{a_n - L} < \varepsilon$", the threshold $N$ depends on $\varepsilon$. Say so when you write a proof.
- **Combining frequent statements.** "$n$ is even" and "$n$ is odd" both hold frequently, but their conjunction never holds. Two eventual statements do combine.
- **Reversing strength.** A theorem with a stronger hypothesis is a weaker theorem.
- **Showing sharpness with a forbidden case.** The equality case must satisfy every hypothesis: $a = b = -1$ is not allowed in AM-GM.
- **Writing "obvious" in place of a step.** If you cannot give the argument in a line, write it out.
