1. The diagonal holds the coefficients of the squares, and each off-diagonal entry is half the coefficient of the mixed term: $\begin{pmatrix} 3 & -2 & 0 \\ -2 & 2 & 3 \\ 0 & 3 & -1 \end{pmatrix}$.

2. $b_Q(u, v) = 2u_1 v_1 + 3(u_1 v_2 + u_2 v_1)$, so $\frac12 b_Q$ has matrix $\begin{pmatrix} 1 & 3/2 \\ 3/2 & 0 \end{pmatrix}$.

3. (a) $(2, 2, 0)$. (b) $xy = \frac14(x + y)^2 - \frac14(x - y)^2$, so $(1, 1, 0)$. (c) The matrix has rank $1$ and is positive semidefinite, so $(1, 0, 2)$.

4. Positive semidefinite but not definite ($(x + y)^2$); positive definite ($(x + y)^2 + 2y^2$); negative definite (eigenvalues $-3 \pm 2\sqrt2$); indefinite (eigenvalues $4$ and $-2$).

5. The discriminants are $3$, $12$ and $-1$ (the matrix of $2xy$ is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$). Since $12 = 3 \cdot 2^2$, the first two agree in $\Q^\times / (\Q^\times)^2$, and the substitution $y \mapsto y/2$ carries $x^2 + 12y^2$ to $x^2 + 3y^2$. They are equivalent.

7. The matrix $\begin{pmatrix} 1 & 2 \\ 2 & -2 \end{pmatrix}$ has eigenvalues $2$ and $-3$. The maximum $2$ is taken at $\pm(2, 1)/\sqrt5$, the minimum $-3$ at $\pm(1, -2)/\sqrt5$.

8. Collect $x$ first: $Q = (x + 2y + 2z)^2 - (y + 3z)^2 + 8z^2$. The signature is $(2, 1, 0)$, and the determinant $-8$ is negative, as one negative square requires.

11. Over $\mathbb F_q$ a nondegenerate form is fixed by its rank and its discriminant up to squares. The discriminants are $1$ and $-1$. In $\mathbb F_3$ the element $-1$ is not a square; in $\mathbb F_5$ it is, since $2^2 = 4 = -1$.

13. The eigenvalues are $4$ on $(1, 1)$ and $2$ on $(1, -1)$. In the rotated coordinates the curve is $4u^2 + 2v^2 = 8$.

14. Complete the square in vector form: the centre solves $2Ax_0 = -b$ with $A = \begin{pmatrix} 2 & 2 \\ 2 & 5 \end{pmatrix}$ and $b = (-12, -24)$, so $x_0 = (1, 2)$, and the constant becomes $6 + \frac12 b^T x_0 = -24$. Then diagonalize $A$.

16. The matrix is $(1 - a) I + a J$ with $J$ the all-ones matrix. Its eigenvalues are $1 + 2a$ on $(1, 1, 1)$ and $1 - a$ twice. Positive definite for $-\frac12 < a < 1$, semidefinite for $-\frac12 \le a \le 1$.

17. Let $V_+$ be spanned by the first $p$ vectors of a diagonalizing basis, and let $W$ be a subspace on which $Q$ is positive definite. The span $V_{\le 0}$ of the other $q + r$ basis vectors has $Q \le 0$, so $W \cap V_{\le 0} = 0$ and $\dim W \le n - (q + r) = p$. The number $p$ is now defined without a basis, and so is $q$ (apply the same to $-Q$).

18. The rank $r$ is an invariant, and for each $r \ge 1$ the nondegenerate part is fixed by its discriminant, which has two possible classes, since $\mathbb F_q^\times / (\mathbb F_q^\times)^2$ has order $2$. Both occur: $x_1^2 + \cdots + x_r^2$ and $x_1^2 + \cdots + x_{r-1}^2 + c x_r^2$ with $c$ a non-square. Rank $0$ gives one class, so the total is $1 + 2n$.

19. Write $x = \sum c_i u_i$. Orthogonality to $u_1$ means $c_1 = 0$, and then $x^T A x = \sum_{i \ge 2} \lambda_i c_i^2 \le \lambda_2$, with equality at $x = u_2$. For the given matrix the eigenvalues are $2 + \sqrt2$, $2$ and $2 - \sqrt2$, with eigenvectors $(1, \sqrt2, 1)$, $(-1, 0, 1)$ and $(1, -\sqrt2, 1)$, so the constrained maximum is $2$, at $(-1, 0, 1)/\sqrt2$.

20. An isotropic vector $e$ in a nondegenerate space lies in a hyperbolic plane: there is $f$ with $Q(f) = 0$ and $b(e, f) = 1$, where $b$ is the symmetric form with $Q(v) = b(v, v)$. Then $Q(ae + f) = 2a$, which takes every value as $a$ runs over $F$.
