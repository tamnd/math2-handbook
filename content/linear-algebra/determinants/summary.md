## What to remember

- **[Definition](/00KDZRW4C0/).** Over a commutative ring $R$, the determinant is the unique map $\det \colon M_n(R) \to R$ that is linear in each column, vanishes when two columns are equal, and takes the value $1$ at $I_n$. The [Leibniz formula](/016PE4VZ8Q/) is $\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \, a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$. For $n = 2$ it is $ad - bc$, and for $n = 3$ it is the [rule of Sarrus](/7H2P40X0MV/), which has no analogue for $n \ge 4$.
- **[Row operations](/09YB3WQG38/).** Since $\det A^{\mathsf{T}} = \det A$, every rule holds for rows and for columns. A [triangular matrix](/0K1KKMFHYH/) has determinant equal to the product of its diagonal entries. Row reduction with the factors kept computes $\det A$ in about $n^3$ operations.
- **[Products](/04CPJ6AF00/) and [invertibility](/FBSAPTP1PR/).** $\det(AB) = \det A \det B$ for $A, B \in M_n(R)$. Over a field, $A$ is invertible if and only if $\det A \ne 0$, and then $\det(A^{-1}) = (\det A)^{-1}$. [Over a commutative ring](/03Q7RE2HXR/), $A$ is invertible if and only if $\det A$ is a unit of $R$.
- **[Laplace expansion](/0C08BQ3M05/) and the [adjugate](/07W9H8QF38/).** For $n \ge 2$, with cofactors $C_{ij} = (-1)^{i+j} \det A_{ij}$, $\det A = \sum_j a_{ij} C_{ij}$ for each row $i$, and the same along each column. The adjugate is the transpose of the cofactor matrix, and $A \operatorname{adj} A = \operatorname{adj} A \, A = (\det A) I_n$ over any commutative ring. If $\det A$ is a unit, then $A^{-1} = (\det A)^{-1} \operatorname{adj} A$.
- **[Cramer's rule](/0977KZ6PQB/).** If $A$ is an $n \times n$ matrix over a field with $\det A \ne 0$, the unique solution of $Ax = b$ is $x_i = \det A_i / \det A$, where $A_i$ is $A$ with column $i$ replaced by $b$.
- **Blocks.** If $A$ and $D$ are square, $\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \det D$ ([block triangular rule](/0J9TVTNB4K/)). If moreover $A$ is invertible, $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \det(D - C A^{-1} B)$ ([Schur complement](/0KA7A4ENVJ/)). For $A$ of size $m \times n$ and $B$ of size $n \times m$, $\det(I_m + AB) = \det(I_n + BA)$, and the [Cauchy–Binet formula](/08WE2W7DYS/) gives $\det(AB)$ as a sum over the $m$-element subsets of $\set{1, \dots, n}$, which is $0$ when $m > n$.
- **Special values.** The [Vandermonde determinant](/0P84B554AS/) with rows $(1, x_i, \dots, x_i^{n-1})$ is $\prod_{i<j} (x_j - x_i)$. For invertible $A$ and column vectors $u, v$, $\det(A + u v^{\mathsf{T}}) = (1 + v^{\mathsf{T}} A^{-1} u) \det A$. Over a field, the [rank](/HVHQ50TJB1/) of a matrix is the largest size of a nonzero minor.
- **Geometry.** For an endomorphism $T$ of a finite-dimensional space, $\det T$ is the determinant of its matrix in any one basis used for both the domain and the codomain ([determinant of a linear map](/0X0HQYSZ0K/)). For a real $n \times n$ matrix $A$ and a measurable $S \subseteq \R^n$, the [volume](/RC5BTSG8T2/) of $A(S)$ is $\abs{\det A}$ times that of $S$, and the sign of $\det A$ says whether $A$ keeps the [orientation](/0QJJAQ6ZYZ/).

| Row operation | Effect on $\det$ |
|---|---|
| Swap two rows | multiplied by $-1$ |
| Multiply one row by $c$ | multiplied by $c$ |
| Add $c$ times one row to another row | unchanged |

: Row operations and the determinant. The same holds for columns.

## Common errors

- **Treating $\det$ as linear.** It is linear in each row separately, not in the whole matrix: $\det(A + B) \ne \det A + \det B$ in general, and $\det(cA) = c^n \det A$ for an $n \times n$ matrix, not $c \det A$.
- **Losing a factor in row reduction.** Dividing a row by $c$ divides the determinant by $c$, and a swap changes the sign; only adding a multiple of another row is free.
- **Forgetting the ring.** A nonzero determinant gives an inverse over a field, not over $\Z$: $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has determinant $2$ and no integer inverse.
- **Transposing the wrong way.** The adjugate is the *transpose* of the cofactor matrix. Its $(i, j)$ entry is $C_{ji}$.
- **A block formula that is too good.** $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is not $\det A \det D - \det B \det C$ and in general not $\det(AD - BC)$; only the triangular case and the Schur complement are safe.
- **Two bases for one map.** The determinant of an endomorphism uses the same basis on both sides. The matrix of the identity from one basis to another can have any nonzero determinant.
