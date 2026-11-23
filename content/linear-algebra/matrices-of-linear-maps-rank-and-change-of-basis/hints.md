1. Write each image in the basis $C$: $(a, b) = a(1, 1) + (b - a)(0, 1)$. The images $(1, 0)$, $(0, 1)$, $(2, -1)$ give $[T]_{C,E} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 1 & -3 \end{pmatrix}$.

3. The columns $(1, 1, 1)$ and $(1, 2, 3)$ span the plane $b_1 - 2b_2 + b_3 = 0$. The vector $(2, 3, 5)$ is not in it, since $2 - 6 + 5 = 1$. The vector $(1, 0, -1)$ is, and $x = (2, -1)$.

5. Rows $1$ and $3$ are multiples of $(1, 2, 3)$, and row $2$ is a multiple of it exactly when $t = 6$. So the rank is $1$ for $t = 6$ and $2$ otherwise.

6. The determinant is $2$, so the rank over $\R$ is $3$. Over $\mathbb{F}_2$ the determinant is $0$ and the sum of the three rows is $0$, while the first two rows are independent; the rank is $2$.

7. Conjugate by $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which reverses the order of the basis. The determinants are $-2$ and $0$, so the second pair is not similar.

9. $P$ has the new basis vectors as columns, so it turns new coordinates into old ones. The new coordinates are $P^{-1}\binom{3}{4} = \binom{3}{-2}$, and indeed $3(1, 2) - 2(0, 1) = (3, 4)$.

10. The matrix is $\begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{pmatrix}$, with determinant $2$. Solving gives $p = 1 + x^2$.

13. $AB = 0$ says $\operatorname{Col} B \subseteq \operatorname{Null} A$. So $\operatorname{rank} B \le \dim \operatorname{Null} A = n - \operatorname{rank} A$.

16. $\det A = 0$ and $\operatorname{Null} A^{\mathsf{T}} = \R(1, -1, 1)$, so the condition is $b_1 - b_2 + b_3 = 0$. For $b = (1, 5, 4)$ the solutions are $(3, -1, 0) + t(-1, 1, 1)$. For $b = (1, 0, 0)$ the test gives $1 \ne 0$.

18. $BA = A^{-1}(AB)A$. For the counterexample take $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$: then $AB = B \ne 0$ but $BA = 0$, and only $0$ is similar to $0$.

19. Take traces: $\operatorname{tr}(XY - YX) = 0$, while $\operatorname{tr} I = n \cdot 1$. Over $\mathbb{F}_2$, $X = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $Y = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ give $XY - YX = \operatorname{diag}(1, -1) = I$.

20. $A = u\mathbf{1}^{\mathsf{T}} + \mathbf{1}u^{\mathsf{T}}$ with $u = (1, 2, \dots, n)$, a sum of two matrices of rank $1$, so the rank is at most $2$. The top left $2 \times 2$ block $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ has determinant $-1$.

21. Choose a basis of $F^n$ whose last $n - r$ vectors span $\operatorname{Null} A$. The images of the first $r$ vectors are a basis of $\operatorname{Col} A$; extend them to a basis of $F^m$. In these bases the matrix of $x \mapsto Ax$ is the block matrix, and the change of basis formula gives $P$ and $Q$.

22. Use the matrix units $E_{ij}$. For $i \ne j$, $E_{ij} = E_{ii}E_{ij}$ while $E_{ij}E_{ii} = 0$, so $f(E_{ij}) = 0$. Also $E_{ii} = E_{ij}E_{ji}$ and $E_{jj} = E_{ji}E_{ij}$, so $f(E_{ii}) = f(E_{jj}) = c$ for all $i, j$.

23. Apply rank-nullity to the restriction of $x \mapsto Ax$ to $\operatorname{Col} B$: its image is $\operatorname{Col}(AB)$ and its kernel is $\operatorname{Col} B \cap \operatorname{Null} A$. That kernel has dimension at most $\dim \operatorname{Null} A = n - \operatorname{rank} A$.

24. If $A$ is not scalar, some $v$ is not an eigenvector, and $v$, $Av$ is a basis. By the Cayley–Hamilton relation $A^2 = (\operatorname{tr} A)A - (\det A)I$, the matrix of $A$ in this basis is $\begin{pmatrix} 0 & -\det A \\ 1 & \operatorname{tr} A \end{pmatrix}$. The transpose is not scalar either and has the same trace and determinant, so it is similar to the same matrix.

25. Write $A = uv^{\mathsf{T}}$, so $\operatorname{tr} A = v^{\mathsf{T}}u$. If $\operatorname{tr} A \ne 0$, take $u$ followed by a basis of $\operatorname{Null} A = \set{x : v^{\mathsf{T}}x = 0}$. If $\operatorname{tr} A = 0$, then $u \in \operatorname{Null} A$; take $u$, then a vector $w$ with $v^{\mathsf{T}}w = 1$, then $n - 2$ further vectors that complete $u$ to a basis of $\operatorname{Null} A$.
