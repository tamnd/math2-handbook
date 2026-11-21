A symmetric matrix such as $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ has real eigenvalues, here $6$ and $1$, and eigenvectors $(2, 1)$ and $(1, -2)$ that are orthogonal. So in the rotated coordinates along these two directions, $A$ simply stretches by $6$ and by $1$. The quadratic form $5x^2 + 4xy + 2y^2$ becomes $6u^2 + v^2$, and the level curve $5x^2 + 4xy + 2y^2 = 1$ is an ellipse with semi-axes $1/\sqrt 6$ and $1$ along the eigenvectors. This is the spectral theorem in its oldest form, the principal axis theorem, and it holds for every real symmetric matrix of any size.

The theorem is about the interplay of an operator with an inner product, and the adjoint is the tool that expresses it. The adjoint $T^*$ is defined by $\langle Tv, w \rangle = \langle v, T^* w \rangle$; in an orthonormal basis its matrix is the conjugate transpose. Then the question "which operators have an orthonormal basis of eigenvectors?" has a short answer. Over $\C$ they are the normal operators, with $T T^* = T^* T$. Over $\R$ they are the self-adjoint operators, with $T^* = T$. The rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ shows the difference: it is normal, it has the orthonormal eigenvectors $\frac{1}{\sqrt 2}(1, -i)$ and $\frac{1}{\sqrt 2}(1, i)$ over $\C$, and it has no real eigenvector at all. The same results run through quantum mechanics, where observables are self-adjoint operators and their eigenvalues are the values a measurement can give, and through statistics, where a covariance matrix is diagonalized to find principal components.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The adjoint.** The [adjoint](/0R9NMSM1ZP/) of a linear map, the [matrix of the adjoint](/0DBTE6HVBD/) in orthonormal bases and in arbitrary ones, and the [kernel and image of the adjoint](/YPP8XT6B7Y/).
2. **Self-adjoint operators.** [Self-adjoint and skew-adjoint operators](/0NEGN5CRSC/), the theorem that [their eigenvalues are real](/0C4NT4GT3X/) and that an eigenvector exists, and the [orthogonality of eigenspaces](/0JHGAV9H25/) for distinct eigenvalues.
3. **Schur's theorem and normal operators.** The [Schur decomposition](/V1JG4C7R7B/) of a complex operator, and its real form, and the class of [normal operators](/0C8BR8XRTR/).
4. **The spectral theorems.** The [complex spectral theorem](/04CW1P44VD/), the [spectral theorem for Hermitian matrices](/0DGZBQWZWN/) and the [real spectral theorem](/06J4PXRG22/), with two proofs of the last.
5. **Consequences.** The [spectral decomposition](/D5KVBA1K9R/) into orthogonal projections, the [normal form of a real normal operator](/G6T1FNE3JC/), [simultaneous diagonalization](/BFQQDA489F/) of commuting families, and the [Rayleigh quotient](/06WHP8SE98/).

## A first reading

Read these first, in order: [adjoint](/0R9NMSM1ZP/), [matrix of the adjoint](/0DBTE6HVBD/), [self-adjoint operator](/0NEGN5CRSC/), [eigenvalues of a self-adjoint operator are real](/0C4NT4GT3X/), [orthogonality of eigenspaces](/0JHGAV9H25/), [real spectral theorem](/06J4PXRG22/), [spectral theorem for Hermitian matrices](/0DGZBQWZWN/) and [spectral decomposition](/D5KVBA1K9R/). This path proves the principal axis theorem and its complex version with the fewest detours.

The [Schur decomposition](/V1JG4C7R7B/), [normal operators](/0C8BR8XRTR/) and the [complex spectral theorem](/04CW1P44VD/) come next. The real normal form, simultaneous diagonalization and the Rayleigh quotient can wait for a second pass; the Rayleigh quotient matters most for numerical work and leads to the [Courant-Fischer theorem](/CJK2HS2508/).

## Before you start

You need [inner product spaces](/1D4JTZ9VS3/) with [orthonormal bases](/0FWJ0VW561/) and the [Gram-Schmidt process](/0VT6P0GNQR/), and the [orthogonal complements and projections](/8GQVME4SZZ/) of the previous chapter. From [eigenvalues and eigenvectors](/6R1D6QPY3S/) you need the characteristic polynomial and eigenspaces, and from [diagonalization](/Z6S6PWMJPH/) the idea of a basis of eigenvectors. Over $\C$ the existence of an eigenvalue rests on the fundamental theorem of algebra. For a functional on a finite-dimensional space, the [Riesz representation theorem](/04GYPXDXNH/) is what makes the adjoint exist.
