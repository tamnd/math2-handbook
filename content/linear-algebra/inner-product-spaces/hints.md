1. (a) Yes: $\ip{x}{x} = x_1^2 + 3x_2^2$. (b) No: positivity fails at $(0, 1)$, which gives $-1$. (c) No: it gives $0$ at $(1, 0)$ and $-2$ at $(1, -1)$. (d) Yes: $\ip{x}{x} = 2x_1^2 + 2x_1 x_2 + x_2^2 = x_1^2 + (x_1 + x_2)^2$, which is $0$ only at $x = 0$.

2. $\ip{x}{y} = 2(1 - i) + (1 + i)(-i) = 3 - 3i$ and $\ip{y}{x} = 3 + 3i$. $\norm{x} = \sqrt6$ and $\norm{y} = \sqrt3$. $\ip{ix}{y} = i(3 - 3i) = 3 + 3i$, while $\ip{x}{iy} = \overline{i}(3 - 3i) = -3 - 3i$.

5. $\ip{x}{y} = 1 \cdot \overline{i} + i \cdot 0 = -i$, whose real part is $0$; so $\norm{x + y}^2 = 3 = 2 + 1$. But $x + iy = (0, i)$ has $\norm{x + iy}^2 = 1 \ne 3$. The identity for $x$ and $iy$ tests $\operatorname{Re}\ip{x}{iy} = \operatorname{Im}\ip{x}{y}$, which here is $-1$.

8. (a) Yes: the Gram matrix of $v_1 = v_2$ for any unit vector. (b) No: $\det = -1 < 0$. (c) Yes: it is Hermitian with positive diagonal and $\det = 3 - 2 = 1 > 0$, so it is positive definite; a positive semidefinite Hermitian matrix is the Gram matrix of the columns of its square root. (d) No: a diagonal entry is $\norm{v_2}^2 \ge 0$.

9. The coefficient must be $\ip{v_2}{u_1} / \ip{u_1}{u_1} = \overline{i}/2 = -i/2$; the student used its conjugate. The correct vector is $u_2 = (1, 0) + \frac{i}{2}(i, 1) = \left(\frac12, \frac{i}{2}\right)$, and $\ip{u_2}{u_1} = -\frac{i}{2} + \frac{i}{2} = 0$. The student's vector gives $\ip{u_2}{u_1} = -2i$.

11. $\ip{x}{x} = (x_1 - x_2)^2 + 2x_2^2$. The vectors orthogonal to $(1, 0)$ satisfy $x_1 - x_2 = 0$, and $\ip{(1, 1)}{(1, 1)} = 2$. One answer is $(1, 0)$, $\frac{1}{\sqrt2}(1, 1)$.

13. (a) Apply the inequality to $(1, 2, 3)$ and $(a, b, c)$; equality when $(a, b, c)$ is a multiple of $(1, 2, 3)$. (b) Apply it to $(\sqrt{x_i})_i$ and $(1/\sqrt{x_i})_i$; equality when all $x_i$ are equal.

17. A nonzero polynomial of degree at most $2$ cannot vanish at the three points $0, 1, 2$; the cubic $t(t - 1)(t - 2)$ can. Gram-Schmidt gives $u_1 = 1$, $u_2 = t - 1$, $u_3 = t^2 - 2t + \frac13$, with squared norms $3$, $2$ and $\frac23$.

18. $u_1 = v_1$ with $\norm{u_1}^2 = 2$, and $\ip{v_2}{u_1} = 1 - i$. So $u_2 = v_2 - \frac{1 - i}{2} u_1 = \left(\frac{1 + i}{2}, \frac{1 - i}{2}, 1\right)$, with $\norm{u_2}^2 = 2$. Divide each $u_j$ by $\sqrt2$.

21. $(Ax) \cdot (Ax) = \norm{Ax}^2$ is $0$ only when $Ax = 0$, so positivity holds exactly when $\ker A = 0$. If $A^{\mathsf T} A c = 0$, then $\norm{Ac}^2 = c^{\mathsf T} A^{\mathsf T} A c = 0$, so $Ac = 0$.

22. Write $u = a + bt + ct^2$ and solve $\ip{t^k}{u} = \delta_{k0}$ for $k = 0, 1, 2$, a system whose matrix is the Hilbert matrix $H_3$. The answer is $u = 9 - 36t + 30t^2$. For the space of all polynomials, see the first remark of the [Riesz representation theorem](/04GYPXDXNH/).

24. Expand the right side: the squares give $\sum_{j \ne k} a_j^2 b_k^2$ and the cross terms give $-2\sum_{j < k} a_j b_j a_k b_k$. Equality in Cauchy-Schwarz means every $2 \times 2$ minor $a_j b_k - a_k b_j$ is $0$, that is, the vectors are dependent.

25. For additivity, apply the parallelogram law to $\frac{x + x'}{2} + y$ and $\frac{x - x'}{2}$, and again with $-y$; subtracting gives $\ip{x}{y} + \ip{x'}{y} = 2\ip{\frac{x + x'}{2}}{y}$. With $x' = 0$ this gives $\ip{x}{y} = 2\ip{x/2}{y}$, and so additivity. Induction gives integers, then rationals. The map $t \mapsto \ip{tx}{y}$ is continuous because the norm is, so it is linear in $t$.

26. If the family is dependent, $\det G = 0$. Otherwise $\det G = \norm{u_1}^2 \cdots \norm{u_k}^2$ with the Gram-Schmidt vectors $u_j$, and $\norm{u_j} \le \norm{v_j}$ by the Pythagorean theorem, with equality exactly when $v_j$ is orthogonal to $v_1, \dots, v_{j-1}$. For a square matrix, $\det(A^{\mathsf T} A) = (\det A)^2$.

27. $h$ is linear in $x$ and conjugate symmetric because $M^* = M$. If $a > 0$, then $h(x, x) = a\abs{x_1 + \frac{b}{a} x_2}^2 + \frac{ad - \abs{b}^2}{a}\abs{x_2}^2$. For the converse, evaluate at $e_1$, and at $x = (-b, a)$, where $h(x, x) = a(ad - \abs{b}^2)$.

28. $u_{af} = \overline{a}\, u_f$, so the form is linear in $f$. The maximum is reached at $v = u_f / \norm{u_f}$, by Cauchy-Schwarz. The dual basis vector $e_i^*$ is $\ip{\cdot}{e_i}$, so its representative is $e_i$.
