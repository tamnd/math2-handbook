1. ◦ Let $T \colon \R^3 \to \R^2$ be $T(x_1, x_2, x_3) = (x_1 + 2x_2, \, 3x_3 - x_1)$, with the dot products. Find the [adjoint](/0R9NMSM1ZP/) $T^*(y_1, y_2)$.

2. ◦ Which of these matrices are normal, and which are Hermitian? (a) $\begin{pmatrix} 2 & -3 \\ 3 & 2 \end{pmatrix}$. (b) $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$. (c) $\begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$. (d) $\begin{pmatrix} 1 & i \\ -i & 2 \end{pmatrix}$. (e) $\begin{pmatrix} i & 0 \\ 0 & 2 \end{pmatrix}$.

3. ◦ Find the eigenvalues of $A = \begin{pmatrix} 10 & 12 \\ 12 & 17 \end{pmatrix}$ and an orthogonal matrix $Q$ with $Q^{\mathsf{T}} A Q$ diagonal.

4. ◦ Let $S$ and $T$ be [self-adjoint](/0NEGN5CRSC/) operators on a complex inner product space. Which of these are always self-adjoint? (a) $T^2$. (b) $S T$. (c) $S T + T S$. (d) $i T$. (e) $R + R^*$, for an arbitrary operator $R$.

5. ◦ Let $A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$. Compute the [Rayleigh quotient](/06WHP8SE98/) at $(1, 1, 1)$ and at $(1, -1, 1)$, and state the bounds they give on the largest and the smallest eigenvalue of $A$.

6. ◦ Find the error: "The matrix $\begin{pmatrix} 2 & 3 \\ 0 & -1 \end{pmatrix}$ has the distinct eigenvalues $2$ and $-1$, so by the [orthogonality of eigenspaces](/0JHGAV9H25/) its eigenvectors are orthogonal." Compute the eigenvectors and name the missing hypothesis.

7. ◦ A self-adjoint operator $T$ on $\R^3$ has the eigenvalues $1$, $2$, $2$, and the eigenspace for $1$ is $\R(1, 1, 0)$. Find the eigenspace for $2$ and the matrix of $T$ in the standard basis.

8. ◦ Find the eigenvalues of the Hermitian matrix $\begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$ and an eigenvector for each, and check that the two eigenvectors are orthogonal.

9. • On $\mathcal{P}_1(\R)$, the polynomials of degree at most $1$, take $\langle p, q \rangle = \int_0^1 p q \, dx$ and $D p = p'$. Find $D^*(1)$ and $D^*(x)$, and check one case of $\langle D p, q \rangle = \langle p, D^* q \rangle$.

10. • On $\R^2$ take $\langle x, y \rangle = x^{\mathsf{T}} M y$ with $M = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$. Show that the adjoint of $x \mapsto A x$ is $y \mapsto M^{-1} A^{\mathsf{T}} M y$, and compute it for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

11. • Let $T \colon V \to W$ be linear between finite-dimensional inner product spaces. Show that $T^* T$ is self-adjoint, that $\ker T^* T = \ker T$, and that every eigenvalue of $T^* T$ is a real number $\ge 0$.

12. • Find a [Schur decomposition](/V1JG4C7R7B/) $A = Q U Q^{\mathsf{T}}$ of $A = \begin{pmatrix} 3 & -1 \\ 1 & 1 \end{pmatrix}$ with $Q$ real orthogonal and $U$ upper triangular.

13. • Orthogonally diagonalize $A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$. (Try the vectors $(1, c, 1)$ and $(1, 0, -1)$.)

14. • Let $A = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$. Write its [spectral decomposition](/D5KVBA1K9R/) $\lambda_1 P_1 + \lambda_2 P_2$, and use it to find a symmetric matrix $S$ with positive eigenvalues and $S^2 = A$, and the inverse $A^{-1}$.

15. • Let $T$ be a normal operator on a finite-dimensional complex inner product space. Use the [complex spectral theorem](/04CW1P44VD/) to show: (a) if every eigenvalue of $T$ is real, then $T$ is self-adjoint; (b) if every eigenvalue has absolute value $1$, then $T^* T = I$.

16. • Let $T$ be [normal](/0C8BR8XRTR/). Show that $\norm{T v} = \norm{T^* v}$ for every $v$. Deduce that $\ker T = \ker T^*$, and that $T v = \lambda v$ implies $T^* v = \overline{\lambda} v$.

17. • Let $A = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 5 & 0 \\ -1 & 0 & 1 \end{pmatrix}$. Check that $A B = B A$, and find an orthonormal basis of $\R^3$ of common eigenvectors. Give an orthonormal eigenbasis of $A$ that does not diagonalize $B$.

18. • Let $\omega = (2, -1, 2)$, let $K$ be the matrix of $x \mapsto \omega \times x$, and let $A = I + K$. Show that $A$ is normal, find its eigenvalues, and find an orthonormal basis in which $A$ has the [real normal form](/G6T1FNE3JC/).

19. • Let $A$ be a real symmetric matrix. Show that every diagonal entry satisfies $\lambda_{\min} \le a_{ii} \le \lambda_{\max}$. Deduce that $\begin{pmatrix} 1 & 2 & 3 \\ 2 & -1 & 0 \\ 3 & 0 & 5 \end{pmatrix}$ has an eigenvalue $\le -1$ and an eigenvalue $\ge 5$.

20. ★ Show that a real $2 \times 2$ matrix is normal if and only if it is symmetric or has the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.

21. ★ Let $T$ be a normal operator on a finite-dimensional complex inner product space. Show that if $T^k = 0$ for some $k \ge 1$, then $T = 0$, and that if $T^2 = T$, then $T$ is an orthogonal projection. Give examples showing that both claims fail without normality.

22. ★ Let $A$ and $B$ be real symmetric $n \times n$ matrices, with $x^{\mathsf{T}} B x \ge 0$ for all $x$. List the eigenvalues in decreasing order. Use the [Courant-Fischer theorem](/CJK2HS2508/) to show that $\lambda_k(A + B) \ge \lambda_k(A)$ for every $k$.

23. ★ Let $T$ be self-adjoint with $\langle T v, v \rangle \ge 0$ for all $v$. Show that there is exactly one self-adjoint $S$ with $\langle S v, v \rangle \ge 0$ for all $v$ and $S^2 = T$.

24. ★ Let $A$ be a complex $n \times n$ matrix with eigenvalues $\lambda_1, \dots, \lambda_n$, repeated by multiplicity. Use the Schur decomposition to show that $\sum_i \abs{\lambda_i}^2 \le \sum_{i,j} \abs{a_{ij}}^2$, with equality if and only if $A$ is normal.
