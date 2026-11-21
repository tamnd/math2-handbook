2. $\operatorname{Row}(A) = \R(1, 2, 3)$; $\operatorname{Nul}(A)$ has basis $(-2, 1, 0)$, $(-3, 0, 1)$; $\operatorname{Col}(A) = \R(1, 2)$; $\operatorname{Nul}(A^{\mathsf{T}}) = \R(-2, 1)$. Each basis vector of a null space has dot product $0$ with the matching row or column.

4. (a) is idempotent but not symmetric: a projection, but not an orthogonal one. (b) and (d) are orthogonal projections, onto $\R(1, 1)$ and $\R(1, -1)$. (c) is symmetric, but $P^2 = I \neq P$.

5. The component of $b$ along the normal $(1, 1, 1)$ is $\frac{6}{3}(1, 1, 1) = (2, 2, 2)$. The closest point is $(-1, 0, 1)$, and the distance is $\norm{(2, 2, 2)} = 2\sqrt 3$.

7. $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ gives $A A^{\mathsf{T}} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, which is singular. For an $m \times n$ matrix $A$, the $m \times m$ matrix $A A^{\mathsf{T}}$ has rank at most $n$, so it can be invertible only when $m \le n$, and then exactly when the rows of $A$ are independent.

8. $Q = \frac{1}{5} \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ and $R = \begin{pmatrix} 5 & 4 \\ 0 & 3 \end{pmatrix}$.

12. $A^{\mathsf{T}} A = \begin{pmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{pmatrix}$ and $A^{\mathsf{T}} y = (3, 3, 9)$. The solution is $a = -3/20$, $b = -9/20$, $c = 3/4$, with residual $(-1, 3, -3, 1)/20$ and residual sum of squares $1/20$.

13. If $A^{\mathsf{T}} A x = 0$, then $0 = x^{\mathsf{T}} A^{\mathsf{T}} A x = \norm{A x}^2$.

15. $Q$ has columns $\frac{1}{3}(2, 1, 2)$ and $\frac{1}{3}(2, -2, -1)$, and $R = \begin{pmatrix} 3 & 3 \\ 0 & 6 \end{pmatrix}$. Then $Q^{\mathsf{T}} b = (5/3, -1/3)$ and $\hat x = (11/18, -1/18)$.

17. $A^{\mathsf{T}} A = \begin{pmatrix} 1 + \varepsilon^2 & 1 \\ 1 & 1 + \varepsilon^2 \end{pmatrix}$ has eigenvalues $2 + \varepsilon^2$ and $\varepsilon^2$, so $\sigma_1 = \sqrt{2 + \varepsilon^2}$ and $\sigma_2 = \varepsilon$. When $1 + \varepsilon^2$ rounds to $1$, the computed $A^{\mathsf{T}} A$ is singular, although $A$ has independent columns.

19. $c_0 = 1/5$ and $c_2 = 4/7$, so $p = \frac{6}{7} x^2 - \frac{3}{35}$, and $\norm{f - p}^2 = \frac{2}{9} - \frac{2}{25} - \frac{32}{245} = \frac{128}{11025}$.

20. Let $u \in \operatorname{im} P$ and $w \in \ker P$, and look at $\norm{P(u + t w)}^2 \le \norm{u + t w}^2$ for real or complex $t$. The left side is $\norm{u}^2$, so $0 \le 2 \operatorname{Re}(\bar t \langle u, w \rangle) + \abs{t}^2 \norm{w}^2$ for all $t$; small $t$ forces $\langle u, w \rangle = 0$. So $\ker P \subseteq (\operatorname{im} P)^\perp$, and the two have the same dimension because $V = \operatorname{im} P \oplus \ker P$.

21. If $f \perp U$, pick polynomials $p_n \to f$ uniformly. Then $\norm{f}^2 = \langle f, f - p_n \rangle \le \norm{f} \norm{f - p_n} \to 0$. So $U^\perp = 0$ and $(U^\perp)^\perp = V$, which contains $\abs{x}$, not a polynomial.

22. The planes meet in a line, which gives one zero angle. The other principal vectors are the unit vectors of $U$ and $W$ orthogonal to that line, and they lie in the plane orthogonal to the line, together with $n_1$ and $n_2$. There the angle between two lines equals the angle between their normals.

23. $Q_1 = Q_2 R_2 R_1^{-1}$, and $T = R_2 R_1^{-1}$ is upper triangular with positive diagonal. Then $T^{\mathsf{T}} T = Q_1^{\mathsf{T}} Q_1 = I$, so $T^{\mathsf{T}} = T^{-1}$ is both lower and upper triangular, hence diagonal, with $t_{ii}^2 = 1$ and $t_{ii} > 0$.

24. Write $p = x^3 - q$ with $\deg q \le 2$. Minimizing $\norm{p}$ means taking $q$ as the best approximation of $x^3$ by polynomials of degree at most $2$, so $p$ is orthogonal to all of them, as $P_3$ is. The answer is $x^3 - \frac{3}{5} x = \frac{2}{5} P_3$, with minimum $\frac{8}{175}$.
