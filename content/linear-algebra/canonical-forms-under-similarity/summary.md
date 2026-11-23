## What to remember

Throughout, $F$ is a field, $V$ has finite dimension $n \ge 1$ over $F$, and $A \in M_n(F)$ or $T \colon V \to V$ is linear.

- **Cyclic pieces.** For $v \ne 0$, the [cyclic subspace](/42MMQBTP0M/) $Z(v; T)$ spanned by $v, T v, T^2 v, \dots$ has dimension $\deg m_v$, and on it $T$ acts by the [companion matrix](/0ZCWPNZTQ3/) $C(m_v)$. For monic $p$ of degree $n$, $C(p)$ has characteristic and minimal polynomial both equal to $p$, and $T$ has a cyclic vector if and only if $m_T = \chi_T$.
- **Invariant factors decide similarity.** By the [cyclic decomposition theorem](/R3Z20J19BR/), $V = Z(v_1) \oplus \cdots \oplus Z(v_r)$ with annihilators $d_1 \mid \cdots \mid d_r$ that depend only on $T$; $d_r = m_T$ and $d_1 \cdots d_r = \chi_T$. The [rational canonical form](/042JWAR3Q0/) $C(d_1) \oplus \cdots \oplus C(d_r)$ exists over every field, and two matrices are similar if and only if their [invariant factors](/F7GJPMVBXA/) agree.
- **Two lists, one class.** The elementary divisors are the prime powers in the factorizations of the $d_i$. To go back, sort the powers of each irreducible and multiply the largest ones together to get $d_r$, the next largest to get $d_{r-1}$, and so on.
- **No roots needed.** The invariant factors are the nonconstant diagonal entries of the Smith normal form of $xI - A$; with $D_k$ the monic gcd of the $k \times k$ minors, the $k$-th diagonal entry is $D_k / D_{k-1}$ ([characteristic matrix](/92VZF0QRM8/)). Hence [similarity does not depend on the field](/5PVFX89NM7/), and [$A$ is similar to $A^{\mathsf T}$](/C708QKZPE6/) by a symmetric matrix.
- **Jordan form needs splitting.** If $\chi_A$ splits over $F$, then $A$ is similar over $F$ to a direct sum of [Jordan blocks](/07PH4RX0X5/) $J_k(\lambda)$, unique up to order ([Jordan normal form](/085HQ5G5TE/)). Without splitting there may be no Jordan form over $F$.
- **Ranks give the blocks.** For each eigenvalue $\lambda$, with $r_j = \operatorname{rank}(A - \lambda I)^j$, the number of blocks $J_j(\lambda)$ is $r_{j-1} - 2 r_j + r_{j+1}$ ([nilpotent normal form](/Z2RTKWZZAZ/), [computing the Jordan form](/7M1W0ZA49Q/)). The number of blocks for $\lambda$ is the geometric multiplicity, and the largest block size is the exponent of $x - \lambda$ in $m_A$.
- **Real matrices.** Every $A \in M_n(\R)$ has a [real Jordan form](/MPFT45RFGV/) with blocks $J_k(\lambda)$, $\lambda \in \R$, and $C_k(a, b)$, $b > 0$, one for each pair of conjugate blocks $J_k(a \pm ib)$.
- **Commuting matrices.** The [centralizer](/GXZGWZSJ2J/) of $A$ has dimension $\sum_{i, j} \deg \gcd(d_i, d_j) \ge n$, with equality exactly when $A$ is cyclic, and then every matrix commuting with $A$ is a polynomial in $A$. In [Weyr form](/9XEA4VR8WP/) with structure $(n_1, n_2, \dots)$ for a single eigenvalue, this dimension is $\sum n_i^2$.
- **Classes and modules.** Similarity classes in $M_n(F)$ correspond to lists of invariant factors ([classification](/H3E52HTEZ2/)); over $\mathbb{F}_q$ this counts the [conjugacy classes of $GL_n(\mathbb{F}_q)$](/4FV9TDGWWH/), $q^2 - 1$ of them for $n = 2$. Similar matrices are the same as isomorphic [$F[x]$-modules](/KGVTFBZX59/).

## The normal forms side by side

| Form | Field needed | Blocks | Unique up to |
|---|---|---|---|
| Rational canonical form | any field | $C(d_i)$, $d_1 \mid \cdots \mid d_r$ | nothing: it is unique |
| Elementary divisor form | any field | $C(p^e)$ for the prime powers $p^e$ | order of the blocks |
| Jordan normal form | $\chi_A$ splits over $F$ | $J_k(\lambda)$, $\lambda \in F$ | order of the blocks |
| Real Jordan form | $F = \R$ | $J_k(\lambda)$ and $C_k(a, b)$ with $b > 0$ | order of the blocks |

: Four normal forms for similarity. All four decide similarity over their field; they differ in what the field must contain and in the size of the blocks.

## Common errors

- **Trusting $\chi_A$ alone.** $\chi_A$ and $m_A$ together decide similarity only for $n \le 3$. In size $4$, $J_2(0) \oplus J_2(0)$ and $J_2(0) \oplus J_1(0) \oplus J_1(0)$ share both.
- **One block per eigenvalue.** The number of Jordan blocks for $\lambda$ is $\dim \ker (A - \lambda I)$, not $1$ and not the algebraic multiplicity.
- **Stopping at $\dim \ker (A - \lambda I)$.** The kernel dimension gives the number of blocks, but not their sizes; ranks of higher powers are needed from $n = 4$ on.
- **Invariant factors that do not divide.** The list $x + 1, x - 3$ is a list of elementary divisors, not of invariant factors; the invariant factor list is the single polynomial $(x + 1)(x - 3)$.
- **Mixing conventions.** Companion matrices in rows or in columns, and Jordan blocks with ones above or below the diagonal, are transposes of each other. Fix one convention before comparing matrices.
