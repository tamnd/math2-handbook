1. (a) is an inner product: it is symmetric and bilinear, and $\langle x, x\rangle = 3x_1^2 - 2x_1x_2 + x_2^2 = 2x_1^2 + (x_1 - x_2)^2$, which is positive for $x \ne 0$. The length of $(1, 1)$ is $\sqrt 2$. (b) is not: $\langle (1, -1), (1, -1)\rangle = 1 - 2 - 2 + 1 = -2$.

2. $\langle x, y\rangle = 2 \cdot (-i) + (1 - i) \cdot 3 = 3 - 5i$ and $\langle y, x\rangle = 3 + 5i$. $\norm{x} = \sqrt{4 + 2} = \sqrt 6$ and $\norm{y} = \sqrt{10}$. Cauchy-Schwarz reads $\abs{3 - 5i}^2 = 34 \le 60$.

3. Symmetry and bilinearity are clear. If $\langle p, p\rangle = p(-1)^2 + p(0)^2 + p(1)^2 = 0$, then $p$ has the three roots $-1, 0, 1$, so $p = 0$ because its degree is at most $2$. The values are $\langle t, t^2\rangle = 0$, $\langle 1, t^2\rangle = 2$, $\norm{1} = \sqrt 3$ and $\norm{t^2} = \sqrt 2$.

5. From $\norm{x + y}^2 = \norm{x}^2 + 2\langle x, y\rangle + \norm{y}^2$ you get $\langle x, y\rangle = \frac{36 - 9 - 16}{2} = \frac{11}{2}$. The parallelogram law gives $\norm{x - y}^2 = 18 + 32 - 36 = 14$, so $\norm{x - y} = \sqrt{14}$.

6. Complex polarization gives $\langle x, y\rangle = \frac14(10 - 2 + 8i - 4i) = 2 + i$, so $\langle y, x\rangle = 2 - i$. The parallelogram law gives $2\norm{x}^2 + 2\norm{y}^2 = 10 + 2 = 12$, so $\norm{x}^2 + \norm{y}^2 = 6$.

8. The pairwise dot products of $(2, 3, 6)$, $(3, -6, 2)$, $(6, 2, -3)$ are $0$, and each has squared length $49$. The coordinates are $\langle v, e_i\rangle = 8, 5, 3$, so $v = 8e_1 + 5e_2 + 3e_3$, and $64 + 25 + 9 = 98 = \norm{v}^2$.

9. $A$ is not: Cauchy-Schwarz requires $\abs{G_{12}}^2 \le G_{11}G_{22}$, and $9 > 8$. $B$ is not: a Gram matrix is Hermitian, so its $(2, 1)$ entry would be $1 - i$. $C$ is: in $\C^2$ with the standard inner product, $v_1 = (\sqrt 2, 0)$ and $v_2 = \left(\frac{1 + i}{\sqrt 2}, \sqrt 2\right)$ have $\langle v_1, v_2\rangle = 1 - i$, $\norm{v_1}^2 = 2$ and $\norm{v_2}^2 = 3$.

10. A symmetric real matrix gives an inner product exactly when it is positive definite, which for this matrix means that the leading principal minors $1$, $1 - t^2$ and $\det G = 1 - 2t^2$ are positive. Answer: $\abs{t} < 1/\sqrt 2$.

12. Over $\R$, $\langle x + y, x - y\rangle = \norm{x}^2 - \langle x, y\rangle + \langle y, x\rangle - \norm{y}^2$, and the middle terms cancel by symmetry. Over $\C$ they leave $2i\operatorname{Im}\langle y, x\rangle$. Here $\norm{x}^2 = \norm{y}^2 = 2$, while $x + y = (1 + i, 2)$ and $x - y = (1 - i, 0)$ give $\langle x + y, x - y\rangle = (1 + i)^2 = 2i$.

14. $\langle v_2, v_1\rangle = 8$ and $\norm{v_1}^2 = 4$, so $u_2 = v_2 - 2v_1 = (-2, -1, 1, 2)$ with $\norm{u_2}^2 = 10$. The result is $e_1 = \frac12(1, 1, 1, 1)$, $e_2 = \frac{1}{\sqrt{10}}(-2, -1, 1, 2)$.

