1. ◦ Let $U$ be the span of $(1, 2, -1, 0)$ and $(0, 1, 1, 1)$ in $\R^4$. Find a basis of the [orthogonal complement](/0XJXTBCB2T/) $U^\perp$ and check that $\dim U + \dim U^\perp = 4$.

2. ◦ On the space $P_2$ of real polynomials of degree at most $2$, use the inner product $\ip{p}{q} = \int_0^1 p(x)q(x)\,dx$. Let $U$ be the subspace of constant polynomials. Describe $U^\perp$ by one condition on $p$, give its dimension, and find a basis of the form $x - a$, $x^2 - b$.

3. ◦ Find the orthogonal projection of $v = (3, 3, 0)$ onto the line spanned by $a = (2, -1, 2)$ in $\R^3$, and the distance from $v$ to the line.

4. ◦ Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$. Give a basis of each of the four [fundamental subspaces](/GQF2KG1R1N/) $\operatorname{Row} A$, $\operatorname{Nul} A$, $\operatorname{Col} A$ and $\operatorname{Nul} A^{\mathsf{T}}$, and check the two orthogonality relations. Then use $\operatorname{Nul} A^{\mathsf{T}}$ to decide whether $Ax = (1, 3)$ and $Ax = (2, 4)$ have solutions.

5. ◦ Which of the following are [orthogonal projections](/0B8KZRT28M/) of $\R^2$? For each one that is, name the line it projects onto; for each one that is not, say which condition fails.
$$P_1 = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad P_2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}, \quad P_3 = \frac{1}{10}\begin{pmatrix} 1 & 3 \\ 3 & 9 \end{pmatrix}, \quad P_4 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

6. ◦ Find the [QR decomposition](/0ERWG4NXQ9/) of $A = \begin{pmatrix} 2 & 4 \\ 1 & -1 \\ 2 & 1 \end{pmatrix}$, with $Q$ a $3 \times 2$ matrix with orthonormal columns and $R$ upper triangular with positive diagonal.

7. ◦ Find the [minimum-norm solution](/QM2Y84VDX8/) of the single equation $2x_1 - x_2 + 2x_3 = 18$ and its length. Explain why this length is the distance from the origin to the plane $2x_1 - x_2 + 2x_3 = 18$.

8. ◦ Find the [principal angles](/YHVD3773AW/) between the planes $z = 0$ and $x = z$ in $\R^3$.

9. • Let $U$ be the plane in $\R^3$ spanned by $(1, 0, 1)$ and $(1, 1, 0)$. Compute the matrix of the projection onto $U$ in two ways: as $A(A^{\mathsf{T}}A)^{-1}A^{\mathsf{T}}$, and as $I - \frac{nn^{\mathsf{T}}}{n^{\mathsf{T}}n}$ for a normal vector $n$. Then project $v = (3, 0, 0)$ onto $U$ and find the distance from $v$ to $U$.

10. • Use the QR decomposition of Exercise 6 to find the least-squares solution $\hat x$ of $Ax = b$ for $b = (1, 2, 3)$. Check the answer with the [normal equations](/4D7MRG4D91/), compute the residual $r = b - A\hat x$, and verify that $\norm{b}^2 = \norm{A\hat x}^2 + \norm{r}^2$.

11. • Find the [least-squares](/0BYTQ4X1HC/) line $y = c_0 + c_1 t$ for the points $(-1, 1)$, $(0, 0)$, $(1, 2)$, $(2, 5)$. Give the residuals, check that they add up to $0$, and give the sum of their squares.

12. • Let $P$ and $Q$ be orthogonal projections on a finite-dimensional inner product space. Prove that $PQ$ is an orthogonal projection if and only if $PQ = QP$, and that in this case its image is $\operatorname{im} P \cap \operatorname{im} Q$. Then let $P$ project $\R^2$ onto the $x$-axis and $Q$ onto the line $y = x$, and show that $PQ$ is not even idempotent.

