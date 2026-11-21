## What to remember

- **Invertible:** an $n \times n$ matrix $A$ is invertible when $AB = BA = I_n$ for some $B$. The inverse is unique and $(AB)^{-1} = B^{-1}A^{-1}$. For square matrices over a field, one of $AB = I_n$ and $BA = I_n$ implies the other. A $2 \times 2$ matrix is invertible exactly when $ad - bc \ne 0$, with inverse $\frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
- **Elementary matrices:** each row operation is $A \mapsto EA$, where $E$ is the result of the same operation on $I$. The inverse of $E$ is the elementary matrix of the reverse operation. Multiplying on the right performs a column operation.
- **Row reduction decides and computes:** $A$ is invertible if and only if its reduced row echelon form is $I_n$, if and only if $A$ is a product of elementary matrices. Row reducing $[A \mid I_n]$ gives $[I_n \mid A^{-1}]$ when $A$ is invertible, and a zero row on the left when it is not.
- **The invertible matrix theorem:** for square $A$ over a field, these are equivalent: $A$ is invertible; $A$ has $n$ pivots; $Ax = 0$ has only the trivial solution; $Ax = b$ is solvable for every $b$; the columns are independent; the columns span $F^n$; $\operatorname{rank} A = n$; $\det A \ne 0$.
- **Triangular matrices** are invertible exactly when every diagonal entry is nonzero, and the inverse is triangular of the same kind, with diagonal entries $1/t_{ii}$.
- **The groups:** $\mathrm{SL}_n(F)$, the kernel of $\det$ on $\mathrm{GL}_n(F)$, is a normal subgroup. The transvections $T_{ij}(c) = I + cE_{ij}$ ($i \ne j$) generate $\mathrm{SL}_n(F)$, and every invertible $A$ is a product of transvections times $\operatorname{diag}(1, \dots, 1, \det A)$.
- **LU:** elimination without row exchanges gives $A = LU$, with $L$ unit lower triangular (it stores the multipliers) and $U$ upper triangular. An invertible $A$ has one if and only if all leading principal minors $\Delta_k$ are nonzero; it is then unique, with pivots $u_{kk} = \Delta_k / \Delta_{k-1}$.
- **Schur complement and updates:** if the block $A$ of $M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is invertible, then $\det M = \det A \cdot \det(M/A)$ with $M/A = D - CA^{-1}B$, and $M$ is invertible exactly when $M/A$ is. By Sherman-Morrison, $A + uv^{\mathsf{T}}$ is invertible exactly when $1 + v^{\mathsf{T}}A^{-1}u \ne 0$.
- **Equivalence:** $B = PAQ$ with $P$, $Q$ invertible. Every $m \times n$ matrix of rank $r$ is equivalent to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$, so matrices of the same size are equivalent exactly when their ranks agree.

## Factorizations

| Factorization | Exists | Unique |
|---|---|---|
| Product of elementary matrices | exactly when $A$ is invertible | no |
| [Transvections](/YSS4XNY9RC/) times $\operatorname{diag}(1, \dots, 1, \det A)$ | for every invertible $A$ | no |
| [$A = LU$](/0RKG5YW66Y/) | for invertible $A$, exactly when all $\Delta_k \ne 0$ | yes, for invertible $A$ |
| $PA = LU$, with row exchanges | for every square $A$ | no |
| [$A = LDV$](/R424G32KFA/) | when $A$ is invertible and has an $LU$ | yes; $V = L^{\mathsf{T}}$ if $A$ is symmetric |
| [Block LDU](/5QTK7JWXF3/) with middle factor $\operatorname{diag}(A, M/A)$ | when the block $A$ is invertible | yes |
| [Rank normal form](/T2H2QV0M06/) $PAQ = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$ | for every $m \times n$ matrix | $r$ is; $P$, $Q$ are not |

: The factorizations of the chapter. $L$ is unit lower triangular, $U$ upper triangular, $D$ diagonal, $V$ unit upper triangular, $P$ a permutation matrix in $PA = LU$, and $\Delta_k$ the $k$-th leading principal minor.

## Common errors

- **Reversing the order in $(AB)^{-1}$.** The inverse of a product is $B^{-1}A^{-1}$: the map applied last is undone first.
- **Using one-sided inverses for non-square matrices.** The $2 \times 3$ matrix $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ has right inverses but no left inverse.
- **Mixing up rows and columns.** $T_{ij}(c)A$ adds $c$ times row $j$ to row $i$; $AT_{ij}(c)$ adds $c$ times column $i$ to column $j$.
- **Computing $A^{-1}$ to solve $Ax = b$.** Elimination, or $LU$ and two triangular solves, is cheaper and more accurate in floating point. Form the inverse only when you need its entries.
- **Expecting $LU$ for every invertible matrix.** The exchange matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has $\Delta_1 = 0$ and no $LU$ decomposition. Allow a permutation.
- **Using the diagonal test on a matrix that is not triangular.** $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has nonzero diagonal and is singular.
