Draw the curve $5x^2 - 4xy + 8y^2 = 36$ in the plane. The cross term $-4xy$ hides its shape. Completing the square gives

$$5x^2 - 4xy + 8y^2 = 5\Bigl(x - \frac{2}{5}y\Bigr)^2 + \frac{36}{5} y^2,$$

so the left side is positive at every point except the origin, and the curve is bounded. But the new variables $x - \tfrac25 y$ and $y$ are not perpendicular coordinates, so this does not tell you the lengths or the directions of the axes. For that, write the form as $x^{\mathsf T} A x$ with the symmetric matrix

$$A = \begin{pmatrix} 5 & -2 \\ -2 & 8 \end{pmatrix}.$$

Its eigenvalues are $4$ and $9$, with eigenvectors $(2, 1)$ and $(1, -2)$, which are perpendicular. In coordinates $u, v$ along the unit vectors $(2, 1)/\sqrt5$ and $(1, -2)/\sqrt5$ the equation becomes $4u^2 + 9v^2 = 36$. The curve is an ellipse with semi-axis $3$ in the direction $(2, 1)$ and semi-axis $2$ in the direction $(1, -2)$. The same eigenvalues say that on the unit circle the form takes values between $4$ and $9$.

Two different reductions appeared here, and they answer different questions. Completing squares uses an invertible change of variables that need not keep lengths. It works over any field in which $2$ is invertible and shows which forms are the same up to a change of basis. Over $\R$ the coefficients it produces are not unique, but their signs are: every diagonal form of $5x^2 - 4xy + 8y^2$ has two positive coefficients. Over $\C$ even the signs disappear, since $-1$ is a square. Over a finite field what survives is the determinant up to a square factor. The eigenvalue reduction uses only rotations. It needs real symmetric matrices, and it keeps lengths, so it gives the axes of conics and quadric surfaces and the extreme values of a form on the unit sphere.

The chapter first sets up quadratic forms and their symmetric bilinear forms over a general field. It then diagonalizes them and asks what is invariant over $\R$, over $\C$, over finite fields and over $\Q$. It ends with the real theory: definiteness, the principal axis theorem and its geometry.

## What the chapter covers

1. **Quadratic forms and their polar forms.** A [quadratic form](/0RBQS1JJCR/) is a map that scales by $a^2$ and has a bilinear [polar form](/0HYFWKKY3C/). Outside characteristic $2$ it is the same thing as a symmetric bilinear form, or, on $F^n$, a symmetric matrix up to congruence.
2. **Diagonalization and the law of inertia.** Every form over a field of characteristic not $2$ has a [diagonal form](/0Z3FEWZ8HA/). Over $\R$, [Sylvester's law of inertia](/0WFED3K3DQ/) shows that the numbers of positive, negative and zero coefficients do not depend on the choice. Together they make the [signature](/07EZA80NEH/), which classifies real forms.
3. **Forms over other fields.** Over $\C$ [the rank alone classifies](/0CEX9BRXRZ/). Over a [finite field of odd characteristic](/2HBR7137AD/) the rank and the [discriminant](/MZFRXECCMC/) classify. Over $\Q$ the discriminant is only one invariant among several.
4. **Definite and indefinite forms.** [Positive definite forms](/0RP20HFYM3/) and the [five types](/01RBSSGMY5/) of real forms, with tests by eigenvalues, minors and completing squares.
5. **The principal axis theorem and its geometry.** The [principal axis theorem](/0PR5P9Z4KM/) diagonalizes a real form by a rotation. The group applies it to [conics](/1DGT7X9E35/), [quadric surfaces](/F42W4DQHBK/) and [extreme values on unit vectors](/YS4HT1EYE5/).

## A first reading

For the real theory, which most courses need, read in this order:

1. [Quadratic form](/0RBQS1JJCR/)
2. [Polar form of a quadratic form](/0HYFWKKY3C/)
3. [Diagonalization of a quadratic form](/0Z3FEWZ8HA/)
4. [Sylvester's law of inertia](/0WFED3K3DQ/)
5. [Signature of a quadratic form](/07EZA80NEH/)
6. [Positive definite quadratic form](/0RP20HFYM3/)
7. [Principal axis theorem](/0PR5P9Z4KM/)
8. [Three conics put in normal form](/1DGT7X9E35/)
9. [Extreme values of a quadratic form on unit vectors](/YS4HT1EYE5/)

On a first pass you can skip the examples in characteristic $2$ attached to the first entry and the whole third group. Come back to them when you need forms over $\C$, over finite fields or over $\Q$.

## Before you start

You need [bilinear forms](/0SQZMXB6GP/) and their matrices, [symmetric bilinear forms](/0AXZNE5XNH/), the [change of basis rule](/0SPYAGE7T0/) $A \mapsto P^{\mathsf T} A P$ and [matrix congruence](/WJWNYSQKK8/), all from the chapter on bilinear and sesquilinear forms. The words [nondegenerate](/01NHFZF2SK/) and [isotropic](/MZHFGPV1YT/) come from the same chapter. For the last two groups you need the [real spectral theorem](/06J4PXRG22/): a real symmetric matrix has an orthonormal basis of eigenvectors. The tests for [positive definite matrices](/0KX66CZMBB/) in the chapter on positive definite matrices are the matrix side of the fourth group.
