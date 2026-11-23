Compare two real matrices with the same eigenvalues $3$ and $-2$:
$$A = \begin{pmatrix} 2 & 2 \\ 2 & -1 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 & 5 \\ 0 & -2 \end{pmatrix}.$$
For $A$, the eigenvectors are $(2, 1)$ for $3$, since $A(2, 1) = (6, 3)$, and $(1, -2)$ for $-2$, since $A(1, -2) = (-2, 4)$. Their dot product is $2 - 2 = 0$. For $B$, the eigenvectors are $(1, 0)$ and $(1, -1)$, at an angle of $45$ degrees. After scaling, the eigenvectors of $A$ form an orthonormal basis, so the change of basis is a rotation and $A = QDQ^{\mathsf{T}}$ with $Q^{-1} = Q^{\mathsf{T}}$. For $B$ the change of basis distorts lengths and angles.

The difference shows up at once in geometry. The quadratic form of $A$ is $2x^2 + 4xy - y^2$. In the coordinates $u$ and $v$ along the unit vectors $\frac{1}{\sqrt{5}}(2, 1)$ and $\frac{1}{\sqrt{5}}(1, -2)$ it becomes $3u^2 - 2v^2$, so the curve $2x^2 + 4xy - y^2 = 6$ is a hyperbola with axes along these perpendicular lines. Nothing like this is possible for $B$, whose eigenvector directions are not perpendicular. And the reason $A$ behaves well is visible: $A$ is symmetric, $A^{\mathsf{T}} = A$, and $B$ is not.

The chapter explains this and pushes it as far as it goes. The transpose is replaced by the adjoint $T^*$, defined by $\ip{Tv}{w} = \ip{v}{T^*w}$, so that the theory works for operators on spaces of polynomials and functions, and in bases that are not orthonormal. Symmetric matrices become self-adjoint operators, which have real eigenvalues and an orthonormal basis of eigenvectors. The rotation by a right angle has no real eigenvalues, but over $\C$ its eigenvectors $(1, -i)$ and $(1, i)$ are orthogonal too. The class that contains both examples is that of the normal operators, with $TT^* = T^*T$. Over $\C$ they are exactly the operators that are diagonal in some orthonormal basis, and this is the spectral theorem.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The adjoint.** The [adjoint of a linear map](/0R9NMSM1ZP/), its [matrix](/0DBTE6HVBD/), which is the conjugate transpose in orthonormal bases, and the [kernel and image of the adjoint](/YPP8XT6B7Y/).
2. **Self-adjoint operators.** [Self-adjoint operators](/0NEGN5CRSC/), the proof that their [eigenvalues are real](/0C4NT4GT3X/), and the [orthogonality of eigenspaces](/0JHGAV9H25/) of a normal operator.
3. **Triangular form and normality.** The [Schur decomposition](/V1JG4C7R7B/), which makes every complex operator triangular in an orthonormal basis, and [normal operators](/0C8BR8XRTR/).
4. **The spectral theorems.** The [complex spectral theorem](/04CW1P44VD/) for normal operators, the [spectral theorem for Hermitian matrices](/0DGZBQWZWN/) and the [real spectral theorem](/06J4PXRG22/) for symmetric matrices.
5. **Consequences.** The [spectral decomposition](/D5KVBA1K9R/) into orthogonal projections, the [normal form of a real normal operator](/G6T1FNE3JC/), [simultaneous diagonalization](/BFQQDA489F/) of commuting families, and the [Rayleigh quotient](/06WHP8SE98/).

## A first reading

A short course takes these entries in order.

- [Adjoint of a linear map](/0R9NMSM1ZP/), with the adjoint of differentiation.
- [Matrix of the adjoint](/0DBTE6HVBD/).
- [Self-adjoint operator](/0NEGN5CRSC/), with the orthogonal diagonalization of a symmetric $2 \times 2$ matrix.
- [Eigenvalues of a self-adjoint operator are real](/0C4NT4GT3X/).
- [Normal operator](/0C8BR8XRTR/).
- [Complex spectral theorem](/04CW1P44VD/).
- [Real spectral theorem](/06J4PXRG22/).
- [Spectral decomposition of a normal operator](/D5KVBA1K9R/).
- [Rayleigh quotient](/06WHP8SE98/).

The [Schur decomposition](/V1JG4C7R7B/) is the tool behind the complex spectral theorem and is worth reading with it. The [real normal form](/G6T1FNE3JC/) is needed for the orthogonal matrices of the next chapter, and [simultaneous diagonalization](/BFQQDA489F/) can wait until commuting families come up.

## Before you start

The chapter assumes the following.

- [Inner product spaces](/1D4JTZ9VS3/): inner products over $\R$ and $\C$, norms and orthonormal bases.
- [Orthogonal complements, projections and least squares](/8GQVME4SZZ/): orthogonal complements and orthogonal projections.
- [Diagonalization, triangularization and invariant subspaces](/Z6S6PWMJPH/): invariant subspaces and diagonalizable operators.
- [Eigenvalues, the characteristic polynomial and the minimal polynomial](/6R1D6QPY3S/): eigenvalues, eigenvectors and the fact that a complex operator has an eigenvalue.
