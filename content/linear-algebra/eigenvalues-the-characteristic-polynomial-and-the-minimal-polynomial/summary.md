## What to remember

- **[Eigenvalues](/0BQAA2BK3Q/) and [eigenspaces](/0G0RFPG8HR/).** For a linear map $T \colon V \to V$ over a field $F$, $\lambda \in F$ is an eigenvalue when $Tv = \lambda v$ for some $v \ne 0$. The eigenspace $E_\lambda = \ker(T - \lambda I)$ is a subspace, and its nonzero vectors are the [eigenvectors](/0N6960W0BV/) for $\lambda$. Eigenvalues depend on the field: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has none in $\R$ and two in $\C$.
- **[Characteristic polynomial](/0VSSPAFM2C/).** For an $n \times n$ matrix over a commutative ring, $p_A(t) = \det(tI_n - A)$ is monic of degree $n$, and similar matrices have the same one. Over a field, $\lambda$ is an eigenvalue of $A$ if and only if $p_A(\lambda) = 0$ ([roots](/053QVHF6N7/)), so $A$ has at most $n$ eigenvalues.
- **[Coefficients](/0FRYPZ6D0X/).** $p_A(t) = \sum_{k=0}^n (-1)^k E_k(A) t^{n-k}$, with $E_k(A)$ the sum of the principal minors of size $k$. For $n = 2$, $p_A(t) = t^2 - (\operatorname{tr} A) t + \det A$. If $p_A$ splits over $F$ with roots $\lambda_1, \dots, \lambda_n$ listed with multiplicity, then $\operatorname{tr} A^k = \sum_i \lambda_i^k$ for $k \ge 1$ and $\det A = \prod_i \lambda_i$ ([trace](/0NMXDCNNKR/), [determinant](/0C2F40MEBC/)).
- **[Independence](/0HNMFG8F8K/) and multiplicities.** Eigenvectors for distinct eigenvalues are linearly independent. For an eigenvalue $\lambda$ of an $n \times n$ matrix over a field, the [geometric multiplicity](/099TWVJ909/) $n - \operatorname{rank}(A - \lambda I)$ lies between $1$ and the [algebraic multiplicity](/0FY42N02DV/), the multiplicity of $\lambda$ as a root of $p_A$.
- **[Existence](/08CJB2NQ92/).** Over an algebraically closed field, every linear map of a finite-dimensional space $V \ne 0$ has an eigenvalue. Over $\R$, such a map has an [invariant subspace of dimension $1$ or $2$](/KAV44BRV77/), and a real eigenvalue if $\dim V$ is odd.
- **[$AB$ and $BA$](/MCXV71BY74/).** For $A$ of size $m \times n$ and $B$ of size $n \times m$ over a commutative ring, $x^n p_{AB}(x) = x^m p_{BA}(x)$. Over a field they have the same nonzero eigenvalues with the same algebraic multiplicities; for $m = n$, $p_{AB} = p_{BA}$.
- **[Minimal polynomial](/03NDVCSHSB/).** For $V$ finite-dimensional over $F$, the polynomials $f$ with $f(T) = 0$ form a nonzero ideal of $F[x]$, and $m_T$ is its monic generator. It [divides every annihilating polynomial](/0VTAD25A3G/), and its [roots in $F$ are exactly the eigenvalues](/0QF4ZEFG52/) of $T$. If $Tv = \lambda v$, then $f(T) v = f(\lambda) v$.
- **[Cayley–Hamilton](/0F765KFC2J/).** Over a commutative ring, $p_A(A) = 0$. Over a field, $m_A \mid p_A \mid m_A^{\,n}$ ([divisibility](/093X6MN6Y6/)). If $A$ is invertible, with $p_A(t) = t^n + c_{n-1} t^{n-1} + \dots + c_0$, then $A^{-1} = -c_0^{-1}(A^{n-1} + c_{n-1} A^{n-2} + \dots + c_1 I)$, and $A^k = r(A)$ where $r$ is the remainder of $t^k$ on division by $p_A$ ([inverse and powers](/R4CPYXFJEQ/)).

| | Characteristic polynomial $p_A$ | Minimal polynomial $m_A$ |
|---|---|---|
| Definition | $\det(tI - A)$ | monic generator of $\set{f : f(A) = 0}$ |
| Degree | always $n$ | between $1$ and $n$ |
| Roots in $F$ | the eigenvalues, with algebraic multiplicity | the eigenvalues, each at least once |
| Of $I_n$ | $(t - 1)^n$ | $t - 1$ |
| $A$ is a root | by Cayley–Hamilton | by definition |

: The two polynomials of a square matrix over a field. They have the same roots and the same irreducible factors, but usually different multiplicities.

## Common errors

- **Row reducing first.** Row operations change the eigenvalues. The eigenvalues of $A$ are not the pivots of an echelon form of $A$.
- **Allowing $v = 0$.** Every $\lambda$ satisfies $A0 = \lambda 0$. An eigenvector must be nonzero, while the eigenvalue $0$ is allowed and means that $A$ is singular.
- **Assuming a basis of eigenvectors.** A repeated root of $p_A$ can have a one-dimensional eigenspace: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $p_A = (t - 1)^2$ and only the line through $e_1$ as eigenspace.
- **Adding or multiplying eigenvalues.** The eigenvalues of $A + B$ and of $AB$ are not in general sums or products of eigenvalues of $A$ and $B$.
- **Substituting a matrix for $t$ inside the determinant.** "$p_A(A) = \det(AI - A) = \det 0 = 0$" is not a proof: $p_A(A)$ is a matrix and $\det(AI - A)$ is a number.
- **Confusing $p_A$ and $m_A$.** $m_A$ divides $p_A$, not the converse, and $\deg m_A$ can be smaller than $n$.
- **Ignoring the sign convention.** Some books use $\det(A - tI) = (-1)^n p_A(t)$. The roots are the same, but the coefficient formulas change sign for odd $n$.
