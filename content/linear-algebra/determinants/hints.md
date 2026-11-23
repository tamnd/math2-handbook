1. Sarrus: $(-16 - 5 + 0) - (60 + 4 + 0) = -85$. Along the first column: $2 \cdot (-8 - 2) - 0 + 5 \cdot (-1 - 12) = -20 - 65 = -85$.

2. $\det(3A) = 3^4 \cdot (-2) = -162$, $\det(A^{-1}) = -\tfrac{1}{2}$, $\det(\operatorname{adj} A) = (\det A)^{3} = -8$ (take determinants in $A \operatorname{adj} A = (\det A) I_4$), $\det(-A^3) = (-1)^4 (-2)^3 = -8$ and $\det(A^{\mathsf{T}} A) = 4$.

4. The error is to confuse "nonzero" with "a unit". Over $\Z$ the determinant $2$ is not a unit, so there is no integer inverse. Over $\Q$ the inverse is $\begin{pmatrix} 1 & -3/2 \\ -1 & 2 \end{pmatrix}$. Over $\Z/5$, $2^{-1} = 3$, and the inverse is $3 \operatorname{adj} A = \begin{pmatrix} 1 & 1 \\ 4 & 2 \end{pmatrix}$. Over $\Z/2$ the determinant is $0$, so $A$ is not invertible.

9. (a) The edge vectors $(3, 1)$ and $(1, 5)$ give the determinant $14$, so the area is $7$. (b) $\det(u, v, w) = 14$, so the volume is $14/6 = 7/3$. The determinant is positive, so the orientation is the same.

11. Subtract row $n - 1$ from row $n$, then row $n - 2$ from row $n - 1$, and so on up to row $2$. Row $i$ minus row $i - 1$ is $(0, \dots, 0, 1, \dots, 1)$ with the first $1$ in position $i$. The result is upper triangular with ones on the diagonal.

14. Add rows $2$, $3$, $4$ to row $1$, take out the factor $t + 3$, then subtract column $1$ from the other columns: $\det A_t = (t + 3)(t - 1)^3$. The rank is $4$ for $t \ne 1, -3$. For $t = 1$ all entries are $1$ and the rank is $1$. For $t = -3$ the upper left $3 \times 3$ minor is $-16 \ne 0$, so the rank is $3$.

16. $L$ is the composite of $X \mapsto AX$ and $X \mapsto XB$. In the basis $E_{11}, E_{21}, E_{12}, E_{22}$ the first map has the block diagonal matrix with two blocks $A$, so its determinant is $(\det A)^2$; in the basis $E_{11}, E_{12}, E_{21}, E_{22}$ the second has two blocks $B^{\mathsf{T}}$, so its determinant is $(\det B)^2$. Here $\det A = -2$ and $\det B = 3$, so $\det L = 36$.

20. Expand along the first column. The entry $-1$ in position $(2, 1)$ contributes $(-1)^{3} \cdot (-1) \cdot M_{21} = M_{21}$, and $M_{21}$ has first row $(1, 0, \dots, 0)$, so $M_{21} = D_{n-2}$. Then $D_1 = 1 = F_2$ and $D_2 = 2 = F_3$ start the induction.

22. The steps are
$$\begin{pmatrix} 1 & 2 & -2 \\ 1 & 1 & 2 \\ -1 & -5 & 2 \end{pmatrix}, \qquad \begin{pmatrix} -1 & 3 \\ -4 & 4 \end{pmatrix}, \qquad (8),$$
where the second step divides by the interior entries $1, 2, 1, 3$ of the original matrix and the last step by the centre entry $1$ of the first step. The determinant is $8$.

23. If $AB = BA$, then $A^2 + B^2 = (A + iB)(A - iB)$ as complex matrices, and $\det(A - iB)$ is the complex conjugate of $\det(A + iB)$, since $A$ and $B$ are real. So $\det(A^2 + B^2) = \abs{\det(A + iB)}^2$. For the given matrices $A^2 = A$, $B^2 = B$, and $\det(A^2 + B^2) = \det \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} = -1$.

24. Let $E$ be the $n \times n$ matrix with $e_{id} = 1$ if $d \mid i$ and $0$ otherwise, and let $\Phi = \operatorname{diag}(\varphi(1), \dots, \varphi(n))$. Then $G_n = E \Phi E^{\mathsf{T}}$, and $E$ is lower triangular with ones on the diagonal. So $\det G_6 = 1 \cdot 1 \cdot 2 \cdot 2 \cdot 4 \cdot 2 = 32$.

25. Multiply some rows by $-1$ so that the first column consists of ones; this changes only the sign. Subtract row $1$ from each other row. The entries of rows $2, \dots, n$ are now $0$ or $\pm 2$, so a factor $2$ comes out of each of these $n - 1$ rows, and an integer matrix remains.

26. Check that $\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ C & D \end{pmatrix}$, so the determinant is $\det(A - BD^{-1}C) \det D = \det(AD - B D^{-1} C D)$. Now use $D^{-1} C D = C$. In Exercise 17, $CD = E_{11}$ and $DC = E_{22}$.

27. For odd $n$, $\det A = \det A^{\mathsf{T}} = \det(-A) = -\det A$ in $\Z$, so $\det A = 0 = 0^2$. For even $n$, $\det A = (\operatorname{pf} A)^2$, and $\operatorname{pf} A$ is a polynomial in the entries with integer coefficients.

28. If $Ax = 0$ with $x \ne 0$, take $i$ with $\abs{x_i}$ largest. Row $i$ gives $\abs{a_{ii}} \abs{x_i} \le \sum_{j \ne i} \abs{a_{ij}} \abs{x_j} < \abs{a_{ii}} \abs{x_i}$, a contradiction. For the sign, let $D$ be the diagonal part of $A$ and $A(s) = D + s(A - D)$ for $0 \le s \le 1$. Each $A(s)$ is strictly diagonally dominant, so $\det A(s)$ is a polynomial in $s$ with no zero on $[0, 1]$, and $\det A(0) = a_{11} \cdots a_{nn} > 0$.
