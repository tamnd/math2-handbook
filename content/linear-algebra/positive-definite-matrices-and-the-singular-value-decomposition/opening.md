Take the quadratic form $q(x, y) = x^2 + 4xy + 5y^2$. Completing the square gives $q(x, y) = (x + 2y)^2 + y^2$, so $q$ is positive except at the origin, where it is zero. The same form with $3y^2$ in place of $5y^2$ is $(x + 2y)^2 - y^2$, which is negative at $(2, -1)$. The symmetric matrix of the first form is $\begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}$, and completing the square has written it as $L L^{\mathsf{T}}$ with $L = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$, where the rows of $L^{\mathsf{T}}$ hold the coefficients of $x + 2y$ and $y$. This is the [Cholesky decomposition](/0WKG8CYY6A/) found by hand, and the condition "$q > 0$ away from the origin" is what it means for a matrix to be [positive definite](/0KX66CZMBB/).

Read the same identity the other way. With $M = L^{\mathsf{T}} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ we have $M^{\mathsf{T}} M = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}$, and $\norm{M x}^2 = x^{\mathsf{T}} M^{\mathsf{T}} M x$. The eigenvalues of $M^{\mathsf{T}} M$ are $3 \pm 2\sqrt2 = (\sqrt2 \pm 1)^2$, so $M$ stretches some unit vector by $\sqrt2 + 1$ and shrinks another by $\sqrt2 - 1$, and these are the most and the least it stretches any unit vector. The numbers $\sqrt2 \pm 1$ are the [singular values](/09VMDSRXWJ/) of $M$. Their product is $1 = \abs{\det M}$, although both eigenvalues of $M$ equal $1$. Every matrix, square or not, has singular values, and the [singular value decomposition](/000NPTMX6J/) writes it as a rotation, a stretch along perpendicular axes and another rotation. Least squares, low-rank approximation of data, the condition number of a linear system and the normal modes of a vibrating system all come out of this one factorization.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Positive definite and semidefinite matrices.** The definitions of [positive definite](/0KX66CZMBB/) and [positive semidefinite](/01MMVW8CKC/) matrices, for Hermitian and for real symmetric matrices, with examples and non-examples.
2. **Three tests for definiteness.** The [eigenvalue test](/0HYC2RHD3M/), the [Gram matrix theorem](/0AM050KCAW/), which says that $B^* B$ is always semidefinite, and [Sylvester's criterion](/0WKEF78PMV/) by leading principal minors.
3. **Cholesky, square roots and the polar decomposition.** The [Cholesky decomposition](/0WKG8CYY6A/) $A = L L^*$, the unique [positive semidefinite square root](/EQ98KW1ZN4/), and the [polar decomposition](/0J2C7BDJQA/) $A = UP$ of a square matrix into a unitary factor and a stretch.
4. **Singular values and the SVD.** [Singular values](/09VMDSRXWJ/) and what they measure, the [singular value decomposition](/000NPTMX6J/) in its full and reduced forms, and its [geometry](/JAEKA59DNZ/): the unit sphere goes to an ellipsoid.
5. **Pseudoinverse, low-rank approximation and pairs of forms.** The [Moore-Penrose inverse](/0YY8VX28JR/) and minimum-norm least squares, the [Eckart-Young-Mirsky theorem](/JJT6GC055J/) on best approximation by matrices of lower rank, and the [simultaneous diagonalization](/K559AQ9H67/) of a Hermitian form and a positive definite one.

## A first reading

A short course takes these entries in order.

- [Positive definite matrix](/0KX66CZMBB/).
- [Positive semidefinite matrix](/01MMVW8CKC/).
- [The eigenvalue test](/0HYC2RHD3M/).
- [Gram matrices are positive semidefinite](/0AM050KCAW/).
- [Sylvester's criterion](/0WKEF78PMV/), part 1 only.
- [Cholesky decomposition](/0WKG8CYY6A/).
- [Singular value](/09VMDSRXWJ/).
- [Singular value decomposition](/000NPTMX6J/).
- [Moore-Penrose inverse](/0YY8VX28JR/).
- [Eckart-Young-Mirsky theorem](/JJT6GC055J/).

The square root and the polar decomposition can wait until the SVD is familiar, since the SVD gives both of them at once. Part 2 of Sylvester's criterion, on semidefinite matrices, can be left for a second reading, but its warning should not: nonnegative leading minors do not make a matrix semidefinite. The [geometry of the SVD](/JAEKA59DNZ/) is short and worth reading with the decomposition itself. [Simultaneous diagonalization](/K559AQ9H67/) is needed in mechanics and statistics and can be read last.

## Before you start

The chapter assumes the following.

- [Inner products](/0NB0AWGJBW/), [orthonormal bases](/0S9GGTR0EX/) and [orthogonal projection](/0B8KZRT28M/).
- [Least squares](/0BYTQ4X1HC/), for the pseudoinverse.
- [Hermitian matrices](/0P17NGQQMQ/), [unitary matrices](/0AR68JTMDT/) and [orthogonal matrices](/0W02QESPJQ/).
- The [spectral theorem for Hermitian matrices](/0DGZBQWZWN/) and its [real form](/06J4PXRG22/). Almost every proof in the chapter starts from it.
- [Determinants](/DTBK11SR77/) and [minors](/0BT9BYWVRY/), for Sylvester's criterion, and the [LU decomposition](/0RKG5YW66Y/), which the Cholesky decomposition refines.
