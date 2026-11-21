## What to remember

- The **orthogonal complement** of a subspace $U$ is $U^\perp = \set{v : \langle v, u \rangle = 0 \text{ for all } u \in U}$. It is always a subspace. If $U$ is spanned by the rows of a real matrix $A$, then $U^\perp = \operatorname{Nul}(A)$.
- **Orthogonal decomposition:** for a finite-dimensional subspace $U$, $V = U \oplus U^\perp$. In finite dimension $\dim U^\perp = \dim V - \dim U$ and $(U^\perp)^\perp = U$.
- **Fundamental subspaces:** for a real $m \times n$ matrix, $\operatorname{Nul}(A) = \operatorname{Row}(A)^\perp$ in $\R^n$ and $\operatorname{Nul}(A^{\mathsf{T}}) = \operatorname{Col}(A)^\perp$ in $\R^m$. So $Ax = b$ is solvable exactly when $b \perp y$ for every $y$ with $A^{\mathsf{T}} y = 0$.
- **Orthogonal projection:** $P_U v$ is the part of $v$ in $U$. With an orthonormal basis $e_1, \dots, e_k$ of $U$, $P_U v = \sum_i \langle v, e_i \rangle e_i$, and its matrix is $Q Q^{\mathsf{T}}$. With a basis in the columns of $A$, the matrix is $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$. A matrix is an orthogonal projection exactly when $P^2 = P = P^{\mathsf{T}}$.
- **Best approximation:** $P_U v$ is the unique closest point of $U$ to $v$, and $u_0 \in U$ is the closest point exactly when $v - u_0 \in U^\perp$. The distance satisfies $d(v, U)^2 = \norm{v}^2 - \norm{P_U v}^2$.
- **Least squares:** $\hat x$ minimizes $\norm{Ax - b}$ exactly when $A \hat x$ is the projection of $b$ onto $\operatorname{Col}(A)$, exactly when $A^{\mathsf{T}} A \hat x = A^{\mathsf{T}} b$. The solution is unique exactly when the columns of $A$ are independent; otherwise the solutions form $\hat x + \operatorname{Nul}(A)$.
- **QR:** a matrix with independent columns is $A = QR$, with orthonormal columns in $Q$ and $R$ upper triangular with positive diagonal; $Q$ and $R$ are unique. The least-squares solution solves $R \hat x = Q^{\mathsf{T}} b$, and the method avoids $A^{\mathsf{T}} A$, whose condition number is $\kappa(A)^2$.
- **Minimum norm:** if $Ax = b$ is solvable, it has exactly one solution $x_0$ in the row space, and it is the shortest solution. For full row rank, $x_0 = A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1} b$.
- **Principal angles** between subspaces of dimensions $p \le q$ are $0 \le \theta_1 \le \dots \le \theta_p \le \pi/2$, with $\cos \theta_k$ the $k$-th singular value of $Q_1^{\mathsf{T}} Q_2$. The number of zero angles is $\dim (U \cap W)$.

## Three ways to solve least squares

| Method | What it computes | Needs | Accuracy |
|---|---|---|---|
| [Normal equations](/4D7MRG4D91/) | $A^{\mathsf{T}} A \hat x = A^{\mathsf{T}} b$ | independent columns for a unique answer | depends on $\kappa(A)^2$ |
| [QR decomposition](/0ERWG4NXQ9/) | $R \hat x = Q^{\mathsf{T}} b$ | independent columns | depends on $\kappa(A)$ |
| [Least squares by the SVD](/SBP2PCHH9M/) | $\hat x = A^+ b$, the shortest least-squares solution | nothing; works for any rank | the most reliable, and the most work |

: Three routes to the same least-squares solution. They agree in exact arithmetic; they differ in what they need and how errors in the data grow.

## Common errors

- **Using the orthonormal-basis formula with a basis that is not orthonormal.** The sum $\sum_i \langle v, u_i \rangle u_i$ is the projection only for an orthonormal basis. For an orthogonal basis divide each term by $\langle u_i, u_i \rangle$; for an arbitrary basis use $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$.
- **Cancelling $A^{\mathsf{T}}$ in the normal equations.** $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ does not give $Ax = b$: $A^{\mathsf{T}}$ has a null space, and the residual $b - A \hat x$ lies in it.
- **Confusing $A^{\mathsf{T}} A$ with $A A^{\mathsf{T}}$.** Independent columns make the $n \times n$ matrix $A^{\mathsf{T}} A$ invertible; independent rows make the $m \times m$ matrix $A A^{\mathsf{T}}$ invertible. A tall matrix never has $A A^{\mathsf{T}}$ invertible.
- **Expecting $(U^\perp)^\perp = U$ everywhere.** In infinite dimension the double complement is the closure of $U$; the polynomials in $C[-1, 1]$ have complement $0$.
- **Reading the angle between two chosen vectors as a principal angle.** Principal angles come from maximizing pairs or from singular values, not from the first vectors of two bases.
