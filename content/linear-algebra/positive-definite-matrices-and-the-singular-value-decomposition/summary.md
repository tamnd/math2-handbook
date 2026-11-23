## What to remember

- **Definitions.** A Hermitian $n \times n$ matrix $A$ is positive definite if $x^* A x > 0$ for every $x \ne 0$, and positive semidefinite if $x^* A x \ge 0$ for every $x$. A matrix that is not Hermitian is neither, whatever its quadratic form does. For real matrices, read "real symmetric" and $x^{\mathsf{T}} A x$.
- **Eigenvalue test.** A Hermitian $A$ is positive definite if and only if all its eigenvalues are positive, and semidefinite if and only if they are all nonnegative.
- **Gram matrices.** For every $m \times n$ matrix $B$, $B^* B$ is positive semidefinite, because $x^* B^* B x = \norm{Bx}^2$. It is definite exactly when the columns of $B$ are independent. Every positive semidefinite matrix is of the form $B^* B$.
- **Sylvester's criterion.** A Hermitian $A$ is positive definite if and only if its leading principal minors $\Delta_1, \dots, \Delta_n$ are all positive. It is semidefinite if and only if all $2^n - 1$ principal minors $\det A_S$ are nonnegative.
- **Cholesky and the square root.** A positive definite $A$ has exactly one factorization $A = L L^*$ with $L$ lower triangular and with real positive diagonal entries. A positive semidefinite $A$ has exactly one positive semidefinite square root, $A^{1/2} = U \operatorname{diag}(\sqrt{\lambda_i}) U^*$ when $A = U \operatorname{diag}(\lambda_i) U^*$.
- **Polar decomposition.** Every square $A$ is $UP$ with $U$ unitary and $P = (A^* A)^{1/2}$. The factor $P$ is unique, and $U$ is unique when $A$ is invertible.
- **SVD.** Every $m \times n$ matrix of rank $r$ is $A = U \Sigma V^* = \sum_{i=1}^r \sigma_i u_i v_i^*$ with $\sigma_1 \ge \dots \ge \sigma_r > 0$. The $u_i$ with $i \le r$ span the column space, the $v_i$ with $i > r$ span the null space, $\norm{A}_2 = \sigma_1$ and $\norm{A}_F^2 = \sum \sigma_i^2$.
- **Pseudoinverse and best approximation.** $A^+ = V \Sigma^+ U^*$ is the only matrix that satisfies the four Penrose conditions, and $A^+ b$ is the least-squares solution of $Ax = b$ of least norm. The truncation $A_k = \sum_{i \le k} \sigma_i u_i v_i^*$ is a nearest matrix of rank at most $k$, at distance $\sigma_{k+1}$ in the operator norm.
- **Pairs of forms.** If $A$ is Hermitian and $B$ is positive definite, there is an invertible $P$ with $P^* B P = I$ and $P^* A P$ real diagonal, with the roots of $\det(A - \lambda B) = 0$ on the diagonal.

| Factorization | Applies to | Form | Unique? |
|---|---|---|---|
| Spectral | Hermitian $A$ | $A = U D U^*$, $U$ unitary, $D$ real diagonal | $D$ up to order |
| Cholesky | positive definite $A$ | $A = L L^*$, $L$ lower triangular, $l_{ii} > 0$ | yes |
| Square root | positive semidefinite $A$ | $A = B^2$, $B$ positive semidefinite | yes |
| Polar | square $A$ | $A = UP$, $U$ unitary, $P$ semidefinite | $P$ always; $U$ if $A$ is invertible |
| SVD | any $m \times n$ $A$ | $A = U \Sigma V^*$, $U$ and $V$ unitary | $\Sigma$ yes; $U$ and $V$ no |
| Simultaneous | $A$ Hermitian, $B$ positive definite | $P^* B P = I$, $P^* A P = D$ | $D$ up to order |

: The factorizations of the chapter, what they need and what in them is unique.

## Common errors

- **Positive entries are not positive definiteness.** The matrix with $1$ on the diagonal and $3$ off it has the eigenvalue $-2$. Conversely, a positive definite matrix may have negative entries off the diagonal.
- **Leading minors for semidefiniteness.** Nonnegative leading minors do not make a Hermitian matrix semidefinite; part 2 of Sylvester's criterion needs every principal minor.
- **Eigenvalues for singular values.** For a matrix that is not normal, the singular values are not the absolute values of the eigenvalues. Compute the eigenvalues of $A^* A$ and take square roots.
- **The non-Hermitian case.** A real matrix whose quadratic form is positive is not called positive definite unless it is symmetric, and the tests of the chapter apply only to Hermitian matrices.
- **Normalizing in the wrong inner product.** In simultaneous diagonalization the vectors must satisfy $p_i^* B p_i = 1$, not $p_i^* p_i = 1$, and $P$ is in general not unitary.
- **The pseudoinverse as an inverse.** $A A^+$ and $A^+ A$ are orthogonal projections, not identities, and in general $(AB)^+ \ne B^+ A^+$.
