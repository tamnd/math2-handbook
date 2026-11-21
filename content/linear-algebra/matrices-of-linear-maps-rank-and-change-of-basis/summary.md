## What to remember

- **Matrix of a map.** For bases $B = (b_1, \ldots, b_n)$ of $V$ and $C$ of $W$, column $j$ of $[T]_{C,B}$ is $[T b_j]_C$, and $[T v]_C = [T]_{C,B} [v]_B$. The map $T \mapsto [T]_{C,B}$ is an isomorphism $\operatorname{Hom}(V, W) \cong M_{m \times n}(F)$, and $[S \circ T] = [S][T]$ in matching bases.
- **Bases from row reduction.** The pivot columns of $A$ (not of its echelon form) are a basis of the column space. The nonzero rows of an echelon form are a basis of the row space. The special solutions, one per free variable, are a basis of the null space. Row operations keep the row space and the null space and change the column space.
- **Four fundamental subspaces.** For $A$ of size $m \times n$ and rank $r$, the column space and the row space have dimension $r$, the null space $n - r$ and the left null space $m - r$. Over $\R$, the null space is the orthogonal complement of the row space, and the left null space that of the column space.
- **Rank.** Row rank equals column rank. $\operatorname{rank} A + \dim \operatorname{Null}(A) = n$. The rank can depend on the field: an integer matrix can have smaller rank over $\F_p$ than over $\Q$.
- **Rank of a product.** $\operatorname{rank}(AB) \le \min(\operatorname{rank} A, \operatorname{rank} B)$, and by Sylvester's inequality $\operatorname{rank} A + \operatorname{rank} B - n \le \operatorname{rank}(AB)$ when $A$ has $n$ columns. Multiplying by an invertible matrix does not change the rank.
- **Rank factorization.** A matrix of rank $r$ is $A = CR$ with $C$ of size $m \times r$ and $R$ of size $r \times n$, both of rank $r$; one choice is $C$ = the pivot columns and $R$ = the nonzero rows of the reduced echelon form. The rank-one matrices are exactly the products $u v^\top$ with $u, v \ne 0$.
- **Change of basis.** If column $j$ of $P$ is $[b'_j]_B$, then $[v]_B = P [v]_{B'}$, and $[T]_{C',B'} = Q^{-1} [T]_{C,B} P$. For an endomorphism, $[T]_{B'} = P^{-1} [T]_B P$.
- **Similarity.** $A \sim B$ when $B = P^{-1} A P$ for an invertible $P$. Similar matrices have the same rank, trace, determinant, characteristic polynomial and minimal polynomial, but matrices that share all of these need not be similar.
- **Fredholm alternative.** $Ax = b$ has a solution if and only if $y^\top b = 0$ for every $y$ with $A^\top y = 0$. For square $A$, either $Ax = b$ has exactly one solution for every $b$, or $Ax = 0$ has a nonzero solution.

## The four subspaces

| Subspace | Lies in | Dimension | Basis from | Orthogonal complement over $\R$ |
|---|---|---|---|---|
| [Column space](/03AJKXH1AV/) $\operatorname{Col}(A)$ | $F^m$ | $r$ | pivot columns of $A$ | left null space |
| [Row space](/069MCGX635/) $\operatorname{Row}(A)$ | $F^n$ | $r$ | nonzero rows of an echelon form | null space |
| [Null space](/0PHDYNR24D/) $\operatorname{Null}(A)$ | $F^n$ | $n - r$ | special solutions | row space |
| Left null space $\operatorname{Null}(A^\top)$ | $F^m$ | $m - r$ | special solutions of $A^\top y = 0$ | column space |

: The [four fundamental subspaces](/73DVECPAT6/) of an $m \times n$ matrix $A$ of rank $r$. The last column holds only over $\R$ with the dot product; over $\F_2$ the vector $(1, 1)$ is orthogonal to itself, so a subspace and its orthogonal can meet.

## Common errors

- **Writing images as rows.** The coordinates of $T b_j$ go in column $j$, not row $j$. Writing them as rows gives the transpose, which is the matrix of a different map.
- **Taking the pivot columns of the reduced form.** They span the column space of the reduced matrix, which is in general a different subspace. Read off the positions of the pivots from the reduced form, then take those columns of $A$ itself.
- **Mixing up the two directions of change of basis.** With $P$ as above, $[v]_{B'} = P^{-1}[v]_B$, not $P[v]_B$. Before using a formula from another book, check whether its $P$ is this one or its inverse.
- **Deciding similarity by invariants alone.** Equal trace and determinant settle nothing in general. To show two matrices are not similar, find an invariant that differs, such as $\operatorname{rank}(A - \lambda I)$ for an eigenvalue $\lambda$. To show they are similar, find $P$ or bring both to the same canonical form.
- **Expecting $\operatorname{rank}(AB) = \operatorname{rank}(BA)$.** For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $AB = 0$ while $BA = A$ has rank $1$.
