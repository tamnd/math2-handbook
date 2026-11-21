The symmetric matrix $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ gives the number $x^T A x = 2x_1^2 - 2x_1x_2 + 2x_2^2 = x_1^2 + x_2^2 + (x_1 - x_2)^2$, which is positive for every nonzero $x$. Matrices with this property are the positive definite matrices. They are the inner products of $\R^n$ written in coordinates, the Hessians that certify a strict local minimum, the covariance matrices of random vectors without exact linear relations, and the stiffness matrices of stable mechanical systems. They behave like positive numbers: they have positive eigenvalues, positive square roots, and a triangular "square root" $L$ with $A = L L^T$ that turns the solution of $Ax = b$ into two triangular solves.

The second half of the chapter applies this to an arbitrary matrix $A$, square or not. The matrix $A^* A$ is always positive semidefinite, and the square roots of its eigenvalues are the singular values of $A$. They lead to the singular value decomposition $A = U \Sigma V^*$, which exists for every matrix. It gives the rank, the operator norm, orthonormal bases of the four fundamental subspaces, the pseudoinverse, and the best approximations of lower rank. A grey-scale image stored as a $1000 \times 800$ matrix can be replaced by its first $50$ singular layers at about a ninth of the storage, and the error is known exactly from the dropped singular values.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Positive definite and semidefinite matrices.** The definitions of a [positive definite matrix](/0KX66CZMBB/) and a [positive semidefinite matrix](/01MMVW8CKC/), for Hermitian and real symmetric matrices, with examples.
2. **Tests for definiteness.** The [eigenvalue test](/0HYC2RHD3M/), the fact that [Gram matrices are positive semidefinite](/0AM050KCAW/), and [Sylvester's criterion](/0WKEF78PMV/) by leading principal minors.
3. **Factorizations of positive matrices.** The [Cholesky decomposition](/0WKG8CYY6A/) $A = L L^*$, the [square root of a positive semidefinite matrix](/EQ98KW1ZN4/), and the [polar decomposition](/0J2C7BDJQA/) $A = UP$.
4. **Singular values and the SVD.** The [singular values](/09VMDSRXWJ/), the [singular value decomposition](/000NPTMX6J/) in its full and reduced forms, and its [geometry](/JAEKA59DNZ/): the unit circle goes to an ellipse.
5. **Pseudoinverse, low rank and pairs of forms.** The [Moore-Penrose inverse](/0YY8VX28JR/), the [Eckart-Young-Mirsky theorem](/JJT6GC055J/) on low-rank approximation, and the [simultaneous diagonalization](/K559AQ9H67/) of a Hermitian matrix and a positive definite matrix.

## A first reading

Read in this order: [positive definite matrix](/0KX66CZMBB/), [positive semidefinite matrix](/01MMVW8CKC/), [eigenvalue test](/0HYC2RHD3M/), [Sylvester's criterion](/0WKEF78PMV/), [Cholesky decomposition](/0WKG8CYY6A/), [singular value](/09VMDSRXWJ/), [singular value decomposition](/000NPTMX6J/), [geometry of the SVD](/JAEKA59DNZ/), [Moore-Penrose inverse](/0YY8VX28JR/) and [Eckart-Young-Mirsky theorem](/JJT6GC055J/). Work through the attached examples of the SVD by hand; a $2 \times 2$ or $3 \times 2$ case shows every step of the proof.

The square root and the polar decomposition can wait until you need them; the SVD can be proved without them. The Gram matrix theorem is short and worth a look, but its main content reappears in the SVD. The simultaneous diagonalization is a tool for mechanics and statistics and can be left for a second pass.

## Before you start

You need [inner products](/0NB0AWGJBW/) and [orthonormal bases](/0S9GGTR0EX/) from [inner product spaces](/1D4JTZ9VS3/), and [orthogonal projection](/0B8KZRT28M/) and [least squares](/0BYTQ4X1HC/) from [orthogonal complements, projections and least squares](/8GQVME4SZZ/). The central tool is the [spectral theorem for Hermitian matrices](/0DGZBQWZWN/) and its [real form](/06J4PXRG22/), from [adjoints, normal operators and the spectral theorems](/3YM9EK6VMB/). [Unitary matrices](/0AR68JTMDT/) and [orthogonal matrices](/0W02QESPJQ/) are treated in [isometries and the orthogonal and unitary groups](/AZS5BPF5H3/). Sylvester's criterion uses [minors](/0BT9BYWVRY/) from [determinants](/DTBK11SR77/), and the Cholesky decomposition is a symmetric form of the [LU decomposition](/0RKG5YW66Y/).
