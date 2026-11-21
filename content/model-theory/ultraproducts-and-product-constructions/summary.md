## What to remember

- **[Reduced product](/F4WRD396PB/):** for a filter $F$ on $I$, the classes of $\prod_i M_i$ under "agree on a set in $F$". Functions act coordinatewise, and a relation holds when it holds on a set of indices in $F$. Reduced products keep [Horn sentences](/8RRECJJM3G/), so products of groups are groups, but $\R^{\N}$ modulo the cofinite filter is a ring with zero divisors, not a field.
- **[Łoś's theorem](/AGYBSTD7BG/):** if $U$ is an ultrafilter, then $\prod_U M_i \models \varphi([a_1], \ldots, [a_n])$ exactly when $\set{i : M_i \models \varphi(a_1(i), \ldots, a_n(i))} \in U$. The proof is an induction on $\varphi$. Negation uses that $U$ is an ultrafilter, and the existential step uses the axiom of choice to pick witnesses.
- **Principal ultrafilters give nothing new:** if $U$ is principal at $i_0$, the ultraproduct is isomorphic to $M_{i_0}$. All the interesting examples need a nonprincipal ultrafilter, and so the ultrafilter lemma.
- **[Compactness](/EY09JT7270/):** if every finite $\Delta \subseteq T$ has a model $M_\Delta$, then $\prod_\Delta M_\Delta / U$ is a model of $T$ for any ultrafilter $U$ on the finite subsets of $T$ that contains every set $\set{\Delta : \varphi \in \Delta}$.
- **[Ultrapowers](/5ZVJK0V0GF/):** the diagonal map $d(m) = [(m, m, \ldots)]$ is an elementary embedding of $M$ into $M^I/U$. It is onto when $M$ is finite, and $\abs{M^I/U} \le \abs{M}^{\abs{I}}$. With $\R$ and a nonprincipal ultrafilter on $\N$ it gives the hyperreals, and $[(1, 1/2, 1/3, \ldots)]$ is a positive infinitesimal.
- **Elementary equivalence:** $M \equiv N$ exactly when $M$ embeds elementarily into some ultrapower of $N$ ([Frayne](/QPX9HG9BH4/)), and exactly when $M$ and $N$ have isomorphic ultrapowers $M^I/U \cong N^I/U$ ([Keisler–Shelah](/A37HPCKCE2/): Keisler under GCH, Shelah in ZFC).
- **[Elementary classes](/4HNAJQQ8Z0/):** a class is elementary exactly when it is closed under elementary equivalence and ultraproducts, and exactly when it is closed under isomorphism, ultraproducts and ultraroots. It is basic elementary, defined by one sentence, exactly when it and its complement are both closed under isomorphism and ultraproducts.
- **[Feferman–Vaught](/RYMZZ2AWFT/):** the truth of a formula in a product is determined by the truth of finitely many formulas in the factors, combined through a formula about sets of indices. So $M_i \equiv N_i$ for all $i$ gives $\prod M_i \equiv \prod N_i$.
- **[Saturation](/DYXQP8WS63/):** in a countable language, an ultraproduct over a countably incomplete ultrafilter is $\aleph_1$-saturated. A countably incomplete $\kappa$-good ultrafilter gives $\kappa$-saturation when $\abs{L} < \kappa$. [Keisler's order](/TD5D2G5PYP/) compares theories by which regular ultrafilters saturate their ultrapowers.

## Constructions and what they keep

| Construction | Filter on $I$ | Sentences that pass from almost all factors |
|---|---|---|
| [Direct product](/WJ73XYBNE4/) | $\set{I}$ | Horn sentences that hold in all factors |
| [Reduced product](/F4WRD396PB/) | any proper filter | Horn sentences |
| [Ultraproduct](/AX9Q86GB8M/) | ultrafilter | all first-order sentences |
| [Ultrapower](/5ZVJK0V0GF/) | ultrafilter, all factors equal | all first-order formulas with parameters from $M$ |

: The four constructions of the chapter. A larger filter identifies more sequences and keeps more sentences. Only ultrafilters keep negations and disjunctions.

## Common errors

- **Expecting a reduced product to keep everything.** The sentence "every nonzero element has an inverse" is not Horn, and it fails in $\R^{\N}$ modulo the cofinite filter, where $(1, 0, 1, 0, \ldots)$ is nonzero and has no inverse.
- **Using a principal ultrafilter by accident.** A nonprincipal ultrafilter contains no finite set. An argument that only needs some set in $U$ may silently work in a single factor.
- **Applying Łoś's theorem beyond first-order logic.** An ultrapower of $(\N, <)$ over a nonprincipal ultrafilter is not well ordered, and an ultraproduct of finite sets of growing size is infinite. Second-order and infinitary properties do not pass.
- **Taking the index set of Keisler–Shelah to be $\N$.** The theorem gives some index set and ultrafilter. Shelah showed that it is consistent that two countable elementarily equivalent structures have no isomorphic ultrapowers over $\N$.
- **Confusing elementary and basic elementary.** Fields of characteristic $0$ form an elementary class, but not a basic one: the complement, the fields of positive characteristic, is not closed under ultraproducts.
- **Forgetting the size bound.** An ultrapower of a countable structure over a nonprincipal ultrafilter on $\N$ is uncountable when the structure is infinite, so it is never a countable nonstandard model.
