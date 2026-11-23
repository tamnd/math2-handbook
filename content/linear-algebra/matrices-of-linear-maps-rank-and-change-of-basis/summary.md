## What to remember

- **[Matrix of a linear map](/0YQSGNYE3K/):** for bases $B$ of $V$ and $C$ of $W$, column $j$ of $[f]_{C,B}$ is the coordinate vector $[f(b_j)]_C$, and $[f(v)]_C = [f]_{C,B}[v]_B$. The map $f \mapsto [f]_{C,B}$ is an [isomorphism](/06HMCTAQH3/) $\operatorname{Hom}(V, W) \cong M_{m \times n}(F)$, and the [matrix of a composition is the product](/05Q1B7MH0M/), $[g \circ f]_{D,B} = [g]_{D,C}[f]_{C,B}$.
- **[Four fundamental subspaces](/73DVECPAT6/):** an $m \times n$ matrix $A$ of rank $r$ has $\dim \operatorname{Col} A = \dim \operatorname{Row} A = r$, $\dim \operatorname{Null} A = n - r$ and $\dim \operatorname{Null} A^{\mathsf{T}} = m - r$. A basis of the column space is given by the pivot columns of $A$ itself, not of its echelon form; a basis of the row space by the nonzero rows of any echelon form.
- **[Rank](/0ZC9YTXZRY/):** the rank of $A$ is the number of pivots, the dimension of the column space, the dimension of the row space ([row rank equals column rank](/0TZAG60ZYT/)) and the largest size of a nonzero minor. It depends on the field: a matrix of integers can have a smaller rank over $\mathbb{F}_p$ than over $\Q$.
- **[Rank-nullity for matrices](/TR48YQGCCA/):** $\operatorname{rank} A + \dim \operatorname{Null} A = n$, the number of columns.
- **[Rank of a product](/02FDWY55AS/):** $\operatorname{rank}(AB) \le \min(\operatorname{rank} A, \operatorname{rank} B)$, with equality for the rank of $B$ when $A$ is invertible, and [Sylvester's inequality](/GS8WE1ZYV9/) $\operatorname{rank}(AB) \ge \operatorname{rank} A + \operatorname{rank} B - n$ for $A$ of size $m \times n$.
- **[Rank factorization](/5JGAG62VN8/):** a matrix of rank $r \ge 1$ is $CR$ with $C$ of size $m \times r$ and $R$ of size $r \times n$, both of rank $r$; take the pivot columns of $A$ and the nonzero rows of its reduced row echelon form. A matrix has rank $1$ exactly when it is $uv^{\mathsf{T}}$ with $u, v \ne 0$.
- **[Change of basis](/0MQXVZEBMT/):** if column $j$ of $P$ is $[b'_j]_B$, then $[v]_B = P[v]_{B'}$ and $[v]_{B'} = P^{-1}[v]_B$. With $Q$ the matrix for the bases $C$, $C'$ of $W$, $[T]_{C',B'} = Q^{-1}[T]_{C,B}P$; for an endomorphism, $[T]_{B'} = P^{-1}[T]_B P$.
- **[Similarity](/0E89HQATM8/):** $A$ and $B$ are similar when $B = P^{-1}AP$ for an invertible $P$, that is, when they are matrices of one endomorphism. Similar matrices have the same rank, trace, determinant, characteristic polynomial and minimal polynomial, but [these do not decide similarity](/J4Q3B9ZNHF/).
- **[Trace](/0KZDNGA561/) and [Fredholm alternative](/4HH8C9V8JQ/):** the trace of an endomorphism is the trace of any of its matrices, and a projection $P$ has $\operatorname{tr} P = (\operatorname{rank} P) \cdot 1_F$. For $A$ of size $m \times n$, $Ax = b$ has a solution if and only if $y^{\mathsf{T}} b = 0$ for every $y$ with $A^{\mathsf{T}} y = 0$.

| Subspace | Lives in | Dimension | Basis from row reduction |
|---|---|---|---|
| [Column space](/03AJKXH1AV/) $\operatorname{Col} A$ | $F^m$ | $r$ | pivot columns of $A$ |
| [Row space](/069MCGX635/) $\operatorname{Row} A$ | $F^n$ | $r$ | nonzero rows of an echelon form |
| [Null space](/0PHDYNR24D/) $\operatorname{Null} A$ | $F^n$ | $n - r$ | one vector for each free variable |
| Left null space $\operatorname{Null} A^{\mathsf{T}}$ | $F^m$ | $m - r$ | null space of $A^{\mathsf{T}}$, or the last $m - r$ rows of $E$ with $EA$ in echelon form |

: The four subspaces of an $m \times n$ matrix $A$ of rank $r$.

## Common errors

- **Writing images as rows.** The columns of $[f]_{C,B}$ are the coordinates of the images $f(b_j)$. Writing them as rows gives the transpose, which is the matrix of a different map.
- **Using the pivot columns of the echelon form.** Row operations change the column space. The pivot positions are read from the echelon form, but the basis vectors must be taken from $A$.
- **Turning the change of basis matrix the wrong way.** $P$ with the new basis vectors as columns turns new coordinates into old ones. New coordinates are $P^{-1}[v]_B$, not $P[v]_B$.
- **Taking the trace in two bases.** The diagonal of a matrix of $T \colon V \to V$ is the trace only when the same basis is used for the input and the output.
- **Deciding similarity by invariants.** Equal rank, trace, determinant and characteristic polynomial do not prove that two matrices are similar; one different value proves that they are not.
- **Forgetting the field.** The rank of the same integer matrix can drop when the entries are read modulo a prime, and a trace that counts a rank over $\R$ can be $0$ over $\mathbb{F}_2$.
