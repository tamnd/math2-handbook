## What to remember

- **[Categoricity](/1JJCGNX240/):** $T$ is $\kappa$-categorical when it has a model of size $\kappa$ and any two models of size $\kappa$ are isomorphic, that is, $I(T, \kappa) = 1$. A theory with an infinite model is never categorical outright, since it has models of every infinite size $\kappa \ge \abs{L}$.
- **[Łoś–Vaught test](/ZR7Y5C235P/):** if $T$ has no finite models and is $\kappa$-categorical for some infinite $\kappa \ge \abs{L}$, then $T$ is complete. All three hypotheses are needed, and the converse fails: $\operatorname{Th}(\Z, <)$ is complete and categorical in no infinite cardinal.
- **Four patterns:** a complete countable theory with infinite models is totally categorical, $\aleph_0$-categorical only, uncountably categorical only, or categorical in no infinite cardinal. By [Morley's categoricity theorem](/V7N84P60SJ/) there is no other pattern, and the [standard examples](/20QJANNKP7/) show that all four occur.
- **[Atomic](/HSJ4F9J8SM/) and [prime](/S8W40PYNHX/) models:** $M$ is atomic when every tuple realizes an isolated type, and prime when it embeds elementarily into every model of $T$. In a countable language, $M$ is prime exactly when it is countable and atomic, and any two countable atomic models are isomorphic. A prime model exists exactly when the isolated types are dense in each $S_n(T)$.
- **[Countable saturated models](/7GN6XF590M/):** a complete countable $T$ has a countable saturated model exactly when it is [small](/W6XM5NVNRP/), that is, $\abs{S_n(T)} \le \aleph_0$ for all $n$. The countable saturated model realizes every type, every countable model embeds elementarily into it, and it is unique up to isomorphism.
- **[Ryll-Nardzewski](/1513J40TKA/):** for complete countable $T$ with infinite models, these are equivalent: $T$ is $\aleph_0$-categorical; each $S_n(T)$ is finite; there are finitely many formulas in $x_1, \ldots, x_n$ up to equivalence modulo $T$; every type is isolated; the countable model has finitely many automorphism orbits on $n$-tuples for each $n$. Then the countable model is both prime and saturated.
- **Counting countable models:** $I(T, \aleph_0)$ is never $2$ ([Vaught](/E5W3RRSY5Z/)); every finite number from $3$ on occurs ([Ehrenfeucht](/XT2D23G98S/) and its coloured variants); an infinite number is $\aleph_0$, $\aleph_1$ or $2^{\aleph_0}$ ([Morley](/JFG783DEG8/)). Whether exactly $\aleph_1 < 2^{\aleph_0}$ countable models can occur is the [Vaught conjecture](/YVBHE2SEE6/), open for first-order theories.
- **Smallness as the first dividing line:** a theory that is not small has some $S_n(T)$ of size $2^{\aleph_0}$, so it has $2^{\aleph_0}$ countable models. A small theory has a prime model and a countable saturated model, and they coincide exactly when $T$ is $\aleph_0$-categorical.

## The standard theories side by side

| Theory | $\aleph_0$-categorical | Countable models | Small | Prime model | Countable saturated model |
|---|---|---|---|---|---|
| [Dense linear orders without endpoints](/2W4S2H4VYA/) | yes | $1$ | yes | $(\Q, <)$ | $(\Q, <)$ |
| [Infinitely many infinite classes](/N232QBKCAA/) | yes | $1$ | yes | the countable model | the countable model |
| [Ehrenfeucht's theory](/XT2D23G98S/) | no | $3$ | yes | constants unbounded | constants bounded, no least upper bound |
| $\mathrm{ACF}_0$ | no | $\aleph_0$ | yes | [$\overline{\Q}$](/NS2NZRZXJB/) | transcendence degree $\aleph_0$ |
| [Order of $\Z$](/91WRBX69MB/) | no | $2^{\aleph_0}$ | yes | $(\Z, <)$ | $\Z \cdot \Q$ |
| [Independent unary predicates](/9MV9VG8G67/) | no | $2^{\aleph_0}$ | no | none | none |

: Six complete theories in countable languages. The last two rows show that $2^{\aleph_0}$ countable models can come from a small theory as well as from one that is not small. Only an $\aleph_0$-categorical theory has the same model in the last two columns.

## Common errors

- **Dropping a hypothesis of the Łoś–Vaught test.** The theory of nonempty sets is categorical in every infinite cardinal and is not complete, because it has finite models. In a language with $\aleph_1$ constants, categoricity in $\aleph_0$ does not give completeness.
- **Reading $\aleph_0$-categoricity as categoricity in every size.** Dense linear orders have one countable model and many models of each uncountable size.
- **Confusing atomic with prime.** $(\R, <)$ is atomic for dense linear orders, but it is not prime, since it does not embed into $(\Q, <)$. The equivalence of prime with atomic needs the model to be countable.
- **Confusing prime with minimal.** $(\Q, <)$ is prime, but it has the proper elementary substructure $\Q \cap (0, 1)$.
- **Reversing the implication about smallness.** A theory that is not small has $2^{\aleph_0}$ countable models, but $2^{\aleph_0}$ countable models do not make a theory non-small; $\operatorname{Th}(\Z, <)$ is small.
- **Counting the wrong types.** Smallness and the Ryll-Nardzewski theorem count types over the empty set, or equivalently over finite sets. Over the countable model, the theory of $(\Q, <)$ has $2^{\aleph_0}$ types, one for each cut.
- **Applying the never-two theorem to an incomplete theory.** The theory saying that there are infinitely many elements and that a unary predicate holds of everything or of nothing has exactly two countable models.
