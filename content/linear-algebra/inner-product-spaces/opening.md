A vector space by itself has no lengths and no angles. It says which vectors are sums and multiples of others, but not which pairs are perpendicular or how far apart two vectors are. An inner product adds exactly this. It is one map $V \times V \to \R$ or $\C$ with three axioms, and from it come lengths, distances, right angles, projections and the formulas of plane geometry, in any dimension and for any kind of vector.

Two examples show the reach of the idea. On the polynomials of degree at most $3$, the formula $\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx$ is an inner product, and the [Gram-Schmidt process](/0VT6P0GNQR/) applied to $1, x, x^2, x^3$ gives the [Legendre polynomials](/JPDVZM20EX/), which are at right angles to each other. On $\C^n$ the formula $\sum_k x_k \overline{y_k}$ is an inner product, and the conjugate is what makes it work: without it the vector $(1, i)$ would have squared length $1 + i^2 = 0$. Fourier coefficients, least squares and the spectral theorem all rest on these two ideas: orthogonality and the coordinates it gives.

The chapter treats real and complex spaces side by side. It uses the convention of most mathematics books: a complex inner product is linear in the first slot and conjugate-linear in the second. Physics books and Mathlib use the other slot, and formulas copied from them must be adjusted.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Inner products.** The axioms of an [inner product](/0NB0AWGJBW/), the dot product and the [standard inner product on $\C^n$](/TFZ8DYVJ1J/), and the [inner product space](/0QVNCJXRY3/) as a vector space with one chosen inner product.
2. **Length and the two inequalities.** The [induced norm](/0MFJJV97RJ/), the [Cauchy-Schwarz inequality](/0RFWW56Y22/) $\abs{\ip{x}{y}} \le \norm{x}\norm{y}$, and the [triangle inequality](/SRN4T2G6AM/), which makes the length a norm.
3. **The norm and the inner product determine each other.** The [parallelogram law](/026HPGYGS4/) holds for every induced norm, and the [polarization identity](/05FKHRT0B4/) recovers the inner product from the norm.
4. **Right angles.** [Orthogonal vectors](/0Y2X7P2WB7/) and the [Pythagorean theorem](/0BVTDM872V/), whose converse fails over $\C$.
5. **Orthonormal families and coordinates.** [Orthonormal families](/0RW9TNNT87/) and [bases](/0S9GGTR0EX/), the [coordinate formula](/09DZ8CD1AK/) $v = \sum_i \ip{v}{e_i} e_i$, [Bessel's inequality](/0RBT5PB74K/) and [Parseval's identity](/047RFCNVSK/).
6. **Making a basis orthonormal.** The Gram-Schmidt process and the [existence of orthonormal bases](/0Y85GYEGSF/).
7. **The Gram matrix and linear forms.** The [Gram matrix](/00SPJSDT3Z/) of a family, its rank and its determinant, and the [Riesz representation theorem](/04GYPXDXNH/).

## A first reading

For a first reading, take these ten entries in order: [inner product](/0NB0AWGJBW/), [norm induced by an inner product](/0MFJJV97RJ/), [Cauchy-Schwarz inequality](/0RFWW56Y22/), [triangle inequality](/SRN4T2G6AM/), [orthogonal vectors](/0Y2X7P2WB7/), [Pythagorean theorem](/0BVTDM872V/), [orthonormal basis](/0S9GGTR0EX/), [coordinates in an orthonormal basis](/09DZ8CD1AK/), [Gram-Schmidt process](/0VT6P0GNQR/) and [existence of an orthonormal basis](/0Y85GYEGSF/). Work the attached examples on $\C^2$ with care: most errors in this chapter are a missing conjugate or the wrong slot.

The polarization identity, Bessel's inequality, the Gram matrix and the Riesz theorem can wait for a second pass. They are short, and each becomes important later: polarization for isometries, Bessel and Parseval for Fourier series, the Gram matrix for least squares, and the Riesz theorem for the [adjoint](/0R9NMSM1ZP/) of the next chapters.

## Before you start

You need the [dot product](/0S52TNNTH9/), [length](/0XKBKGTCPC/) and [angle](/0ZEHZY85E6/) in $\R^2$ and $\R^3$ from the [first chapter](/VKVAJ94SKZ/) of this volume, and bases and dimension from the chapter on [vector spaces, span, independence, bases and dimension](/MVH97H8B2J/). The Riesz theorem uses [linear forms](/07YQ1C78G0/) and the [dual space](/07JBSZE0V4/). You also need complex numbers with their conjugates and moduli, and, for the Gram determinant, [determinants](/DTBK11SR77/). Orthogonal complements, projections and least squares come in the [next chapter](/8GQVME4SZZ/), and they use everything here.
