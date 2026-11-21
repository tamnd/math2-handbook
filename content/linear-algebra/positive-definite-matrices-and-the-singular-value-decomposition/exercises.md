1. ◦ Decide for each real symmetric matrix whether it is positive definite, positive semidefinite but not definite, or neither: $\begin{pmatrix} 3 & 2 \\ 2 & 2 \end{pmatrix}$, $\begin{pmatrix} 1 & 3 \\ 3 & 4 \end{pmatrix}$, $\begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}$.

2. ◦ For which real $t$ is $\begin{pmatrix} 1 & t \\ t & 4 \end{pmatrix}$ positive definite? For which is it positive semidefinite?

3. ◦ Compute the leading principal minors of $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{pmatrix}$ and use [Sylvester's criterion](/0WKEF78PMV/) to decide whether $A$ is positive definite.

4. ◦ Find the [singular values](/09VMDSRXWJ/) of $\begin{pmatrix} 0 & 2 \\ -3 & 0 \end{pmatrix}$ and of the $1 \times 3$ matrix $\begin{pmatrix} 1 & 2 & 2 \end{pmatrix}$.

5. ◦ Write down the [Moore-Penrose inverse](/0YY8VX28JR/) of $\operatorname{diag}(2, 0, -1)$ and of the column vector $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$.

6. ◦ True or false, for real $n \times n$ matrices: (a) every positive definite matrix has positive diagonal entries; (b) every symmetric matrix with positive entries is positive semidefinite; (c) a matrix whose eigenvalues are all positive satisfies $x^T A x > 0$ for all $x \ne 0$. Give a counterexample to each false statement.

7. ◦ Find the positive semidefinite [square root](/EQ98KW1ZN4/) of $\begin{pmatrix} 13 & 12 \\ 12 & 13 \end{pmatrix}$.

8. • Find the [Cholesky decomposition](/0WKG8CYY6A/) of the matrix $A$ of exercise 3. Then show that for every $n$ the $n \times n$ matrix with entries $\min(i, j)$ is $L L^T$, where $L$ is the lower triangular matrix of ones, and deduce that it is positive definite.

9. • Let $A$ be positive definite. Show that $A^{-1}$ is positive definite and that $\det A > 0$. Is $A^2$ positive definite? Is $A + A^{-1}$?

10. • Let $A$ be positive semidefinite and $x^* A x = 0$. Show that $A x = 0$. Give a Hermitian matrix that is not semidefinite for which the conclusion fails.

11. • Find the [polar decomposition](/0J2C7BDJQA/) $A = UP$ of the symmetric matrix $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$. Describe $U$ geometrically.

12. • Find a full [singular value decomposition](/000NPTMX6J/) $A = U \Sigma V^T$ of $A = \begin{pmatrix} 2 & 2 \\ -1 & 1 \end{pmatrix}$.

13. • Show that every singular value of a unitary matrix is $1$, and that the singular values of a Hermitian matrix are the absolute values of its eigenvalues.

14. • Find the pseudoinverse of $J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, check the four Penrose conditions, and find the least-squares solution of smallest norm of $J x = (1, 3)^T$.

15. • Use exercise 12 and the [Eckart-Young-Mirsky theorem](/JJT6GC055J/) to find a best rank-one approximation $A_1$ of $\begin{pmatrix} 2 & 2 \\ -1 & 1 \end{pmatrix}$, and compute $\norm{A - A_1}_2$ and $\norm{A - A_1}_F$.

16. • Let $A = \begin{pmatrix} 2 & 2 \\ 2 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$. Check that $B$ is positive definite, solve $\det(A - \lambda B) = 0$, and find an invertible $P$ with $P^T B P = I$ and $P^T A P$ diagonal, as in the [simultaneous diagonalization theorem](/K559AQ9H67/). Is $A$ positive definite?

17. ★ Let $A$ be positive definite and $B$ Hermitian, both $n \times n$. Show that $AB$ is diagonalizable with real eigenvalues, and that its eigenvalues are positive when $B$ is also positive definite.

18. ★ Prove Hadamard's inequality for positive definite matrices: $\det A \le a_{11} a_{22} \cdots a_{nn}$. Use the Cholesky decomposition. When does equality hold?

19. ★ Let $A$ and $B$ be positive definite $n \times n$ matrices. Prove that $\det(A + B) \ge \det A + \det B$, with equality only for $n = 1$.

20. ★ Let $A$ be an $m \times n$ matrix of rank $r \ge 1$. Prove that $\norm{A}_2 \le \norm{A}_F \le \sqrt r\, \norm{A}_2$, and describe the matrices for which each inequality is an equality.
