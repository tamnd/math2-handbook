1. ◦ Let $U = \operatorname{span}\set{(1, 0, 1, 0), (0, 1, 0, 1)}$ in $\R^4$ with the dot product. Find a basis of the [orthogonal complement](/0XJXTBCB2T/) $U^\perp$ and check that $\dim U + \dim U^\perp = 4$.

2. ◦ Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$. Find a basis of each of $\operatorname{Row}(A)$, $\operatorname{Nul}(A)$, $\operatorname{Col}(A)$ and $\operatorname{Nul}(A^{\mathsf{T}})$, and check the two orthogonality relations of the [fundamental subspaces](/GQF2KG1R1N/).

3. ◦ Find the matrix $P$ of the [orthogonal projection](/0B8KZRT28M/) of $\R^2$ onto the line $\R(3, 4)$. Compute $P(1, 0)$, the trace of $P$, and check that $P^2 = P$.

4. ◦ Which of these matrices are orthogonal projections of $\R^2$? (a) $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$. (b) $\frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. (c) $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. (d) $\frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$. For each one that is not, say which of $P^2 = P$ and $P^{\mathsf{T}} = P$ fails.

5. ◦ Find the point of the plane $x + y + z = 0$ closest to $b = (1, 2, 3)$, and the distance from $b$ to the plane.

6. ◦ Fit a line $y = st$ through the origin to the points $(1, 1)$, $(2, 3)$, $(3, 4)$ by [least squares](/0BYTQ4X1HC/). Find $s$.

7. ◦ A student argues: "The columns of $A$ are independent, so $A^{\mathsf{T}} A$ is invertible; by symmetry $A A^{\mathsf{T}}$ is invertible too." Give a $2 \times 1$ matrix $A$ that refutes the second claim, and say for which shapes of $A$ the matrix $A A^{\mathsf{T}}$ can be invertible.

8. ◦ Find the [QR decomposition](/0ERWG4NXQ9/) of $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$ with positive diagonal entries in $R$.

9. • Let $U$ and $W$ be subspaces of a finite-dimensional inner product space. Show that $(U + W)^\perp = U^\perp \cap W^\perp$. Then use the [double complement](/0PXN9G4MX1/) to show that $(U \cap W)^\perp = U^\perp + W^\perp$.

10. • Let $P$ be the orthogonal projection onto a subspace $U$ of a finite-dimensional inner product space. Show that $I - P$ is the orthogonal projection onto $U^\perp$, and that $\norm{v}^2 = \norm{P v}^2 + \norm{v - P v}^2$ for every $v$.

11. • Let $U$ be the plane in $\R^3$ spanned by $u_1 = (1, 0, 1)$ and $u_2 = (1, 1, -1)$. Compute the projection of $v = (1, 1, 1)$ onto $U$ in two ways: with the orthogonal basis $u_1, u_2$, and as $v$ minus its component along a normal vector of $U$. Find the distance from $v$ to $U$.

12. • Fit a parabola $y = a + bt + ct^2$ to the points $(-1, 1)$, $(0, 0)$, $(1, 0)$, $(2, 2)$ by the [normal equations](/4D7MRG4D91/). Give $a$, $b$, $c$ and the residual sum of squares.

13. • Show that $\operatorname{Nul}(A^{\mathsf{T}} A) = \operatorname{Nul}(A)$ for every real matrix $A$. Deduce that $A^{\mathsf{T}} A$ is invertible exactly when the columns of $A$ are independent.

14. • Find the [minimum-norm solution](/QM2Y84VDX8/) of the system $x + y + z = 3$, $x - y = 1$, and its norm. Check that it lies in the row space of the coefficient matrix.

15. • Find the thin QR decomposition of $A = \begin{pmatrix} 2 & 6 \\ 1 & -3 \\ 2 & 0 \end{pmatrix}$. Use it to find the least-squares solution of $Ax = (1, 1, 1)$, and check the answer with the normal equations.

16. • Find the [principal angles](/YHVD3773AW/) between the planes $z = 0$ and $x = z$ in $\R^3$, and a pair of principal vectors for each angle.

17. • Let $A = \begin{pmatrix} 1 & 1 \\ \varepsilon & 0 \\ 0 & \varepsilon \end{pmatrix}$ with $\varepsilon > 0$. Find the singular values of $A$, and show that $\kappa(A^{\mathsf{T}} A) = \kappa(A)^2$. Explain what goes wrong when $A^{\mathsf{T}} A$ is formed in arithmetic that rounds $1 + \varepsilon^2$ to $1$.

18. • Let $A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \\ 2 & -2 \end{pmatrix}$ and $b = (1, 0, 1)$. Describe all least-squares solutions of $Ax = b$, and find the one of least norm.

19. • In $C[-1, 1]$ with $\langle f, g \rangle = \int_{-1}^{1} f g \, dx$, find the polynomial $p$ of degree at most $2$ that is closest to $f(x) = x^4$, using [Legendre polynomials](/QFYGJVA996/). Compute $\norm{f - p}^2$.

20. ★ Let $P$ be a linear map of a finite-dimensional inner product space with $P^2 = P$ and $\norm{P v} \le \norm{v}$ for all $v$. Show that $P$ is the orthogonal projection onto its image.

21. ★ In $V = C[-1, 1]$ with $\langle f, g \rangle = \int_{-1}^{1} f g \, dx$, let $U$ be the subspace of polynomials. Use the Weierstrass approximation theorem to show that $U^\perp = \set{0}$. Conclude that $(U^\perp)^\perp \neq U$, and that $V \neq U \oplus U^\perp$.

22. ★ Let $U$ and $W$ be two distinct planes through $0$ in $\R^3$, with normal vectors $n_1$ and $n_2$. Show that their principal angles are $0$ and $\theta$, where $\cos \theta = \abs{n_1 \cdot n_2} / (\norm{n_1} \norm{n_2})$.

23. ★ Prove the uniqueness part of the thin QR decomposition: if $A = Q_1 R_1 = Q_2 R_2$, where $Q_1, Q_2$ have orthonormal columns and $R_1, R_2$ are upper triangular with positive diagonals, then $Q_1 = Q_2$ and $R_1 = R_2$.

24. ★ Among all monic polynomials $p(x) = x^3 + a x^2 + b x + c$, find the one that minimizes $\int_{-1}^{1} p(x)^2 \, dx$, and the minimum value. Explain with best approximation why the answer is a multiple of the Legendre polynomial $P_3$.
