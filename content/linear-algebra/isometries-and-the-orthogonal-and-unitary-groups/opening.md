Take the matrix
$$Q = \frac{1}{3}\begin{pmatrix} 2 & 2 & 1 \\ -2 & 1 & 2 \\ 1 & -2 & 2 \end{pmatrix}.$$
Its columns $\frac{1}{3}(2, -2, 1)$, $\frac{1}{3}(2, 1, -2)$ and $\frac{1}{3}(1, 2, 2)$ have length $1$, since $4 + 4 + 1 = 9$, and they are pairwise orthogonal: $4 - 2 - 2 = 0$, $2 - 4 + 2 = 0$ and $2 + 2 - 4 = 0$. These six facts say $Q^{\mathsf{T}}Q = I$, and they are enough to make $Q$ keep every length. For example, $Q(1, 1, 1) = \frac{1}{3}(5, 1, 1)$, and both vectors have squared length $3$.

So $Q$ moves space as a rigid body about the origin. Which motion is it? Its determinant is $1$, so it keeps orientation, and the vector $(1, 0, 1)$ is fixed: $Q(1, 0, 1) = (1, 0, 1)$. The motion is therefore a turn about the line through $(1, 0, 1)$. To find the angle, take $(1, 0, -1)$, which is perpendicular to the axis. It goes to $\frac{1}{3}(1, -4, -1)$, and the cosine of the angle between the two is $\frac{2/3}{2} = \frac{1}{3}$. The trace gives the same number without any vector, since $\tr Q = \frac{5}{3} = 1 + 2\cos\theta$. So $Q$ turns space by $\arccos\frac{1}{3} \approx 70.5$ degrees about the line through $(1, 0, 1)$.

The matrix $-Q$ also keeps lengths, but its determinant is $-1$ and it fixes no nonzero vector. It turns about the same axis and then reflects in the plane perpendicular to it. So in space every length-preserving linear map is a rotation, or a rotation followed by a reflection, and three numbers from the matrix tell them apart: the determinant, the axis and the trace.

This chapter studies such maps in every dimension. The linear maps that keep the norm are exactly those that keep the inner product, and they form groups. Over $\R$ these are the orthogonal group $O(n)$ of matrices with $Q^{\mathsf{T}}Q = I$ and its subgroup $SO(n)$ of rotations; over $\C$ they are the unitary group $U(n)$ and $SU(n)$. In the plane everything is a rotation or a reflection in a line, in space Euler's theorem gives every rotation an axis, and in general an orthogonal matrix splits into turns of perpendicular planes and signs $\pm 1$. Reflections generate the whole group.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Linear isometries.** [Linear isometries](/07SJXTWVQW/), the theorem that [isometries preserve inner products](/0R7VXTYHYZ/), and [orthogonal matrices](/0W02QESPJQ/).
2. **The orthogonal groups.** The [orthogonal group](/WWK2E8BRGF/) $O(n)$ and the [special orthogonal group](/6WBVP2PB1Y/) $SO(n)$.
3. **The unitary groups.** [Unitary matrices](/0AR68JTMDT/), the [unitary group](/VW5H9XFNJB/) $U(n)$ and the [special unitary group](/ZRYYPHWESP/) $SU(n)$.
4. **Rotations and reflections in low dimension.** [Rotation matrices](/HNY4CPEEJA/), [reflections](/06BRDF3F0E/) and Householder matrices, the [classification of the orthogonal group of the plane](/C97Z06HHB2/), and the [classification of $O(3)$ with Euler's rotation theorem](/2ZVG43GSKA/).
5. **Orthogonal maps in every dimension.** The [normal form of an orthogonal matrix](/QTY3VMFGY1/), the [Cartan–Dieudonné theorem](/0VMWGYY35Q/) on products of reflections, and the [Cayley transform](/HKQ5YY027B/).

## A first reading

A short course takes these entries in order.

- [Linear isometry](/07SJXTWVQW/).
- [Isometries preserve inner products](/0R7VXTYHYZ/).
- [Orthogonal matrix](/0W02QESPJQ/).
- [Orthogonal group](/WWK2E8BRGF/) and [special orthogonal group](/6WBVP2PB1Y/).
- [Rotation matrix](/HNY4CPEEJA/).
- [Reflection](/06BRDF3F0E/).
- [Classification of the orthogonal group of the plane](/C97Z06HHB2/).
- [Classification of $O(3)$ and Euler's rotation theorem](/2ZVG43GSKA/).
- [Normal form of an orthogonal matrix](/QTY3VMFGY1/).

The unitary groups can be read next, or later if only the real case is needed. The [Cartan–Dieudonné theorem](/0VMWGYY35Q/) and the [Cayley transform](/HKQ5YY027B/) can wait for a second pass.

## Before you start

The chapter assumes the following.

- [Inner product spaces](/1D4JTZ9VS3/): orthonormal bases and the norm of an inner product.
- [Orthogonal complements, projections and least squares](/8GQVME4SZZ/): orthogonal complements and projections.
- [Adjoints, normal operators and the spectral theorems](/3YM9EK6VMB/): the adjoint and the [normal form of a real normal operator](/G6T1FNE3JC/).
- [Determinants](/DTBK11SR77/), [eigenvalues](/6R1D6QPY3S/) and [diagonalization](/Z6S6PWMJPH/).
- [Groups](/BAZT8JJ70S/) and [homomorphisms](/E1506A5A55/): subgroups, normal subgroups, index and kernels.
