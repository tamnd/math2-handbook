## What to remember

- **Indiscernibles.** A family $(a_i)_{i \in I}$, with $(I, <)$ a linear order, is an [order-indiscernible sequence](/4016QKAHFB/) over $A$ if $a_{i_1} \dots a_{i_n}$ and $a_{j_1} \dots a_{j_n}$ have the same type over $A$ whenever $i_1 < \dots < i_n$ and $j_1 < \dots < j_n$. It is an indiscernible set if this holds for all tuples of distinct indices. Its Ehrenfeucht–Mostowski type is the set of formulas true at all its increasing tuples. An infinite indiscernible sequence is constant or injective.
- **Existence.** If $\mathcal{M}$ has an injective sequence $(b_n)_{n \in \N}$ and $I$ is an infinite linear order, then some $\mathcal{N} \equiv \mathcal{M}$ has an injective indiscernible sequence $(a_i)_{i \in I}$ that satisfies every formula true at all increasing tuples of $(b_n)$. The proof is [Ramsey's theorem](/00TQV3F5S4/) plus compactness; Morley's form uses the [Erdős–Rado theorem](/S1BHE358VX/) and sets of size $\beth_\alpha$ for all $\alpha < \omega_1$. See [existence of indiscernibles](/RG6D2FAS14/).
- **Ehrenfeucht–Mostowski models.** In a Skolem theory, $\operatorname{EM}(I, \Phi)$ is the Skolem hull of an indiscernible sequence with type $\Phi$. Order embeddings $I \to J$ extend to elementary embeddings, $\operatorname{Aut}(I, <)$ embeds in its automorphism group, $\abs{I} \le \abs{\operatorname{EM}(I, \Phi)} \le \abs{I} + \abs{L} + \aleph_0$, and over a well-order with $L$ countable it realizes only countably many types over each countable set. See [Ehrenfeucht–Mostowski models](/TSGB29FJM0/).
- **Generalized indiscernibles.** An $\mathcal{I}$-indexed family is [indiscernible](/RQS808ZC8T/) if tuples of indices with the same quantifier-free type in $\mathcal{I}$ give tuples with the same type. A theory is stable exactly when every order-indiscernible sequence is an indiscernible set, and Scow proved that the modeling property of an ordered index structure holds exactly when its age is a [Ramsey class](/8XS8FCTF8T/).
- **Vaught's theorem.** For countable $L$, a $(\kappa, \lambda)$-model with $\kappa > \lambda \ge \aleph_0$ gives an $(\aleph_1, \aleph_0)$-model. The proof goes through a Vaughtian pair $\mathcal{N} \prec \mathcal{M}$, $\mathcal{N} \neq \mathcal{M}$, with $P^{\mathcal{N}} = P^{\mathcal{M}}$ infinite, and a theory with a Vaughtian pair is not $\aleph_1$-categorical. See [Vaught's two-cardinal theorem](/XT227BYP7B/).
- **Chang's theorem.** For countable $L$ and $\kappa^{<\kappa} = \kappa$, an $(\aleph_1, \aleph_0)$-model gives a $(\kappa^+, \kappa)$-model. The condition forces $\kappa$ to be regular, and under the generalized continuum hypothesis every regular $\kappa$ satisfies it. See [Chang's two-cardinal theorem](/4STP69KESQ/).
- **Hanf number.** The [Hanf number](/A9XBRF3A7Z/) $h(\mathcal{L})$ is the least $\kappa$ such that every sentence of $\mathcal{L}$ with a model of size at least $\kappa$ has arbitrarily large models.

| Logic | Hanf number | Reason |
|---|---|---|
| first-order logic | $\aleph_0$ | the Löwenheim–Skolem theorem |
| $L_{\omega_1\omega}$, countable signatures | $\beth_{\omega_1}$ | Morley's form of the existence of indiscernibles, and sentences with largest model $\beth_\alpha$ |
| countable first-order theories with types to omit | $\beth_{\omega_1}$ | the same method, with Chang's reduction of $L_{\omega_1\omega}$ sentences to such theories |
| $L_{\infty\omega}$ | none | $\forall x \bigvee_{\beta < \mu} x = c_\beta$ has models of size $\mu$ only |
| second-order logic | exists | above the least inaccessible cardinal, if there is one |

: Hanf numbers of the logics in the chapter. A logic whose sentences form a set has a Hanf number, by Hanf's argument; $L_{\infty\omega}$ has a proper class of sentences.

## Common errors

- **Confusing sequences with sets.** An increasing sequence in a dense linear order is order-indiscernible but not an indiscernible set, since $x_1 < x_2$ holds at $(a_0, a_1)$ and fails at $(a_1, a_0)$.
- **Forgetting the parameters.** Indiscernible over $\emptyset$ does not mean indiscernible over $A$. The sequence $1, 2, 3, \ldots$ in $(\Q, <)$ is indiscernible over $\set{0}$ but not over $\set{3/2}$.
- **Looking for indiscernibles in the given model.** The existence theorem gives them in some $\mathcal{N} \equiv \mathcal{M}$. In $(\Z, <)$ itself no injective sequence is indiscernible, because the distance between two elements is expressed by a formula.
- **Dropping the Skolem functions.** Without them the set of an indiscernible sequence may already be a substructure that is not a model, as an increasing sequence in a dense linear order shows.
- **Reading Vaught's theorem backwards.** An $(\aleph_1, \aleph_0)$-model does not give $(\kappa, \lambda)$-models for all $\kappa > \lambda \ge \aleph_0$; when each element outside $P$ is determined by a subset of $P$, every model has at most $\lambda + 2^\lambda$ elements.
- **Applying Chang's theorem at a singular cardinal.** For $\kappa = \aleph_\omega$ the condition $\kappa^{<\kappa} = \kappa$ fails by König's theorem, whatever the continuum is.
