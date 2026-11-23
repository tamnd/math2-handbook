1. ◦ Let $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x + 2z, y - z)$. Find the [matrix](/0YQSGNYE3K/) $[T]_{C,E}$, where $E$ is the standard basis of $\R^3$ and $C = ((1, 1), (0, 1))$.

2. ◦ Let $S(x, y) = (x + y, y)$ and $T(x, y) = (2x, x - y)$ on $\R^2$. Find the standard matrices of $T \circ S$ and $S \circ T$ as products of matrices, and check one column of each by applying the maps to a basis vector.

3. ◦ Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}$. Find an equation for the [column space](/03AJKXH1AV/) of $A$ in $\R^3$. Is $(2, 3, 5)$ in it? Is $(1, 0, -1)$? If so, solve $Ax = b$.

4. ◦ Find a basis of the [null space](/0PHDYNR24D/) of $A = \begin{pmatrix} 1 & -1 & 0 & 2 \\ 0 & 0 & 1 & -1 \end{pmatrix}$. Then give the dimensions of the four fundamental subspaces of a $5 \times 3$ matrix of rank $2$.

5. ◦ For which real $t$ does $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & t \\ 3 & 6 & 9 \end{pmatrix}$ have rank $1$, and what is its rank otherwise?

6. ◦ Find the rank of $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ over $\R$ and over $\mathbb{F}_2$.

7. ◦ Show that $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$ are [similar](/0E89HQATM8/). Show that $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 5 & 0 \\ 0 & 0 \end{pmatrix}$ are not, although they have the same trace.

8. ◦ Find the [trace](/0KZDNGA561/) of the linear map $X \mapsto X + X^{\mathsf{T}}$ on $M_2(\R)$.

9. ◦ Find the error: "Let $B' = ((1, 2), (0, 1))$ and $P = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$. The coordinates of $v = (3, 4)$ in $B'$ are $P\binom{3}{4} = \binom{3}{10}$." Find the correct coordinates.

10. • Let $T \colon P_2 \to \R^3$, $T(p) = (p(-1), p(0), p(1))$. Find the matrix of $T$ in the basis $(1, x, x^2)$ and the standard basis, show that $T$ is an isomorphism, and find $p$ with $T(p) = (2, 1, 2)$.

11. • Let $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$. Compute $P^{-1}AP$, and say what it tells you about the map $x \mapsto Ax$ in the basis formed by the columns of $P$.

12. • Let $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x + y, y + z)$. Use the [change of basis formula](/0MQXVZEBMT/) to find $[T]_{C',B'}$ for $B' = ((1, 0, 0), (1, 1, 0), (1, 1, 1))$ and $C' = ((1, 0), (1, 1))$, and check one column directly.

13. • Let $A$ be $m \times n$ and $B$ be $n \times p$ with $AB = 0$. Show that $\operatorname{rank} A + \operatorname{rank} B \le n$.

14. • Find the [rank factorization](/5JGAG62VN8/) $A = CR$ of $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \\ 1 & 2 & 0 \end{pmatrix}$, with $C$ made of pivot columns of $A$ and $R$ of the nonzero rows of its reduced row echelon form.

15. • Let $A = uv^{\mathsf{T}}$ with $u, v \in F^n$. Show that $A^2 = (\operatorname{tr} A)A$. Deduce that a matrix of rank $1$ is a projection if and only if its trace is $1$.

16. • Let $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 1 & 1 \\ 1 & -1 & 2 \end{pmatrix}$. Use the [Fredholm alternative](/4HH8C9V8JQ/) to find the condition on $b$ for $Ax = b$ to be solvable. Solve it for $b = (1, 5, 4)$ and show that it has no solution for $b = (1, 0, 0)$.

17. • Find a basis of each of the four fundamental subspaces of $A = \begin{pmatrix} 1 & -1 \\ 2 & -2 \\ -1 & 1 \end{pmatrix}$, and check that the row space and the null space are orthogonal, and so are the column space and the left null space.

18. • Show that if $A$ is invertible, then $AB$ and $BA$ are similar for every $n \times n$ matrix $B$. Give $2 \times 2$ matrices $A$ and $B$ for which $AB$ and $BA$ are not similar.

19. • Show that there are no $n \times n$ matrices $X, Y$ over a field with $XY - YX = I$ when $n \cdot 1 \ne 0$ in the field. Find $2 \times 2$ matrices over $\mathbb{F}_2$ with $XY - YX = I$.

20. • Let $A$ be the $n \times n$ real matrix with entries $a_{ij} = i + j$, where $n \ge 2$. Show that $\operatorname{rank} A = 2$.

21. ★ Let $A$ be an $m \times n$ matrix of rank $r$. Show that there are invertible matrices $Q$ of size $m$ and $P$ of size $n$ with $Q^{-1}AP = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$. Deduce that two $m \times n$ matrices have the same rank exactly when one is $Q^{-1}AP$ for the other.

22. ★ Let $f$ be a linear form on $M_n(F)$ with $f(XY) = f(YX)$ for all $X$ and $Y$. Show that $f = c \operatorname{tr}$ for some $c \in F$.

23. ★ Let $A$ be $m \times n$ and $B$ be $n \times p$. Show that $\operatorname{rank}(AB) = \operatorname{rank} B - \dim(\operatorname{Col} B \cap \operatorname{Null} A)$, and deduce [Sylvester's rank inequality](/GS8WE1ZYV9/) $\operatorname{rank}(AB) \ge \operatorname{rank} A + \operatorname{rank} B - n$.

24. ★ Show that every $2 \times 2$ matrix $A$ over a field is similar to its transpose. (If $A$ is not scalar, find a vector $v$ with $v, Av$ a basis.)

25. ★ Let $A$ be an $n \times n$ matrix of rank $1$. Show that $A$ is similar to $\operatorname{diag}(\operatorname{tr} A, 0, \dots, 0)$ if $\operatorname{tr} A \ne 0$, and to the matrix $E_{12}$ with a single $1$ in position $(1, 2)$ if $\operatorname{tr} A = 0$.
