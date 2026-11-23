1. The matrix of $T$ is $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 3 \\ 1 & 0 & -1 \end{pmatrix}$, so $T^*$ has the matrix $A^{\mathsf{T}}$ and $T^*(y) = (y_1 + y_3,\ 2y_1,\ 3y_2 - y_3)$. For the given vectors $Tx = (1, 0, 1)$ and $T^*y = (1, 0, 2)$, and both inner products equal $1$.

3. The eigenvalues are $8$ and $3$, with eigenvectors $(2, 1)$ and $(1, -2)$. So $Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}$ and $D = \operatorname{diag}(8, 3)$.

4. The trace is $5$ and the determinant is $6 - \abs{1 - i}^2 = 4$, so the eigenvalues are $4$ and $1$. The eigenvectors $(1 - i, 2)$ and $(1 - i, -1)$ have squared lengths $6$ and $3$, so $U$ has the columns $\frac{1}{\sqrt{6}}(1 - i, 2)$ and $\frac{1}{\sqrt{3}}(1 - i, -1)$, and $D = \operatorname{diag}(4, 1)$.

6. The eigenvalues are $2$ and $-3$, with eigenvectors $(2, 1)$ and $(1, -2)$. So $A = 2P_1 - 3P_2$ with $P_1 = \frac{1}{5}\begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}$ and $P_2 = \frac{1}{5}\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$, and $A^4 = 16P_1 + 81P_2 = \begin{pmatrix} 29 & -26 \\ -26 & 68 \end{pmatrix}$.

9. Work in the orthonormal basis $e_1 = 1$, $e_2 = \sqrt{3}(2x - 1)$. Since $T e_1 = 0$ and $T e_2 = 2\sqrt{3}x = \sqrt{3}e_1 + e_2$, the matrix of $T$ is $\begin{pmatrix} 0 & \sqrt{3} \\ 0 & 1 \end{pmatrix}$, and $T^*$ has its transpose. Converting back gives $T^*(1) = 6x - 3$ and $T^*(x) = 4x - 2$. The basis $1, x$ is not orthonormal, since $\ip{1}{x} = \frac{1}{2}$.

12. $P_4 = \frac{1}{3}(A - I)(A - 3I) = \frac{1}{3}\begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & -1 \\ 1 & -1 & 1 \end{pmatrix}$, which is $vv^{\mathsf{T}}/3$ for $v = (1, -1, 1)$. With $A^{-1} = P_1 + \frac{1}{3}P_3 + \frac{1}{4}P_4$ one gets
$$A^{-1} = \frac{1}{12}\begin{pmatrix} 5 & 3 & 1 \\ 3 & 9 & 3 \\ 1 & 3 & 5 \end{pmatrix}.$$

14. The quotients are $4$, $\frac{73}{17} \approx 4.29412$ and $\frac{1351}{314} \approx 4.30255$. The largest eigenvalue is $\frac{5 + \sqrt{13}}{2} \approx 4.30278$, and every quotient is below it.

17. The eigenvectors are $(1, 0)$ for $2$ and $(1, -1)$ for $-1$, and they are not orthogonal, so no orthonormal eigenbasis exists. The real spectral theorem needs $B$ to be symmetric; the student has used the converse of "self-adjoint implies real eigenvalues", which is false.

19. The kernel is spanned by $(-1, 1, -1)$. On its complement take $u_1 = \frac{1}{\sqrt{2}}(1, 1, 0)$ and $u_2 = \frac{1}{\sqrt{6}}(1, -1, -2)$. Then $Au_1 = \sqrt{3}u_2$ and $Au_2 = -\sqrt{3}u_1$, so in the basis $u_1, u_2, \frac{1}{\sqrt{3}}(-1, 1, -1)$ the matrix is
$$\begin{pmatrix} 0 & -\sqrt{3} & 0 \\ \sqrt{3} & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$

20. In an orthonormal eigenbasis, $v = \sum_i c_i u_i$ gives $\norm{Tv}^2 = \sum_i \abs{\lambda_i}^2\abs{c_i}^2 \le \max_i \abs{\lambda_i}^2 \norm{v}^2$, with equality at an eigenvector. For the example, $\norm{A}^2$ is the largest eigenvalue of $A^{\mathsf{T}}A = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix}$, which is $16$; it is reached at $v = \frac{1}{\sqrt{5}}(1, 2)$.

21. For $\lambda_k \ge \mu_k$, a subspace of $\R^{n-1}$ becomes a subspace of $\R^n$ by adding a last coordinate $0$, and the Rayleigh quotients of $A$ and $B$ agree on it. For $\mu_k \ge \lambda_{k+1}$, intersect the span of the first $k + 1$ eigenvectors of $A$ with the hyperplane $x_n = 0$; the intersection has dimension at least $k$ and $R \ge \lambda_{k+1}$ on it. In the example, $1 \le \frac{5 - \sqrt{5}}{2} \le 3 \le \frac{5 + \sqrt{5}}{2} \le 4$.

22. Expand in an orthonormal eigenbasis $u_1, \dots, u_n$: the sum equals $\sum_i \lambda_i w_i$ with $w_i = \abs{\ip{v_1}{u_i}}^2 + \abs{\ip{v_2}{u_i}}^2$. Bessel's inequality gives $0 \le w_i \le 1$, and $\sum_i w_i = 2$, so the sum is at most $\lambda_1 + \lambda_2$, with equality for $v_j = u_j$. Taking $v_1 = e_i$ and $v_2 = e_j$ gives $a_{ii} + a_{jj} \le \lambda_1 + \lambda_2$. In Exercise 11, $\lambda_1 + \lambda_2 = 7$ and the largest such sum is $3 + 3 = 6$.

23. By [simultaneous diagonalization](/BFQQDA489F/), $A = UD_1U^*$ and $B = UD_2U^*$ with one unitary $U$, so $A + B$ and $AB$ are unitarily diagonalizable, hence normal. In the example $AB = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is nilpotent and nonzero, and $A + B = \begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$ has $(A + B)(A + B)^{\mathsf{T}} \ne (A + B)^{\mathsf{T}}(A + B)$.
