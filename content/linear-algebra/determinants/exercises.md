1. ◦ Let $A = \begin{pmatrix} 3 & -1 \\ 5 & 2 \end{pmatrix}$. Compute $\det A$ and $A^{-1}$ with the [2 × 2 formula](/0ZN2J42SK7/), and solve $3x - y = 4$, $5x + 2y = 3$ by Cramer's rule.

2. ◦ Compute the determinant of $\begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & -1 \\ 2 & 4 & 1 \end{pmatrix}$ by the [rule of Sarrus](/7H2P40X0MV/), and check the value by a Laplace expansion along the first row.

3. ◦ Let $A$ be a real $4 \times 4$ matrix with $\det A = 3$. Find $\det(2A)$, $\det(-A)$, $\det(A^{-1})$ and $\det(A^{\mathsf{T}} A^2)$.

4. ◦ Let $A$ be a $3 \times 3$ matrix with $\det A = 5$. The matrix $B$ is made from $A$ in three steps: swap rows $1$ and $3$; multiply the new row $2$ by $-4$; add $7$ times the new row $1$ to the new row $3$. Find $\det B$, using the [effect of row operations](/09YB3WQG38/).

5. ◦ For $A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 3 & 4 \\ 0 & 5 & -2 \end{pmatrix}$, compute the cofactors $C_{21}$, $C_{22}$, $C_{23}$, and then $\det A$ by [Laplace expansion](/0C08BQ3M05/) along row $2$.

6. ◦ Compute the $4 \times 4$ [Vandermonde determinant](/0P84B554AS/) with rows $(1, x, x^2, x^3)$ for $x = -1, 0, 1, 2$, in this order.

7. ◦ Compute $\det \begin{pmatrix} 1 & 2 & 7 & -3 \\ 3 & 4 & 0 & 5 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 5 & 3 \end{pmatrix}$ with the [block triangular rule](/0J9TVTNB4K/).

8. ◦ Decide which of these matrices are invertible over the stated ring, and give the inverse when it exists: (a) $\begin{pmatrix} 3 & 5 \\ 4 & 7 \end{pmatrix}$ over $\Z$; (b) $\begin{pmatrix} 2 & 6 \\ 1 & 4 \end{pmatrix}$ over $\Z$; (c) $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\Z/6$; (d) $\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}$ over $\Z/6$. Use the theorem on [determinants over commutative rings](/03Q7RE2HXR/).

9. ◦ (a) Do the ordered bases $(e_2, e_3, e_1)$ and $(e_3, e_2, e_1)$ of $\R^3$ have the same [orientation](/0QJJAQ6ZYZ/) as $(e_1, e_2, e_3)$? (b) Find the volume of the tetrahedron with vertices $0$, $(1, 0, 2)$, $(2, 1, 0)$ and $(0, 3, 1)$.

10. • Let $K$ be a field in which $2 \ne 0$, and let $A$ be an $n \times n$ matrix over $K$ with $A^{\mathsf{T}} = -A$. Prove that $\det A = 0$ when $n$ is odd. Then give a $1 \times 1$ matrix over $\F_2$ that satisfies $A^{\mathsf{T}} = -A$ and has determinant $1$.

11. • Let $A$ be a real $n \times n$ matrix. Prove: (a) if $A^{\mathsf{T}} A = I$, then $\det A = \pm 1$; (b) if $A^k = 0$ for some $k \ge 1$, then $\det A = 0$; (c) if $A^2 = -I$, then $n$ is even.

12. • Prove that the determinant of every $3 \times 3$ matrix whose entries are all $1$ or $-1$ is divisible by $4$. Give such a matrix with determinant $4$.

