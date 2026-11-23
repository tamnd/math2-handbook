1. The determinants are $-5$, $0$ and $5$. The first matrix is indefinite. The second has trace $13$ and determinant $0$, so it is semidefinite but not definite. The third has positive determinant and negative trace, so both eigenvalues are negative and it is negative definite.

4. $A^{\mathsf{T}} A = \operatorname{diag}(9, 4)$, so the singular values are $3$ and $2$. The eigenvalues of $A$ are $\pm i\sqrt6$, of absolute value $\sqrt6$; the matrix is not normal, and the two lists differ.

7. The singular values are not read off the diagonal of a triangular matrix. Here $A^{\mathsf{T}} A = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix}$ has trace $17$ and determinant $16$, so its eigenvalues are $16$ and $1$, and the singular values are $4$ and $1$. Their product is $4 = \abs{\det A}$.

8. $AX = \operatorname{diag}(1, 0)$, $XA = A$, $AXA = A$ and $XAX = X$. So conditions 1, 2 and 3 hold, and condition 4 fails because $XA$ is not symmetric. Writing $A = u v^{\mathsf{T}}$ with $u = (1, 0)$ and $v = (1, 1)$ gives $A^+ = v u^{\mathsf{T}} / (\norm{u}^2 \norm{v}^2) = \frac12 \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$.

10. Work column by column: $l_{11} = 2$, $l_{21} = -1$, $l_{31} = 2$, then $l_{22} = \sqrt{10 - 1} = 3$, $l_{32} = (1 + 2)/3 = 1$ and $l_{33} = \sqrt{9 - 4 - 1} = 2$. So $L$ has rows $(2, 0, 0)$, $(-1, 3, 0)$ and $(2, 1, 2)$, and $\det A = (2 \cdot 3 \cdot 2)^2 = 144$.

14. The eigenvalues are $16$ and $4$, with eigenvectors $(1, 1)$ and $(1, -1)$, so $A^{1/2} = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$. The polynomial must send $16$ to $4$ and $4$ to $2$, so $p(t) = (t + 8)/6$.

16. $A^{\mathsf{T}} A = \begin{pmatrix} 5 & 3 \\ 3 & 5 \end{pmatrix}$ has eigenvalues $8$ and $2$ with eigenvectors $v_1 = \frac{1}{\sqrt2}(1, 1)$ and $v_2 = \frac{1}{\sqrt2}(-1, 1)$. Then $A v_1 = 2\sqrt2 \, (1, 0)$ and $A v_2 = \sqrt2 \, (0, 1)$, so $\sigma_1 = 2\sqrt2$, $\sigma_2 = \sqrt2$, $U = I$, and $V$ has columns $v_1$ and $v_2$.

18. The matrix has rank one: $A = u v^{\mathsf{T}}$ with $u = (2, 2)$ and $v = (1, 1)$, so $A^+ = v u^{\mathsf{T}} / (\norm{u}^2 \norm{v}^2) = v u^{\mathsf{T}} / 16 = \frac18 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Both $A A^+$ and $A^+ A$ equal $\frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, the projection onto the line of $v$. The answer is $A^+ (1, 3) = (\frac12, \frac12)$.

20. $\det(A - \lambda B) = (2 - \lambda)(1 - 2\lambda) - (2 - \lambda)^2 = (2 - \lambda)(-1 - \lambda)$, so $\lambda = 2$ and $\lambda = -1$. The null vectors $(1, 0)$ and $(-1, 1)$ already have $p^{\mathsf{T}} B p = 1$, so $P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ and $P^{\mathsf{T}} A P = \operatorname{diag}(2, -1)$. One value is negative, so $A$ is indefinite.

22. For the example take $A = \operatorname{diag}(1, 2)$ and $B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$. For the proof, write $AB = A^{1/2} \, (A^{1/2} B A^{1/2}) \, A^{-1/2}$. The middle matrix is positive definite, so $AB$ is similar to a positive definite matrix.

23. Write $A = L L^*$. Then $\det A = \prod_j l_{jj}^2$, while $a_{jj} = \sum_{k \le j} \abs{l_{jk}}^2 \ge l_{jj}^2$. Equality in every $j$ means that $L$, and so $A$, is diagonal.

24. Take $P$ with $P^* B P = I$ and $P^* A P = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, all $\lambda_i > 0$. Then $\det(A + B)$, $\det A$ and $\det B$ are $\prod_i (1 + \lambda_i)$, $\prod_i \lambda_i$ and $1$, each divided by $\abs{\det P}^2$. This reduces the claim to $\prod_i (1 + \lambda_i) \ge 1 + \prod_i \lambda_i$, which holds because the expanded product contains both terms and other nonnegative ones.

25. Expand $\norm{A - W}_F^2 = \norm{A}_F^2 + n - 2 \operatorname{Re} \operatorname{tr}(W^* A)$. With an SVD $A = X \Sigma Y^*$, $\operatorname{tr}(W^* A) = \sum_i \sigma_i z_{ii}$ for the unitary $Z = Y^* W^* X$, and $\abs{z_{ii}} \le 1$; the maximum is at $Z = I$, that is $W = X Y^*$, which is the polar factor. For exercise 15 the nearest orthogonal matrix is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, at distance $\sqrt{10}$.

26. With $A = U \Sigma V^*$, the matrix $A^* A + \varepsilon I = V (\Sigma^{\mathsf{T}} \Sigma + \varepsilon I) V^*$ is positive definite. The product equals $V D_\varepsilon U^*$, where $D_\varepsilon$ has the entries $\sigma_i / (\sigma_i^2 + \varepsilon)$, which tend to $1/\sigma_i$ when $\sigma_i > 0$ and are $0$ when $\sigma_i = 0$.
