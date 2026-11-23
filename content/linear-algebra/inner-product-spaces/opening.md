On $\R^2$, define a product of two vectors by

$$\langle x, y\rangle = x_1y_1 - x_1y_2 - x_2y_1 + 2x_2y_2.$$

It is linear in each slot and symmetric. It is also positive, because completing the square gives $\langle x, x\rangle = (x_1 - x_2)^2 + x_2^2$, which is $0$ only when $x_2 = 0$ and then $x_1 = 0$. So it is an [inner product](/0NB0AWGJBW/), and it gives $\R^2$ a geometry that is not the usual one.

Measure the standard basis vectors $e_1 = (1, 0)$ and $e_2 = (0, 1)$ with it. The products are $\langle e_1, e_1\rangle = 1$, $\langle e_2, e_2\rangle = 2$ and $\langle e_1, e_2\rangle = -1$. So $e_1$ has length $1$, $e_2$ has length $\sqrt 2$, and the angle $\theta$ between them has $\cos\theta = -1/(1 \cdot \sqrt 2)$, so $\theta = 135^\circ$. In this geometry the coordinate axes are not perpendicular.

Perpendicular axes can be made by hand. Keep $e_1$, and remove from $e_2$ its component along $e_1$:

$$f_2 = e_2 - \frac{\langle e_2, e_1\rangle}{\langle e_1, e_1\rangle}\, e_1 = (0, 1) + (1, 0) = (1, 1).$$

Then $\langle f_2, e_1\rangle = 1 - 1 = 0$ and $\langle f_2, f_2\rangle = 1 - 1 - 1 + 2 = 1$. So $(e_1, f_2)$ is an orthonormal basis for this inner product, although $f_2$ does not look perpendicular to $e_1$ on paper.

Now coordinates cost nothing. For $v = (3, 2)$ the two inner products are $\langle v, e_1\rangle = 3 - 2 = 1$ and $\langle v, f_2\rangle = 3 - 3 - 2 + 4 = 2$, and indeed $e_1 + 2f_2 = (3, 2)$. No linear system was solved. The squared length is the sum of the squared coordinates, $1 + 4 = 5$, and the formula $(x_1 - x_2)^2 + x_2^2$ gives the same $1 + 4$. Even a linear form becomes a vector: the form $f(x) = x_1$ takes the values $f(e_1) = 1$ and $f(f_2) = 1$, so $f(x) = \langle x, u\rangle$ with $u = e_1 + f_2 = (2, 1)$. A check: $\langle x, (2, 1)\rangle = 2x_1 - x_1 - 2x_2 + 2x_2 = x_1$.

This page took an inner product, found lengths and an angle, built an orthonormal basis by Gram-Schmidt, read off coordinates and a squared length, and represented a linear form. The chapter proves that each of these steps works in every finite-dimensional inner product space, over $\R$ and over $\C$.

The chapter is in seven groups, read in order.

## What the chapter covers

1. **Inner products and the spaces that carry them.** The three axioms of an [inner product](/0NB0AWGJBW/), the conjugate that the complex case needs, and the [inner product space](/0QVNCJXRY3/) as a space with one chosen inner product.
2. **Length and the two inequalities.** The [induced norm](/0MFJJV97RJ/), the [Cauchy-Schwarz inequality](/0RFWW56Y22/) and the [triangle inequality](/SRN4T2G6AM/), which make the length a norm and the space a metric space.
3. **The norm and the inner product determine each other.** The [parallelogram law](/026HPGYGS4/) holds for every induced norm, and the [polarization identity](/05FKHRT0B4/) recovers the inner product from lengths.
4. **Right angles.** [Orthogonal vectors](/0Y2X7P2WB7/) and the [Pythagorean theorem](/0BVTDM872V/), whose converse fails over $\C$.
5. **Orthonormal families and coordinates.** [Orthonormal families](/0RW9TNNT87/) and [orthonormal bases](/0S9GGTR0EX/), [coordinates as inner products](/09DZ8CD1AK/), [Bessel's inequality](/0RBT5PB74K/) and [Parseval's identity](/047RFCNVSK/).
6. **Building orthonormal bases.** The [Gram-Schmidt process](/0VT6P0GNQR/) and the [existence of an orthonormal basis](/0Y85GYEGSF/), with any orthonormal family as its first vectors.
7. **The Gram matrix and linear forms.** The [Gram matrix](/00SPJSDT3Z/) of a family, and the [Riesz representation theorem](/04GYPXDXNH/) in finite dimensions.

## A first reading

A short path through the chapter:

1. [Inner product](/0NB0AWGJBW/), for the axioms and the role of the conjugate.
2. [Norm induced by an inner product](/0MFJJV97RJ/).
3. [Cauchy-Schwarz inequality](/0RFWW56Y22/), with one of its two proofs.
4. [Orthogonal vectors](/0Y2X7P2WB7/).
5. [Orthonormal basis](/0S9GGTR0EX/).
6. [Coordinates in an orthonormal basis](/09DZ8CD1AK/).
7. [Gram-Schmidt process](/0VT6P0GNQR/).
8. [Existence of an orthonormal basis](/0Y85GYEGSF/).
9. [Riesz representation theorem in finite dimensions](/04GYPXDXNH/).

On a first pass you can skip the parallelogram law and polarization, Bessel's inequality and the Gram matrix. They return when the norm of a space is in question, in [orthogonal projection](/0B8KZRT28M/) and in least squares.

## Before you start

You need the [dot product and the geometry of vectors in the plane and in space](/VKVAJ94SKZ/), and [bases and dimension](/MVH97H8B2J/), in particular the extension of an independent list to a basis. The last entry uses [dual spaces](/9K7FFF26QR/). You should also be at ease with complex numbers, their conjugates and moduli, and with $2 \times 2$ and $3 \times 3$ determinants.
