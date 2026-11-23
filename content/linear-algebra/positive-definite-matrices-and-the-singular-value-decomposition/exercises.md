1. ◦ Classify each real symmetric matrix as positive definite, positive semidefinite but not definite, negative definite, or indefinite:
$$\begin{pmatrix} 1 & 3 \\ 3 & 4 \end{pmatrix}, \qquad \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}, \qquad \begin{pmatrix} -2 & 1 \\ 1 & -3 \end{pmatrix}.$$

2. ◦ For which real numbers $t$ is $\begin{pmatrix} 2 & t \\ t & 8 \end{pmatrix}$ positive definite? For which is it positive semidefinite?

3. ◦ Compute the leading principal minors of $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{pmatrix}$ and decide with [Sylvester's criterion](/0WKEF78PMV/) whether the matrix is positive definite.

4. ◦ Find the singular values of $\begin{pmatrix} 0 & 2 \\ -3 & 0 \end{pmatrix}$ and compare them with the absolute values of its eigenvalues.

5. ◦ Find the singular value of the $1 \times 3$ matrix $A = (1 \ 2 \ 2)$ and its pseudoinverse $A^+$.

6. ◦ True or false? Give a reason or a counterexample for each.
(a) A real symmetric matrix whose entries are all positive is positive definite.
(b) Every diagonal entry of a positive definite matrix is real and positive.
(c) A real $2 \times 2$ matrix whose eigenvalues are both positive satisfies $x^{\mathsf{T}} A x > 0$ for all $x \ne 0$.

7. ◦ Find the error. A student writes: "$A = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}$ is triangular with diagonal $2, 2$, so its singular values are $2$ and $2$." Find the singular values of $A$ and check your answer against $\abs{\det A}$.

8. ◦ Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ and $X = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Which of the four Penrose conditions does $X$ satisfy? Find $A^+$.

9. ◦ Show that every singular value of a unitary matrix equals $1$, and that the singular values of a Hermitian matrix are the absolute values of its eigenvalues.

10. • Find the [Cholesky decomposition](/0WKG8CYY6A/) of
$$A = \begin{pmatrix} 4 & -2 & 4 \\ -2 & 10 & 1 \\ 4 & 1 & 9 \end{pmatrix},$$
and use it to compute $\det A$.

11. • Find the error. A student argues that $A = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{pmatrix}$ is positive definite because it is symmetric, its diagonal entries are positive and $\det A > 0$. Compute $\det A$ and the leading minors, find a vector $x$ with $x^{\mathsf{T}} A x < 0$, and find the eigenvalues of $A$.

12. • Let $A$ be positive definite. Prove that $A$ is invertible and that $A^{-1}$ is positive definite.

13. • Let $A$ be positive semidefinite and $x$ a vector with $x^* A x = 0$. Prove that $A x = 0$. Show by an example that the conclusion fails for a Hermitian matrix that is not semidefinite.

14. • Find the [square root](/EQ98KW1ZN4/) of $A = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix}$, and a real polynomial $p$ of degree at most $1$ with $p(A) = A^{1/2}$.

15. • Find the [polar decomposition](/0J2C7BDJQA/) $A = UP$ of $A = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}$. Check that $UP = PU$ here, and say why this was to be expected.

16. • Find a [singular value decomposition](/000NPTMX6J/) of $A = \begin{pmatrix} 2 & 2 \\ -1 & 1 \end{pmatrix}$.

17. • For the matrix $A$ of exercise 16, find the best rank-one approximation $A_1$ and its error in the operator norm and in the Frobenius norm. Then compute the operator norm error of the rank-one matrix $B = \begin{pmatrix} 2 & 2 \\ -1 & -1 \end{pmatrix}$, which keeps the first row of $A$.

18. • Let $A = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$. Find $A^+$ and check the four Penrose conditions. Then find the least-squares solution of least norm of $Ax = (1, 3)$.

19. • Let $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$. Compute $A^+ = A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1}$ and use it to find the solution of least norm of $x_1 + x_2 = 1$, $x_2 + x_3 = 2$. Check that it is orthogonal to the null space of $A$.

20. • Let $A = \begin{pmatrix} 2 & 2 \\ 2 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$. Find the roots of $\det(A - \lambda B) = 0$ and a real invertible $P$ with $P^{\mathsf{T}} B P = I$ and $P^{\mathsf{T}} A P$ diagonal. What does the result say about the definiteness of $A$?

21. • Let $A$ be a matrix of rank $r \ge 1$. Prove that $\norm{A}_2 \le \norm{A}_F \le \sqrt r \, \norm{A}_2$, and give a matrix for which each inequality is an equality.

22. ★ Let $A$ and $B$ be positive definite $n \times n$ matrices. Show by an example that $AB$ need not be Hermitian. Then prove that $AB$ is always diagonalizable and that its eigenvalues are real and positive.

23. ★ Prove Hadamard's inequality: if $A$ is positive definite, then $\det A \le a_{11} a_{22} \cdots a_{nn}$, with equality exactly when $A$ is diagonal.

24. ★ Let $A$ and $B$ be positive definite $n \times n$ matrices. Prove that $\det(A + B) \ge \det A + \det B$.

25. ★ Let $A$ be an $n \times n$ complex matrix with polar decomposition $A = UP$. Prove that $\norm{A - U}_F \le \norm{A - W}_F$ for every unitary $W$. Find the orthogonal matrix nearest to the matrix of exercise 15 in the Frobenius norm, and the distance.

26. ★ Let $A$ be an $m \times n$ complex matrix. Prove that $(A^* A + \varepsilon I)^{-1} A^*$ exists for every $\varepsilon > 0$ and tends to $A^+$ as $\varepsilon \to 0^+$.