13. • Let $d_1, d_2, d_3$ be nonzero and let $M = \operatorname{diag}(d_1, d_2, d_3) + J$, where $J$ is the $3 \times 3$ matrix of ones. Use the [matrix determinant lemma](/0BC3Q6K92H/) to show that $\det M = d_1 d_2 d_3 \left(1 + \frac{1}{d_1} + \frac{1}{d_2} + \frac{1}{d_3}\right)$, and evaluate it for $d = (1, 2, 3)$.

14. • Solve $x + y + z = 6$, $x + 2y + 3z = 14$, $x + 4y + 9z = 36$. Compute the determinant of the coefficient matrix as a Vandermonde determinant, and find $y$ by [Cramer's rule](/0977KZ6PQB/).

15. • Compute $\det \begin{pmatrix} 2 & 0 & 1 & 1 \\ 0 & 2 & 1 & -1 \\ 1 & 1 & 3 & 0 \\ 1 & -1 & 0 & 3 \end{pmatrix}$ with the [Schur complement](/0KA7A4ENVJ/) of the upper left $2 \times 2$ block.

16. • Let $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}$. Compute $\det(AA^{\mathsf{T}})$ in two ways: directly, and by the [Cauchy-Binet formula](/08WE2W7DYS/) as a sum of squares of $2 \times 2$ minors.

17. • Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$. Compute $\det(I_3 + AB)$ by the [Weinstein-Aronszajn identity](/0G24VQ1088/), with a $2 \times 2$ determinant only.

18. • For which real $s$ is the matrix $\begin{pmatrix} 1 & s & 1 \\ s & 1 & 1 \\ 1 & 1 & s \end{pmatrix}$ invertible? For each other value of $s$, find its rank by [minors](/HVHQ50TJB1/).

19. • (a) Let $V$ be the space of real polynomials of degree at most $2$, and let $T(p)(x) = p(1 - x)$. Find the [determinant of the linear map](/0X0HQYSZ0K/) $T$. (b) Let $A$ be a fixed real $2 \times 2$ matrix, and let $L(X) = AX$ on the space of real $2 \times 2$ matrices. Show that $\det L = (\det A)^2$.

20. • Compute the determinant of $\begin{pmatrix} 2 & 1 & 3 \\ 1 & 4 & 1 \\ 3 & 1 & 2 \end{pmatrix}$ by [Dodgson condensation](/RQ44FKS5QM/), and check it by the rule of Sarrus.

21. • Let $A$ be the real skew-symmetric $4 \times 4$ matrix with $a_{12} = 2$, $a_{13} = -1$, $a_{14} = 1$, $a_{23} = 3$, $a_{24} = 0$, $a_{34} = 4$. Compute its [Pfaffian](/NH5HWBPWS9/) and its determinant.

22. ★ Let $D_n$ be the determinant of the $n \times n$ tridiagonal matrix with $3$ on the diagonal, $1$ just above and just below the diagonal, and $0$ elsewhere. Show that $D_n = 3 D_{n-1} - D_{n-2}$ for $n \ge 3$, and prove that $D_n = F_{2n+2}$, where $F_1 = F_2 = 1$ and $F_{k+1} = F_k + F_{k-1}$ are the Fibonacci numbers.

23. ★ Let $A$ and $B$ be real $n \times n$ matrices with $AB = BA$. Prove that $\det(A^2 + B^2) \ge 0$. Then show that the hypothesis $AB = BA$ is needed, with $A = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$.

24. ★ Let $A$ be an $n \times n$ matrix over a field with $n \ge 2$ and $\operatorname{rank} A = n - 1$. Prove that the [adjugate](/07W9H8QF38/) has rank $1$ and that each of its columns lies in $\ker A$.

25. ★ Prove that the determinant of every skew-symmetric integer matrix is the square of an integer. Treat odd and even sizes separately.

26. ★ Let $A$ be an invertible $n \times n$ matrix over a field, with $n \ge 2$. Prove that $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2} A$. Then show that $\operatorname{adj}(\operatorname{adj} A) = A$ for every $2 \times 2$ matrix $A$, invertible or not.
