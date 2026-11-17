## What to remember

- **Full second-order logic** lets relation variables range over all relations on the domain. It defines equality by $\forall X\, (X(x) \to X(y))$, finiteness by one sentence, and $\N$ and $\R$ up to isomorphism. It is neither compact nor Löwenheim–Skolem, and its valid sentences are not computably enumerable.
- **Henkin semantics** lets relation variables range over a family $D_n \subseteq \mathcal{P}(M^n)$ that satisfies comprehension. It is many-sorted first-order logic, so completeness, compactness and Löwenheim–Skolem return, and second-order Peano arithmetic gets non-standard models.
- **Comprehension** is the schema $\exists X\, \forall \bar x\, (X(\bar x) \leftrightarrow \varphi)$ with $X$ not free in $\varphi$. It is valid in the full semantics, and it is what lets a proof instantiate $\forall X$ by a formula. An instance is impredicative when $\varphi$ quantifies over relations.
- **Higher-order logic** adds variables of every finite type. In the standard semantics it reduces to second-order logic, and in the Henkin semantics it has a complete proof system.
- **Frege's theorem:** second-order logic with Hume's principle, $\#F = \#G \leftrightarrow F \approx G$, proves the second-order Peano axioms for $0$, successor and the natural numbers. Hume's principle is consistent; Frege's Basic Law V is not.
- **Monadic second-order logic** quantifies only over sets. On words it defines exactly the regular languages; on graphs it expresses connectivity and bipartiteness, and its existential part expresses 3-colourability.
- **Branching quantifiers, IF logic and dependence logic** restrict what an existential choice may depend on. Branching sentences with a first-order matrix, IF sentences and dependence logic sentences have exactly the power of existential second-order logic, so they are compact and Löwenheim–Skolem, but they are not closed under classical negation. Adding that negation to the Henkin quantifier loses both properties.
- A **generalized quantifier** is an isomorphism-closed class of structures. $L(Q_0)$ ("infinitely many") is not compact; $L(Q_1)$ ("uncountably many") has a complete proof system and is countably compact, but fails downward Löwenheim–Skolem.
- **Plural quantification** reads $\exists X$ as "there are some things". It interprets monadic second-order logic without sets, but has no empty plurality.

## Properties of the logics

| Logic | Compact | Downward Löwenheim–Skolem | Valid sentences computably enumerable |
|---|---|---|---|
| First-order logic | yes | yes | yes |
| Second-order logic, full semantics | no | no | no |
| Second-order logic, Henkin semantics | yes | yes | yes |
| Monadic second-order logic, full semantics | no | no | no |
| Existential second-order, IF and dependence logic | yes | yes | no |
| First-order logic with the Henkin quantifier and negation | no | no | no |
| $L(Q_0)$ | no | yes | no |
| $L(Q_1)$ | for countable sets | no | yes |
| Plural logic | no | no | no |

: The rows for monadic and plural logic are negative because the induction axiom and the completeness of an order quantify only over sets. The existential logics are compact because their sentences say that functions exist, which first-order logic with new function symbols can say; their validities are not enumerable because the negation of second-order arithmetic is existential.

## Common errors

- **Forgetting which semantics is meant.** "Second-order logic is not compact" is a statement about the full semantics. With the Henkin semantics, the same sentences form a compact logic, and second-order Peano arithmetic is no longer categorical.
- **Leaving out parameters or allowing $X$ in $\varphi$.** Comprehension without parameters is too weak to make $\forall X\, (X(x) \to X(y))$ define equality, and comprehension with $X$ free in $\varphi$ is inconsistent.
- **Reading a Henkin quantifier as a linear prefix.** In $\forall x_1 \exists y_1 \forall x_2 \exists y_2$ the choice of $y_2$ sees $x_1$; in the Henkin quantifier it does not. The same matrix can give a sentence true in all structures with at least two elements and a sentence true only in infinite ones.
- **Hiding too little in IF logic.** To make $w$ independent of $x$, the slash must also hide every variable chosen after $x$ by Eloise, since such a variable can copy $x$ and pass on its value.
- **Expecting excluded middle.** An IF sentence can be undetermined, and in dependence logic $\varphi \lor \neg\varphi$ is not always true; the negation there is not classical.
- **Confusing MSO on words with MSO on sets.** Even length is MSO-definable on words because the order gives a set to alternate along. On a pure set, "even size" is not MSO-definable.
