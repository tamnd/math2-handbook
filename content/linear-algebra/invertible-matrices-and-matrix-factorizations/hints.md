1. The determinant is $1$, so the inverse is $\begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$. Then $(x, y) = (2 \cdot 4 - 5 \cdot 1, -4 + 3) = (3, -1)$.

4. $(AB)^{-1} = B^{-1} A^{-1} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$.

6. The product is $\begin{pmatrix} 2 & 1 \\ -6 & -1 \end{pmatrix}$, not $A$. The student stored the row operation $R_2 \to R_2 - 3R_1$ in $L$ instead of its inverse. The correct factor is $L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$, with the same $U$.

7. The determinants are $1$, $-1$, $6$ and $0$. So the first lies in all three groups, the second in $\mathrm{GL}_2(\Z)$ and $\mathrm{GL}_2(\Q)$ but not in $\mathrm{SL}_2(\Z)$, the third only in $\mathrm{GL}_2(\Q)$, and the fourth in none.

10. $L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 1 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 1 & 1 & 2 \\ 0 & 3 & 3 \\ 0 & 0 & 3 \end{pmatrix}$, so the minors are $1$, $3$ and $9$. Forward substitution gives $y = (3, 3, 3)$, and back substitution gives $x = (1, 0, 1)$.

11. $\det A = 1$ and $A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}$. Then $M/A = 4 - (1, 1) A^{-1} (1, 2)^{\mathsf{T}} = 2$ and $\det M = 1 \cdot 2 = 2$. The last row of $M^{-1}$ is $(-S^{-1} C A^{-1}, S^{-1}) = (-2, \tfrac12, \tfrac12)$.

14. The row replacements $R_2 \to R_2 - R_1$, then $R_1 \to R_1 - 2R_2$, then $R_2 \to R_2 - R_1$ reduce the matrix to $I_2$. Inverting them in reverse order gives $\begin{pmatrix} 3 & 2 \\ 4 & 3 \end{pmatrix} = T_{21}(1)\, T_{12}(2)\, T_{21}(1)$.

16. $\det A = -1$, but the leading $2 \times 2$ minor is $0$; if $A = LU$, that minor would be $u_{11} u_{22} = 0$, and then $\det A = u_{11} u_{22} u_{33} = 0$. Exchanging rows 2 and 3 gives $PA = LU$ with $L = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$.

17. The rank is $2$, since row 2 is $-2$ times row 1. One answer is $P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 2 & 1 & 0 \end{pmatrix}$ and $Q = \begin{pmatrix} 1 & 1 & -3 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$; other pairs work too.

20. If $L_1 U_1 = L_2 U_2$ with $A$ invertible, then $U_1$ and $U_2$ are invertible, and $L_2^{-1} L_1 = U_2 U_1^{-1}$. The left side is unit lower triangular and the right side is upper triangular, so both equal $I_n$.

21. The complement of $A$ is the number $1 + v^{\mathsf{T}} A^{-1} u$, and the complement of the corner $(1)$ is $A + uv^{\mathsf{T}}$. So $M$ is invertible exactly when either one is. The upper left block of $M^{-1}$ is $(A + uv^{\mathsf{T}})^{-1}$ by one formula and $A^{-1} - A^{-1} u (1 + v^{\mathsf{T}} A^{-1} u)^{-1} v^{\mathsf{T}} A^{-1}$ by the other.

22. Scalar matrices $cI_n$ with $c \ne 0$ commute with everything. Conversely, if $C$ commutes with $I_n + E_{ij}$ for every $i \ne j$, then $CE_{ij} = E_{ij}C$. Comparing column $j$ of both sides gives $c_{ki} = 0$ for $k \ne i$ and $c_{ii} = c_{jj}$.

23. The product of two unit upper triangular matrices is unit upper triangular, and so is the inverse, by the triangular case. The three entries above the diagonal are free, which gives $p^3$ elements. For $X = T_{12}(1)$ and $Y = T_{23}(1)$, the $(1,3)$ entry of $XY$ is $1$ and that of $YX$ is $0$.

24. Write $A = P^{-1} N_r Q^{-1}$ with $N_r = E_{11} + \dots + E_{rr}$; each $P^{-1} E_{ii} Q^{-1}$ has rank $1$. For the lower bound, use $\operatorname{rank}(B + C) \le \operatorname{rank} B + \operatorname{rank} C$, since the column space of $B + C$ lies in the sum of the column spaces.
