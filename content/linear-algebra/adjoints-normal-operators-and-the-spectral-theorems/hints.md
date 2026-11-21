2. (a) normal, not Hermitian. (b) and (c) are neither: for (c), $A A^{\mathsf{T}} = \operatorname{diag}(4, 1)$ but $A^{\mathsf{T}} A = \operatorname{diag}(1, 4)$. (d) Hermitian, hence normal. (e) normal, not Hermitian.

4. (a) yes. (b) only when $S T = T S$, since $(S T)^* = T S$. (c) yes. (d) no: $(iT)^* = -iT$, so $iT$ is skew-adjoint. (e) yes.

5. $R(1, 1, 1) = 10/3$ and $R(1, -1, 1) = 2/3$. So $\lambda_{\max} \ge 10/3$ and $\lambda_{\min} \le 2/3$. The eigenvalues are $2 - \sqrt 2$, $2$ and $2 + \sqrt 2$.

6. The eigenvectors are $(1, 0)$ for $2$ and $(1, -1)$ for $-1$, with dot product $1$. The proposition needs $T$ normal, and this matrix is not.

9. In the orthonormal basis $e_0 = 1$, $e_1 = \sqrt 3 (2x - 1)$, $D e_0 = 0$ and $D e_1 = 2 \sqrt 3 \, e_0$. Transpose: $D^* e_0 = 2\sqrt 3 \, e_1$ and $D^* e_1 = 0$. So $D^*(1) = 12x - 6$ and $D^*(x) = 6x - 3$.

12. The only eigenvalue is $2$, with eigenvector $(1, 1)$. With $Q = \frac{1}{\sqrt 2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, $Q^{\mathsf{T}} A Q = \begin{pmatrix} 2 & 2 \\ 0 & 2 \end{pmatrix}$.

14. $\lambda_1 = 9$ with $P_1 = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $\lambda_2 = 1$ with $P_2 = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$. Then $S = 3 P_1 + P_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $A^{-1} = \frac{1}{9} P_1 + P_2 = \frac{1}{9} \begin{pmatrix} 5 & -4 \\ -4 & 5 \end{pmatrix}$.

17. Common eigenvectors: $\frac{1}{\sqrt 2}(1, 0, 1)$, $\frac{1}{\sqrt 2}(1, 0, -1)$ and $(0, 1, 0)$, with eigenvalues $3, 1, 3$ for $A$ and $0, 2, 5$ for $B$. The eigenspace of $A$ for $3$ is a plane, so $\frac{1}{\sqrt 3}(1, 1, 1)$, $\frac{1}{\sqrt 6}(1, -2, 1)$, $\frac{1}{\sqrt 2}(1, 0, -1)$ is also an eigenbasis of $A$; $B$ does not map $(1, 1, 1)$ to a multiple of it.

18. $K^{\mathsf{T}} = -K$, so $A$ and $A^{\mathsf{T}} = I - K$ commute. The eigenvalues are $1$ and $1 \pm 3i$, since $\norm{\omega} = 3$. Take $f_1 = \omega / 3$, $f_2 = \frac{1}{\sqrt 5}(1, 2, 0)$ and $f_3 = f_1 \times f_2$; the matrix is $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -3 \\ 0 & 3 & 1 \end{pmatrix}$.

20. Write the matrix as $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Comparing $A A^{\mathsf{T}}$ and $A^{\mathsf{T}} A$ gives $b^2 = c^2$ and $(a - d)(b - c) = 0$. Then split into the cases $b = c$ and $b = -c \ne 0$.

21. In an orthonormal eigenbasis, $T^k = 0$ forces $\lambda^k = 0$ for every eigenvalue, and $T^2 = T$ forces $\lambda \in \set{0, 1}$; use the spectral decomposition. Counterexamples: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$.

22. By Courant-Fischer, $\lambda_k(A + B)$ is a maximum over $k$-dimensional subspaces $U$ of the minimum of $x^{\mathsf{T}} (A + B) x$ over unit $x \in U$. For each $x$, $x^{\mathsf{T}} (A + B) x \ge x^{\mathsf{T}} A x$, so each minimum, and then the maximum, can only grow.

23. Existence: $S = \sum_j \sqrt{\lambda_j} P_j$. Uniqueness: if $S$ is such a root, then $S$ commutes with $T = S^2$, so it preserves each eigenspace $E_j$ of $T$. On $E_j$ it is self-adjoint with nonnegative eigenvalues and square $\lambda_j I$, so it is $\sqrt{\lambda_j} I$ there.

24. Write $A = Q U Q^*$. The sum $\sum \abs{a_{ij}}^2 = \operatorname{tr}(A^* A)$ does not change under unitary similarity, so it equals $\sum_i \abs{\lambda_i}^2 + \sum_{i < j} \abs{u_{ij}}^2$. Equality means $U$ is diagonal.