13. • Find the error. To project $v = (1, 2, 3)$ onto the plane spanned by $u_1 = (1, 1, 0)$ and $u_2 = (1, 0, 1)$, a student computes
$$\frac{\ip{v}{u_1}}{\ip{u_1}{u_1}}u_1 + \frac{\ip{v}{u_2}}{\ip{u_2}{u_2}}u_2 = \frac{3}{2}(1, 1, 0) + 2(1, 0, 1) = \left(\tfrac{7}{2}, \tfrac{3}{2}, 2\right).$$
Show that the answer is wrong by a test that does not need the correct answer, and then find the correct projection.

14. • On the space of real $2 \times 2$ matrices take $\ip{A}{B} = \tr(A^{\mathsf{T}}B)$. Show that the symmetric matrices and the skew-symmetric matrices are orthogonal complements of each other. Find the symmetric matrix closest to $A = \begin{pmatrix} 1 & 4 \\ 0 & 3 \end{pmatrix}$ and the distance from $A$ to the symmetric matrices.

15. • On the polynomials with $\ip{p}{q} = \int_{-1}^{1} p(x)q(x)\,dx$, find the polynomial of degree at most $2$ closest to $x^4$, using the Legendre polynomials $1$, $x$ and $\frac{1}{2}(3x^2 - 1)$. Give the squared distance as a fraction.

16. • On the continuous functions on $[-\pi, \pi]$ with $\ip{f}{g} = \int_{-\pi}^{\pi} f(x)g(x)\,dx$, find the function of the form $a_0 + a_1\cos x + b_1\sin x$ closest to $f(x) = x^2$, and the squared distance in closed form.

17. • Find all solutions of $x_1 + x_2 + x_3 = 3$, $x_1 - x_3 = 2$. Show that exactly one of them lies in the row space of the coefficient matrix, that it is the shortest, and that it equals $A^{\mathsf{T}}(AA^{\mathsf{T}})^{-1}b$.

18. • In $\R^4$ let $U$ be the span of $e_1$ and $e_2$, and $W$ the span of $(1, 1, 1, 1)$ and $(1, -1, 1, -1)$. Find the principal angles between $U$ and $W$, and show that every unit vector of $U$ makes the same angle with $W$.

19. • Find the error. To solve the inconsistent system $x_1 = 2$, $x_2 = 1$, $x_1 - x_2 = 0$ by least squares, a student drops the last equation, which is the only one that fails, and answers $(x_1, x_2) = (2, 1)$. Find the least-squares solution and compare the two sums of squared errors.

20. ★ Let $P$ be an operator on a finite-dimensional inner product space with $P^2 = P$ and $\norm{Pv} \le \norm{v}$ for all $v$. Prove that $P$ is the orthogonal projection onto its image. Show by an example that the inequality cannot be dropped.

21. ★ Let $u_1, \dots, u_k$ be linearly independent vectors in a real inner product space, $U$ their span, and $G(w_1, \dots, w_j)$ the Gram matrix with entries $\ip{w_i}{w_l}$. Prove that for every $v$
$$d(v, U)^2 = \frac{\det G(u_1, \dots, u_k, v)}{\det G(u_1, \dots, u_k)}.$$
Check the formula on the data of Exercise 9.

22. ★ Let $V$ be the space of real sequences with only finitely many nonzero terms, with $\ip{x}{y} = \sum_n x_n y_n$, and let $U = \set{x \in V : \sum_n x_n / n = 0}$. Prove that $U^\perp = \set{0}$. Deduce that $V \neq U \oplus U^\perp$ and $(U^\perp)^\perp \neq U$, and say which hypothesis of the [orthogonal decomposition](/0SP7P0G7KQ/) theorem fails.

23. ★ Let $A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \\ 2 & -2 \end{pmatrix}$ and $b = (1, 2, 3)$. Show that the least-squares solutions of $Ax = b$ are exactly the $x$ with $x_1 - x_2 = \frac{5}{6}$. Prove that, for any real matrix, exactly one least-squares solution lies in the row space and that it is the shortest, and find it here.
