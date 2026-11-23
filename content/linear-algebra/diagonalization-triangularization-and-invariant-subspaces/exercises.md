1. ◦ Let $A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix}$ act on $\R^3$. (a) Is the line spanned by $(1, -1, 0)$ invariant under $A$? Is the line spanned by $e_3$? (b) Show that $U = \operatorname{span}(e_1, e_2)$ is invariant, and write the matrix of the restriction $A|_U$ in the basis $e_1, e_2$ and the matrix of the quotient operator on $\R^3 / U$ in the basis $e_3 + U$. (c) Deduce the characteristic polynomial of $A$.

2. ◦ Diagonalize $A = \begin{pmatrix} 5 & -2 \\ 1 & 2 \end{pmatrix}$ over $\R$: find an invertible $P$ and a diagonal $D$ with $A = P D P^{-1}$.

3. ◦ For the matrix $A$ of Exercise 2, find a formula for every entry of $A^k$, $k \ge 0$, and use it to write down $A^3$.

4. ◦ Decide which of these matrices are diagonalizable over $\R$, and give the reason in each case:
$$\text{(a)} \begin{pmatrix} 1 & 4 & 5 \\ 0 & 2 & 6 \\ 0 & 0 & 3 \end{pmatrix}, \qquad \text{(b)} \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \qquad \text{(c)} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.$$
For (c), answer the same question over $\C$.

5. ◦ A real $3 \times 3$ matrix $A$ satisfies $A^2 - 3A + 2I = 0$ and $\operatorname{tr} A = 4$. Show that $A$ is diagonalizable over $\R$ and find its characteristic polynomial.

6. ◦ Let $A = \begin{pmatrix} 4 & 1 \\ -1 & 2 \end{pmatrix}$. Find its eigenvalue, its eigenspace and its generalized eigenspace. Find a vector $v$ with $(A - 3I) v \ne 0$ and $(A - 3I)^2 v = 0$, and write the matrix of $A$ in the basis $(A - 3I) v, v$.

7. ◦ Show that both matrices are nilpotent and find their indices:
$$N_1 = \begin{pmatrix} 3 & -9 \\ 1 & -3 \end{pmatrix}, \qquad N_2 = \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.$$

8. ◦ Let $A = \begin{pmatrix} 0 & 1 \\ -4 & 4 \end{pmatrix}$. Find an invertible real matrix $Q$ such that $Q^{-1} A Q$ is upper triangular, and decide whether $A$ is diagonalizable over $\R$.

9. • Let $F$ be a field of characteristic different from $2$ and let $A \in M_n(F)$ satisfy $A^3 = A$. Show that $A$ is diagonalizable over $F$ with all eigenvalues in $\set{-1, 0, 1}$. Then show that $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{F}_2$ satisfies $A^3 = A$ and is not diagonalizable over $\mathbb{F}_2$.

10. • Let $u, v \in F^n$ be nonzero column vectors and $A = u v^{\mathsf T}$. (a) Show that $A^2 = (v^{\mathsf T} u) A$. (b) Show that $A$ is diagonalizable over $F$ if and only if $v^{\mathsf T} u \ne 0$. (c) For $u = (1, 2, -1)^{\mathsf T}$ and $v = (3, 1, 1)^{\mathsf T}$ in $\R^3$, give the eigenvalues of $A$ with their algebraic multiplicities and a basis of eigenvectors.

11. • Let
$$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}.$$
Check that $A B = B A$, and find one invertible $P$ such that $P^{-1} A P$ and $P^{-1} B P$ are both diagonal. Show that the basis $e_1, (0, 1, 1), (0, 1, -1)$ diagonalizes $A$ but not $B$.

12. • Let $T$ be an endomorphism of a finite-dimensional space $V$. Show that the following are equivalent: (i) $\ker T \cap \operatorname{im} T = 0$; (ii) $V = \ker T \oplus \operatorname{im} T$; (iii) $\ker T = \ker T^2$. Give a $2 \times 2$ matrix for which all three fail.

13. • Find the error. "Claim: the sum of two diagonalizable $n \times n$ matrices is diagonalizable. Proof: write $A = P D P^{-1}$ and $B = P E P^{-1}$ with $D$ and $E$ diagonal; then $A + B = P (D + E) P^{-1}$." Show that the claim is false with $A = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}$, and state a hypothesis under which the conclusion holds.

