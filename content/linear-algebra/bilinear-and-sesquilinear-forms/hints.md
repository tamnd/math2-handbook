1. $A = \begin{pmatrix} 3 & -1 \\ 2 & 5 \end{pmatrix}$. Then $B(u, v) = 2$ and $B(v, u) = 11$, so $B$ is not symmetric, as $A \ne A^{\mathsf{T}}$ already shows.

4. Congruence does not keep eigenvalues; it keeps the rank and the determinant up to a nonzero square, and here both determinants are $1$. The matrix $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, with columns $(1, 0)$ and $(1, 1)$, gives $P^{\mathsf{T}} P = C$.

7. The form $a x^2 + b y^2$ with $a, b \ne 0$ is isotropic if and only if $-b/a$ is a square. Over $\F_5$, $-2 = 3$ is not a square (the squares are $1, 4$), so the form is anisotropic. Over $\F_{11}$, $-2 = 9 = 3^2$, and $(3, 1)$ gives $9 + 2 = 11 = 0$.

12. Take $f_1 = (1, 1, 0)$, with $B(f_1, f_1) = 2$. Then $f_1^\perp$ is $y_1 + y_2 + 2y_3 = 0$; take $f_2 = (1, -1, 0)$, with $B(f_2, f_2) = -2$, and then $f_3 = (1, 1, -1)$, orthogonal to both, with $B(f_3, f_3) = -2$. The matrix is $\operatorname{diag}(2, -2, -2)$. Check: $\det A = 2$, $\det P = 2$, and $8 = 2^2 \cdot 2$.

14. $u = e_1$ and $v = (2, -1)$ give $B_2(u, v) = 0$ and $B_2(v, u) = 2$. A reflexive form is symmetric or alternating. $B_c(e_1, e_1) = 1$ rules out alternating, and $B_c$ is symmetric only for $c = 0$. Answer: $c = 0$.

15. The matrix is $\begin{pmatrix} 3 & 3 & 5 \\ 3 & 5 & 9 \\ 5 & 9 & 17 \end{pmatrix} = V^{\mathsf{T}} V$, where $V$ is the Vandermonde matrix with rows $(1, a, a^2)$ for $a = 0, 1, 2$. So its determinant is $(\det V)^2 = 2^2 = 4 \ne 0$. For $B'$, $p$ is in the radical if and only if $p(0) = p(1) = 0$, so the radical is $\operatorname{span}(t^2 - t)$.

16. For $B_1$, $-\det = 1$ is a square, and $x^2 + 6xy + 8y^2 = (x + 2y)(x + 4y)$. The isotropic vectors $u = (2, -1)$ and $z = (4, -1)$ have $B_1(u, z) = -2$, so $v = -\tfrac{1}{2} z = (-2, \tfrac{1}{2})$ completes the pair. For $B_2$, $x^2 + 6xy + 7y^2 = (x + 3y)^2 - 2y^2$, which is $0$ only for $x = y = 0$, because $2$ is not a square in $\Q$.

19. The vectors orthogonal to $e_1$ and $e_2$ satisfy $x_2 + x_3 = 0$ and $-x_1 + 2x_3 + x_4 = 0$. Correcting $e_3$ and $e_4$ by multiples of $e_1, e_2$ gives the vectors $w_3 = (2, -1, 1, 0)$ and $w_4 = (1, 0, 0, 1)$ of that complement, with $B(w_3, w_4) = 2$. Take $u_2 = w_3$ and $v_2 = \tfrac{1}{2} w_4 = (\tfrac{1}{2}, 0, 0, \tfrac{1}{2})$. Check: the Pfaffian of $A$ is $2$, and $\det P = \tfrac{1}{2}$.

21. The determinant is an invariant only up to nonzero squares, and $4 = 2^2 \cdot 1$. For $a \ne 0$ the plane $\langle a, -a \rangle$ is hyperbolic, so both forms are isometric to $H \perp H$. Explicitly, the columns $e_1, e_3, (0, \tfrac{3}{2}, 0, \tfrac{1}{2}), (0, \tfrac{1}{2}, 0, \tfrac{3}{2})$ carry $\operatorname{diag}(1, 1, -1, -1)$ to $\operatorname{diag}(1, -1, 2, -2)$.

22. (a) $\omega((1, 1, 0, 0), (0, 0, 1, -1)) = 1 - 1 = 0$ and $\dim L = 2$. One answer is $L' = \operatorname{span}(e_1, e_4)$. (b) Take an isotropic $W$ with $W \cap L = \{0\}$ of largest dimension $k$, and suppose $k < m$. Then $(W + L)^\perp = W^\perp \cap L$ has dimension $m - k$, so $W^\perp \cap (W + L) = W + (W^\perp \cap L)$ has dimension $m < 2m - k = \dim W^\perp$. A vector $v \in W^\perp$ outside $W + L$ makes $W + Fv$ isotropic with $(W + Fv) \cap L = \{0\}$, against the choice of $W$.

23. Every vector is isotropic, so the Lagrangian subspaces are the planes on which $\omega$ vanishes. Each of the $15$ nonzero vectors $u$ has $u^\perp$ of dimension $3$, which contains $u$ and $(8 - 2)/2 = 3$ such planes through $u$. Each plane has $3$ nonzero vectors, so there are $15 \cdot 3 / 3 = 15$ Lagrangian subspaces.

24. Let $V_+ = \operatorname{span}(e_1, \dots, e_p)$, on which $B$ is positive definite. A totally isotropic $W$ meets $V_+$ only in $0$, so $\dim W \le q$; in the same way $\dim W \le p$. The vectors $e_i + e_{p + i}$ for $i \le \min(p, q)$ span a totally isotropic subspace of dimension $\min(p, q)$, which is therefore maximal.

25. $x - y = (0, -2, -2)$ has $B(x - y, x - y) = 4 - 4 = 0$. For $x + y = (2, 2, 2)$, $B(x + y, x + y) = 4$ and $B(x, x + y) = 2$, so $\tau_{x + y}(x) = -y$, and then $\tau_y(-y) = y$. The matrix is $\begin{pmatrix} 1 & -2 & 2 \\ 2 & -1 & 2 \\ 2 & -2 & 3 \end{pmatrix}$.

26. Take $u = (1, 1, 1)$, $a = (1, 1, 0)$ and $b = (0, 1, 1)$. Since $B(u, u) = 1 \ne 0$, $V = \operatorname{span}(u) \perp u^\perp$. In $H$ every vector has $B(v, v) = 2 v_1 v_2 = 0$, while $\langle 1 \rangle \perp \langle 1 \rangle$ has $B(e_1, e_1) = 1$, so they are not isometric. The theorem fails because the characteristic is $2$.
