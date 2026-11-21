## What to remember

- A [system](/0GT4WWGWH2/) of $m$ linear equations in $n$ unknowns over a field $F$ is one matrix equation $Ax = b$, with $A$ the $m \times n$ [coefficient matrix](/0P7A2MJD24/) and $[A \mid b]$ the [augmented matrix](/0YCDZ7N8VD/).
- The three [elementary row operations](/04XWH28452/) are $R_i \leftrightarrow R_j$, $R_i \leftarrow cR_i$ with $c \neq 0$, and $R_i \leftarrow R_i + cR_j$ with $i \neq j$. Each one can be undone by another one, so [row equivalent](/006BHFWMAP/) augmented matrices have the same solution set.
- Every matrix is row equivalent to exactly one matrix in [reduced row echelon form](/0WF5AQYTW6/), by the [uniqueness theorem](/BF9SMZMJZE/). So the [pivot columns](/0J0BBCMJ5W/) and their number, the rank, belong to the matrix, not to the way it was reduced. [Row echelon forms](/0VYCDGMJJJ/) that are not reduced are not unique.
- $Ax = b$ is consistent if and only if no echelon form of $[A \mid b]$ has a row $(0, \ldots, 0 \mid c)$ with $c \neq 0$. A consistent system has a unique solution if and only if every column of $A$ is a pivot column; this is the [existence and uniqueness theorem](/BKA191KD1S/).
- In [Rouché–Capelli](/0HV1SKWPMS/) form: $Ax = b$ is solvable if and only if $\operatorname{rank} A = \operatorname{rank}[A \mid b]$, and then the solution set has dimension $n - \operatorname{rank} A$.
- The [solution set](/PDH3HKXWAZ/) is empty or $p + N$, with $p$ one solution and $N = \set{x : Ax = 0}$ the solution set of the [homogeneous system](/04KGXJG1A2/). The [parametric form](/KQT68YPHD1/) uses the free variables as the parameters.
- A homogeneous system with more unknowns than equations has a nonzero solution, and an [underdetermined system](/QJ0P26J9BV/) never has exactly one solution.
- [Gaussian elimination](/0JVJ2WCXZH/) of an $n \times n$ matrix costs about $\tfrac23 n^3$ operations, and [back substitution](/0ATFVE08MW/) then costs $n^2$.

| Echelon form of $[A \mid b]$ | Ranks | Over $\R$ | Over $\F_q$ |
|---|---|---|---|
| has a row $(0, \ldots, 0 \mid c)$, $c \neq 0$ | $\operatorname{rank} A < \operatorname{rank}[A \mid b]$ | no solution | no solution |
| no such row, every column of $A$ a pivot column | $\operatorname{rank} A = \operatorname{rank}[A \mid b] = n$ | exactly one | exactly one |
| no such row, $k \ge 1$ free variables | $\operatorname{rank} A = \operatorname{rank}[A \mid b] = n - k$ | infinitely many | exactly $q^k$ |

: The three cases for a system $Ax = b$ with $n$ unknowns, read from an echelon form or from ranks. The count $q^k$ is from [linear systems over finite fields](/J6A58MEM8R/).

## Common errors

- **Reading the answer from an echelon form of $A$ alone.** Consistency depends on $b$. Reduce the augmented matrix $[A \mid b]$, and look at its last column.
- **Operations that are not elementary.** Multiplying a row by $0$, or replacing two rows at once by expressions in the old rows, can change the solution set. Do one operation at a time, from the current rows.
- **Dividing by an expression that may be $0$.** With a parameter in the system, a step such as "divide by $1 - a$" is valid only for $a \neq 1$. Treat the excluded values as separate cases.
- **Comparing echelon forms that are not reduced.** Two different echelon forms do not show that two matrices are not row equivalent. Compare the reduced forms.
- **Too few parameters.** The number of parameters in the solution set is the number of free variables, $n - \operatorname{rank} A$, not $n - m$. Equations that repeat information do not count.
- **Expecting overdetermined systems to be inconsistent.** More equations than unknowns usually means no solution, but not always: the equations may be compatible. Row reduce and check.
