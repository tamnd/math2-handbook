## What to remember

- **Inverse.** An $n \times n$ matrix $A$ over a field is invertible when $AB = BA = I_n$ for some $B$. The inverse is unique. For square matrices over a field, $AB = I_n$ alone already gives $BA = I_n$. For $2 \times 2$ matrices, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ when $ad - bc \ne 0$.
- **Products.** Over a commutative ring, if $A$ and $B$ are invertible then $(AB)^{-1} = B^{-1} A^{-1}$. Over a field, a product of square matrices is invertible if and only if every factor is.
- **Row reduction.** For an $n \times n$ matrix $A$ over a field, the following are equivalent: $A$ is invertible; $Ax = 0$ has only the trivial solution; the reduced row echelon form of $A$ is $I_n$; $A$ is a product of elementary matrices. Reducing $[A \mid I_n]$ ends at $[I_n \mid A^{-1}]$ when $A$ is invertible.
- **Triangular matrices.** Over a field, a triangular matrix is invertible if and only if its diagonal has no zero, and the inverse is triangular of the same kind, with diagonal entries $t_{ii}^{-1}$.
- **Groups.** $\mathrm{GL}_n(F)$ is the group of invertible $n \times n$ matrices, and $\mathrm{SL}_n(F)$, the kernel of $\det$, is its subgroup of matrices of determinant $1$. Over a field $F$, the transvections $T_{ij}(c) = I_n + cE_{ij}$, $i \ne j$, generate $\mathrm{SL}_n(F)$. Every $A \in \mathrm{GL}_n(F)$ is a product of transvections times $\operatorname{diag}(1, \dots, 1, \det A)$.
- **LU.** If the leading principal minors $\Delta_1, \dots, \Delta_{n-1}$ of a square matrix $A$ over a field are nonzero, then $A = LU$ with $L$ unit lower triangular and $U$ upper triangular, and $\Delta_k = u_{11} \cdots u_{kk}$. An invertible matrix has at most one such factorization. With row exchanges, $PA = LU$ always exists.
- **Schur complement.** If $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ over a field has $A$ square and invertible, then $M$ is invertible if and only if $S = D - CA^{-1}B$ is, and $\det M = \det A \det S$. The lower right block of $M^{-1}$ is $S^{-1}$.
- **Sherman-Morrison.** For invertible $A$ and column vectors $u$, $v$, the matrix $A + uv^{\mathsf{T}}$ is invertible if and only if $1 + v^{\mathsf{T}} A^{-1} u \ne 0$, and then $(A + uv^{\mathsf{T}})^{-1} = A^{-1} - \dfrac{A^{-1} u v^{\mathsf{T}} A^{-1}}{1 + v^{\mathsf{T}} A^{-1} u}$.
- **Equivalence.** Over a field, $A$ and $B$ of size $m \times n$ are equivalent, $B = PAQ$ with $P$ and $Q$ invertible, if and only if they have the same rank. A matrix of rank $r$ is equivalent to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.

| Elementary matrix | On the left of $A$ | On the right of $A$ | Inverse | Determinant |
|---|---|---|---|---|
| $P_{ij}$, exchange | exchanges rows $i$ and $j$ | exchanges columns $i$ and $j$ | $P_{ij}$ | $-1$ |
| $D_i(c)$, $c \ne 0$, scaling | multiplies row $i$ by $c$ | multiplies column $i$ by $c$ | $D_i(c^{-1})$ | $c$ |
| $T_{ij}(c)$, $i \ne j$, replacement | adds $c$ times row $j$ to row $i$ | adds $c$ times column $i$ to column $j$ | $T_{ij}(-c)$ | $1$ |

: The three types of elementary matrices. Note that the indices swap roles between row and column operations for a replacement.

## Common errors

- **Reversing the reversal.** $(AB)^{-1}$ is $B^{-1} A^{-1}$. The inverse of a sum is not the sum of the inverses: $I + I$ has inverse $\tfrac12 I$, not $2I$.
- **Stopping too early.** An echelon form is not enough to read off $A^{-1}$; the left block of $[A \mid I_n]$ must reach $I_n$. A row of zeros on the left at any stage shows that $A$ is singular.
- **Mixing up the order of elementary factors.** If $E_k \cdots E_1 A = I_n$, then $A^{-1} = E_k \cdots E_1$ and $A = E_1^{-1} \cdots E_k^{-1}$. The first operation done is the rightmost factor.
- **Assuming LU exists.** An invertible matrix need not have $A = LU$. The exchange matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has none, because $\Delta_1 = 0$. Check the leading principal minors, or allow a permutation $P$.
- **Using one-sided inverses for non-square matrices.** A $2 \times 3$ matrix can have a right inverse that is not a left inverse. The theorem that one-sided inverses are two-sided is for square matrices only.
- **Confusing equivalence and similarity.** Equivalence $B = PAQ$ keeps only the rank; similarity $B = P^{-1}AP$ keeps the trace, the determinant and much more. Matrices of the same rank can fail to be similar.
