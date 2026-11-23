## What to remember

Throughout, $\mathbb{K}$ is $\R$ or $\C$, $V$ is a vector space over $\mathbb{K}$, and every inner product is linear in the first slot and conjugate-linear in the second.

- **Three axioms.** An [inner product](/0NB0AWGJBW/) satisfies $\langle ax + by, z\rangle = a\langle x, z\rangle + b\langle y, z\rangle$, $\langle y, x\rangle = \overline{\langle x, y\rangle}$ and $\langle x, x\rangle > 0$ for $x \ne 0$. It is part of the data of an [inner product space](/0QVNCJXRY3/): changing it changes lengths, angles and which vectors are orthogonal.
- **Length and its inequalities.** The [induced norm](/0MFJJV97RJ/) is $\norm{x} = \sqrt{\langle x, x\rangle}$. The [Cauchy-Schwarz inequality](/0RFWW56Y22/) $\abs{\langle x, y\rangle} \le \norm{x}\norm{y}$ holds for all $x, y$, with equality if and only if $x, y$ are linearly dependent. The [triangle inequality](/SRN4T2G6AM/) $\norm{x + y} \le \norm{x} + \norm{y}$ follows, with equality if and only if $y = 0$ or $x = cy$ with real $c \ge 0$.
- **Norm and inner product determine each other.** Every induced norm satisfies the [parallelogram law](/026HPGYGS4/) $\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2$. The [polarization identity](/05FKHRT0B4/) recovers $\langle x, y\rangle$ from norms, so a linear map between inner product spaces over the same field that keeps norms keeps inner products.
- **Pythagoras.** For pairwise [orthogonal](/0Y2X7P2WB7/) vectors the squared norms add ([Pythagorean theorem](/0BVTDM872V/)). For any $x, y$, $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ if and only if $\operatorname{Re}\langle x, y\rangle = 0$; so the converse holds over $\R$ and fails over $\C$.
- **Orthonormal families.** An [orthonormal family](/0RW9TNNT87/) is linearly independent. For orthonormal $e_1, \dots, e_k$ and any $x$, [Bessel's inequality](/0RBT5PB74K/) gives $\sum_i \abs{\langle x, e_i\rangle}^2 \le \norm{x}^2$, with equality if and only if $x \in \operatorname{span}(e_1, \dots, e_k)$.
- **Coordinates are inner products.** If $e_1, \dots, e_n$ is an [orthonormal basis](/0S9GGTR0EX/) of a finite-dimensional $V$, then $v = \sum_i \langle v, e_i\rangle e_i$ ([coordinates](/09DZ8CD1AK/)) and $\langle x, y\rangle = \sum_i \langle x, e_i\rangle\overline{\langle y, e_i\rangle}$ ([Parseval](/047RFCNVSK/)). The coordinate map is an isometry onto $\mathbb{K}^n$ with the standard inner product.
- **Gram-Schmidt.** From linearly independent $v_1, \dots, v_k$ the [Gram-Schmidt process](/0VT6P0GNQR/) makes an orthonormal family with the same first $j$ spans for every $j$. Hence every space of finite dimension $n$ has an orthonormal basis, and every orthonormal family has at most $n$ vectors and [extends to one](/0Y85GYEGSF/).
- **Gram matrix.** The [Gram matrix](/00SPJSDT3Z/) $G_{ij} = \langle v_i, v_j\rangle$ is Hermitian and positive semidefinite. It is invertible if and only if $v_1, \dots, v_k$ are independent, and then $\det G > 0$ is the squared volume of the box they span.
- **Riesz.** On a finite-dimensional inner product space each linear form is $f = \langle \cdot, u\rangle$ for exactly one $u$, which is $u = \sum_i \overline{f(e_i)}\, e_i$ for any orthonormal basis ([Riesz representation](/04GYPXDXNH/)). The map $u \mapsto \langle \cdot, u\rangle$ is a bijection $V \to V^*$ that is conjugate-linear over $\C$.

## Real and complex side by side

| Fact | Over $\R$ | Over $\C$ |
|---|---|---|
| Second slot | linear | conjugate-linear: $\langle x, cy\rangle = \bar c\langle x, y\rangle$ |
| Polarization | $\frac14(\norm{x + y}^2 - \norm{x - y}^2)$ | four terms $\frac14\sum_{k=0}^{3} i^k\norm{x + i^k y}^2$ |
| $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ | exactly when $x \perp y$ | exactly when $\operatorname{Re}\langle x, y\rangle = 0$ |
| Riesz map $u \mapsto \langle \cdot, u\rangle$ | linear isomorphism | conjugate-linear bijection |
| Gram matrix | symmetric | Hermitian |

: Where the real and the complex case differ. Every other statement of the chapter reads the same over both fields.

## Common errors

- **Dropping the conjugate.** On $\C^n$ the product $\sum_i z_i w_i$ is not an inner product: it gives $\langle (1, i), (1, i)\rangle = 0$. The standard inner product is $\sum_i z_i\overline{w_i}$.
- **Pulling a scalar out of the second slot unchanged.** Over $\C$, $\langle x, cy\rangle = \bar c\langle x, y\rangle$, not $c\langle x, y\rangle$.
- **Using the dot product after changing the inner product.** Orthogonality, lengths and the output of Gram-Schmidt depend on the inner product.
- **Coordinates from an orthogonal basis that is not normalized.** If the $u_i$ are orthogonal but not unit vectors, the coefficient of $u_i$ is $\langle v, u_i\rangle / \norm{u_i}^2$, not $\langle v, u_i\rangle$.
- **Reading Bessel as an equality.** For an orthonormal family that does not span $V$, the sum of the squared coefficients can be strictly smaller than $\norm{x}^2$; the gap is the squared distance from $x$ to the span.
- **Gram-Schmidt on a dependent list.** If $v_j$ lies in the span of the earlier vectors, then $u_j = 0$ and it cannot be normalized.
