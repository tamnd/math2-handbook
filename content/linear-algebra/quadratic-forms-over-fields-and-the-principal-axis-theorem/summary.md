## What to remember

- **Forms and matrices.** Let $F$ be a field of characteristic not $2$. A quadratic form $Q$ on a vector space $V$ over $F$ determines its polar form $B(u, v) = \tfrac12\bigl(Q(u + v) - Q(u) - Q(v)\bigr)$, the unique symmetric bilinear form with $B(v, v) = Q(v)$. On $F^n$, $Q(x) = x^{\mathsf T} A x$ for a unique symmetric $A$, whose off-diagonal entries are half the cross coefficients. The substitution $x = Py$ with $P$ invertible replaces $A$ by $P^{\mathsf T} A P$.
- **Diagonalization.** If $\operatorname{char} F \ne 2$ and $\dim V = n$ is finite, then $V$ has a basis $e_1, \ldots, e_n$ orthogonal for $B$, and $Q = \sum_i a_i x_i^2$ with $a_i = Q(e_i)$. The $a_i$ are not unique.
- **Sylvester's law of inertia.** For a real quadratic form on a space of finite dimension, the numbers $p, q, r$ of positive, negative and zero coefficients are the same in every diagonal form. Two real forms on $V$ are equivalent if and only if they have the same signature $(p, q, r)$; then $Q \sim x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2$.
- **Complex forms.** Over an algebraically closed field of characteristic not $2$, every form of rank $r$ is equivalent to $x_1^2 + \cdots + x_r^2$, and the rank is the only invariant.
- **Finite fields.** Over $\F_q$ with $q$ odd, every nondegenerate form in $n$ variables is equivalent to $x_1^2 + \cdots + x_{n-1}^2 + d x_n^2$, with $d$ its discriminant. Two nondegenerate forms of the same dimension are equivalent if and only if their discriminants agree. Every form in $n \ge 3$ variables is isotropic.
- **Discriminant.** For $\operatorname{char} F \ne 2$ the discriminant is $\det A$ in $F^\times / F^{\times 2}$, and $0$ for a degenerate form. It is an invariant, because $\det(P^{\mathsf T} A P) = (\det P)^2 \det A$.
- **Definiteness.** A real form on a space of dimension $n$ is positive definite if and only if its signature is $(n, 0, 0)$. For $Q = x^{\mathsf T} A x$ with $A$ real symmetric, this holds if and only if all eigenvalues of $A$ are positive, if and only if all leading principal minors of $A$ are positive.
- **Principal axis theorem.** For a real symmetric $n \times n$ matrix $A$ with eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n$ there is an orthogonal $P$ with $\det P = 1$ such that $x = Py$ gives $x^{\mathsf T} A x = \sum_i \lambda_i y_i^2$.
- **Extreme values.** For the same $A$, $\lambda_n \norm{x}^2 \le x^{\mathsf T} A x \le \lambda_1 \norm{x}^2$ for all $x \in \R^n$. On unit vectors the maximum is $\lambda_1$ and the minimum is $\lambda_n$, attained exactly at the unit eigenvectors for these eigenvalues.

| Field | Complete invariants of a form on $F^n$ | Normal form | Classes on $F^n$ |
|---|---|---|---|
| $\C$, or any algebraically closed field of characteristic not $2$ | rank $r$ | $x_1^2 + \cdots + x_r^2$ | $n + 1$ |
| $\R$ | signature $(p, q, r)$ | $x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2$ | $(n+1)(n+2)/2$ |
| $\F_q$, $q$ odd | rank and discriminant of the nondegenerate part | $x_1^2 + \cdots + x_{r-1}^2 + d x_r^2$ | $2n + 1$ |
| $\Q$ | rank and discriminant are not enough | none this simple | infinitely many for $n \ge 1$ |

: How the field decides the classification of quadratic forms in characteristic not 2.

## Common errors

- **The wrong matrix.** The matrix of $x^2 + 6xy$ is $\begin{pmatrix} 1 & 3 \\ 3 & 0 \end{pmatrix}$, with half the cross coefficient on each side. A triangular matrix with $6$ in one corner gives the same form, but its eigenvalues say nothing about the signs of the form.
- **Confusing the two reductions.** Completing squares gives the right signs but arbitrary values. Only an orthogonal change of variables gives the eigenvalues and the lengths of axes. The congruent matrices $\operatorname{diag}(1, -3)$ and $\operatorname{diag}(3, -1)$ have the same signature and different eigenvalues.
- **Counting squares of dependent linear forms.** Writing $Q$ as a sum of $\pm L_i^2$ gives the signature only when the linear forms $L_i$ are linearly independent.
- **Testing semidefiniteness with leading minors.** Nonnegative leading principal minors do not make a matrix positive semidefinite; all principal minors must be nonnegative.
- **Reversing the discriminant test.** Equal discriminants decide equivalence over $\F_q$ with $q$ odd, not over $\R$ or $\Q$: $x^2 + y^2$ and $-x^2 - y^2$ have the same discriminant.
- **Forgetting the characteristic.** Over $\F_2$ the form $xy$ has no symmetric matrix and no diagonal form.
