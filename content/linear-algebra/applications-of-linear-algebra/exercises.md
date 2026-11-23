1. ◦ Balance the combustion of ethane, $a\,\mathrm{C_2H_6} + b\,\mathrm{O_2} \to c\,\mathrm{CO_2} + d\,\mathrm{H_2O}$. Write one equation for each element, find the null space of the $3 \times 4$ coefficient matrix, and give the smallest positive integer solution.

2. ◦ A one-way roundabout has three junctions, met in the order $A$, $B$, $C$. Let $x_1$, $x_2$, $x_3$ be the flows, in cars per hour, on the arcs $A \to B$, $B \to C$ and $C \to A$. At $A$, $400$ cars per hour enter and $100$ leave; at $B$, $200$ enter and $500$ leave; at $C$, $300$ enter and $300$ leave. Write the three conservation equations, solve them in parametric form, and find the smallest possible flow on the arc $A \to B$ if no flow is negative.

3. ◦ A $12\,\mathrm{V}$ battery in series with a $2\,\Omega$ resistor feeds two resistors of $6\,\Omega$ and $3\,\Omega$ connected in parallel. Let $I_1$ be the current through the battery and $I_2$, $I_3$ the currents through the $6\,\Omega$ and $3\,\Omega$ resistors. Write the junction equation and the two loop equations, and solve them.

4. ◦ Find the polynomial $p$ of degree at most $2$ with $p(-1) = 4$, $p(0) = 1$ and $p(2) = 1$, by solving the Vandermonde system. Compute the determinant of the Vandermonde matrix from the product formula, and write down the Lagrange basis polynomial that is $1$ at $t = 0$ and $0$ at $t = -1$ and $t = 2$.

5. • In a two-sector economy, producing one unit of good $1$ uses $0.2$ units of good $1$ and $0.4$ units of good $2$, and producing one unit of good $2$ uses $0.3$ units of good $1$ and $0.1$ units of good $2$. Write the consumption matrix $C$, compute $(I - C)^{-1}$, and find the production $x$ that meets the outside demand $d = (50, 50)$. By how much must each sector raise its output when the outside demand for good $1$ rises by one unit?

6. • Fit the line $y = c_0 + c_1 x$ to the points $(0, 1)$, $(1, 1)$, $(2, 2)$, $(3, 2)$ by least squares. Compute the residual vector, check that it is orthogonal to both columns of the design matrix, and compute $R^2$.

7. • Find the error. A student fits the line through the origin $y = c x$ to the points $(1, 2)$, $(2, 3)$, $(3, 2)$ by least squares, gets $c = 1$, and computes $R^2 = 1 - \norm{r}^2 / \norm{y - \bar y \mathbf 1}^2$. The result is negative, so the student concludes that the fit must contain an arithmetic mistake. Compute this number, and explain what is actually wrong.

8. ★ Let $(x_1, y_1), \dots, (x_m, y_m)$ be real data whose $x_i$ are not all equal, and let $y = \hat c_0 + \hat c_1 x$ be the least-squares line. Prove that the line passes through $(\bar x, \bar y)$, that $\hat c_1 = S_{xy}/S_{xx}$ with $S_{xy} = \sum (x_i - \bar x)(y_i - \bar y)$ and $S_{xx} = \sum (x_i - \bar x)^2$, and that $R^2 = S_{xy}^2 / (S_{xx} S_{yy})$, the square of the correlation coefficient, when the $y_i$ are not all equal.

9. ◦ Let $a_0 = 2$, $a_1 = 1$ and $a_{n+2} = a_{n+1} + 6 a_n$. Write the companion matrix $M$ with $(a_{n+1}, a_{n+2})^{\mathsf T} = M (a_n, a_{n+1})^{\mathsf T}$, find its eigenvalues, and give a closed formula for $a_n$. Check it against $a_5$ computed from the recurrence.

10. • A population has juveniles and adults, counted once a year. Each juvenile produces on average $1$ juvenile and each adult $4$ juveniles in the next count; half of the juveniles survive to become adults, and no adult survives two counts. Write the Leslie matrix $L$, find its eigenvalues and eigenvectors, and give a formula for $x_k = L^k x_0$ when $x_0 = (6, 0)$. What are the long-run growth factor and the long-run ratio of juveniles to adults?

11. • Let $A = \begin{pmatrix} 0.8 & 0.6 \\ 0.3 & 0.5 \end{pmatrix}$ and $x_{k+1} = A x_k$. Find the eigenvalues and eigenvectors, decide whether the origin is an attractor, a repeller or a saddle, and write $x_k$ in closed form for $x_0 = (3, 0)$. For which starting vectors does $x_k \to 0$?

12. ◦ For the column-stochastic matrix $P = \begin{pmatrix} 0.7 & 0.2 \\ 0.3 & 0.8 \end{pmatrix}$, find the eigenvalues, the steady-state vector, and the distribution $x_k = P^k x_0$ for $x_0 = (1, 0)$.

13. • Find the error. Let
$$P = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.$$
A student checks that $P$ is column-stochastic and that $(\tfrac13, \tfrac13, \tfrac13)$ is its only steady-state vector, and concludes that $P^k x_0 \to (\tfrac13, \tfrac13, \tfrac13)$ for every probability vector $x_0$. Show that the conclusion is false, and say which hypothesis of the convergence theorem fails.

