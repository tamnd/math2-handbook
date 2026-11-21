2. The third row is the sum of the first two and the first two rows are independent, so the rank is $2$. The column space and the row space have dimension $2$, the null space $3$ and the left null space $1$, spanned by $(1, 1, -1)$.

3. The column space of $R$ is not that of $A$. The pivot is in column $1$, so take column $1$ of $A$: $(1, 2)$ is a basis.

5. (a) Similar: both have trace $5$ and determinant $-2$, so the same two distinct eigenvalues, and both are diagonalizable. (b) Not similar: the traces are $5$ and $6$. (c) Not similar: the ranks are $1$ and $0$.

7. $3 + 4 - 5 \le \operatorname{rank}(AB) \le \min(3, 4)$, so the rank is $2$ or $3$.

8. $\operatorname{Null}(A^\top)$ is spanned by $(1, -2, 1)$, so the condition is $b_1 - 2b_2 + b_3 = 0$. The first system is solvable, with $x = (0, 1)$; the second is not.

11. The reduced form is $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ with pivots in columns $1$ and $3$. Column space: $(1, 2, 1)$, $(1, 3, 2)$. Row space: $(1, 2, 0)$, $(0, 0, 1)$. Null space: $(-2, 1, 0)$. Left null space: $(1, -1, 1)$. Then $C$ has columns $(1, 2, 1)$ and $(1, 3, 2)$, and $R$ is the first two rows of the reduced form.

15. On the basis of matrix units, $X \mapsto AXB$ has trace $\operatorname{tr} A \cdot \operatorname{tr} B$: the coefficient of $E_{ij}$ in $A E_{ij} B$ is $a_{ii} b_{jj}$. Hence $X \mapsto AX - XA$ has trace $n \operatorname{tr} A - n \operatorname{tr} A = 0$.

20. The third row is twice the first plus the second, so $(2, 1, -1)$ spans $\operatorname{Null}(A^\top)$, and the condition is $2b_1 + b_2 - b_3 = 0$.

21. If the eigenvalues are distinct, both matrices are similar to the same diagonal matrix. If there is one eigenvalue $\lambda$ and $A \ne \lambda I$, pick $v$ with $(A - \lambda I)v \ne 0$; in the basis $(A - \lambda I)v$, $v$ the matrix is $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$. A multiple of $I$ is similar only to itself.

22. Use matrix units. For $i \ne j$, $E_{ij} = E_{ij} E_{jj}$ and $E_{jj} E_{ij} = 0$, so $f(E_{ij}) = 0$. Also $f(E_{ii}) = f(E_{i1} E_{1i}) = f(E_{1i} E_{i1}) = f(E_{11})$. Take $c = f(E_{11})$.

23. Restrict $A$ to $\operatorname{Col}(B)$ and to its subspace $\operatorname{Col}(BC)$. By rank–nullity, $\operatorname{rank} B - \operatorname{rank}(AB)$ and $\operatorname{rank}(BC) - \operatorname{rank}(ABC)$ are the dimensions of $\ker A \cap \operatorname{Col}(B)$ and $\ker A \cap \operatorname{Col}(BC)$, and the second space lies in the first.

24. $A^2 = 0$ means $\operatorname{Col}(A) \subseteq \operatorname{Null}(A)$, so $r \le n - r$. The matrix with $a_{12} = a_{34} = 1$ and all other entries $0$ has rank $2$.

25. $T$ fixes each $E_{ii}$ and swaps $E_{ij}$ with $E_{ji}$ for $i < j$. So in the basis of matrix units, $T$ is a direct sum of $n$ blocks $(1)$ and $n(n-1)/2$ blocks $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, each of trace $0$ and determinant $-1$.
