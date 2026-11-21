1. (a) Yes: it is $3x - \sqrt 2\, y - z = 1$. (b) No: $xy$ is a product of unknowns. (c) Yes: $\sin(\pi/4)$ is a constant. (d) No.

2. $A$ is in reduced row echelon form. $B$ is in row echelon form but not reduced, since its second leading entry is $2$ and there is a $3$ above it. $C$ is in neither, since the leading entry of row $2$ is to the left of that of row $1$. $D$ is in row echelon form but not reduced, because of the $5$ above the third leading entry.

4. The pivot columns are $1$, $2$ and $4$, and $x_3$ is free. With $x_3 = t$, the solutions are $(3 - 2t,\ 1 + t,\ t,\ 2)$ for $t \in \R$.

5. (a) Yes; it undoes itself. (b) Yes; it undoes itself. (c) No: the factor must be nonzero. (d) No: in a replacement $R_i \leftarrow R_i + cR_j$ the rows must differ, and this one turns $R_3$ into a zero row that no operation can restore. (e) Yes; it is undone by $R_1 \leftarrow R_1 - 2R_3$.

6. Consistent exactly when $h = 0$. Then $x_3$ is free, so there are infinitely many solutions.

11. The reduced row echelon form of the augmented matrix is $\left[\begin{array}{rrrr|r} 1 & 2 & 0 & 2 & 3 \\ 0 & 0 & 1 & 1 & 2 \end{array}\right]$, with $x_2 = s$ and $x_4 = t$ free. So $p = (3, 0, 2, 0)$, and $N$ has the basis $(-2, 1, 0, 0)$, $(-2, 0, -1, 1)$.

12. Elimination gives the rows $(1, 1, 1 \mid 1)$, $(0, 1, a - 1 \mid 1)$ and $(0, 0, 3 - a \mid b - 3)$. For $a \neq 3$ there is exactly one solution. For $a = 3$ and $b \neq 3$ there is none. For $a = 3$ and $b = 3$ there are infinitely many.

13. $A$ has rank $2$, and its third row is the sum of the first two. So $\operatorname{rank}[A \mid b] = 2$ exactly when $b_3 = b_1 + b_2$; the determinant of $[A \mid b]$ is $b_3 - b_1 - b_2$.

17. The division by $1 - a^2$ fails for $a = \pm 1$. For $a = 1$ both equations are $x + y = 1$, and the solutions are $(1 - t, t)$ for $t \in \R$. For $a = -1$ the equations $x - y = 1$ and $-x + y = 1$ add to $0 = 2$, so there is no solution.

19. There are $1$ of rank $0$, $4 + 2 + 1 = 7$ of rank $1$ (pivot in column $1$, $2$ or $3$) and $4 + 2 + 1 = 7$ of rank $2$ (pivot columns $\set{1, 2}$, $\set{1, 3}$ or $\set{2, 3}$), so $15$ in all. Two $2 \times 3$ matrices are row equivalent if and only if they have the same row space, so each row space of dimension at most $2$ belongs to exactly one RREF.

20. Gauss–Jordan elimination on $[A \mid b]$ uses only the four operations, so it runs inside $\Q$ and gives a rational RREF. By uniqueness this is also the RREF over $\R$, so the consistency test and the free variables are the same over both fields. Setting the free variables to $0$ gives a rational solution; if the real solution is unique, there are no free variables, and the unique solution is this one.

21. For a square matrix, every column is a pivot column if and only if every row of an echelon form has a pivot. If both hold, no echelon form of $[A \mid b]$ can have a row $(0, \ldots, 0 \mid c)$ with $c \neq 0$. If not, write the echelon form as $E = PA$ with $P$ invertible; its last row is zero, and $b = P^{-1} e_n$ gives an inconsistent system.

22. Let $x_i = 1$ when light $i$ is pressed. Pressing a set of lights switches off the pattern $b$ exactly when $Ax = b$ over $\F_2$, where $A$ has $1$ on the diagonal and next to it and $0$ elsewhere. Row reduction of $[A \mid b]$ ends with the row $(0, 0, 0, 0, 0 \mid b_1 + b_2 + b_4 + b_5)$. For all lights on, press lights $2$ and $5$, or lights $1$ and $4$.
