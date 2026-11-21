## What to remember

- A Hermitian matrix $A$ is **positive definite** when $x^* A x > 0$ for all $x \ne 0$, and **positive semidefinite** when $x^* A x \ge 0$ for all $x$. The definitions in this book require $A$ to be Hermitian (real symmetric in the real case).
- **Tests.** For Hermitian $A$: $A$ is positive definite $\iff$ all eigenvalues are positive $\iff$ $A = B^* B$ with $B$ invertible $\iff$ all leading principal minors $\Delta_1, \dots, \Delta_n$ are positive. $A$ is positive semidefinite $\iff$ all eigenvalues are $\ge 0$ $\iff$ $A = B^* B$ for some $B$ $\iff$ all principal minors $\det A_S$ are $\ge 0$.
- **Cholesky.** A positive definite $A$ has exactly one factorization $A = L L^*$ with $L$ lower triangular and positive real diagonal entries.
- **Square root and polar form.** A positive semidefinite $A$ has exactly one positive semidefinite $B$ with $B^2 = A$. Every square matrix is $A = UP$ with $U$ unitary and $P = (A^* A)^{1/2}$; $U$ is unique when $A$ is invertible.
- **Singular values** of an $m \times n$ matrix $A$ are $\sigma_i = \sqrt{\lambda_i(A^* A)}$, in decreasing order. The number of nonzero ones is the rank, $\norm{A}_2 = \sigma_1$, and $\norm{A}_F^2 = \sum \sigma_i^2$.
- **SVD.** $A = U \Sigma V^* = \sum_{i=1}^r \sigma_i u_i v_i^*$ with $U$, $V$ unitary. The first $r$ columns of $U$ and $V$ are orthonormal bases of the column spaces of $A$ and $A^*$; the remaining columns span the null spaces of $A^*$ and $A$.
- **Pseudoinverse.** $A^+ = \sum_{i=1}^r \sigma_i^{-1} v_i u_i^*$ is the unique matrix that satisfies the four Penrose conditions, and $A^+ b$ is the least-squares solution of $Ax = b$ of smallest norm. With independent columns, $A^+ = (A^* A)^{-1} A^*$.
- **Eckart-Young-Mirsky.** The truncated SVD $A_k = \sum_{i \le k} \sigma_i u_i v_i^*$ is a best approximation of rank at most $k$, with $\norm{A - A_k}_2 = \sigma_{k+1}$ and $\norm{A - A_k}_F^2 = \sigma_{k+1}^2 + \cdots + \sigma_r^2$.
- **Pairs.** For $A$ Hermitian and $B$ positive definite there is an invertible $P$ with $P^* B P = I$ and $P^* A P$ real diagonal; the diagonal entries are the roots of $\det(A - \lambda B) = 0$.

## Decompositions compared

| Decomposition | Applies to | Factors | Unique |
|---|---|---|---|
| [Spectral](/0DGZBQWZWN/) $A = U D U^*$ | Hermitian $A$ | $U$ unitary, $D$ real diagonal | $D$ up to order |
| [Cholesky](/0WKG8CYY6A/) $A = L L^*$ | positive definite $A$ | $L$ lower triangular, diagonal $> 0$ | yes |
| [Square root](/EQ98KW1ZN4/) $A = B^2$ | positive semidefinite $A$ | $B$ positive semidefinite | yes |
| [Polar](/0J2C7BDJQA/) $A = UP$ | square $A$ | $U$ unitary, $P$ positive semidefinite | $P$ always; $U$ if $A$ is invertible |
| [SVD](/000NPTMX6J/) $A = U \Sigma V^*$ | any $m \times n$ matrix $A$ | $U$, $V$ unitary, $\Sigma$ diagonal with entries $\ge 0$ | $\Sigma$ always; $U$, $V$ not |

: Five factorizations of the chapter and its prerequisites. The last four use only positive semidefinite matrices and unitary factors, the matrix versions of $r \ge 0$ and $e^{i\theta}$.

## Common errors

- **Positive entries are not positive definiteness.** The matrix $\begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}$ has $x^T A x = -4$ at $x = (1, -1)$. Conversely, a positive definite matrix can have negative entries off the diagonal.
- **Leading minors for semidefiniteness.** Nonnegative leading minors do not give a positive semidefinite matrix: $\operatorname{diag}(0, -1)$ has leading minors $0$ and $0$. Check all principal minors, or the eigenvalues.
- **Dropping symmetry.** Sylvester's criterion and the eigenvalue test are for Hermitian matrices. The matrix $\begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}$ has positive leading minors and the eigenvalue $1$ only, yet $x^T A x = -3$ at $x = (1, -1)$.
- **Eigenvalues are not singular values.** For a non-normal matrix such as a shear, the numbers $\abs{\lambda_i}$ and $\sigma_i$ differ. They agree for normal matrices.
- **Mismatched vectors in the SVD.** Choosing $U$ and $V$ separately as eigenvectors of $A A^*$ and $A^* A$ can give wrong signs. Choose $v_i$ first, then put $u_i = A v_i / \sigma_i$.
- **Inverting $A^* A$ when it is singular.** The formula $(A^* A)^{-1} A^*$ needs independent columns. In general, use the SVD to find $A^+$.
