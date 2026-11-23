## What to remember

- An $L$-[structure](/983GZBQYT4/) $\mathcal{M}$ has a nonempty domain $M$, an element $c^{\mathcal{M}}$ for each constant, a total function $f^{\mathcal{M}} \colon M^n \to M$ for each $n$-ary function symbol and a relation $R^{\mathcal{M}} \subseteq M^n$ for each $n$-ary relation symbol.
- [Satisfaction](/2RBQPV02AS/) $\mathcal{M} \models \varphi[s]$ is defined by recursion on $\varphi$. The connectives follow their truth tables, and $\mathcal{M} \models \forall x \, \varphi[s]$ holds when $\mathcal{M} \models \varphi[s[x \mapsto a]]$ for every $a \in M$; for $\exists x$, for some $a \in M$.
- A sentence is [true](/K7XDVK5854/) in $\mathcal{M}$ when it is satisfied under one assignment, or equivalently under all of them. Each sentence is true or false in $\mathcal{M}$, so $\mathrm{Th}(\mathcal{M})$ is complete.
- $\mathcal{M}$ is a [model](/MVCH6N9SNW/) of $T$ when $T \subseteq \mathrm{Th}(\mathcal{M})$. $T \models \sigma$ when every model of $T$ is a model of $\sigma$, and more axioms give fewer models.
- $\varphi$ is [valid](/5SDS9T8E7J/) if and only if $\neg \varphi$ is unsatisfiable, if and only if its universal closure is valid. The valid sentences are exactly the provable ones, so they form a computably enumerable set, but by Church's theorem not, in general, a decidable one.
- [Coincidence](/FM580NZ9W6/): satisfaction depends only on the values of the free variables and on the symbols that occur. [Substitution](/A7S460KHBM/): if $t$ is substitutable for $x$ in $\varphi$, then $\mathcal{M} \models \varphi[t/x][s]$ if and only if $\mathcal{M} \models \varphi[s[x \mapsto t^{\mathcal{M}}[s]]]$.
- [Isomorphism invariance](/NDTJ2E895C/): an isomorphism $h \colon \mathcal{M} \to \mathcal{N}$ gives $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{N} \models \varphi[h \circ s]$. So automorphisms fixing $A$ preserve every relation [definable](/1DQ1M6ZWS4/) with parameters from $A$.
- The [Herbrand universe](/NFW38QJ3A7/) is the set of closed terms, and in a [Herbrand structure](/HKW429DSDK/) each term denotes itself. A set of universal sentences without equality has a model if and only if it has a Herbrand model.

| Notion | Definition | Reduction |
|---|---|---|
| $\varphi$ is satisfiable | $\mathcal{M} \models \varphi[s]$ for some $\mathcal{M}$ and $s$ | $\neg \varphi$ is not valid |
| $\varphi$ is valid | $\mathcal{M} \models \varphi[s]$ for every $\mathcal{M}$ and $s$ | $\neg \varphi$ is not satisfiable |
| $\mathcal{M} \models T$ | every sentence of $T$ is true in $\mathcal{M}$ | $T \subseteq \mathrm{Th}(\mathcal{M})$ |
| $T \models \sigma$ | every model of $T$ is a model of $\sigma$ | $T \cup \set{\neg \sigma}$ has no model |
| $\set{\gamma_1, \ldots, \gamma_n} \models \sigma$ | as above, for a finite set | $(\gamma_1 \land \cdots \land \gamma_n) \to \sigma$ is valid |
| $\mathcal{M} \equiv \mathcal{N}$ | $\mathrm{Th}(\mathcal{M}) = \mathrm{Th}(\mathcal{N})$ | implied by $\mathcal{M} \cong \mathcal{N}$, but weaker |

: The semantic notions of first-order logic and how they reduce to one another. The last row is strictly weaker than isomorphism: $(\Q, <)$ and $(\R, <)$ have the same theory but are not isomorphic.

## Common errors

- Asking whether a formula with free variables is true in a structure. It is satisfied or not under an assignment; only sentences are true or false outright.
- Allowing an empty domain or a partial function. Division is not a function symbol of a field structure on $\R$, because it is undefined at $0$, and the convention of nonempty domains is what makes $\forall x \, P(x) \to \exists x \, P(x)$ and the drinker principle valid.
- Reading $\models$ in two ways without noticing. $\mathcal{M} \models \sigma$ is truth in one structure; $T \models \sigma$ is consequence over all models of $T$.
- Using the substitution lemma when the term is not substitutable. Rename bound variables first.
- Expecting the converse of the automorphism method. A relation can be invariant under every automorphism and still not be definable: in the rigid structure $(\N, <)$ every subset is invariant, but only countably many subsets are definable.
- Applying the Herbrand model theorem to sentences that are not universal, or that use equality. A satisfiable sentence of the form $\exists x \, \varphi$ can fail to have a Herbrand model; Skolemize first.
