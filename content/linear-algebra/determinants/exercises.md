1. ◦ Compute $\det \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & -2 \end{pmatrix}$ by the [rule of Sarrus](/7H2P40X0MV/), and check the value by a [Laplace expansion](/0C08BQ3M05/) along the first column.

2. ◦ Let $A$ be a real $4 \times 4$ matrix with $\det A = -2$. Find $\det(3A)$, $\det(A^{-1})$, $\det(\operatorname{adj} A)$, $\det(-A^3)$ and $\det(A^{\mathsf{T}} A)$.

3. ◦ Compute the determinant of
$$\begin{pmatrix} 1 & 2 & 1 & 0 \\ 2 & 5 & 3 & 1 \\ -1 & 0 & 2 & 4 \\ 3 & 6 & 4 & 3 \end{pmatrix}$$
by reducing it to triangular form with row additions only.

4. ◦ Find the error. A student writes: "The matrix $A = \begin{pmatrix} 4 & 3 \\ 2 & 2 \end{pmatrix}$ has $\det A = 2 \ne 0$, so $A$ is invertible as a matrix over $\Z$." Is $A$ invertible over $\Z$? Over $\Q$? Over $\Z/5$? Over $\Z/2$? Give the inverse whenever it exists.

5. ◦ Use [Cramer's rule](/0977KZ6PQB/) to find $y$ alone, without solving for $x$ and $z$, in the system $x + 2y - z = 2$, $2x - y + z = 3$, $3x + y + 2z = 11$.

6. ◦ Show that $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 3 \end{pmatrix}$ has an inverse with integer entries, and find it with the [adjugate](/07W9H8QF38/).

7. ◦ Compute the $4 \times 4$ [Vandermonde determinant](/0P84B554AS/) whose rows are $(1, x, x^2, x^3)$ for $x = 1, -1, 2, -2$, in this order.

8. ◦ Compute the determinant of
$$\begin{pmatrix} 2 & 1 & 4 & 0 & 7 \\ 1 & 3 & -1 & 5 & 2 \\ 0 & 0 & 1 & 2 & 0 \\ 0 & 0 & 3 & 1 & 1 \\ 0 & 0 & 0 & 2 & 4 \end{pmatrix}.$$

9. ◦ (a) Find the area of the triangle in $\R^2$ with vertices $(1, 2)$, $(4, 3)$ and $(2, 7)$. (b) Find the volume of the tetrahedron in $\R^3$ with vertices $0$, $u = (1, 2, 0)$, $v = (0, 1, 3)$ and $w = (2, 0, 2)$, and decide whether the ordered basis $(u, v, w)$ has the same [orientation](/0QJJAQ6ZYZ/) as the standard basis.

10. • For which integers $k$ is $\begin{pmatrix} k & 1 \\ 1 & k \end{pmatrix}$ invertible as a matrix over $\Z$? For which $k \in \Z/7$ is it invertible over $\Z/7$?

11. • Let $A_n$ be the $n \times n$ matrix with entries $a_{ij} = \min(i, j)$. Prove that $\det A_n = 1$ for every $n \ge 1$.

12. • Use the [Schur complement](/0KA7A4ENVJ/) of the upper left $3 \times 3$ block to compute
$$\det \begin{pmatrix} 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 0 & -1 \\ 1 & 1 & 0 & 5 & 2 \\ 0 & 2 & 1 & 3 & 4 \end{pmatrix}$$
with one $2 \times 2$ determinant.

13. • Let $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \\ 1 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix}$. Compute $\det(I_4 + AB)$ with the [Weinstein–Aronszajn identity](/0G24VQ1088/).

14. • Let $A_t = \begin{pmatrix} t & 1 & 1 & 1 \\ 1 & t & 1 & 1 \\ 1 & 1 & t & 1 \\ 1 & 1 & 1 & t \end{pmatrix}$ with $t \in \R$. Factor $\det A_t$, and find the [rank](/HVHQ50TJB1/) of $A_t$ for every $t$.

