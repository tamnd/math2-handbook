3. (a) and (c) are quadratic forms. (b) fails $Q(av) = a^2 Q(v)$: at $(1, 0)$ the value doubles when $v$ doubles. (d) scales correctly, but $b_Q$ is not bilinear: with $u = (1, 0)$, $b_Q(u, (0, 1)) = 1$ and $b_Q(u, (0, -1)) = 1$, not $-1$.

4. The three linear forms are dependent, since $x - z = (x - y) + (y - z)$. With $s = x - y$, $t = y - z$ the form is $s^2 + t^2 - (s + t)^2 = -2st$, which has signature $(1, 1, 1)$ on $\R^3$.

5. (a) Positive definite: $2 > 0$ and $\det = 10 - 4 = 6 > 0$. (b) Negative semidefinite but not definite: it is $-(x - y)^2$. (c) Indefinite: it is $(x + y)^2 - z^2$, of signature $(1, 1, 1)$.

8. The form uses only the symmetric part $\begin{pmatrix} 1 & 3/2 \\ 3/2 & 1 \end{pmatrix}$, whose determinant $1 - \tfrac94$ is negative. The form is indefinite: $Q(1, -1) = -1$.

9. The matrix $\begin{pmatrix} 4 & 3 \\ 3 & -4 \end{pmatrix}$ has trace $0$ and determinant $-25$, so eigenvalues $\pm 5$. Maximum $5$ at $\pm(3, 1)/\sqrt{10}$, minimum $-5$ at $\pm(1, -3)/\sqrt{10}$.

10. $Q = (x - y + 2z)^2 + (y + z)^2 - 2z^2$. With $u = x - y + 2z$, $v = y + z$, $w = z$, the inverse substitution gives $P = \begin{pmatrix} 1 & 1 & -3 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$ and $P^{\mathsf T} A P = \operatorname{diag}(1, 1, -2)$. Signature $(2, 1, 0)$; the third column $v = (-3, -1, 1)$ gives $Q(v) = -2$.

12. The squares are $1, 2, 4$, and $-1 = 6$ is not one, so $x^2 + y^2 \ne 0$ for $(x, y) \ne 0$. Take $v_1 = (1, 2)$, $v_2 = (5, 1)$: $Q(v_1) = 15 = 1$, $Q(v_2) = 78 = 1$, $B(v_1, v_2) = 3 \cdot 7 = 0$. The determinants $9 = 2$ and $1$ are both squares.

15. The centre solves $\begin{pmatrix} 9 & -2 \\ -2 & 6 \end{pmatrix} c = (5, 10)$, so $c = (1, 2)$, and the value there is $-30$. The eigenvalues are $5$ on $(1, 2)$ and $10$ on $(2, -1)$, so $5u^2 + 10v^2 = 30$: an ellipse with semi-axis $\sqrt6$ along $(1, 2)$ and $\sqrt3$ along $(2, -1)$.

17. The critical points satisfy $x^2 = 2y$ and $y^2 = 2x$, so they are $(0, 0)$ and $(2, 2)$. The Hessian at $(0, 0)$ is indefinite (a saddle); at $(2, 2)$ it is $\begin{pmatrix} 12 & -6 \\ -6 & 12 \end{pmatrix}$, positive definite, so $f(2, 2) = -8$ is a local minimum.

21. Take $v \ne 0$ with $Q(v) = 0$. Since $B$ is nondegenerate there is $w$ with $B(v, w) \ne 0$; scale it so that $B(v, w) = 1$. Then $Q(tv + w) = 2t + Q(w)$, and $t = (c - Q(w))/2$ gives the value $c$. Over $\F_q$ every form in at least $3$ variables is isotropic.

22. Count the solutions of $ac = b^2 + d$ one value of $b$ at a time. If $b^2 + d \ne 0$ there are $p - 1$ pairs $(a, c)$; if $b^2 + d = 0$ there are $2p - 1$. The number of $b$ with $b^2 = -d$ is $1$ for $d = 0$, and $2$ or $0$ for $d \ne 0$ as $-d$ is a square or not. Over $\F_7$ the class of $x^2 + y^2$ has $3 \cdot 42 = 126$ matrices and the class of $2xy$ has $3 \cdot 56 = 168$.

23. Write $x = \sum_i c_i u_i$ in an orthonormal eigenbasis; $x \perp u_1$ means $c_1 = 0$, and then $x^{\mathsf T} A x = \sum_{i \ge 2} \lambda_i c_i^2 \le \lambda_2$, with equality at $u_2$. For the given form the eigenvalues are $4, 1, -2$, so the maximum is $1$, at $\pm(2, -1, -2)/3$.

24. Write $M = L^{\mathsf T} L$ with $L$ invertible (Cholesky), apply the principal axis theorem to $(L^{-1})^{\mathsf T} A L^{-1}$, and take $P = L^{-1} R$ with $R$ orthogonal. The diagonal entries $\lambda$ satisfy $\det(P^{\mathsf T}(A - \lambda M)P) = 0$. Here $\det(A - \lambda M) = \lambda^2 - 1$, and $P = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 0 & -2 \end{pmatrix}$ gives $P^{\mathsf T} M P = I$ and $P^{\mathsf T} A P = \operatorname{diag}(1, -1)$.

25. If $W$ is positive definite for $Q$ and $N$ is spanned by the basis vectors with coefficient $\le 0$, then $Q \le 0$ on $N$, so $W \cap N = 0$ and $\dim W \le n - \dim N = p$. For the inequality, let $N_i$ be such a subspace for $Q_i$, of dimension $n - p(Q_i)$; on $N_1 \cap N_2$ the form $Q_1 + Q_2$ is $\le 0$, and this subspace has dimension at least $n - p(Q_1) - p(Q_2)$. Strict: $Q_1 = x^2$, $Q_2 = -x^2$ on $\R$.