15. $u_1 = (1, 1, 1)$ with $\norm{u_1}^2 = 6$. Then $\langle v_2, u_1\rangle = 5$ gives $u_2 = \frac16(-5, 1, 1)$, and $u_3 = (0, 0, 1) - \frac12 u_1 - \frac35 u_2 = \frac15(0, -3, 2)$. The orthonormal basis is $\frac{1}{\sqrt 6}(1, 1, 1)$, $\frac{1}{\sqrt{30}}(-5, 1, 1)$, $\frac{1}{\sqrt{30}}(0, -3, 2)$; check that all three products, with the weights $1, 2, 3$, vanish.

16. The coefficient must make $\langle u_2, v_1\rangle = \langle v_2, v_1\rangle - c\langle v_1, v_1\rangle$ zero, so $c = \langle v_2, v_1\rangle / \langle v_1, v_1\rangle = (2 - i)/5$; the student used its conjugate $(2 + i)/5$. The student's vector is $\frac15(1 - 2i, 6 - 2i)$, and its inner product with $v_1$ is $-2i$. The correct vector is $u_2 = \frac15(1 + 2i, 4 - 2i)$, of length $1$. Over $\R$ the two orders agree, which hides the error.

19. Since the values $p(-1), p(0), p(1)$ can be chosen freely, $\langle p, u\rangle = p(1)$ for all $p$ forces $u(-1) = 0$, $u(0) = 0$, $u(1) = 1$, so $u = \frac12(t^2 + t)$. For degree at most $2$, $p'(0) = \frac12(p(1) - p(-1))$, so $w(-1) = -\frac12$, $w(0) = 0$, $w(1) = \frac12$, and $w = \frac12 t$.

21. Test the parallelogram law on $x = (1, 0)$ and $y = (0, 1)$. Then $\norm{x \pm y}_p = 2^{1/p}$, and the law reads $2 \cdot 2^{2/p} = 4$, which holds only for $p = 2$. For $p = 2$ the norm comes from the dot product. Answer: $p = 2$ only.

22. Put $y = 0$ to get $\norm{T x} = \norm{x}$. Expanding both sides of $\norm{T x - T y}^2 = \norm{x - y}^2$ then leaves $\langle T x, T y\rangle = \langle x, y\rangle$. For linearity, expand $\norm{T(ax + by) - aT x - bT y}^2$: every term is an inner product of two images, so the sum equals $\norm{(ax + by) - ax - by}^2 = 0$.

23. Let $B(x, y) = \langle T x, y\rangle$. Expanding gives $\sum_{k=0}^{3} i^k B(x + i^k y, x + i^k y) = 4B(x, y)$ over $\C$. Every term on the left is $0$, so $\langle T x, y\rangle = 0$ for all $y$; take $y = T x$. Over $\R$ the rotation $T(x_1, x_2) = (-x_2, x_1)$ has $\langle T x, x\rangle = -x_2x_1 + x_1x_2 = 0$.

24. If the $v_i$ are dependent, then $\det G = 0$. Otherwise $\det G = \norm{u_1}^2 \cdots \norm{u_k}^2$ for the Gram-Schmidt vectors $u_i$, and $v_i = u_i + w_i$ with $w_i$ in the span of the earlier vectors and orthogonal to $u_i$, so $\norm{u_i} \le \norm{v_i}$ by Pythagoras. Equality holds if and only if some $v_i = 0$ or the $v_i$ are pairwise orthogonal.

25. Take an orthonormal basis $f_1, \dots, f_n$ for the given inner product and let $P x = (\langle x, f_1\rangle, \dots, \langle x, f_n\rangle)$; Parseval's identity says $\langle x, y\rangle = (Px) \cdot (Py)$. For (a), $\langle x, x\rangle = 2x_1^2 + (x_1 - x_2)^2$, so $P = \begin{pmatrix} \sqrt 2 & 0 \\ 1 & -1 \end{pmatrix}$ works; so does $QP$ for every orthogonal $Q$.
