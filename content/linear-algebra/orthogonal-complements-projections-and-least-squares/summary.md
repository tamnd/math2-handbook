## What to remember

- **[Orthogonal complement](/0XJXTBCB2T/):** for any subset $S$ of an inner product space $V$, the set $S^\perp$ of vectors orthogonal to every element of $S$ is a subspace, and $S^\perp = (\operatorname{span} S)^\perp$. In $\R^n$, the complement of the span of $u_1, \dots, u_k$ is the null space of the matrix with rows $u_1^{\mathsf{T}}, \dots, u_k^{\mathsf{T}}$.
- **[Orthogonal decomposition](/0SP7P0G7KQ/):** if $U$ is a finite-dimensional subspace of $V$, every $v \in V$ is uniquely $u + w$ with $u \in U$ and $w \in U^\perp$, so $V = U \oplus U^\perp$. If $V$ has finite dimension, $\dim U + \dim U^\perp = \dim V$ and the [double complement](/0PXN9G4MX1/) is $(U^\perp)^\perp = U$. Both can fail for an infinite-dimensional $U$.
- **[Fundamental subspaces](/GQF2KG1R1N/):** for a real $m \times n$ matrix $A$, $\operatorname{Nul} A = (\operatorname{Row} A)^\perp$ in $\R^n$ and $\operatorname{Nul} A^{\mathsf{T}} = (\operatorname{Col} A)^\perp$ in $\R^m$. So $Ax = b$ is solvable exactly when $b$ is orthogonal to every solution of $A^{\mathsf{T}}y = 0$. Over $\C$, use $A^*$.
- **[Orthogonal projection](/0B8KZRT28M/):** for $U$ finite-dimensional with orthonormal basis $e_1, \dots, e_k$, $P_U v = \sum_i \ip{v}{e_i} e_i$. If the columns of a real $A$ form a basis of $U$, the matrix is $A(A^{\mathsf{T}}A)^{-1}A^{\mathsf{T}}$, and $QQ^{\mathsf{T}}$ if they are orthonormal. An operator on a finite-dimensional space is an orthogonal projection exactly when $P^2 = P$ and $P^* = P$.
- **[Best approximation](/0MCDDSCB9Z/):** for $U$ finite-dimensional, $P_U v$ is the unique closest point of $U$ to $v$, and with an orthonormal basis of $U$ the distance is given by $d(v, U)^2 = \norm{v}^2 - \sum_i \abs{\ip{v}{e_i}}^2$.
- **[Least squares](/0BYTQ4X1HC/) and the [normal equations](/4D7MRG4D91/):** for a real $m \times n$ matrix $A$ and $b \in \R^m$, $\hat x$ minimizes $\norm{Ax - b}$ exactly when $A^{\mathsf{T}}A\hat x = A^{\mathsf{T}}b$. These equations are always consistent, since $\operatorname{Nul}(A^{\mathsf{T}}A) = \operatorname{Nul} A$, and the solution is unique exactly when the columns of $A$ are independent. The residual $b - A\hat x$ is orthogonal to $\operatorname{Col} A$.
- **[QR decomposition](/0ERWG4NXQ9/):** a real $m \times n$ matrix with independent columns is $QR$ with $Q^{\mathsf{T}}Q = I_n$ and $R$ upper triangular with positive diagonal, and the pair is unique. Least squares becomes $R\hat x = Q^{\mathsf{T}}b$, which avoids the squared condition number $\kappa(A^{\mathsf{T}}A) = \kappa(A)^2$.
- **[Minimum-norm solution](/QM2Y84VDX8/):** a consistent system $Ax = b$ has exactly one solution in $\operatorname{Row} A$, and it is the shortest. For independent rows it is $A^{\mathsf{T}}(AA^{\mathsf{T}})^{-1}b$.
- **[Principal angles](/YHVD3773AW/):** for subspaces with orthonormal bases in the columns of $Q_1$ and $Q_2$, $\cos\theta_k = \sigma_k(Q_1^{\mathsf{T}}Q_2)$. [Legendre and Fourier approximation](/899D63WW04/) is the projection formula with an orthogonal basis of functions.

| Method | Solves | Needs | Accuracy |
|---|---|---|---|
| [Normal equations](/4D7MRG4D91/) | $A^{\mathsf{T}}A\hat x = A^{\mathsf{T}}b$ | nothing; unique $\hat x$ if columns independent | condition number squared |
| [QR decomposition](/0ERWG4NXQ9/) | $R\hat x = Q^{\mathsf{T}}b$ | independent columns | condition number of $A$ |
| [Pseudoinverse](/0YY8VX28JR/) | $\hat x = A^+ b$ | nothing | condition number of $A$; gives the shortest $\hat x$ |

: Three ways to compute a least-squares solution of $Ax = b$.

## Common errors

- **Projecting onto a basis that is not orthogonal.** The sum $\sum_i \frac{\ip{v}{u_i}}{\ip{u_i}{u_i}} u_i$ is the projection only when the $u_i$ are pairwise orthogonal. Otherwise orthogonalize first, or solve the normal equations.
- **Cancelling inverses of rectangular matrices.** $A(A^{\mathsf{T}}A)^{-1}A^{\mathsf{T}}$ is not $I$ when $A$ is $m \times n$ with $m > n$, since $A$ has no inverse.
- **Taking an idempotent for an orthogonal projection.** $P^2 = P$ gives a projection along some complement. It is orthogonal only if, in addition, $P^* = P$, as $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ shows.
- **Forgetting finite dimension.** $V = U \oplus U^\perp$ and $(U^\perp)^\perp = U$ need $U$ finite-dimensional, or closed in a Hilbert space.
- **Discarding equations.** Solving a square subsystem of an overdetermined system does not give the least-squares solution. Every equation enters the normal equations.
- **Using the transpose over $\C$.** For complex matrices the left null space that is orthogonal to the column space is $\operatorname{Nul} A^*$, not $\operatorname{Nul} A^{\mathsf{T}}$.
