2. The coefficient matrix has the rows $(1, 2, -1)$, $(2, 5, 1)$, $(-1, 1, 4)$, and the augmented matrix adds the column $(3, 10, 3)$. The unique solution is $(x, y, z) = (2, 1, 1)$.

4. (a) and (b) are reduced. (d) is in echelon form but not reduced, since its second pivot is $2$ and there is a $3$ above it. (c) and (e) are in neither: in (c) the leading entry of row 2 lies to the left of that of row 1, and in (e) a zero row lies above a nonzero row.

6. The basic variables are $x_1$ and $x_3$, the free ones $x_2 = s$ and $x_4 = t$. The solutions are $(1, 0, 2, 0) + s(2, 1, 0, 0) + t(-3, 0, 1, 1)$ for $s, t \in \R$.

9. Subtracting the first equation from the second gives $y - z = 1$, so $y = 1 + z$ and $x = -y - z = 2 + z$ in $\F_3$. With $z = t$ the solutions are $(2 + t, 1 + t, t)$: the three triples $(2, 1, 0)$, $(0, 2, 1)$ and $(1, 0, 2)$, as the count $3^{3 - 2}$ predicts.

11. Eliminate $x$ and then $y$; the last row becomes $(0, 0, a - 3 \mid b - 3)$. If $a \neq 3$ there is exactly one solution. If $a = 3$ and $b \neq 3$ there is none. If $a = 3$ and $b = 3$ there are infinitely many.

14. Division by $1 - a^2$ needs $a \neq 1$ as well as $a \neq -1$. For $a = 1$ both equations are $x + y = 1$, and there are infinitely many solutions. For $a = -1$ the equations $x - y = 1$ and $-x + y = 1$ contradict each other. So there is exactly one solution, $\left(\tfrac{1}{1 + a}, \tfrac{1}{1 + a}\right)$, exactly when $a \neq \pm 1$.

15. Before, the only solution is $(1, 1)$. After, the rows are $(0, 2 \mid 2)$ and $(0, -2 \mid -2)$, and every $(x, 1)$ is a solution. The second operation used the old $R_1$ instead of the new one, so the step is not a composition of elementary operations, and it cannot be undone.

17. The third row of $A$ is the sum of the first two, so $\operatorname{rank} A = 2$. Then $\operatorname{rank}\,[A \mid b] = 2$ if $c = 3$ and $3$ otherwise, so the system is consistent only for $c = 3$. Its solutions are then $(0, 1, 0) + t(-1, -1, 1)$, a line.

20. There are $15$. Rank $0$: the zero matrix, $1$. Rank $1$: pivot in column $1$, $4$; in column $2$, $2$; in column $3$, $1$. Rank $2$: pivots in columns $1, 2$, $4$; in columns $1, 3$, $2$; in columns $2, 3$, $1$.

22. The rows satisfy $R_1 - 2R_2 + R_3 = 0$, while the right sides give $1 - 4 + 8 = 5$. So any solution would satisfy $0 = 5$, which fails over $\Q$ and over $\F_p$ for every $p \neq 5$. Over $\F_5$ the first two rows are not proportional, so the rank is $2$, the system is consistent, and there are $5^{3 - 2} = 5$ solutions.

23. Gauss-Jordan elimination over $\Q$ uses only rational arithmetic. By uniqueness its result is also the reduced form over $\R$. Since there is a real solution, the last column has no pivot. Setting every free variable to $0$ then gives a rational solution.

24. Both conditions say that the reduced form of $A$ has a pivot in every column. With $n$ rows and $n$ columns, that is the same as a pivot in every row. A pivot in every column means there are no free variables, so $Ax = 0$ has only $x = 0$. A pivot in every row means no echelon form of $[A \mid b]$ can have a pivot in its last column.

25. The presses $x \in \F_2^5$ give the pattern $Tx$, where $T$ has $1$ on the diagonal and next to it and $0$ elsewhere. Row reduction gives $\operatorname{rank} T = 4$. The null space is spanned by $(1, 1, 0, 1, 1)$. Since $T$ is symmetric, the consistency condition is $b_1 + b_2 + b_4 + b_5 = 0$. For $b = (1, 1, 1, 1, 1)$ there are $2^{5 - 4} = 2$ solutions: press lights $2$ and $5$, or lights $1$ and $4$.

26. Subtract row $0$ from rows $1$ and $2$ of the matrix with rows $(1, x_i, x_i^2)$. Row $i$ becomes $(x_i - x_0)(0, 1, x_i + x_0)$, so divide by the nonzero $x_i - x_0$. Then the difference of the two lower rows is $(0, 0, x_2 - x_1)$, again nonzero. There are three pivots, so there are no free variables and the last column of the augmented matrix is never a pivot column.
