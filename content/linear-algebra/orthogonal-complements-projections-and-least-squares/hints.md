1. Solve $x_1 + 2x_2 - x_3 = 0$ and $x_2 + x_3 + x_4 = 0$ with $x_3, x_4$ free. A basis is $(3, -1, 1, 0)$, $(2, -1, 0, 1)$, and $2 + 2 = 4$.

3. The coefficient is $\frac{\ip{v}{a}}{\ip{a}{a}} = \frac{3}{9}$, so the projection is $\frac{1}{3}(2, -1, 2)$. The error is $\frac{1}{3}(7, 10, -2)$, with squared length $\frac{153}{9} = 17$, so the distance is $\sqrt{17}$. Check: $\norm{v}^2 = 18 = 1 + 17$.

5. $P_1$ and $P_3$ are orthogonal projections, onto the lines $\R(1, 1)$ and $\R(1, 3)$: both are symmetric with $P^2 = P$. $P_2$ is idempotent but not symmetric; it projects onto $\R(1, 1)$ along the $y$-axis. $P_4$ is symmetric but $P_4^2 = I \neq P_4$; it is the reflection in the $x$-axis.

7. The solution in the row space is a multiple of $(2, -1, 2)$; substituting $t(2, -1, 2)$ gives $9t = 18$, so $x = (4, -2, 4)$ with length $6$. The solutions form the plane, and the shortest one is the foot of the perpendicular from $0$.

10. $Q^{\mathsf{T}}b = (\frac{10}{3}, -\frac{5}{3})$, and back substitution in $R\hat x = Q^{\mathsf{T}}b$ gives $\hat x = (\frac{5}{3}, -\frac{5}{9})$. The normal equations are $9x_1 + 9x_2 = 10$, $9x_1 + 18x_2 = 5$. The residual is $\frac{1}{9}(-1, -2, 2)$, and $14 = \frac{125}{9} + \frac{1}{9}$.

11. With $\sum t = 2$, $\sum t^2 = 6$, $\sum y = 8$ and $\sum ty = 11$, the normal equations are $4c_0 + 2c_1 = 8$, $2c_0 + 6c_1 = 11$, so $y = \frac{13}{10} + \frac{7}{5}t$. The residuals are $\frac{1}{10}(11, -13, -7, 9)$, and the sum of squares is $\frac{21}{5}$.

15. The coefficient of $x$ is $0$ by symmetry. The other two are $\frac{2/5}{2} = \frac{1}{5}$ and $\frac{8/35}{2/5} = \frac{4}{7}$, so the polynomial is $\frac{1}{5} + \frac{4}{7} \cdot \frac{3x^2 - 1}{2} = \frac{6}{7}x^2 - \frac{3}{35}$. The squared distance is $\frac{2}{9} - 2 \cdot \frac{1}{25} - \frac{2}{5} \cdot \frac{16}{49} = \frac{128}{11025}$.

16. The functions $1$, $\cos x$, $\sin x$ are orthogonal, with squared norms $2\pi$, $\pi$, $\pi$. Here $\ip{x^2}{1} = \frac{2\pi^3}{3}$, $\ip{x^2}{\cos x} = -4\pi$ and $\ip{x^2}{\sin x} = 0$, so the answer is $\frac{\pi^2}{3} - 4\cos x$. The squared distance is $\frac{2\pi^5}{5} - \frac{2\pi^5}{9} - 16\pi = \frac{8\pi^5}{45} - 16\pi \approx 4.138$.

19. The residual of $(2, 1)$ is $(0, 0, -1)$, and $A^{\mathsf{T}}(0, 0, -1) = (-1, 1) \neq 0$, so it is not orthogonal to the column space. The normal equations $2x_1 - x_2 = 2$, $-x_1 + 2x_2 = 1$ give $(\frac{5}{3}, \frac{4}{3})$, with sum of squared errors $\frac{1}{3}$ instead of $1$.

20. Take $u \in \operatorname{im} P$ and $w \in \ker P$. Then $P(u + tw) = u$ for every scalar $t$, so $\norm{u}^2 \le \norm{u + tw}^2 = \norm{u}^2 + 2t\operatorname{Re}\ip{w}{u} + t^2\norm{w}^2$ for all real $t$; over $\C$ apply this also to $iw$. This forces $\ip{w}{u} = 0$, so $\ker P \perp \operatorname{im} P$, and $V = \operatorname{im} P \oplus \ker P$ is then the orthogonal decomposition. Without the inequality, $P_2$ of Exercise 5 sends $(1, 0)$ to $(1, 1)$.

21. Write $v = p + r$ with $p \in U$ and $r \perp U$. Subtracting from the last column of $G(u_1, \dots, u_k, v)$ the combination of the first $k$ columns that corresponds to $p$, and then doing the same with the rows, leaves the determinant unchanged and turns the last row and column into $(0, \dots, 0, \norm{r}^2)$. For Exercise 9 the determinants are $9$ and $3$, and $9 / 3 = 3 = (\sqrt{3})^2$.

22. Let $y \in V$ be nonzero, with $y_k \neq 0$ and $y_n = 0$ for $n > N$. The vector $x = e_k - \frac{N + 1}{k}e_{N + 1}$ lies in $U$ and has $\ip{x}{y} = y_k \neq 0$. So $U^\perp = \set{0}$, $U \oplus U^\perp = U \neq V$ because $e_1 \notin U$, and $(U^\perp)^\perp = V$. The theorem needs $U$ finite-dimensional, and $U$ is not.

23. $\operatorname{Col} A$ is the line through $a = (1, -1, 2)$, and the projection of $b$ is $\frac{5}{6}a$. Since $Ax = (x_1 - x_2)a$, the least-squares solutions are the $x$ with $x_1 - x_2 = \frac{5}{6}$. In general they form $\hat x + \operatorname{Nul} A$, and $\operatorname{Nul} A = (\operatorname{Row} A)^\perp$, so exactly one of them is in $\operatorname{Row} A$, and Pythagoras makes it the shortest. Here $\operatorname{Row} A = \R(1, -1)$, and the answer is $(\frac{5}{12}, -\frac{5}{12})$.
