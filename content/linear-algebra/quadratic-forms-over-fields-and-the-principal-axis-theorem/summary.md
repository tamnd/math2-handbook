## What to remember

- A **quadratic form** on $F^n$ is a homogeneous polynomial $Q(x) = \sum_{i \le j} c_{ij} x_i x_j$. Its **polar form** is $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$, with $b_Q(v, v) = 2Q(v)$. When $\operatorname{char} F \ne 2$, $Q(x) = x^T A x$ for exactly one symmetric $A$, with $a_{ii} = c_{ii}$ and $a_{ij} = a_{ji} = c_{ij}/2$.
- **Diagonalization.** Outside characteristic $2$, every symmetric $A$ has an invertible $P$ with $P^T A P$ diagonal; completing squares finds one. The diagonal entries are not unique.
- **Sylvester's law of inertia.** Over $\R$, every diagonal form of $Q$ has the same numbers $p$, $q$, $r$ of positive, negative and zero coefficients. The **signature** $(p, q, r)$ is a complete invariant, and the rank is $p + q$. By the principal axis theorem, $p$, $q$, $r$ are the numbers of positive, negative and zero eigenvalues of $A$.
- **Other fields.** Over $\C$, a form of rank $r$ is equivalent to $x_1^2 + \cdots + x_r^2$. Over a finite field with $q$ odd, a nondegenerate form is equivalent to $x_1^2 + \cdots + x_{n-1}^2 + d x_n^2$ with $d = \det A$, so there are two classes in each dimension, and every form in $n \ge 3$ variables is isotropic.
- The **discriminant** is $\det A$ modulo nonzero squares. It is an invariant over every field of characteristic not $2$, but in general not a complete one.
- **Types.** A real form is positive definite ($Q > 0$ off $0$), negative definite, positive semidefinite ($Q \ge 0$), negative semidefinite, or indefinite. In terms of the signature, positive definite means $(n, 0, 0)$ and indefinite means $p > 0$ and $q > 0$.
- **Principal axis theorem.** For real symmetric $A$ there is an orthogonal $P$, with $\det P = 1$, such that $x = Py$ gives $Q = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$, where the $\lambda_i$ are the eigenvalues of $A$ and the columns of $P$ are orthonormal eigenvectors.
- **Extremes.** On unit vectors, $x^T A x$ takes the largest value $\lambda_{\max}$ and the smallest value $\lambda_{\min}$, exactly at the unit eigenvectors for these eigenvalues.

## Classification by field

| Field | Allowed changes | Complete invariants | Classes of nondegenerate forms in dimension $n$ |
|---|---|---|---|
| $\C$ | invertible linear | rank | $1$ |
| $\R$ | invertible linear | signature $(p, q, r)$ | $n + 1$ |
| $\R$ | rotations | eigenvalues of $A$ | infinitely many |
| $\mathbb F_q$, $q$ odd | invertible linear | rank, discriminant | $2$ |
| $\Q$ | invertible linear | discriminant is not enough | infinitely many |

: How far a quadratic form can be simplified. The row for $\Q$ only records that the discriminant takes infinitely many values and does not classify; for example $x^2 + y^2$ and $3x^2 + 3y^2$ have the same discriminant but are not equivalent.

## Common errors

- **Doubling the cross terms wrongly.** The symmetric matrix of $x^2 + 6xy + y^2$ has off-diagonal entries $3$, not $6$.
- **Reading the signature off the diagonal.** The diagonal entries of $A$ do not give $p$ and $q$: $x^2 + 4xy + y^2$ has positive diagonal but is indefinite. Diagonalize first, or use the eigenvalues.
- **Confusing equivalence with orthogonal equivalence.** An invertible change of variables keeps only the signs of the coefficients; a rotation keeps the coefficients themselves. The axes and the lengths of the semi-axes of a conic need the second.
- **Forgetting the linear terms.** For a conic $x^T A x + b^T x + c = 0$ with $A$ invertible, first move the centre $x_0 = -\frac12 A^{-1} b$ to the origin, then rotate. The constant changes to $c + \frac12 b^T x_0$.
- **Using $\frac12$ in characteristic $2$.** Over $\mathbb F_2$ the form $xy$ has no symmetric matrix $A$ with $Q(x) = x^T A x$; the correspondence with symmetric bilinear forms needs $2 \ne 0$.
- **Applying definiteness to complex forms.** Over $\C$, $Q(iv) = -Q(v)$, so a nonzero complex quadratic form takes no fixed sign; definiteness is a notion for real forms (or for Hermitian forms).
