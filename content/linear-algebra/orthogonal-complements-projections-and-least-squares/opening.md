Ask for two numbers $x$ and $y$ with $x = 1$, $y = 1$ and $x + y = 3$. The first two equations force $x + y = 2$, so the system has no solution. In matrix form it is $Ax = b$ with columns $a_1 = (1, 0, 1)$ and $a_2 = (0, 1, 1)$ and right side $b = (1, 1, 3)$, and $b$ is not in the plane spanned by the columns. The best we can do is to choose $x$ and $y$ so that the error vector $r = b - Ax$ is as short as possible. Try $x = y = \frac{4}{3}$: then $Ax = (\frac{4}{3}, \frac{4}{3}, \frac{8}{3})$ and
$$r = \left(-\tfrac{1}{3}, -\tfrac{1}{3}, \tfrac{1}{3}\right), \qquad r \cdot a_1 = -\tfrac{1}{3} + \tfrac{1}{3} = 0, \qquad r \cdot a_2 = -\tfrac{1}{3} + \tfrac{1}{3} = 0.$$
The error is orthogonal to both columns, so it is orthogonal to the whole plane. Every other point $Az$ of the plane differs from $Ax$ by a vector $w$ of the plane, and Pythagoras gives $\norm{b - Az}^2 = \norm{r}^2 + \norm{w}^2$, which is larger unless $w = 0$. So $x = y = \frac{4}{3}$ is the best choice, with squared error $\norm{r}^2 = \frac{1}{3}$.

Three questions come out of this small computation, and they are the chapter. First, the set of vectors orthogonal to a plane must be described, and for the plane of columns it is the null space of $A^{\mathsf{T}}$. Second, the point $Ax$ is the foot of the perpendicular from $b$, the orthogonal projection of $b$, and one needs a formula for it and a proof that it is the closest point. Third, the numbers $\frac{4}{3}$ have to be found, not guessed. The two conditions $r \cdot a_1 = 0$ and $r \cdot a_2 = 0$ say $A^{\mathsf{T}}(b - Ax) = 0$, that is,
$$\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \end{pmatrix},$$
a square system with the solution $x = y = \frac{4}{3}$. These are the normal equations, and they solve every problem of fitting a model to data by least squares.

The same geometry answers other questions. When a system has many solutions, the shortest one is the one orthogonal to the null space. Two subspaces of the same space sit at a list of angles, read off from a small matrix of inner products. In a space of functions, the projection onto the polynomials of low degree is the best approximation in mean square, and it is computed with Legendre polynomials or Fourier coefficients.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Orthogonal complements.** The [orthogonal complement](/0XJXTBCB2T/) of a subspace, the [orthogonal decomposition](/0SP7P0G7KQ/) $V = U \oplus U^\perp$ for a finite-dimensional $U$, the [double complement](/0PXN9G4MX1/) $(U^\perp)^\perp = U$ in finite dimension, and the [orthogonality of the four fundamental subspaces](/GQF2KG1R1N/) of a matrix.
2. **Projection and best approximation.** The [orthogonal projection](/0B8KZRT28M/), its formulas and its matrix, and the [best approximation theorem](/0MCDDSCB9Z/): the projection is the unique closest point.
3. **Least squares.** The [least-squares problem](/0BYTQ4X1HC/), the [normal equations](/4D7MRG4D91/) that solve it, and the [QR decomposition](/0ERWG4NXQ9/) that solves it more accurately.
4. **Three more uses.** The [minimum-norm solution](/QM2Y84VDX8/) of an underdetermined system, the [principal angles](/YHVD3773AW/) between two subspaces, and [approximation by Legendre polynomials and by trigonometric polynomials](/899D63WW04/).

## A first reading

A short course takes these entries in order.

- [Orthogonal complement](/0XJXTBCB2T/), computed as a null space.
- [Orthogonal decomposition](/0SP7P0G7KQ/), with the dimension formula.
- [Orthogonality of the fundamental subspaces](/GQF2KG1R1N/), the picture behind every linear system.
- [Orthogonal projection](/0B8KZRT28M/), with the line and the plane examples.
- [Best approximation theorem](/0MCDDSCB9Z/).
- [Least squares](/0BYTQ4X1HC/), with the line through four points.
- [Normal equations](/4D7MRG4D91/).
- [QR decomposition](/0ERWG4NXQ9/).

The [double complement](/0PXN9G4MX1/) is short and can be read with the decomposition. The [minimum-norm solution](/QM2Y84VDX8/) completes the story of $Ax = b$ for systems with many solutions. [Principal angles](/YHVD3773AW/) use the singular value decomposition and can wait until it is familiar, and the [approximation of functions](/899D63WW04/) is the bridge to Fourier series.

## Before you start

The chapter assumes the following.

- [Inner product spaces](/1D4JTZ9VS3/): inner products, norms, orthonormal bases and the [Gram–Schmidt process](/0VT6P0GNQR/).
- [Matrices of linear maps, rank and change of basis](/S6559D61BP/): column space, null space, rank and the rank–nullity theorem.
- [Direct sums, complements and quotient spaces](/QHKTJ89V6S/): direct sums of subspaces.
- [Overview and vectors in the plane and in space](/VKVAJ94SKZ/): the dot product and angles in $\R^2$ and $\R^3$.
- For the principal angles only, the [singular value decomposition](/000NPTMX6J/), from the chapter on [positive definite matrices and the singular value decomposition](/SS4EVPKT3A/).
