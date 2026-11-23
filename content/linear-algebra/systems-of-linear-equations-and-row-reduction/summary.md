## What to remember

- A [system](/0GT4WWGWH2/) of $m$ [linear equations](/0Q3ZT8J05R/) in $n$ unknowns over a field $F$ is $Ax = b$ with $A$ an $m \times n$ matrix over $F$ and $b \in F^m$. Its solutions are the $x \in F^n$ that satisfy all the equations at once. It is [consistent](/0X6V9B1V10/) when it has at least one solution. A [homogeneous](/04KGXJG1A2/) system $Ax = 0$ is always consistent.
- The [elementary row operations](/04XWH28452/) are swapping two rows, multiplying a row by a nonzero element of $F$, and adding a multiple of one row to another. Each can be undone by one of the same kind. Applied to the [augmented matrix](/0YCDZ7N8VD/) $[A \mid b]$, they do not change the set of solutions.
- Every matrix over a field is [row equivalent](/006BHFWMAP/) to a matrix in [row echelon form](/0VYCDGMJJJ/), which is not unique, and to exactly one matrix in [reduced row echelon form](/0WF5AQYTW6/), by the [uniqueness theorem](/BF9SMZMJZE/). So the [pivot](/0J0BBCMJ5W/) positions and their number, the rank, depend only on the matrix.
- [Gaussian elimination](/0JVJ2WCXZH/) reaches an echelon form in about $\tfrac23 n^3$ operations for an $n \times n$ matrix. [Back substitution](/0ATFVE08MW/) solves an upper triangular system with nonzero diagonal in about $n^2$. [Gauss-Jordan elimination](/098D6FQN3N/) goes on to the reduced form.
- $Ax = b$ holds exactly when $b = x_1 v_1 + \cdots + x_n v_n$ for the columns $v_j$ of $A$. So the system is consistent exactly when $b$ is in the span of the columns, by the [vector equation](/E7SAHXQEVC/) view.
- [Existence and uniqueness](/BKA191KD1S/), over a field $F$: $Ax = b$ is consistent exactly when the last column of an echelon form of $[A \mid b]$ is not a pivot column. Suppose it is consistent and $k$ of the first $n$ columns have no pivot. Then the solution is unique if $k = 0$. If $k \ge 1$ there are infinitely many solutions when $F$ is infinite, and $q^k$ of them when $F$ has $q$ elements.
- [Structure](/PDH3HKXWAZ/): the solutions of $Ax = 0$ form a subspace $N$ of $F^n$ of dimension $n - \operatorname{rank} A$. If $p$ is one solution of $Ax = b$, the full solution set is $p + N$. The free variables are the parameters of the [parametric form](/KQT68YPHD1/).
- [Rouché-Capelli](/0HV1SKWPMS/): $Ax = b$ is consistent exactly when $\operatorname{rank} A = \operatorname{rank}\,[A \mid b]$. The solution is then unique exactly when $\operatorname{rank} A = n$.
- If $m < n$, a system is never uniquely solvable, and $Ax = 0$ has a nonzero solution. If $m > n$, the system is usually inconsistent; see [overdetermined and underdetermined systems](/QJ0P26J9BV/).

The pivots of an echelon form of $[A \mid b]$ decide every case. The table assumes the field is infinite, such as $\Q$, $\R$ or $\C$.

| Pivots of an echelon form of $[A \mid b]$ | Solutions of $Ax = b$ | $\operatorname{rank} A$ and $\operatorname{rank}\,[A \mid b]$ |
|---|---|---|
| a pivot in the last column | none | $\operatorname{rank} A < \operatorname{rank}\,[A \mid b]$ |
| none in the last column, one in each of the first $n$ columns | exactly one | both equal $n$ |
| none in the last column, some of the first $n$ columns without one | infinitely many | equal, and less than $n$ |

: The three cases of a linear system over an infinite field

## Common errors

- Replacing two rows at once from each other's old values, for example $R_1 \leftarrow R_1 - R_2$ and $R_2 \leftarrow R_2 - R_1$ in one step. This is not a sequence of elementary operations, and it can change the solution set.
- Multiplying a row by $0$, or by an expression such as $a - 1$ that may be $0$. Likewise, dividing by a parameter without treating separately the values that make it $0$.
- Reading the solutions off an echelon form that is not reduced as if it were reduced. Such a form still needs back substitution, and its pivots need not be $1$.
- Concluding "no solution" from a zero row $(0, \dots, 0 \mid 0)$. That row says $0 = 0$. Only a row $(0, \dots, 0 \mid c)$ with $c \neq 0$ shows that the system is inconsistent.
- Counting equations instead of pivots. Three equations in three unknowns can have infinitely many solutions or none. What matters is the rank.
- Believing that row operations keep the column space. They keep the row space and the null space, but they can change the column space.
- Calling the solution set of $Ax = b$ with $b \neq 0$ a subspace. It does not contain $0$; it is a translate $p + N$ of the null space.
