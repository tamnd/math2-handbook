1. Carbon gives $x_1 = x_3$, hydrogen $4x_1 = 2x_4$ and oxygen $2x_2 = 2x_3 + x_4$. With $x_1 = 1$ the solution is $(1, 2, 1, 2)$: $\mathrm{CH_4} + 2\,\mathrm{O_2} \to \mathrm{CO_2} + 2\,\mathrm{H_2O}$.

2. The system is $c_0 = 1$, $c_0 + c_1 + c_2 = 3$, $c_0 + 2c_1 + 4c_2 = 7$, with solution $p(t) = t^2 + t + 1$.

4. Solve $(P - I) q = 0$: $-0.1 q_1 + 0.2 q_2 = 0$, so $q_1 = 2 q_2$, and with $q_1 + q_2 = 1$ the steady state is $(2/3, 1/3)$.

6. $A^2$ has $2$ on the diagonal and $2$ at the opposite pairs $(1, 3)$ and $(2, 4)$, and $A^3 = 4A$. So there are $4$ walks of length $3$ from $1$ to $2$. The trace of $A^3$ is $0$, so there are no triangles.

7. Press the centre and the three cells of the bottom row. The top middle cell is switched once, by the centre; every other cell is switched $0$, $2$ or $4$ times. Since the matrix of the $3 \times 3$ game is invertible over $\mathbb F_2$, this is the only solution without repeated presses.

9. The companion matrix $\begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $2$ and $-1$, so $a_n = \alpha 2^n + \beta (-1)^n$. The initial values give $a_n = \frac13 (2^n - (-1)^n)$.

11. The eigenvalues are $3$ on $(1, 1)$ and $-1$ on $(1, -1)$. Write $x(0) = \frac12 (1, 1) + \frac12 (1, -1)$, so $x(t) = \frac12 e^{3t} (1, 1) + \frac12 e^{-t} (1, -1)$. One positive and one negative eigenvalue make the origin a saddle.

13. The matrix is $G = \begin{pmatrix} 0 & 0 & 1/2 \\ 1 & 0 & 1/2 \\ 0 & 1 & 0 \end{pmatrix}$, and $Gq = q$ gives $q = (1, 2, 2)/5$. The matrix is irreducible and has cycles of lengths $2$ and $3$; computing shows $G^5$ has all entries positive, so by [Perron-Frobenius](/62NS7PV1M9/) the steady state is unique.

14. The coordinates are the dot products $x \cdot h_i$: $9$, $-3$, $-\sqrt2$, $0$. Then $81 + 9 + 2 + 0 = 92 = 4 + 16 + 36 + 36$. Dropping $-\sqrt2$ gives $(3, 3, 6, 6)$ and an error of length $\sqrt2$.

16. The eigenvalues of the Laplacian of $C_4$ are $0$, $2$, $2$, $4$, so there are $2 \cdot 2 \cdot 4 / 4 = 4$ spanning trees, one for each edge removed. Between opposite vertices two paths of resistance $2$ are in parallel, giving $1\ \Omega$. Between adjacent vertices $1\ \Omega$ is in parallel with $3\ \Omega$, giving $\frac34\ \Omega$.

17. The rank of the $16 \times 16$ matrix over $\mathbb F_2$ is $12$, so there are four independent quiet patterns, and a state is solvable exactly when it is orthogonal to all of them. Every quiet pattern has an even number of ones, so the all-ones state passes. There are $2^4 = 16$ solutions. Each press switches at most $5$ lights, so at least $4$ presses are needed, and $4$ suffice: press the cells $(1, 3)$, $(2, 1)$, $(3, 4)$ and $(4, 2)$, whose neighbourhoods cover the board exactly once.

18. The trace is $2 - a - b$ and $1$ is an eigenvalue, so the other is $1 - a - b$, with $\abs{1 - a - b} < 1$. The steady state is $q = \frac{1}{a + b} (b, a)$. Writing $x_0 = q + c\, w$ with $w = (1, -1)$ the second eigenvector gives $P^n x_0 = q + c (1 - a - b)^n w$, so $P^n \to \begin{pmatrix} q & q \end{pmatrix}$.

19. The first normal equation is $\sum (y_i - c_0 - c_1 x_i) = 0$, that is $\bar y = c_0 + c_1 \bar x$. For $R^2$, centre the data: the fitted centred values are $c_1 (x_i - \bar x)$ with $c_1 = S_{xy} / S_{xx}$, so $R^2 = c_1^2 S_{xx} / S_{yy} = S_{xy}^2 / (S_{xx} S_{yy}) = r^2$.

20. The Laplacian is $4I - J$, with eigenvalues $0$ and $4$ (three times). The incidence matrix is $4 \times 6$ of rank $4 - 1 = 3$, so the cycle space has dimension $6 - 3 = 3$. The number of spanning trees is $4 \cdot 4 \cdot 4 / 4 = 16$.