14. • Let $A = \begin{pmatrix} 1 & 1 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ over $\R$. (a) Find $p_A$ and $m_A$. (b) Check that $1 = (t - 1)^2 - t (t - 2)$, and use this identity to write the projections of $\R^3$ onto $\ker (A - I)^2$ along $\ker (A - 2I)$ and onto $\ker (A - 2I)$ along $\ker (A - I)^2$ as explicit matrices. (c) Give a basis of each of the two kernels.

15. • For the matrix $A$ of Exercise 14, find the Jordan-Chevalley decomposition $A = S + N$. Show that $\operatorname{diag}(1, 1, 2)$ does not commute with $A - \operatorname{diag}(1, 1, 2)$, so the diagonal of $A$ is not $S$.

16. • Let $T = \begin{pmatrix} -1 & 1 & 0 \\ -1 & 0 & 1 \\ -1 & 1 & 0 \end{pmatrix}$ over $\R$. Find the ranks of $T$, $T^2$ and $T^3$, the Fitting components $\ker T^3$ and $\operatorname{im} T^3$, and the matrix of $T$ on each component in a basis of your choice. Check that the first is nilpotent and the second invertible.

17. • Let $A = \begin{pmatrix} 0 & 3 \\ 1 & 0 \end{pmatrix}$ and let $B$ be the $4 \times 4$ block matrix $\begin{pmatrix} A & I_2 \\ 0 & A \end{pmatrix}$. Decide which of $A$, $A \oplus A$ and $B$ are semisimple over $\Q$, which are diagonalizable over $\Q$, and which are diagonalizable over $\R$.

18. • A real $5 \times 5$ matrix $A$ has $p_A = (t - 2)^3 (t + 1)^2$, $\operatorname{rank}(A - 2I) = 3$ and $\operatorname{rank}(A + I) = 3$. Find the geometric multiplicities of $2$ and $-1$, the dimensions of the two generalized eigenspaces and $\operatorname{rank}(A - 2I)^5$. Is $A$ diagonalizable?

19. • The sequence $x_0 = 2$, $x_1 = 1$, $x_{k+2} = x_{k+1} + 6 x_k$ starts $2, 1, 13, 19, \dots$. Write $v_{k+1} = A v_k$ with $v_k = (x_{k+1}, x_k)$, diagonalize $A$, and find a closed formula for $x_k$. Compute $x_6$.

20. • Let $A \in M_n(\C)$. Show that $A$ is diagonalizable if and only if $\ker (A - \lambda I) = \ker (A - \lambda I)^2$ for every eigenvalue $\lambda$ of $A$.

21. ★ Let $F$ be a field, $n \ge 1$, and let $N$ be the endomorphism of $F^n$ with $N e_1 = 0$ and $N e_i = e_{i-1}$ for $2 \le i \le n$. Show that the $N$-invariant subspaces are exactly $0$ and $\operatorname{span}(e_1, \dots, e_k)$ for $1 \le k \le n$, so there are exactly $n + 1$ of them.

22. ★ Let $q$ be a prime power and $D = \operatorname{diag}(1, 1, 0)$ over $\mathbb{F}_q$. Show that $D$ has exactly $2(q + 3)$ invariant subspaces in $\mathbb{F}_q^3$. How many is that for $q = 2$?

23. ★ Show that the diagonalizable matrices are dense in $M_n(\C)$: for every $A \in M_n(\C)$ and every $\varepsilon > 0$ there is a diagonalizable $B$ with $\abs{a_{ij} - b_{ij}} < \varepsilon$ for all $i, j$.

24. ★ Let $T$ be an invertible endomorphism of a finite-dimensional complex vector space. Show that there is exactly one pair $S, U$ with $T = S U$, $S$ diagonalizable, $U - \mathrm{id}$ nilpotent and $S U = U S$.

25. ★ (a) Let $T$ be an invertible endomorphism of a finite-dimensional space $V$ and let $U$ be $T$-invariant. Show that $T(U) = U$ and that $U$ is $T^{-1}$-invariant. (b) Let $V = F[x, x^{-1}]$ be the space of Laurent polynomials over a field $F$, $T$ the multiplication by $x$, and $U = F[x]$. Show that $T$ is invertible and $U$ is $T$-invariant, but $T(U) \ne U$ and $U$ is not $T^{-1}$-invariant.