14. ★ Let $0 \le a, b \le 1$ with $a + b > 0$, and let $P = \begin{pmatrix} 1 - a & b \\ a & 1 - b \end{pmatrix}$. Show that $q = \frac{1}{a + b} (b, a)$ is the unique steady-state vector, that the other eigenvalue is $1 - a - b$, and that every probability vector $x_0$ satisfies $P^k x_0 = q + (1 - a - b)^k (x_{0,1} - q_1)(1, -1)$. Deduce that $P^k x_0 \to q$ for every $x_0$ unless $a = b = 1$.

15. • Three web pages link as follows: page $1$ links to page $2$, page $2$ links to page $3$, and page $3$ links to pages $1$ and $2$. Write the link matrix $S$, and find the steady-state vector of $S$. Then find the PageRank vector for the damping factor $\alpha = \tfrac12$, that is, the steady-state vector of $G = \tfrac12 S + \tfrac16 J$. Which page ranks first in each case?

16. ★ Let $S$ be an $n \times n$ column-stochastic matrix, $0 < \alpha < 1$, $J$ the $n \times n$ all-ones matrix and $G = \alpha S + \frac{1 - \alpha}{n} J$. Prove that $I - \alpha S$ is invertible, and that the steady-state vector of $G$ is
$$r = \frac{1 - \alpha}{n} (I - \alpha S)^{-1} \mathbf 1.$$

17. ◦ Solve $x' = Ax$ with $A = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$ and $x(0) = (3, 2)$.

18. • Solve $x' = Ax$ with $A = \begin{pmatrix} -1 & -2 \\ 2 & -1 \end{pmatrix}$ and $x(0) = (1, 0)$, as a real function of $t$. Describe the path of $x(t)$ in the plane.

19. ◦ In homogeneous coordinates of the plane, let $T$ be the translation by $(1, 2)$ and $F$ the reflection in the $x$-axis. Write $FT$ and $TF$ as $3 \times 3$ matrices, and find the images of the point $(1, 1)$ under both. Which of the two products means "first translate, then reflect"?

20. • Find the error. To rotate the plane by $90^\circ$ anticlockwise about the point $(2, 1)$, a student uses the matrix $R\, T_{(-2,-1)}\, T_{(2,1)}$, where $R$ is the rotation about the origin and $T_v$ the translation by $v$, in homogeneous coordinates. Compute where the student's matrix sends $(3, 1)$, give the correct matrix, and find the correct image of $(3, 1)$.

21. ◦ With $\omega = e^{-2\pi i/4} = -i$ and $F_{jk} = \omega^{jk}$ for $0 \le j, k \le 3$, compute the discrete Fourier transforms $X = Fx$ of $x = (1, 0, -1, 0)$ and of $x = (0, 1, 0, -1)$. Check that $\norm{X}^2 = 4 \norm{x}^2$ in both cases.

22. • Find the coordinates of $x = (2, 4, 6, 6)$ in the orthonormal Haar basis $h_0 = \tfrac12 (1, 1, 1, 1)$, $h_1 = \tfrac12 (1, 1, -1, -1)$, $h_2 = \tfrac{1}{\sqrt 2} (1, -1, 0, 0)$, $h_3 = \tfrac{1}{\sqrt 2} (0, 0, 1, -1)$. Keep only the two coordinates of largest absolute value, write the compressed vector, and give the length of the error.

23. • Let
$$B = \begin{pmatrix} 2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Find the singular values of $B$, the best approximation $B_1$ of rank $1$, and $\norm{B - B_1}_F$. What share of the energy $\norm{B}_F^2$ does $B_1$ keep, and how many numbers does it take to store $B_1$ as $\sigma_1 u_1 v_1^{\mathsf T}$?

24. ◦ Let $A$ be the adjacency matrix of the $4$-cycle with the edges $12$, $23$, $34$, $41$. Compute $A^2$ and $A^3$, and show that $A^3 = 4A$. How many walks of length $3$ go from vertex $1$ to vertex $2$, and how many from vertex $1$ to vertex $3$? Why does the $4$-cycle have no closed walk of odd length?

25. • On the $3 \times 3$ Lights Out board, with all lights off, find the presses that switch on the top middle light and nothing else. Explain why this set of presses is the only one.

26. ★ Let $A$ be the Lights Out matrix of the $n \times n$ board, over $\mathbb F_2$. Prove that $y^{\mathsf T} A y = \sum_i y_i$ for every $y \in \mathbb F_2^{n^2}$, and deduce that the pattern with all lights on can be switched off on every board.

27. • Let $\Gamma$ be a graph with $n$ vertices, incidence matrix $B$ (for some orientation of the edges) and Laplacian $L = B B^{\mathsf T}$. Prove that $x^{\mathsf T} L x = \sum_{ij} (x_i - x_j)^2$, where the sum runs over the edges, and deduce that $L$ is positive semidefinite and that the dimension of the null space of $L$ is the number of connected components of $\Gamma$.

28. • For the $4$-cycle of Exercise 24, write the Laplacian $L$, find its eigenvalues, and use the matrix-tree theorem to count the spanning trees. Treat each edge as a $1\,\Omega$ resistor and find the effective resistance between two opposite vertices and between two adjacent vertices.

29. ★ For the complete graph $K_4$, show that $L = 4I - J$, find the eigenvalues of $L$, the dimension of the cycle space and the number of spanning trees, and show that the effective resistance between any two vertices is $\tfrac12\,\Omega$ when every edge is a $1\,\Omega$ resistor.
