2. $\langle Tu, Tv \rangle = \langle u, v \rangle = \frac{7 - 1 - 4}{2} = 1$, so the angle is $\arccos \frac{1}{2} = \pi/3$.

3. $\operatorname{tr} Q = 1$, so $\cos \theta = 0$ and $\theta = \pi/2$. From $Q - Q^{\mathsf{T}}$, $2 \sin \theta \, u = \frac{2}{3}(1, 2, 2)$, so the axis is $u = \frac{1}{3}(1, 2, 2)$; check $Q(1, 2, 2) = (1, 2, 2)$.

6. $R(\theta) S(\alpha) = S(\alpha + \theta/2)$ gives $S(5\pi/12)$, the reflection in the line at $75°$. $S(\alpha) R(\theta) = S(\alpha - \theta/2)$ gives $S(-\pi/12)$, the line at $-15°$.

8. $C(A) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = R(-\pi/2)$.

11. $Q = I - \frac{2}{3} n n^{\mathsf{T}}$ with $n = (1, -1, -1)$, so $Q$ is the reflection in the plane $x - y - z = 0$.

12. Choose $\lambda$ with $\lambda^n = \det U$ and put $V = \lambda^{-1} U$. There are exactly $n$ pairs, one for each $n$-th root of $\det U$.

14. $C(A) = Q$, the matrix of exercise 3. The axis is the line through $w$, and $\tan(\theta/2) = \norm{w} = 1$ gives $\theta = \pi/2$.

17. $R_x(\pi/2) R_y(\pi/2)$ is the cyclic permutation matrix $e_1 \mapsto e_2 \mapsto e_3 \mapsto e_1$: angle $2\pi/3$ about the line through $(1, 1, 1)$. $R_y(\pi/2) R_x(\pi/2)$ has trace $0$ and fixes $(1, 1, -1)$: angle $2\pi/3$ about that line.

18. $C = s_{(1, 0, -1)} s_{(1, -1, 0)}$: first swap $e_1$ and $e_2$, then swap $e_1$ and $e_3$. A single reflection has determinant $-1$, but $\det C = 1$.

20. For orthonormal $e_i$, the vectors $e_i + e_j$ and $e_i - e_j$ are orthogonal, so $\norm{T e_i} = \norm{T e_j}$ for all $i, j$. Call this common length $c$. If $c > 0$, then $T / c$ maps an orthonormal basis to an orthonormal set.

21. For unit vectors $u$ and $v$ choose $R \in SO(n)$ with $R u = v$; then $R s_u R^{-1} = s_{Ru} = s_v$. For rotations, use $R \rho R^{-1}$, where $\rho$ is the rotation by $\theta$ about $u$: it is the rotation by $\theta$ about $Ru$. Send the axis of one rotation to the axis of the other, choosing the sign of the target vector so that the senses of turning agree.

22. If $(I + A) x = 0$, then $0 = x^{\mathsf{T}} x + x^{\mathsf{T}} A x = \norm{x}^2$, since $x^{\mathsf{T}} A x = 0$. The factors $I - A$ and $(I + A)^{-1}$ commute. If $C(A) x = -x$, then $(I - A) y = -(I + A) y$ for $y = (I + A)^{-1} x$, so $y = 0$.

23. $R = s_a s_b$ with $a, b$ orthogonal to the axis, and $s_a s_b = (-s_a)(-s_b)$. The map $-s_a$ fixes $a$ and is $-1$ on $a^\perp$, a half-turn about $\R a$.

24. $U X U^*$ is again Hermitian with trace $0$, and $\det(U X U^*) = \det X$, so the map keeps the norm $\sqrt{-\det X}$. For the kernel, $U X = X U$ for all $X \in \mathcal{H}$ forces $U$ to be scalar, and a scalar in $SU(2)$ is $\pm I$.
