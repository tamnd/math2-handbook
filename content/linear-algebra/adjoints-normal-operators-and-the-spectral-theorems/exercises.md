1. ◦ Let $T \colon \R^3 \to \R^3$ be $T(x_1, x_2, x_3) = (x_1 + 2x_2,\ 3x_3,\ x_1 - x_3)$, with the dot product. Find a formula for the [adjoint](/0R9NMSM1ZP/) $T^*(y_1, y_2, y_3)$, and check the identity $\ip{Tx}{y} = \ip{x}{T^*y}$ for $x = (1, 0, 0)$ and $y = (0, 1, 1)$.

2. ◦ For each matrix, decide whether it is Hermitian, skew-Hermitian, or [normal](/0C8BR8XRTR/):
$$A_1 = \begin{pmatrix} 1 & 2 - i \\ 2 + i & -3 \end{pmatrix}, \quad A_2 = \begin{pmatrix} i & 1 \\ -1 & 2i \end{pmatrix}, \quad A_3 = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}, \quad A_4 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad A_5 = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}.$$
For $A_5$, which equals its own transpose, compute $A_5^2$.

3. ◦ Find an orthogonal matrix $Q$ and a diagonal matrix $D$ with $A = QDQ^{\mathsf{T}}$ for $A = \begin{pmatrix} 7 & 2 \\ 2 & 4 \end{pmatrix}$.

4. ◦ Find a unitary matrix $U$ and a real diagonal matrix $D$ with $A = UDU^*$ for the [Hermitian matrix](/0DGZBQWZWN/) $A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$.

5. ◦ Let $A = \begin{pmatrix} 3 & -1 \\ 1 & 1 \end{pmatrix}$ and $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$. Compute $U^{\mathsf{T}}AU$ and check that it is a [Schur form](/V1JG4C7R7B/) of $A$. Compare $\sum_{i,j} \abs{a_{ij}}^2$ with the sum of the squares of the eigenvalues, and explain why $A$ is not normal.

6. ◦ Write $A = \begin{pmatrix} 1 & 2 \\ 2 & -2 \end{pmatrix}$ as $\lambda_1 P_1 + \lambda_2 P_2$ with orthogonal projections $P_1$ and $P_2$, as in the [spectral decomposition](/D5KVBA1K9R/). Use it to compute $A^4$.

7. ◦ Let $A = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 1 \\ 0 & 1 & 4 \end{pmatrix}$. Compute the [Rayleigh quotient](/06WHP8SE98/) of $(1, 1, 1)$ and state the lower bound it gives for the largest eigenvalue. Show that $(1, 0, -1)$ is an eigenvector, and find all three eigenvalues.

8. ◦ Let $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}$. Find $\ker A^{\mathsf{T}}$, and use the relation between the [kernel of the adjoint and the image](/YPP8XT6B7Y/) to decide which of $b = (1, 1, 1)$ and $b = (1, 1, 2)$ lie in the image of $A$.

9. • On the space $P_1$ of real polynomials of degree at most $1$, use $\ip{p}{q} = \int_0^1 p(x)q(x)\,dx$, and let $T(a + bx) = bx$. Find $T^*(1)$ and $T^*(x)$. Explain why the adjoint is not the transpose of the matrix $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ of $T$ in the basis $1, x$, and check your answer with the orthonormal basis $1$, $\sqrt{3}(2x - 1)$.

10. • Let $T$ be a normal operator on a finite-dimensional inner product space $V$. Prove that $\ker T = \ker T^*$ and that $V$ is the orthogonal direct sum of $\ker T$ and $\im T$. Then show that both statements fail for $T = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ on $\R^2$.

11. • Find an orthogonal matrix $Q$ and a diagonal matrix $D$ with $A = QDQ^{\mathsf{T}}$ for
$$A = \begin{pmatrix} 3 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 3 \end{pmatrix}.$$

