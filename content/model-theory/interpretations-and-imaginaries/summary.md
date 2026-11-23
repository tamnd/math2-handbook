## What to remember

- **Interpretation.** An $n$-dimensional [interpretation](/7R0SJPH37J/) $\Gamma$ of $N$ in $M$ over $A$ is a formula $\partial(\bar x)$, a formula $\varepsilon(\bar x, \bar y)$, a formula $\varphi_S$ for each symbol $S$ of $N$, all over $A$, and a surjection $f : \partial(M^n) \to N$ with $f(\bar a) = f(\bar b)$ exactly when $M \models \varepsilon(\bar a, \bar b)$, such that each $\varphi_S$ defines the preimage of $S$. When $\varepsilon$ is equality, $N$ is definable in $M$.
- **Reduction.** Each formula $\psi$ of $N$ has a translation $\psi_\Gamma$ with $N \models \psi(f \bar a_1, \dots, f \bar a_k)$ if and only if $M \models \psi_\Gamma(\bar a_1, \dots, \bar a_k)$. For a $\emptyset$-interpretation, a decidable $\operatorname{Th}(M)$ gives a decidable $\operatorname{Th}(N)$. If $\operatorname{Th}(M)$ is stable, so is $\operatorname{Th}(N)$, and $\operatorname{Aut}(M/A)$ maps to $\operatorname{Aut}(N)$. Composing interpretations multiplies their dimensions.
- **Bi-interpretation.** Interpretations $\Gamma$ of $N$ in $M$ and $\Delta$ of $M$ in $N$ form a [bi-interpretation](/KHZ1E7RMMQ/) when the graphs of both composite coordinate maps are definable. Interpretations in both directions are not enough: a set $M$ and the structure $(M^2, E_1, E_2)$ interpret each other but are not $\emptyset$-bi-interpretable.
- **Imaginaries.** $M^{\mathrm{eq}}$ adds a sort $M^n / E$ with the projection $\pi_E$ for each $\emptyset$-definable equivalence relation $E$. It adds no new definable subsets of $M^n$, and each automorphism of $M$ extends uniquely to it. The canonical parameter of $X = \varphi(M, \bar b)$ is the class of $\bar b$ under "defines the same set as"; see [imaginary elements](/Q0HM88QQKN/).
- **Elimination of imaginaries.** $T$ has [elimination of imaginaries](/6M2R0ER3KV/) if each imaginary $e$ is interdefinable with a real tuple $\bar b$: $e \in \operatorname{dcl}(\bar b)$ and $\bar b \in \operatorname{dcl}(e)$. Weak elimination asks only $\bar b \in \operatorname{acl}(e)$. Uniform elimination asks for one $\emptyset$-definable map $f$ with $E(\bar x, \bar y) \leftrightarrow f(\bar x) = f(\bar y)$ for each $E$.
- **Poizat's theorem.** $\mathrm{ACF}_p$ has elimination of imaginaries, and uniform elimination too. A finite set of field elements is coded by the coefficients of the monic polynomial with these roots.
- **Stable embeddedness.** A $\emptyset$-definable set $D$ is [stably embedded](/14WPPDDK8M/) if $\varphi(\mathbb{M}, \bar b) \cap D^n$ is definable with parameters from $D$ for all $\varphi$ and all $\bar b$. In a stable theory every definable set is stably embedded.
- **Hyperimaginaries and reconstruction.** A [hyperimaginary](/NQPCDVV3NB/) is a class of a $\emptyset$-type-definable equivalence relation; stable theories eliminate them. By the [reconstruction theorem](/AM0523XJ9D/), countable $\omega$-categorical $M$ and $N$ are $\emptyset$-bi-interpretable exactly when $\operatorname{Aut}(M) \cong \operatorname{Aut}(N)$ as topological groups.

| Theory | Elimination of imaginaries | Weak elimination | Witness |
|---|---|---|---|
| infinite set, no structure | no | yes | the pair $\set{a, b}$ has no real code |
| equivalence relation with infinitely many infinite classes | no | no | a class $e$ has $\operatorname{acl}(e) \cap M = \emptyset$ |
| $\mathrm{ACF}_p$ | yes, and uniform | yes | Poizat's theorem |
| $\mathrm{RCF}$ | yes | yes | definable choice |
| $\mathrm{DCF}_0$ | yes | yes | stated in the entry |
| ACVF, field sort only | no | not treated | the geometric sorts are needed |

: Elimination of imaginaries in the theories of the chapter. Elimination implies weak elimination, and the first row shows that the converse fails.

## Common errors

- **Transferring in the wrong direction.** An interpretation of $N$ in $M$ carries decidability and stability from $M$ down to $N$, and undecidability from $N$ up to $M$. Interpreting $\Z[i]$ in $\Z$ says nothing about whether $\operatorname{Th}(\Z[i])$ is decidable.
- **Forgetting the parameters.** The field in its affine group needs a parameter, and the transfer of decidability is for interpretations without parameters.
- **Forgetting invariance under $\varepsilon$.** Each $\varphi_S$ must give the same answer on $\varepsilon$-equivalent tuples, or it defines no relation on the quotient; and $\varepsilon$ must be an equivalence relation on the domain, which cross-multiplication on all of $\Z^2$ is not.
- **Taking weak elimination for elimination.** In a pure set, the ordered pair $(a, b)$ codes $\set{a, b}$ only up to the swap, so $\set{a, b}$ has a weak code and no code.
- **Confusing imaginaries with hyperimaginaries.** "Infinitely close" is an intersection of infinitely many formulas, and its classes are not imaginaries; they are hyperimaginaries.
- **Dropping "topological".** The reconstruction theorem needs an isomorphism of topological groups, and it fails for finite structures and without $\omega$-categoricity.
