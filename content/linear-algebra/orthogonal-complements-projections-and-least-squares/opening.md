Four measured points $(0, 1)$, $(1, 2)$, $(2, 2)$, $(3, 4)$ do not lie on one line, so the system that asks for a line $y = c + st$ through all of them has no solution. There is still a best line: the one that makes the sum of squared vertical errors as small as possible. It is $y = 0.9 + 0.9t$, and it comes from geometry, not calculus. The vector of observed values $y \in \R^4$ lies outside the plane of vectors $(c, c + s, c + 2s, c + 3s)$, and the best line corresponds to the point of that plane closest to $y$. That point is the foot of the perpendicular from $y$, and the error vector is orthogonal to the plane.

This picture, a vector split into a part in a subspace and a part orthogonal to it, is the whole chapter. It gives the formula $P = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$ for the matrix of a projection, the normal equations of statistics and data fitting, and the QR decomposition that numerical software uses to solve them. It explains why the null space of a matrix is orthogonal to its row space, and why the shortest solution of an underdetermined system lies in the row space. In a space of functions with $\langle f, g \rangle = \int_{-1}^{1} f g \, dx$, the same projection gives the polynomial of degree at most $2$ closest to $\abs{x}$ in mean square, namely $\frac{3}{16} + \frac{15}{16} x^2$.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Orthogonal complements.** The [orthogonal complement](/0XJXTBCB2T/) of a subspace, the [orthogonal decomposition](/0SP7P0G7KQ/) $V = U \oplus U^\perp$, the [double complement](/0PXN9G4MX1/) $(U^\perp)^\perp = U$, and the [orthogonality of the fundamental subspaces](/GQF2KG1R1N/) of a matrix, which turns the solvability of $Ax = b$ into a test of orthogonality.
2. **Projection and best approximation.** The [orthogonal projection](/0B8KZRT28M/) onto a subspace, with its formulas in an orthonormal basis and in an arbitrary one, and the [best approximation theorem](/0MCDDSCB9Z/): $P_U v$ is the unique closest point of $U$ to $v$.
3. **Least squares.** The [least-squares problem](/0BYTQ4X1HC/), the [normal equations](/4D7MRG4D91/) and the reason they square the condition number, the [QR decomposition](/0ERWG4NXQ9/) as Gram-Schmidt in matrix form, and the [minimum-norm solution](/QM2Y84VDX8/) of an underdetermined system.
4. **Angles and spaces of functions.** [Principal angles](/YHVD3773AW/) between two subspaces, and the [best mean-square approximation](/899D63WW04/) of functions by Legendre polynomials and by trigonometric polynomials.

## A first reading

Read these entries first, in order: [orthogonal complement](/0XJXTBCB2T/), [orthogonal decomposition](/0SP7P0G7KQ/), [orthogonality of the fundamental subspaces](/GQF2KG1R1N/), [orthogonal projection](/0B8KZRT28M/), [best approximation theorem](/0MCDDSCB9Z/), [least squares](/0BYTQ4X1HC/), [normal equations](/4D7MRG4D91/) and [QR decomposition](/0ERWG4NXQ9/). Work the attached examples of least squares by hand; they show the residual orthogonal to the columns in numbers.

The [double complement](/0PXN9G4MX1/) is short and can be taken on trust at first. The [minimum-norm solution](/QM2Y84VDX8/), [principal angles](/YHVD3773AW/) and the function-space example can wait for a second pass. Principal angles use [singular values](/09VMDSRXWJ/), which the chapter on the [singular value decomposition](/000NPTMX6J/) treats in full.

## Before you start

You need [inner product spaces](/1D4JTZ9VS3/): inner products, norms, [orthonormal bases](/0S9GGTR0EX/) and the [Gram-Schmidt process](/0VT6P0GNQR/). From [matrices of linear maps, rank and change of basis](/S6559D61BP/) you need the [column space](/0F0RPPJ2TT/), the [null space](/0PQ2GGY1QV/), [rank](/0EWQEYRVA8/) and the rank-nullity theorem. The decomposition $V = U \oplus U^\perp$ is a special case of the [direct sums](/QHKTJ89V6S/) of an earlier chapter. The pictures in $\R^2$ and $\R^3$ rest on the [dot product and angles](/VKVAJ94SKZ/).
