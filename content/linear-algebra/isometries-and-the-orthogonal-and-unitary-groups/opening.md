The matrix
$$Q = \frac{1}{3} \begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$$
has orthonormal columns, so it keeps lengths and angles: it moves $\R^3$ as a rigid body about the origin. Its determinant is $1$, so it keeps orientation, and by Euler's rotation theorem it is a rotation about an axis. The axis is the line of fixed vectors, here the line through $(1, 1, 1)$, and the angle comes from the trace: $\operatorname{tr} Q = 2 = 1 + 2 \cos \theta$, so $\theta = \pi/3$. The same few facts describe the attitude of a satellite, the orientation of a camera in computer graphics and the symmetries of a molecule.

The chapter studies the maps that keep the inner product, the linear isometries, and the groups they form. Over $\R$ they are the orthogonal matrices, with $Q^{\mathsf{T}} Q = I$, which form the orthogonal group $O(n)$ and the rotation group $SO(n)$. Over $\C$ they are the unitary matrices, with $U^* U = I$, which form $U(n)$ and $SU(n)$. The group $SU(2)$ is the group of unit quaternions, and it [covers the rotations of space twice](/EAK8KT5AMD/): this is how quaternions describe rotations, and how spin enters quantum mechanics. Numerical linear algebra uses orthogonal matrices because they do not magnify errors; the Householder reflections of the chapter are the basic tool of the QR decomposition.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Linear isometries.** [Linear isometries](/07SJXTWVQW/) and the fact that [isometries preserve inner products](/0R7VXTYHYZ/), with the polarization identities and the linearity of distance-preserving maps that fix $0$.
2. **Orthogonal matrices and their groups.** [Orthogonal matrices](/0W02QESPJQ/), the [orthogonal group](/WWK2E8BRGF/) $O(n)$ and the [special orthogonal group](/6WBVP2PB1Y/) $SO(n)$, with [determinant and eigenvalues](/QDZJMFATRW/) of an orthogonal matrix.
3. **Unitary matrices and their groups.** [Unitary matrices](/0AR68JTMDT/), the [unitary group](/VW5H9XFNJB/) $U(n)$ and the [special unitary group](/ZRYYPHWESP/) $SU(n)$, including [$SU(2)$ as the unit quaternions](/A763JSEVW8/).
4. **Rotations and reflections.** [Rotation matrices](/HNY4CPEEJA/), [reflections](/06BRDF3F0E/) and Householder matrices, the [classification of $O(2)$](/C97Z06HHB2/), and the [classification of $O(3)$ with Euler's rotation theorem](/2ZVG43GSKA/).
5. **The structure of orthogonal maps.** The [normal form of an orthogonal matrix](/QTY3VMFGY1/), the [Cartan-Dieudonné theorem](/0VMWGYY35Q/) on products of reflections, and the [Cayley transform](/HKQ5YY027B/).

## A first reading

Read these first, in order: [linear isometry](/07SJXTWVQW/), [isometries preserve inner products](/0R7VXTYHYZ/), [orthogonal matrix](/0W02QESPJQ/), [orthogonal group](/WWK2E8BRGF/), [special orthogonal group](/6WBVP2PB1Y/), [rotation matrix](/HNY4CPEEJA/), [reflection](/06BRDF3F0E/), [classification of $O(2)$](/C97Z06HHB2/) and [classification of $O(3)$](/2ZVG43GSKA/). This path gives the full picture of rigid motions of the plane and of space.

The unitary group can be read next, or later if only the real case matters. The normal form, the Cartan-Dieudonné theorem and the Cayley transform can wait for a second pass. The normal form follows quickly from the real normal form of the previous chapter, and the Cayley transform is mainly a tool for writing rotations with rational entries.

## Before you start

You need [inner product spaces](/1D4JTZ9VS3/) with orthonormal bases, the [orthogonal complements and projections](/8GQVME4SZZ/) of an earlier chapter, and the adjoints and [spectral theorems](/3YM9EK6VMB/) of the previous chapter, in particular the [normal form of a real normal operator](/G6T1FNE3JC/). From earlier chapters you need [determinants](/DTBK11SR77/), [eigenvalues](/6R1D6QPY3S/) and [diagonalization](/Z6S6PWMJPH/). The group language, subgroups, normal subgroups, index and kernels, is in [groups](/BAZT8JJ70S/) and [homomorphisms](/E1506A5A55/).
