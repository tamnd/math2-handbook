## What to remember

- An **inner product** on a vector space over $\mathbb{K} = \R$ or $\C$ is linear in the first slot, conjugate symmetric, $\ip{y}{x} = \overline{\ip{x}{y}}$, and positive definite, $\ip{x}{x} > 0$ for $x \ne 0$. It follows that $\ip{x}{ay} = \overline{a}\ip{x}{y}$. On $\C^n$ the standard inner product is $\ip{x}{y} = \sum_k x_k \overline{y_k} = y^* x$.
- The **induced norm** is $\norm{x} = \sqrt{\ip{x}{x}}$, and $\norm{x + y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2$.
- **Cauchy-Schwarz:** $\abs{\ip{x}{y}} \le \norm{x}\norm{y}$, with equality exactly when $x$ and $y$ are linearly dependent. It gives the **triangle inequality** $\norm{x + y} \le \norm{x} + \norm{y}$, with equality exactly when $y = 0$ or $x = cy$ with $c \ge 0$ real.
- **Parallelogram law and polarization:** $\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2$ for every induced norm, and the norm determines the inner product. A norm comes from an inner product exactly when it satisfies the parallelogram law (the Jordan-von Neumann theorem), so the maximum and taxicab norms on $\R^2$ do not.
- **Pythagoras:** if $x \perp y$, then $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$. The converse holds over $\R$; over $\C$ the identity says only that $\operatorname{Re}\ip{x}{y} = 0$.
- An **orthonormal family** satisfies $\ip{e_i}{e_j} = \delta_{ij}$, and it is linearly independent. In an orthonormal basis, $v = \sum_i \ip{v}{e_i} e_i$ and $\ip{x}{y} = \sum_i \ip{x}{e_i}\overline{\ip{y}{e_i}}$ (Parseval). For any finite orthonormal family, $\sum_i \abs{\ip{x}{e_i}}^2 \le \norm{x}^2$ (Bessel), with equality exactly when $x$ lies in the span.
- **Gram-Schmidt:** from independent $v_1, \dots, v_k$, put $u_j = v_j - \sum_{i < j} \frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}} u_i$ and $e_j = u_j / \norm{u_j}$. The $e_j$ are orthonormal and $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(v_1, \dots, v_j)$ for each $j$. So every finite-dimensional inner product space has an orthonormal basis, and every orthonormal family extends to one.
- The **Gram matrix** $G_{ij} = \ip{v_i}{v_j}$ is Hermitian and positive semidefinite. It is invertible exactly when the $v_i$ are independent, and then $\det G = \norm{u_1}^2 \cdots \norm{u_k}^2$, the squared volume of the parallelepiped they span.
- **Riesz:** in finite dimension each linear form is $f = \ip{\cdot}{u}$ for exactly one $u$, namely $u = \sum_i \overline{f(e_i)}\, e_i$ for an orthonormal basis. The map $u \mapsto \ip{\cdot}{u}$ is a bijection $V \to V^*$, linear over $\R$ and antilinear over $\C$.

## Real and complex side by side

| Fact | Over $\R$ | Over $\C$ (linear in the first slot) |
|---|---|---|
| Symmetry | $\ip{y}{x} = \ip{x}{y}$ | $\ip{y}{x} = \overline{\ip{x}{y}}$ |
| Scalar in the second slot | $\ip{x}{ay} = a\ip{x}{y}$ | $\ip{x}{ay} = \overline{a}\ip{x}{y}$ |
| Square of a sum | $\norm{x}^2 + 2\ip{x}{y} + \norm{y}^2$ | $\norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2$ |
| Polarization | $\frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right)$ | $\frac14 \sum_{k=0}^{3} i^k \norm{x + i^k y}^2$ |
| Pythagorean identity implies $x \perp y$ | yes | no: $x = 1$, $y = i$ in $\C$ |
| Coordinate of $v$ on $e_i$ | $\ip{v}{e_i}$ | $\ip{v}{e_i}$, not $\ip{e_i}{v}$ |
| Riesz map $u \mapsto \ip{\cdot}{u}$ | linear | antilinear |

: The facts of the chapter that change between real and complex spaces. The complex column assumes the convention of this chapter; with linearity in the second slot, the conjugates move to the other factor.

## Common errors

- **A missing conjugate.** The formula $\sum_k x_k y_k$ is not an inner product on $\C^n$, and $A^{\mathsf T} A$ is not the Gram matrix of complex columns; use $A^* A$.
- **The wrong slot.** With this chapter's convention the Gram-Schmidt coefficient is $\ip{v_j}{u_i}$ and the coordinate is $\ip{v}{e_i}$. The other order gives the conjugate, and the result is wrong whenever the value is not real.
- **Checking positivity on a basis only.** A symmetric form can be positive on $e_1$ and $e_2$ and negative on $e_1 + e_2$.
- **Orthogonal is not orthonormal.** In an orthogonal basis that is not normalized, the coordinate is $\ip{v}{u_i} / \norm{u_i}^2$.
- **Projecting onto the old vectors.** In Gram-Schmidt, subtract the components along the new vectors $u_i$, which are orthogonal, not along the $v_i$.
- **Orthogonality without an inner product.** Whether two vectors are orthogonal depends on the inner product: $(1, 1)$ and $(1, -1)$ are orthogonal for the dot product but not for $2x_1 y_1 + x_2 y_2$.
