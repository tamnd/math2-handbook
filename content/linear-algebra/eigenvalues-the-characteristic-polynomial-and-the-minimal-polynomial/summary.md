## What to remember

- A scalar $\lambda \in F$ is an [eigenvalue](/0BQAA2BK3Q/) of an endomorphism $T$ of $V$ when $Tv = \lambda v$ for some $v \ne 0$, that is, when $T - \lambda I$ has a nonzero kernel. The [eigenspace](/0G0RFPG8HR/) is $E_\lambda = \ker(T - \lambda I)$, and its nonzero vectors are the [eigenvectors](/0N6960W0BV/) for $\lambda$.
- The [characteristic polynomial](/0VSSPAFM2C/) $p_A(t) = \det(tI - A)$ is monic of degree $n$, and similar matrices have the same one. The [eigenvalues in $F$ are exactly its roots in $F$](/053QVHF6N7/), so there are at most $n$ of them, and the [spectrum](/0XPX5NC67E/) depends on the field.
- The [coefficients](/0FRYPZ6D0X/) are $p_A(t) = \sum_{k=0}^{n} (-1)^k E_k(A)\, t^{n-k}$, where $E_k(A)$ is the sum of the $k \times k$ principal minors. When $p_A$ splits, $\operatorname{tr} A$ is the [sum](/0NMXDCNNKR/) and $\det A$ the [product](/0C2F40MEBC/) of the eigenvalues, counted with algebraic multiplicity.
- [Eigenvectors for distinct eigenvalues are linearly independent](/0HNMFG8F8K/), so the sum of the eigenspaces is direct. For each eigenvalue, $1 \le g(\lambda) \le a(\lambda)$, where $g$ is the [geometric](/099TWVJ909/) and $a$ the [algebraic multiplicity](/0FY42N02DV/).
- Over an algebraically closed field, every endomorphism of a nonzero finite-dimensional space [has an eigenvalue](/08CJB2NQ92/). A real operator always has an [invariant subspace of dimension 1 or 2](/KAV44BRV77/), and a real eigenvalue when the dimension is odd.
- For an $m \times n$ matrix $A$ and an $n \times m$ matrix $B$, [$x^n p_{AB}(x) = x^m p_{BA}(x)$](/MCXV71BY74/). So $AB$ and $BA$ have the same nonzero eigenvalues with the same multiplicities, and $p_{AB} = p_{BA}$ when $m = n$.
- The polynomials $f$ with $f(T) = 0$ form a nonzero ideal of $F[x]$ when $\dim V$ is finite. Its monic generator is the [minimal polynomial](/03NDVCSHSB/) $m_T$, which [divides every annihilating polynomial](/0VTAD25A3G/) and whose [roots are the eigenvalues](/0QF4ZEFG52/).
- [Cayley-Hamilton](/0F765KFC2J/): $p_A(A) = 0$ for every square matrix over a commutative ring. Hence [$m_A \mid p_A \mid m_A^n$](/093X6MN6Y6/), and when $\det A \ne 0$ the [inverse](/R4CPYXFJEQ/) $A^{-1}$ is a polynomial in $A$ of degree at most $n - 1$.

## Two polynomials of a matrix

| | Characteristic polynomial $p_A$ | Minimal polynomial $m_A$ |
|---|---|---|
| Definition | $\det(tI - A)$ | monic generator of $\set{f : f(A) = 0}$ |
| Degree | exactly $n$ | between $1$ and $n$ (for $n \ge 1$) |
| Roots in $F$ | the eigenvalues | the same eigenvalues |
| Multiplicity of a root $\lambda$ | $a(\lambda)$ | between $1$ and $a(\lambda)$ |
| Relation | $p_A$ divides $m_A^n$ | $m_A$ divides $p_A$ |
| For $\operatorname{diag}(2, 2, 5)$ | $(t - 2)^2 (t - 5)$ | $(t - 2)(t - 5)$ |
| How to find it | one determinant | test the divisors of $p_A$ that contain every eigenvalue |

: The characteristic and the minimal polynomial compared. Both are unchanged when $A$ is replaced by a similar matrix.

## Common errors

- Row reduction changes the eigenvalues. Eigenvalues are computed from $\det(tI - A)$ or from a triangular matrix similar to $A$, not from an echelon form of $A$.
- The diagonal entries are the eigenvalues only for a triangular matrix.
- An eigenvector is nonzero by definition, but the eigenvalue $0$ is allowed: it occurs exactly when $A$ is singular.
- The other convention $\det(A - tI)$ equals $(-1)^n p_A(t)$. It has the same roots, but it is not monic for odd $n$.
- The spectrum depends on the field. A real matrix may have no real eigenvalues, and its characteristic polynomial factors only over $\C$.
- The eigenvalues of $A + B$ are not in general sums of eigenvalues of $A$ and $B$. Both $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ have only the eigenvalue $0$, and their sum has the eigenvalues $1$ and $-1$.
- The substitution $p_A(A) = \det(A I - A) = \det 0 = 0$ is not a proof of Cayley-Hamilton: $p_A(A)$ is a matrix, and the scalar $t$ cannot be replaced by a matrix inside the determinant.
