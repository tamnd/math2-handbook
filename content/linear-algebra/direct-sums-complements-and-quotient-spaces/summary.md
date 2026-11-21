## What to remember

- **Direct sum.** $V = U_1 \oplus \cdots \oplus U_k$ when every $v \in V$ is $u_1 + \cdots + u_k$ with $u_i \in U_i$ in exactly one way. For two subspaces this holds exactly when $U + W = V$ and $U \cap W = 0$; in finite dimension, when $U \cap W = 0$ and $\dim U + \dim W = \dim V$. For three or more subspaces, zero pairwise intersections are not enough.
- **External sum and product.** The direct sum $\bigoplus_i V_i$ consists of the families $(v_i)$ with only finitely many $v_i \ne 0$; the product $\prod_i V_i$ allows all families. They agree for finitely many factors. Maps out of $\bigoplus_i V_i$ and maps into $\prod_i V_i$ are given by families of maps on the factors.
- **Complements** exist for every subspace, by extending a basis of $U$ to a basis of $V$ (Zorn's lemma in general). They are unique only when $U = 0$ or $U = V$, and every complement of $U$ is isomorphic to $V/U$.
- **Projections.** A linear map $P \colon V \to V$ with $P^2 = P$ gives $V = \operatorname{im} P \oplus \ker P$, and every decomposition $V = U \oplus W$ comes from exactly one projection, the one onto $U$ along $W$.
- **Quotient.** $V/U = \set{v + U : v \in V}$, with $v + U = v' + U$ exactly when $v - v' \in U$. The quotient map $\pi(v) = v + U$ is linear and surjective with kernel $U$, and $\dim V/U = \dim V - \dim U$ when $V$ is finite-dimensional.
- **Universal property.** If $T \colon V \to W$ is linear and $U \subseteq \ker T$, there is exactly one linear $\bar T \colon V/U \to W$ with $\bar T \circ \pi = T$, namely $\bar T(v + U) = T(v)$.
- **Isomorphism theorems.** $V/\ker T \cong \operatorname{im} T$; $\;U/(U \cap W) \cong (U + W)/W$; and for $W \subseteq U \subseteq V$, $\;(V/W)/(U/W) \cong V/U$.
- **Codimension.** $\operatorname{codim} U = \dim V/U$. Always $\operatorname{codim}(U \cap W) \le \operatorname{codim} U + \operatorname{codim} W$, with equality when $U + W = V$ and both codimensions are finite.
- **Exact sequences.** $0 \to U \xrightarrow{f} V \xrightarrow{g} W \to 0$ is exact when $f$ is injective, $g$ is surjective and $\operatorname{im} f = \ker g$. Over a field it always splits, $V \cong U \oplus W$, and for a finite exact sequence of finite-dimensional spaces the alternating sum of the dimensions is $0$.

## Constructions compared

| Construction | Elements | Dimension in finite cases | Depends on a choice |
|---|---|---|---|
| [Internal direct sum](/0XYYT5KNTX/) $U \oplus W$ | sums $u + w$, written uniquely | $\dim U + \dim W$ | no |
| [External direct sum](/0S7W6EG32V/) $\bigoplus_i V_i$ | finitely supported families | $\sum_i \dim V_i$ | no |
| [Direct product](/0EX2HPXPJ6/) $\prod_i V_i$ | all families | $\sum_i \dim V_i$ | no |
| [Complement](/0M83V17KHX/) $W$ of $U$ | vectors of a subspace of $V$ | $\dim V - \dim U$ | yes |
| [Quotient](/0BR3FY5Q8M/) $V/U$ | cosets $v + U$ | $\dim V - \dim U$ | no |

: Five constructions. The direct sum and the product differ only for infinite families: $\bigoplus_{n \in \N} \R$ has countable dimension, while $\R^{\N}$ does not. A complement and the quotient are isomorphic, but only the quotient comes without a choice.

## Common errors

- **Checking only pairwise intersections.** Three lines in $\R^2$ meet pairwise in $0$, but their sum is not direct. For several subspaces, test that each $U_i$ meets the sum of the others in $0$, or compare dimensions.
- **Taking the orthogonal complement as the only complement.** In $\R^n$ the [orthogonal complement](/0XJXTBCB2T/) is one complement among many; any subspace of the right dimension that meets $U$ in $0$ will do.
- **Treating a coset as a vector of $V$.** The coset $v + U$ is a set; $v$ is one of its representatives. A formula on $V/U$ is well defined only if it gives the same value for every representative; the condition $U \subseteq \ker T$ ensures this.
- **Concluding $P = 0$ or $P = I$ from $P^2 = P$.** The equation $P(P - I) = 0$ has many solutions, because matrices have zero divisors. Every projection other than $0$ and $I$ is one.
- **Reading $g \circ f = 0$ as exactness.** It says only $\operatorname{im} f \subseteq \ker g$. Exactness asks for equality.
- **Carrying splitting over to groups.** The sequence $0 \to \Z \xrightarrow{2} \Z \to \Z/2 \to 0$ is exact but does not split, and $2\Z$ has no complement in $\Z$. Complements exist because the scalars form a field.