12. • For the matrix $A$ of Exercise 11, compute the projection $P_4$ onto the eigenspace of $4$ by the product formula $\prod_{j \ne i} (A - \lambda_j I)/(\lambda_i - \lambda_j)$, and check that it equals $vv^{\mathsf{T}}/v^{\mathsf{T}}v$ for an eigenvector $v$. Then compute $A^{-1}$ from the spectral decomposition.

13. • Let $S$ be the matrix of $\R^3$ that swaps the first two coordinates, and let $B = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}$. Check that $SB = BS$ and find one orthonormal basis of eigenvectors for both, as in [simultaneous diagonalization](/BFQQDA489F/). Show that the eigenvectors $(1, 1, 1)$ and $(1, 1, -2)$ of $S$, which form an orthogonal basis of its eigenspace for $1$, are not both eigenvectors of $B$.

14. • Let $A = \begin{pmatrix} 4 & 1 \\ 1 & 1 \end{pmatrix}$. Compute the Rayleigh quotients of $x_0 = (1, 0)$, $x_1 = Ax_0$ and $x_2 = Ax_1$ as fractions. Compare them with the exact largest eigenvalue.

15. • Let $A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix}$. Without computing the characteristic polynomial, use two Rayleigh quotients to show that $A$ has an eigenvalue at least $5$ and an eigenvalue at most $-1$. Conclude that $A$ is neither positive nor negative semidefinite.

16. • Prove that a normal operator on a finite-dimensional complex inner product space whose eigenvalues are all real is self-adjoint. Then show by the example $\begin{pmatrix} 2 & 5 \\ 0 & -1 \end{pmatrix}$ that normality cannot be dropped.

17. • Find the error. A student argues: "The eigenvalues of a self-adjoint operator are real. Conversely, the matrix $B = \begin{pmatrix} 2 & 3 \\ 0 & -1 \end{pmatrix}$ has the real eigenvalues $2$ and $-1$, so by the real spectral theorem it has an orthonormal basis of eigenvectors." Find the eigenvectors of $B$, show that the conclusion is false, and say which step is wrong.

18. • Let $A$ and $B$ be self-adjoint operators on a finite-dimensional inner product space. Prove that $AB$ is self-adjoint if and only if $AB = BA$. Check the statement on $A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

19. • Bring the skew-symmetric matrix $A = \begin{pmatrix} 0 & 1 & 1 \\ -1 & 0 & 1 \\ -1 & -1 & 0 \end{pmatrix}$ to its [real normal form](/G6T1FNE3JC/). Give an orthonormal basis that does it, and the form itself.

20. ★ Let $T$ be a normal operator on a finite-dimensional complex inner product space, and let $\norm{T} = \max\{\norm{Tv} : \norm{v} = 1\}$. Prove that $\norm{T} = \max_i \abs{\lambda_i}$, the largest absolute value of an eigenvalue. Then show that $\norm{A} = 4$ for $A = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}$, whose only eigenvalue is $2$.

21. ★ Let $A$ be a real symmetric $n \times n$ matrix with eigenvalues $\lambda_1 \ge \dots \ge \lambda_n$, and let $B$ be the $(n-1) \times (n-1)$ matrix obtained by deleting the last row and column, with eigenvalues $\mu_1 \ge \dots \ge \mu_{n-1}$. Use the min-max description $\lambda_k = \max_{\dim U = k} \min_{u \in U,\, u \ne 0} R(u)$ to prove the interlacing $\lambda_k \ge \mu_k \ge \lambda_{k+1}$. Check it for the matrix of Exercise 11 by deleting its last row and column.

22. ★ Let $A$ be a real symmetric $n \times n$ matrix with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$. Prove that
$$\lambda_1 + \lambda_2 = \max\set{\ip{Av_1}{v_1} + \ip{Av_2}{v_2} : v_1, v_2 \text{ orthonormal}}.$$
Deduce that the sum of any two diagonal entries of $A$ is at most $\lambda_1 + \lambda_2$, and check this for the matrix of Exercise 11.

23. ★ Let $A$ and $B$ be normal operators on a finite-dimensional complex inner product space with $AB = BA$. Prove that $A + B$ and $AB$ are normal. Then show that $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ are normal while neither $A + B$ nor $AB$ is.
