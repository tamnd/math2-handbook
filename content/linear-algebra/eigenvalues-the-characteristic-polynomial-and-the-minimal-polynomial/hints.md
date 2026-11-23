1. $p_A(t) = t^2 - 5t + 6 = (t - 2)(t - 3)$. The eigenspace for $2$ is spanned by $(1, 1)$, and the one for $3$ by $(2, 1)$.

3. $p(t) = t^2 - 2$ in each case. Over $\Q$ the spectrum is empty, and over $\R$ it is $\set{\sqrt{2}, -\sqrt{2}}$. In $\F_7$, $3^2 = 9 = 2$, so the spectrum is $\set{3, 4}$. In $\F_5$ the squares are $0, 1, 4$, so the spectrum is empty.

5. Expanding along the second row, $p_A(t) = (t - 3)\bigl((t - 1)(t - 3) + 1\bigr) = (t - 2)^2 (t - 3)$. For $2$: algebraic multiplicity $2$, but $\operatorname{rank}(A - 2I) = 2$, so the geometric multiplicity is $1$, with eigenvector $(1, 0, 1)$. For $3$: both multiplicities are $1$, with eigenvector $(0, 1, 0)$. The eigenspaces have dimensions adding up to $2 < 3$, so there is no basis of eigenvectors.

8. Row operations do not preserve eigenvalues; this one keeps the determinant $6$ but changes the trace from $7$ to $5$. In fact $p_A(t) = t^2 - 7t + 6 = (t - 1)(t - 6)$, so the eigenvalues are $1$ and $6$.

9. $p_A(t) = t^3 - 3t^2 + 3t - 2$, so $A(A^2 - 3A + 3I) = 2I$ and
$$A^{-1} = \tfrac{1}{2}(A^2 - 3A + 3I) = \tfrac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}.$$

12. From $Nv = \lambda v$ with $v \ne 0$ follows $0 = N^k v = \lambda^k v$, so $\lambda = 0$. The minimal polynomial divides $t^k$, so it is a power of $t$; since $p_N$ divides $m_N^{\,n}$ and is monic of degree $n$, $p_N = t^n$. Cayley–Hamilton gives $N^n = 0$.

17. Put $N = A - 2I$; the geometric multiplicity is $3 - \operatorname{rank} N$. If $a = b = 0$: it is $3$ and $m_A = t - 2$. If exactly one of $a, b$ is zero: it is $2$, $N \ne 0$ and $N^2 = 0$, so $m_A = (t - 2)^2$. If $a \ne 0$ and $b \ne 0$: it is $1$, and $N^2$ has the entry $ab \ne 0$ in position $(1, 3)$, so $m_A = (t - 2)^3$.

20. The minimal polynomial divides $t^2 + t + 1$, which has no real root, so $A$ has no real eigenvalue; for odd $n$ this contradicts [the result on real maps](/KAV44BRV77/). Over $\C$, the roots of $p_A$ are roots of $m_A$, so they are $\omega$ and $\bar\omega$ with $\omega = e^{2\pi i/3}$. As $p_A$ is real, both occur $n/2$ times, and $\det A = (\omega \bar\omega)^{n/2} = 1$. Example: $\begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}$.

21. If $\lambda_1, \lambda_2, \lambda_3$ are the eigenvalues, then $e_1 = \sum \lambda_i = 3$, $e_2 = \sum_{i<j} \lambda_i \lambda_j = \tfrac{1}{2}(3^2 - 11) = -1$, and Newton's identity $\sum \lambda_i^3 = e_1 \sum \lambda_i^2 - e_2 \sum \lambda_i + 3 e_3$ gives $e_3 = -3$. So $p_A(t) = t^3 - 3t^2 - t + 3 = (t - 3)(t - 1)(t + 1)$, and the eigenvalues are $3, 1, -1$.

23. Over $\C$, $p_A$ splits, and $\operatorname{tr} A^k$ is the $k$-th power sum of its roots. Newton's identities $k e_k = \sum_{i=1}^{k} (-1)^{i-1} e_{k-i} \operatorname{tr}(A^i)$ give $e_1 = \dots = e_n = 0$; this step divides by $k$, which needs characteristic $0$. So $p_A = t^n$, and $A^n = 0$ by Cayley–Hamilton. Over $\F_2$, $I_2$ has $\operatorname{tr} I_2 = \operatorname{tr} I_2^2 = 2 = 0$ and is not nilpotent.

24. From $AX = XB$ follows $f(A) X = X f(B)$ for every polynomial $f$. Take $f = p_A$: then $X p_A(B) = 0$. Since $p_A$ and $p_B$ are coprime, $u p_A + v p_B = 1$ for some $u, v \in F[t]$; evaluating at $B$ and using $p_B(B) = 0$ gives $u(B) p_A(B) = I$, so $p_A(B)$ is invertible and $X = 0$.

25. The characteristic polynomial of $T|_U$ divides $p_T$, so it has $\dim U$ distinct roots, and $T|_U$ has $\dim U$ independent eigenvectors, which are eigenvectors of $T$ in $U$. Each eigenspace of $T$ is a line, so $U$ is the sum of the eigenlines it contains. Distinct sets of eigenlines give distinct sums, and there are $2^n$ sets.

26. $f(M) = \operatorname{diag}(f(A), f(B))$, so $f(M) = 0$ exactly when both $m_A$ and $m_B$ divide $f$. Here $p_A = (t - 2)^2$ and $A \ne 2I$, so $m_A = (t - 2)^2$, while $m_B = (t - 2)(t - 5)$. Hence $m_M = (t - 2)^2 (t - 5)$ and $p_M = (t - 2)^3 (t - 5)$.

27. $P(x_1, x_2, x_3) = (x_3, x_1, x_2)$, so for $\zeta^3 = 1$ the vector $(1, \zeta^2, \zeta)$ is an eigenvector for $\zeta$. Then $C v = f(\zeta) v$ with $f(t) = 1 + 2t + 3t^2$. The eigenvalues are $f(1) = 6$ and $f(\omega) = -2 - \omega$ with its conjugate, and $\det C = 6 \abs{2 + \omega}^2 = 6 \cdot 3 = 18$.

28. $f(L)$ is the map $X \mapsto f(A) X$, which is zero exactly when $f(A) = 0$ (take $X = I$). So $L$ and $A$ have the same annihilating polynomials. In the basis $E_{11}, \dots, E_{n1}, E_{12}, \dots, E_{nn}$, taken column by column, $L$ has the block diagonal matrix with $n$ blocks $A$.
