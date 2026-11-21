## What to remember

- **Vector space:** a set $V$ with an addition and a scalar multiplication by a field $F$, satisfying eight axioms: addition is associative and commutative with a zero and negatives, and $a(bv) = (ab)v$, $1v = v$, $a(u + v) = au + av$, $(a + b)v = av + bv$.
- **Subspace:** a subset that contains $0$ and is closed under addition and scalar multiplication. Intersections of subspaces are subspaces. $U \cup W$ is a subspace only if $U \subseteq W$ or $W \subseteq U$. The smallest subspace containing both is $U + W = \set{u + w : u \in U, w \in W}$.
- **Span and independence:** the span of $S$ is the set of finite linear combinations of vectors of $S$, the smallest subspace that contains $S$. A family is linearly independent when $a_1v_1 + \cdots + a_kv_k = 0$ forces all $a_i = 0$; equivalently, no vector is a combination of the others.
- **Column test:** the columns of an $m \times n$ matrix $A$ are independent if and only if $Ax = 0$ has only the solution $0$, if and only if every column has a pivot. More than $m$ vectors in $F^m$ are dependent. The columns span $F^m$ if and only if every row has a pivot.
- **Basis and coordinates:** a basis is an independent spanning family. Each $v$ is then $a_1b_1 + \cdots + a_nb_n$ for exactly one list of scalars, its coordinate vector $[v]_B$, and $v \mapsto [v]_B$ identifies $V$ with $F^n$.
- **Steinitz and dimension:** if $u_1, \dots, u_m$ are independent and $w_1, \dots, w_n$ span $V$, then $m \le n$. So all bases have the same size, $\dim V$. Every vector space has a basis (by Zorn's lemma); every spanning set contains one, and every independent set extends to one.
- **Counting in dimension $n$:** a subspace $W$ has $\dim W \le n$, with equality only for $W = V$. Any $n$ independent vectors form a basis, and so do any $n$ spanning vectors. For finite-dimensional subspaces, $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$.
- **Other fields:** a space of dimension $n$ over $\mathbb{F}_q$ has $q^n$ vectors and $(q^n - 1)(q^n - q) \cdots (q^n - q^{n-1})$ ordered bases. A complex space of dimension $n$ is a real space of dimension $2n$, and $\dim_\C V_\C = \dim_\R V$.

## Standard spaces

| Space | Dimension | A basis |
|---|---|---|
| [$F^n$](/713F6AM1X1/) | $n$ | $e_1, \dots, e_n$ |
| [$M_{m \times n}(F)$](/0RE6X3BGPN/) | $mn$ | the matrix units $E_{ij}$ |
| [$P_n(F)$](/0JGZCDT5DN/), degree at most $n$ | $n + 1$ | $1, x, \dots, x^n$ |
| $F[x]$ | $\aleph_0$ | $1, x, x^2, \dots$ |
| [$F^{(S)}$](/0GZB2SN0PH/), finitely supported functions | $\abs{S}$ | the functions $\delta_s$ |
| $F^S$, $S$ infinite | infinite | one exists by Zorn's lemma; the $\delta_s$ do not span |
| $\C$ over $\R$ | $2$ | $1, i$ |
| $\R$ over $\Q$ | $2^{\aleph_0}$ | a [Hamel basis](/ZCBD0GRGVA/), which exists but cannot be listed |

: Some spaces of the chapter, with their dimensions. The same set can have different dimensions over different fields: $\C$ has dimension $1$ over $\C$ and $2$ over $\R$.

## Common errors

- **Forgetting the zero vector.** A set that does not contain $0$, such as the plane $x + y + z = 1$ or the functions with $f(0) = 1$, is not a subspace. Check $0$ first.
- **Treating independence of a set as independence of each pair.** The vectors $(1, 0)$, $(0, 1)$, $(1, 1)$ are pairwise independent, but the three together are dependent.
- **Ignoring the field.** Independence and dimension depend on the scalars. A family of vectors with integer entries can be independent over $\R$ and dependent over $\mathbb{F}_2$.
- **Allowing infinite sums.** Spans and bases use finite combinations only. The vectors $e_1, e_2, \dots$ are a basis of the finitely supported sequences but not of the space of all sequences.
- **Using the right-size criterion without knowing the dimension.** "$n$ independent vectors form a basis" holds only in a space of dimension $n$. In practice: find $\dim V$ first, then check only one of independence and spanning.
- **Reading pivots off the wrong matrix.** For the column test, put the vectors as columns and use the pivot columns of the original matrix, not of its echelon form, as the basis of the span.
