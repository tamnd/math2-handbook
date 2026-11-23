## What to remember

- **[Internal direct sum](/0XYYT5KNTX/):** for subspaces $U_1, \dots, U_k$ of $V$, the sum $U_1 + \dots + U_k$ is direct when every vector of the sum is $u_1 + \dots + u_k$ with $u_i \in U_i$ in only one way, equivalently when $0$ has only the trivial decomposition. For two subspaces this means $U \cap W = \set{0}$. For three or more, pairwise trivial intersections are not enough; the test is $U_i \cap \sum_{j \ne i} U_j = \set{0}$ for each $i$.
- **[Sums and products](/0EX2HPXPJ6/):** the [external direct sum](/0S7W6EG32V/) $\bigoplus_i V_i$ consists of the families $(v_i)$ with only finitely many $v_i \ne 0$; the direct product $\prod_i V_i$ allows all families. They agree for finitely many factors and differ for infinitely many.
- **[Complements](/0M83V17KHX/):** a complement of $U$ in $V$ is a subspace $W$ with $V = U \oplus W$. [Every subspace has one](/0P9T8WHNMH/): extend a basis of $U$ to a basis of $V$ and take the span of the new vectors (in infinite dimension this uses the axiom of choice). Complements are not unique unless $U = \set{0}$ or $U = V$.
- **[Projections](/033DA1WE8Y/):** a linear map $P \colon V \to V$ with $P^2 = P$ gives $V = \operatorname{im} P \oplus \ker P$, and every decomposition $V = U \oplus W$ comes from exactly one projection with image $U$ and kernel $W$. Then $I - P$ is the projection with image $W$ and kernel $U$.
- **[Quotient space](/0BR3FY5Q8M/):** for a subspace $U$ of $V$, the cosets $v + U$ form a vector space $V/U$ with $(v + U) + (w + U) = (v + w) + U$ and $c(v + U) = cv + U$. Two cosets are equal, $v + U = w + U$, exactly when $v - w \in U$. If $V$ is finite-dimensional, [$\dim V/U = \dim V - \dim U$](/0SXDQ6TN00/), and every complement of $U$ maps isomorphically onto $V/U$.
- **[Universal property](/0ZERJX6PH6/):** if $T \colon V \to W$ is linear and $U \subseteq \ker T$, there is exactly one linear $\bar T \colon V/U \to W$ with $\bar T(v + U) = T(v)$. It is injective exactly when $U = \ker T$.
- **Isomorphism theorems:** [first](/0MTBGVZ4XJ/), $V/\ker T \cong \operatorname{im} T$; [second](/0APN65D6Y6/), $(U + W)/W \cong U/(U \cap W)$; [third](/07RB3EMBWW/), $(V/W)/(U/W) \cong V/U$ for $W \subseteq U \subseteq V$. None of them needs finite dimension.
- **[Codimension](/JJCGJ1EGCQ/):** $\operatorname{codim} U = \dim V/U$, the dimension of any complement. A subspace of codimension $1$ is a hyperplane; $x\F[x]$ has codimension $1$ in $\F[x]$ though both are infinite-dimensional.
- **[Exact sequences](/946YAZNYKX/):** $0 \to U \xrightarrow{f} V \xrightarrow{g} W \to 0$ is exact when $f$ is injective, $g$ is surjective and $\operatorname{im} f = \ker g$. For vector spaces every such sequence splits, $V \cong U \oplus W$, and in finite dimension $\dim V = \dim U + \dim W$.

| | Complement $W$ of $U$ | Quotient $V/U$ |
|---|---|---|
| Where it lives | inside $V$ | outside $V$, as a set of cosets |
| Depends on a choice | yes | no |
| Dimension (finite $V$) | $\dim V - \dim U$ | $\dim V - \dim U$ |
| Comes with a map | inclusion $W \to V$ and projection along $U$ | quotient map $V \to V/U$, $v \mapsto v + U$ |
| Used for | splitting a vector into parts | maps that vanish on $U$ |

: Two ways to cut away a subspace; restricting the quotient map to any complement is an isomorphism.

## Common errors

- **Adding dimensions without checking the intersection.** $\dim U + \dim W = \dim V$ does not give $V = U \oplus W$; the subspaces may overlap. Check $U \cap W = \set{0}$ as well.
- **Testing a sum of three subspaces pairwise.** Three distinct lines in $\R^2$ meet pairwise in $0$, but their sum is not direct.
- **Calling a complement "the" complement.** A plane in $\R^3$ has infinitely many complementary lines. Only with an inner product is there a preferred one, the orthogonal complement.
- **Defining a map on $V/U$ through a representative without checking it.** A formula $v + U \mapsto T(v)$ is well defined only when $T$ vanishes on $U$.
- **Treating cosets as subspaces.** $v + U$ is a subspace only when $v \in U$, and then it is $U$ itself.
- **Confusing the direct sum and the product.** For infinitely many factors, $\bigoplus$ is a proper subspace of $\prod$; the sequences with finitely many nonzero terms are not all sequences.
