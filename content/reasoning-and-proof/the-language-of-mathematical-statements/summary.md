## What to remember

- A [statement](/S9MHMRAX88/) is a declarative sentence that is true or false and not both, even if nobody knows which. An open sentence $P(x)$ is not a statement; it becomes one when $x$ gets a value or is bound by a quantifier. Questions and commands are not statements.
- "$P$ and $Q$" is true when both are true, and "but" means "and". "$P$ or $Q$" is inclusive: it is true when at least one is true, including both. "Neither $P$ nor $Q$" means $\neg P \land \neg Q$. An "and" between two names, as in "$2$ and $3$ are coprime", may state a relation and not join two statements.
- "If $P$, then $Q$" is false only when $P$ is true and $Q$ is false. "$P$ only if $Q$", "$Q$ if $P$", "$Q$ whenever $P$", "$P$ is sufficient for $Q$" and "$Q$ is necessary for $P$" all mean $P \Rightarrow Q$. "$P$ unless $Q$" means $\neg Q \Rightarrow P$. A conditional with variables carries a hidden "for every".
- A conditional is equivalent to its [contrapositive](/04T1CT7212/) $\neg Q \Rightarrow \neg P$, and not in general to its [converse](/09A3N7ZN5G/) $Q \Rightarrow P$ or its [inverse](/VB7B8766D2/) $\neg P \Rightarrow \neg Q$, which are equivalent to each other. The "if" in a definition means "if and only if".
- "For every $x \in A$, $P(x)$" means $\forall x \, (x \in A \Rightarrow P(x))$, and "some $x \in A$ has $P(x)$" means $\exists x \, (x \in A \land P(x))$. Quantifiers of the same kind may change places; $\forall x \, \exists y$ and $\exists y \, \forall x$ in general say different things, and the second implies the first.
- To negate, push "not" inward: $\neg(P \land Q) \equiv \neg P \lor \neg Q$, $\neg(P \lor Q) \equiv \neg P \land \neg Q$, $\neg(P \Rightarrow Q) \equiv P \land \neg Q$, $\neg \forall x \in A \, P(x) \equiv \exists x \in A \, \neg P(x)$ and $\neg \exists x \in A \, P(x) \equiv \forall x \in A \, \neg P(x)$. The domain $A$ of a bounded quantifier is not negated.
- $\exists! x \, P(x)$ means existence, $\exists x \, P(x)$, together with uniqueness, $\forall x \, \forall y \, (P(x) \land P(y) \Rightarrow x = y)$. Uniqueness alone says "at most one". Writing "the $x$ with $P(x)$" presupposes both.
- "Any" can mean "every" or "some", and the scope of "not" in "all … are not …" is unclear. Write "every", "some", "no" and "not all" instead.

| Sentence | As a conditional | Equivalent to $P \Rightarrow Q$ |
|---|---|---|
| If $P$, then $Q$; $Q$ whenever $P$ | $P \Rightarrow Q$ | yes |
| $P$ only if $Q$ | $P \Rightarrow Q$ | yes |
| $P$ is sufficient for $Q$ | $P \Rightarrow Q$ | yes |
| $Q$ is necessary for $P$ | $P \Rightarrow Q$ | yes |
| $Q$ unless $\neg P$ | $P \Rightarrow Q$ | yes |
| Contrapositive: if not $Q$, then not $P$ | $\neg Q \Rightarrow \neg P$ | yes |
| Converse: if $Q$, then $P$ | $Q \Rightarrow P$ | no |
| Inverse: if not $P$, then not $Q$ | $\neg P \Rightarrow \neg Q$ | no |
| $P$ if and only if $Q$ | $(P \Rightarrow Q) \land (Q \Rightarrow P)$ | no, it says more |
| Negation | $P \land \neg Q$ | no, it contradicts it |

: Ways of writing a conditional and the statements most often confused with it

## Common errors

- **Reading "only if" as "if".** "$P$ only if $Q$" puts $Q$ in the conclusion. Proving $Q \Rightarrow P$ instead proves the converse, which may be false: "$n$ is divisible by $4$ only if $n$ is even" is true, and its converse fails at $n = 2$.
- **Treating the converse or the inverse as equivalent.** From "every differentiable function is continuous" nothing follows about continuous functions; $\abs{x}$ is continuous at $0$ and not differentiable there.
- **Negating a conditional with a conditional.** The negation of "if $P$, then $Q$" is "$P$ and not $Q$", not "if $P$, then not $Q$". With a hidden "for every $x$", the negation is one counterexample: some $x$ with $P(x)$ and not $Q(x)$.
- **Swapping quantifiers.** In "for every $x$ there is a $y$", $y$ may depend on $x$. The gap between continuity and uniform continuity is exactly this swap.
- **Proving half of "exactly one".** A solution found by computation gives existence only. A uniqueness argument that divides by $x$ loses the solution $x = 0$.
