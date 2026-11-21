## What to remember

- The **adjoint** of $T \colon V \to W$ is the unique linear map $T^* \colon W \to V$ with $\langle Tv, w \rangle = \langle v, T^* w \rangle$. In orthonormal bases $[T^*] = [T]^*$, the conjugate transpose. In an arbitrary basis $B$ of $V$, $[T^*]_B = H^{-1} [T]_B^* H$ with $H_{ij} = \langle b_j, b_i \rangle$.
- $\ker T^* = (\operatorname{im} T)^\perp$ and $\operatorname{im} T^* = (\ker T)^\perp$, so $\operatorname{rank} T^* = \operatorname{rank} T$.
- A **self-adjoint** operator, $T^* = T$, has only real eigenvalues, and it has an eigenvector even over $\R$: the maximum of $\langle Tv, v \rangle$ on the unit sphere is an eigenvalue. Over $\C$, $T$ is self-adjoint exactly when $\langle Tv, v \rangle$ is real for all $v$.
- For a **normal** operator, $T T^* = T^* T$, eigenvectors for distinct eigenvalues are orthogonal, and $\norm{Tv} = \norm{T^* v}$ for all $v$.
- **Schur:** every complex square matrix is $A = Q U Q^*$ with $Q$ unitary and $U$ upper triangular, with the eigenvalues on the diagonal. A real matrix has a real form with $1 \times 1$ and $2 \times 2$ diagonal blocks and an orthogonal $Q$.
- **Spectral theorems:** over $\C$, $T$ has an orthonormal eigenbasis exactly when $T$ is normal, so $A = U D U^*$. Over $\R$, exactly when $T$ is self-adjoint, so a real matrix is $Q D Q^{\mathsf{T}}$ with $Q$ orthogonal exactly when it is symmetric.
- **Spectral decomposition:** $T = \sum_j \lambda_j P_j$, with $P_j$ the orthogonal projections onto the eigenspaces, $P_i P_j = 0$ for $i \ne j$ and $\sum_j P_j = I$. Then $p(T) = \sum_j p(\lambda_j) P_j$ for every polynomial $p$, and $T^* = \sum_j \overline{\lambda_j} P_j$.
- A **real normal** matrix is orthogonally similar to a block diagonal matrix with blocks $(c)$ and $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$, $b > 0$, one for each pair $a \pm ib$ of non-real eigenvalues.
- **Rayleigh quotient:** for self-adjoint $T$, $R(v) = \langle Tv, v \rangle / \langle v, v \rangle$ has maximum $\lambda_{\max}$ and minimum $\lambda_{\min}$, and an error of size $\varepsilon$ in an eigenvector gives an error of size $\varepsilon^2$ in $R$.

## Which operators diagonalize in an orthonormal basis

| Operator | Condition | Eigenvalues | Orthonormal eigenbasis over $\C$ | over $\R$ |
|---|---|---|---|---|
| [Self-adjoint](/0NEGN5CRSC/) | $T^* = T$ | real | yes | yes |
| Skew-adjoint | $T^* = -T$ | purely imaginary or $0$ | yes | only if $T = 0$ |
| [Unitary or orthogonal](/0AR68JTMDT/) | $T^* T = I$ | $\abs{\lambda} = 1$ | yes | only if $T^2 = I$ |
| [Normal](/0C8BR8XRTR/) | $T T^* = T^* T$ | any | yes | only if self-adjoint |
| General | none | any | not in general; [Schur](/V1JG4C7R7B/) gives a triangular form | not in general |

: Each class in the first four rows is normal. Over $\R$ the eigenbasis exists only when all eigenvalues are real, which for a normal operator means self-adjoint; otherwise the real normal form uses $2 \times 2$ blocks.

## Common errors

- **Taking the transpose in a basis that is not orthonormal.** $[T^*]_B = [T]_B^*$ needs an orthonormal basis $B$. With a weighted inner product or a skew basis, use $H^{-1} [T]_B^* H$.
- **Concluding orthogonality from distinct eigenvalues alone.** $\begin{pmatrix} 2 & 3 \\ 0 & -1 \end{pmatrix}$ has distinct eigenvalues and eigenvectors $(1, 0)$ and $(1, -1)$, which are not orthogonal. Orthogonality needs normality.
- **Reading a complex symmetric matrix as Hermitian.** $A^{\mathsf{T}} = A$ over $\C$ says nothing about real eigenvalues; Hermitian means $A^* = A$.
- **Choosing any eigenbasis for simultaneous diagonalization.** When an operator has a repeated eigenvalue, not every orthonormal eigenbasis of it diagonalizes a commuting partner; diagonalize inside each eigenspace.
- **Using the Rayleigh bounds for a non-symmetric matrix.** For $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ the quotient takes the values $3$ and $-1$, outside the only eigenvalue $1$.
