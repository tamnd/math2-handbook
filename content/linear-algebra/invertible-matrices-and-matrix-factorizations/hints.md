1. $\det A = 1$, so $A^{-1} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$, and $(x, y) = A^{-1}(4, 1)^{\mathsf{T}} = (3, -1)$.

5. Both are upper triangular. The first has a zero on the diagonal, so it is singular. The second is invertible, its inverse has diagonal $1, 1/2, -1$, and the inverse is $\begin{pmatrix} 1 & -2 & -3 \\ 0 & 1/2 & 5/2 \\ 0 & 0 & -1 \end{pmatrix}$.

7. $L = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$, $U = \begin{pmatrix} 2 & 3 \\ 0 & 1 \end{pmatrix}$. For the second matrix, $LU$ has upper left entry $u_{11}$, which must be $0$; then $\det = u_{11}u_{22} = 0$, but the determinant is $-1$.

8. The ranks are $1, 1, 2, 2$, so the first two form one class and the last two another. Over a field the classes of $2 \times 3$ matrices are given by the ranks $0, 1, 2$, so there are three.

11. $A(A - I) = A^2 - A = I$, so $A^{-1} = A - I$, by the [one-sided inverse theorem](/0753Y2X5K6/) or by checking $(A - I)A = I$ directly.

12. If $Bx = 0$ then $ABx = 0$, so $x = 0$; by the [invertible matrix theorem](/ACDFDABVQK/), $B$ is invertible, and then $A = (AB)B^{-1}$ is too. Squareness is used to apply the theorem: the $1 \times 2$ matrix $(1 \ 0)$ times its transpose is $I_1$.

16. One answer is $T_{21}(1)\,T_{12}(1)\,T_{21}(1)$. Reduce the matrix to $I$ with integer row replacements and invert the steps.

18. $L = \begin{pmatrix} 1 & 0 & 0 \\ 1/2 & 1 & 0 \\ 1/2 & 1/2 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 4 & 2 & 2 \\ 0 & 4 & 2 \\ 0 & 0 & 4 \end{pmatrix}$. The minors are $4, 16, 64$, so the pivots are $4, 16/4, 64/16$. Since $U = 4L^{\mathsf{T}}$, $A = L(4I)L^{\mathsf{T}}$.

19. $A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}$, and $M/A = 4 - (1, 1)A^{-1}(1, 2)^{\mathsf{T}} = 2$. So $\det M = 1 \cdot 2 = 2$, and the $(3,3)$ entry of $M^{-1}$ is $(M/A)^{-1} = 1/2$.

22. A central matrix commutes with each $T_{ij}(1) = I + E_{ij}$, so with each $E_{ij}$. Compare entries of $AE_{ij}$ and $E_{ij}A$: this forces $a_{ki} = 0$ for $k \ne i$ and $a_{ii} = a_{jj}$.

23. From $L_1U_1 = L_2U_2$, get $L_2^{-1}L_1 = U_2U_1^{-1}$. The left side is unit lower triangular and the right side upper triangular, so both are diagonal with diagonal $1$, that is, $I$.

24. The Schur complement of $A$ is $-1 - v^{\mathsf{T}}A^{-1}u$, and that of the block $-1$ is $A + uv^{\mathsf{T}}$. Compare the upper left blocks of the two expressions for $M^{-1}$.

25. The first column is any nonzero vector ($q^2 - 1$ choices), the second any vector off the line it spans ($q^2 - q$ choices). The determinant maps $\mathrm{GL}_2(F)$ onto $F^\times$ with kernel $\mathrm{SL}_2(F)$, so divide by $q - 1$. For $q = 3$: $48$ and $24$.

26. Write $A = P^{-1} N_r Q^{-1}$ with the [rank normal form](/T2H2QV0M06/) $N_r = E_{11} + \cdots + E_{rr}$. For the lower bound, the rank of a sum is at most the sum of the ranks.