15. • Let $A$ be an invertible $n \times n$ matrix over a field, with $n \ge 2$. Prove that $\operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2} A$. Check the formula for $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 3 \\ 1 & 0 & 2 \end{pmatrix}$ by computing $\det A$.

16. • Let $A$ and $B$ be real $2 \times 2$ matrices, and let $L$ be the linear map $X \mapsto AXB$ on the space of real $2 \times 2$ matrices. Prove that the [determinant of the linear map](/0X0HQYSZ0K/) $L$ is $(\det A)^2 (\det B)^2$. Evaluate it for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ -1 & 2 \end{pmatrix}$.

17. • Find the error. A student argues: "For $2 \times 2$ blocks, $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD - BC)$, just as $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$." Disprove this with $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, $C = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $D = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.

18. • Let $A(t) = \begin{pmatrix} t & 1 & 0 \\ 0 & t & 1 \\ 1 & 0 & t \end{pmatrix}$. Compute $\frac{d}{dt} \det A(t)$ once by expanding $\det A(t)$ and once by [Jacobi's formula](/357FEAZ0Q4/).

19. • Let $A$ be the real skew-symmetric $4 \times 4$ matrix with $a_{12} = 2$, $a_{13} = -1$, $a_{14} = 3$, $a_{23} = 4$, $a_{24} = 0$ and $a_{34} = 5$. Compute its [Pfaffian](/NH5HWBPWS9/) and its determinant.

20. • Let $D_n$ be the determinant of the $n \times n$ matrix with $1$ on the diagonal, $1$ just above the diagonal, $-1$ just below it and $0$ elsewhere. Prove that $D_n = D_{n-1} + D_{n-2}$ for $n \ge 3$, and conclude that $D_n = F_{n+1}$, where $F_1 = F_2 = 1$ and $F_{k+1} = F_k + F_{k-1}$.

21. • Let $A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$. Compute $\det(AB)$ by the [Cauchy–Binet formula](/08WE2W7DYS/) as a sum of three products of minors, and check it directly. Without computing $BA$, explain why $\det(BA) = 0$.

22. • Compute the determinant of
$$\begin{pmatrix} 2 & 1 & 0 & 1 \\ 1 & 1 & 2 & 0 \\ 0 & 1 & 3 & 1 \\ 1 & 2 & 1 & 1 \end{pmatrix}$$
by [Dodgson condensation](/RQ44FKS5QM/), writing down the $3 \times 3$ and $2 \times 2$ matrices of the intermediate steps.

23. ★ Let $A$ and $B$ be real $n \times n$ matrices with $AB = BA$. Prove that $\det(A^2 + B^2) \ge 0$. Then show that the hypothesis $AB = BA$ cannot be dropped, using $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$.

24. ★ Let $G_n$ be the $n \times n$ matrix with entries $\gcd(i, j)$. Prove that $\det G_n = \varphi(1) \varphi(2) \cdots \varphi(n)$, where $\varphi$ is Euler's function, and compute $\det G_6$. (Use $\gcd(i, j) = \sum_{d \mid i, \, d \mid j} \varphi(d)$.)

25. ★ Prove that the determinant of every $n \times n$ matrix whose entries are all $1$ or $-1$ is divisible by $2^{n-1}$.

26. ★ Let $A, B, C, D$ be $n \times n$ matrices over a field, with $D$ invertible and $CD = DC$. Prove that $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD - BC)$. Check that the matrices of Exercise 17 do not satisfy $CD = DC$.

27. ★ Prove that the determinant of every skew-symmetric $n \times n$ matrix with integer entries is the square of an integer.

28. ★ A real $n \times n$ matrix $A$ is strictly diagonally dominant when $\abs{a_{ii}} > \sum_{j \ne i} \abs{a_{ij}}$ for every $i$. Prove that such a matrix is invertible. Prove further that if all its diagonal entries are positive, then $\det A > 0$.
