1. The first is positive definite: its leading minors are $3$ and $2$. The second is neither: its determinant is $-5$, so it has a negative eigenvalue. The third is positive semidefinite but not definite: its eigenvalues are $13$ and $0$.

4. $A^T A = \operatorname{diag}(9, 4)$ for the first matrix, so the singular values are $3$ and $2$. For the row vector, $A A^T = (9)$, so the only singular value is $3$, the length of the row.

5. $\operatorname{diag}(1/2, 0, -1)$: invert the nonzero diagonal entries and keep the zero. For a nonzero column $a$, $a^+ = a^T / (a^T a)$, here $\frac{1}{25}\begin{pmatrix} 3 & 4 \end{pmatrix}$.

6. (a) True: $a_{ii} = e_i^T A e_i > 0$. (b) False: $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ has determinant $-1$. (c) False without symmetry: $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ has only the eigenvalue $1$, but $x^T A x = -2$ at $x = (1, -1)$.

7. The eigenvalues are $25$ and $1$, with eigenvectors $(1, 1)$ and $(1, -1)$. Take square roots of the eigenvalues: $\begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix}$.

8. $L = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix}$. In general $(L L^T)_{ij}$ counts the indices $k$ with $k \le i$ and $k \le j$, which is $\min(i, j)$. Since $L$ is invertible, $x^T L L^T x = \norm{L^T x}^2 > 0$ for $x \ne 0$.

11. $A^T A = A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$, so $P = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $U = A P^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the reflection in the line $x_1 = x_2$. For a symmetric matrix, $P$ is $A$ with its eigenvalues replaced by their absolute values.

12. $A^T A = \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix}$ has eigenvalues $8$ and $2$, with $v_1 = (1, 1)/\sqrt 2$ and $v_2 = (1, -1)/\sqrt 2$. Then $u_i = A v_i / \sigma_i$ gives $u_1 = (1, 0)$ and $u_2 = (0, -1)$, and $\Sigma = \operatorname{diag}(2\sqrt 2, \sqrt 2)$.

16. Factor: $\det(A - \lambda B) = (2 - \lambda)(-1 - \lambda)$, so $\lambda = 2, -1$. Solving $(A - \lambda B) p = 0$ gives $p_1 = (1, 0)$ and $p_2 = (-1, 1)$, already $B$-orthonormal, so $P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ and $P^T A P = \operatorname{diag}(2, -1)$. Since one $\lambda$ is negative, $A$ is indefinite.

17. Write $AB = A^{1/2} (A^{1/2} B A^{1/2}) A^{-1/2}$. So $AB$ is similar to the Hermitian matrix $A^{1/2} B A^{1/2}$, and this matrix is positive definite when $B$ is, by the Gram matrix test.

18. With $A = L L^*$, $\det A = \prod l_{ii}^2$ and $a_{ii} = \sum_{j \le i} \abs{l_{ij}}^2 \ge l_{ii}^2$. Equality holds exactly when $L$ is diagonal, that is, when $A$ is diagonal.

19. Choose $P$ with $P^* A P = I$ and $P^* B P = D = \operatorname{diag}(d_1, \dots, d_n)$, all $d_i > 0$. Since $\det A = \abs{\det P}^{-2}$, $\det B = \abs{\det P}^{-2} \prod d_i$ and $\det(A + B) = \abs{\det P}^{-2} \prod (1 + d_i)$, the claim is $\prod (1 + d_i) \ge 1 + \prod d_i$. Expand the product: it contains these two terms and other positive terms when $n \ge 2$.

20. Use $\norm{A}_2 = \sigma_1$ and $\norm{A}_F^2 = \sigma_1^2 + \cdots + \sigma_r^2$. The left inequality is an equality exactly when $r = 1$. The right one is an equality exactly when all nonzero singular values are equal, that is, when $A = c W$ for some $c > 0$ and some $W$ whose nonzero singular values are all $1$.
