1. (a) $A (1, -1, 0) = (1, -1, 0)$, so that line is invariant, with eigenvalue $1$. $A e_3 = (1, 1, 3)$ is not a multiple of $e_3$, so the line spanned by $e_3$ is not invariant. (b) $A e_1 = (2, 1, 0)$ and $A e_2 = (1, 2, 0)$ lie in $U$; the restriction has the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, and $A e_3 \equiv 3 e_3 \pmod U$, so the quotient operator is $(3)$. (c) $p_A = (t - 1)(t - 3) \cdot (t - 3) = (t - 1)(t - 3)^2$.

2. The trace is $7$ and the determinant $12$, so the eigenvalues are $3$ and $4$, with eigenvectors $(1, 1)$ and $(2, 1)$. Take $P = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$ and $D = \operatorname{diag}(3, 4)$.

3. With $P^{-1} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$,
$$A^k = \begin{pmatrix} 2 \cdot 4^k - 3^k & 2 \cdot 3^k - 2 \cdot 4^k \\ 4^k - 3^k & 2 \cdot 3^k - 4^k \end{pmatrix}, \qquad A^3 = \begin{pmatrix} 101 & -74 \\ 37 & -10 \end{pmatrix}.$$

6. The only eigenvalue is $3$, with eigenspace spanned by $(1, -1)$. Since $(A - 3I)^2 = 0$, the generalized eigenspace is $\R^2$. Take $v = (1, 0)$: then $(A - 3I) v = (1, -1)$, and in the basis $(1, -1), (1, 0)$ the matrix of $A$ is $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$.

8. The only eigenvalue is $2$, with eigenvector $(1, 2)$. With $Q = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$ one gets $Q^{-1} A Q = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$. $A$ is not diagonalizable, since $A \ne 2I$ and $2$ is its only eigenvalue.

9. The polynomial $t^3 - t = t (t - 1)(t + 1)$ kills $A$, and its roots $0, 1, -1$ are distinct when $1 \ne -1$, that is, when the characteristic is not $2$. Apply the minimal polynomial test. Over $\mathbb{F}_2$, $A^2 = I$, so $A^3 = A$; but $1$ is the only eigenvalue and $A \ne I$.

11. Both products equal $\begin{pmatrix} 2 & 2 & 2 \\ 4 & 1 & 1 \\ 4 & 1 & 1 \end{pmatrix}$. The eigenspace of $A$ for $2$ is the plane spanned by $e_1$ and $(0, 1, 1)$; $B$ maps this plane to itself, and its eigenvectors there are $(1, 1, 1)$ and $(1, -1, -1)$. Take $P$ with columns $(1, 1, 1)$, $(1, -1, -1)$, $(0, 1, -1)$: then $P^{-1} A P = \operatorname{diag}(2, 2, 0)$ and $P^{-1} B P = \operatorname{diag}(3, -1, 1)$. In the other basis, $B e_1 = (1, 2, 2)$ is not a multiple of $e_1$.

14. (a) $p_A = m_A = (t - 1)^2 (t - 2)$. (b) The projection onto $\ker (A - 2I)$ is $(A - I)^2$ and the projection onto $\ker (A - I)^2$ is $-A (A - 2I) = I - (A - I)^2$:
$$(A - I)^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \qquad I - (A - I)^2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$
(c) $\ker (A - I)^2 = \operatorname{span}(e_1, e_2)$ and $\ker (A - 2I) = \operatorname{span}((0, 1, 1))$.

15. $S$ is $1$ on $\ker (A - I)^2$ and $2$ on $\ker (A - 2I)$, so $S = I + (A - I)^2$:
$$S = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}, \qquad N = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
With $X = A - \operatorname{diag}(1, 1, 2)$, the products $\operatorname{diag}(1, 1, 2) X$ and $X \operatorname{diag}(1, 1, 2)$ differ in the last column: $(-1, 1, 0)$ against $(-2, 2, 0)$.

16. The ranks are $2, 1, 1$, so the chains are constant from $T^2$ on. $\ker T^3 = \operatorname{span}(e_1, (0, 1, 1))$ and $\operatorname{im} T^3 = \operatorname{span}((1, 0, 1))$. On the first, in the basis $e_1, (0, 1, 1)$, $T$ has matrix $\begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix}$, whose square is $0$; on the second, $T$ is multiplication by $-1$.

18. The geometric multiplicities are $5 - 3 = 2$ for both eigenvalues, and the generalized eigenspaces have dimensions $3$ and $2$. Then $\operatorname{rank}(A - 2I)^5 = 5 - 3 = 2$. $A$ is not diagonalizable, since $2 < 3$ for the eigenvalue $2$.

19. $A = \begin{pmatrix} 1 & 6 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $3$ and $-2$. Write $x_k = \alpha 3^k + \beta (-2)^k$ and solve with $x_0, x_1$: $x_k = 3^k + (-2)^k$, and $x_6 = 793$.

21. Let $U$ be invariant of dimension $k$. The restriction $N|_U$ is nilpotent on a $k$-dimensional space, so $N^k$ vanishes on $U$, and $U \subseteq \ker N^k = \operatorname{span}(e_1, \dots, e_k)$. Compare dimensions.

22. $D$ is diagonalizable with eigenspaces $E_1 = \operatorname{span}(e_1, e_2)$ and $E_0 = \operatorname{span}(e_3)$. An invariant subspace is $(W \cap E_1) \oplus (W \cap E_0)$, and conversely every such sum is invariant. The plane $E_1$ has $q + 3$ subspaces ($0$, $q + 1$ lines, itself), and $E_0$ has $2$. For $q = 2$ there are $10$.

23. Triangularize: $A = P U P^{-1}$ with $U$ upper triangular. Add small numbers to the diagonal of $U$ to make its diagonal entries distinct. The perturbed matrix has distinct eigenvalues, and the entries of $P (U + E) P^{-1}$ differ from those of $A$ by at most a constant, depending on $P$, times the largest entry of $E$.

24. Take the Jordan-Chevalley decomposition $T = S + N$. The eigenvalues of $S$ are those of $T$, so $S$ is invertible; put $U = \mathrm{id} + S^{-1} N$, where $S^{-1} N$ is nilpotent because $S^{-1}$ and $N$ commute. For uniqueness, rewrite $T = S U$ as $T = S + S (U - \mathrm{id})$ and use the uniqueness of the additive decomposition.

25. (a) $T|_U$ is injective on the finite-dimensional space $U$, so it is onto $U$. Then $U = T(U)$ gives $T^{-1}(U) = U$. (b) $T(F[x]) = x F[x]$, which misses the constant $1$, and $T^{-1}(1) = x^{-1} \notin F[x]$.
