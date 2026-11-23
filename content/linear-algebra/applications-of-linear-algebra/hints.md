2. The equations are $x_1 - x_3 = 300$ at $A$, $x_1 - x_2 = 300$ at $B$ and $x_2 - x_3 = 0$ at $C$. The solutions are $(x_1, x_2, x_3) = (300 + t, t, t)$ with $t \ge 0$, so the smallest flow on $A \to B$ is $300$ cars per hour; the free variable $t$ counts the cars that go once round.

4. The answer is $p(t) = t^2 - 2t + 1 = (t - 1)^2$. The determinant is $(0 - (-1))(2 - (-1))(2 - 0) = 6$, and the Lagrange polynomial is $L(t) = -\tfrac12 (t + 1)(t - 2)$.

6. The normal equations are $4 c_0 + 6 c_1 = 6$ and $6 c_0 + 14 c_1 = 11$, so $y = 0.9 + 0.4 x$. The residual is $(0.1, -0.3, 0.3, -0.1)$, with squared length $0.2$, and $\norm{y - \bar y \mathbf 1}^2 = 1$, so $R^2 = 0.8$.

7. The residual is $(1, 1, -1)$ and $\bar y = 7/3$, so the number is $1 - 3/(2/3) = -7/2$. The arithmetic is right: the formula assumes that $\bar y \mathbf 1$ lies in the model space, which fails without the constant column, so it no longer measures anything between $0$ and $1$. For a model through the origin one uses $\norm{\hat y}^2 / \norm{y}^2 = 14/17$ instead.

8. The first normal equation says that the residuals sum to $0$, which is $\bar y = \hat c_0 + \hat c_1 \bar x$. Substitute this into the second normal equation to get $\hat c_1 S_{xx} = S_{xy}$. Then $\hat y - \bar y \mathbf 1 = \hat c_1 (x - \bar x \mathbf 1)$, whose squared length is $\hat c_1^2 S_{xx} = S_{xy}^2 / S_{xx}$.

10. $L = \begin{pmatrix} 1 & 4 \\ 1/2 & 0 \end{pmatrix}$ has the eigenvalues $2$ and $-1$, with the eigenvectors $(4, 1)$ and $(2, -1)$. Since $x_0 = (4, 1) + (2, -1)$, $x_k = 2^k (4, 1) + (-1)^k (2, -1)$. The population doubles each year in the long run, with four juveniles to each adult.

13. From $x_0 = (1, 0, 0)$ the distributions are $(0, 1, 0)$, $(0, 0, 1)$, $(1, 0, 0)$, and so on, since $P^3 = I$; they never converge. Every power of $P$ is a permutation matrix with zero entries, so $P$ is not regular. The eigenvalues are the three cube roots of $1$, all of absolute value $1$.

14. Check $Pq = q$ and $P(1, -1)^{\mathsf T} = (1 - a - b)(1, -1)^{\mathsf T}$ directly. As $a + b > 0$, the eigenvalue $1 - a - b$ differs from $1$, so the eigenspace for $1$ is a line and $q$ is the only steady state. Any probability vector is $x_0 = q + (x_{0,1} - q_1)(1, -1)$, because both have entries summing to $1$. Finally $\abs{1 - a - b} < 1$ exactly when $0 < a + b < 2$.

15. $S = \begin{pmatrix} 0 & 0 & 1/2 \\ 1 & 0 & 1/2 \\ 0 & 1 & 0 \end{pmatrix}$. Without damping the steady state is $\tfrac15 (1, 2, 2)$, so pages $2$ and $3$ tie. With $\alpha = \tfrac12$ it is $\tfrac{1}{39} (10, 15, 14)$, and page $2$ ranks first.

16. For a column-stochastic $S$, $\sum_i \abs{(Sv)_i} \le \sum_j \abs{v_j}$. If $(I - \alpha S) v = 0$, this gives $\sum \abs{v_j} \le \alpha \sum \abs{v_j}$, so $v = 0$. If $Gr = r$ and the entries of $r$ sum to $1$, then $J r = \mathbf 1$, so $(I - \alpha S) r = \frac{1 - \alpha}{n} \mathbf 1$.

18. The eigenvalue $-1 + 2i$ has the eigenvector $(1, -i)$, and the real part of $e^{(-1 + 2i)t} (1, -i)$ already has the right initial value: $x(t) = e^{-t} (\cos 2t, \sin 2t)$. The point spirals anticlockwise into the origin, at distance $e^{-t}$, going once round every $\pi$ units of time.

20. The two translations cancel, so the student's matrix is $R$, and it sends $(3, 1)$ to $(-1, 3)$. The correct matrix is $T_{(2,1)} R\, T_{(-2,-1)} = \begin{pmatrix} 0 & -1 & 3 \\ 1 & 0 & -1 \\ 0 & 0 & 1 \end{pmatrix}$, which sends $(3, 1)$ to $(2, 2)$.

22. The coordinates are $x \cdot h_0 = 9$, $x \cdot h_1 = -3$, $x \cdot h_2 = -\sqrt 2$ and $x \cdot h_3 = 0$. Keeping $9$ and $-3$ gives $(3, 3, 6, 6)$, and the error $(-1, 1, 0, 0)$ has length $\sqrt 2$.

25. Press the centre and the three lights of the bottom row. The Lights Out matrix of the $3 \times 3$ board has rank $9$ over $\mathbb F_2$, so it is invertible, and every pattern has exactly one solution.

26. The diagonal entries of $A$ are $1$, and $y^{\mathsf T} A y = \sum_i A_{ii} y_i^2 + 2 \sum_{i < j} A_{ij} y_i y_j$. Over $\mathbb F_2$, $y_i^2 = y_i$ and the doubled terms vanish. For a quiet pattern $y$ this gives $\mathbf 1 \cdot y = y^{\mathsf T} A y = 0$, so the all-on pattern is orthogonal to every quiet pattern.

27. The entry of $B^{\mathsf T} x$ for the edge from $i$ to $j$ is $\pm (x_i - x_j)$, and $x^{\mathsf T} L x = \norm{B^{\mathsf T} x}^2$. If $Lx = 0$ then $x^{\mathsf T} L x = 0$, so $x$ takes equal values at the ends of every edge, hence is constant on each component; the indicator vectors of the components form a basis of the null space.

29. The degree of each vertex is $3$ and $A = J - I$, so $L = 4I - J$. Since $J$ has the eigenvalues $4, 0, 0, 0$, $L$ has $0, 4, 4, 4$. The cycle space has dimension $6 - 4 + 1 = 3$, and there are $4 \cdot 4 \cdot 4 / 4 = 16$ spanning trees. The vector $v = \tfrac14 (e_1 - e_2)$ solves $Lv = e_1 - e_2$, so the resistance is $v_1 - v_2 = \tfrac12$.
