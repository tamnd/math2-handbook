1. ◦ Which of these are [linear equations](/0Q3ZT8J05R/) in the unknowns $x$, $y$, $z$ over $\R$? (a) $3x - \sqrt 2\, y = z + 1$. (b) $xy + z = 1$. (c) $x + \sin(\pi/4)\, y = 0$. (d) $\sqrt x + y = 3$.

2. ◦ Say for each matrix whether it is in [reduced row echelon form](/0WF5AQYTW6/), in [row echelon form](/0VYCDGMJJJ/) but not reduced, or in neither.
$$A = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 3 & 2 \\ 0 & 2 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 0 & 3 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 & 5 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$

3. ◦ Write the [coefficient matrix](/0P7A2MJD24/) and the [augmented matrix](/0YCDZ7N8VD/) of the system $2x - z = 1$, $x + y + z = 0$, $3y = 4$ in the unknowns $x, y, z$.

4. ◦ The augmented matrix of a system in $x_1, x_2, x_3, x_4$ has the reduced row echelon form
$$\left[\begin{array}{rrrr|r} 1 & 0 & 2 & 0 & 3 \\ 0 & 1 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & 2 \end{array}\right].$$
Name the [pivot columns and the free variables](/0J0BBCMJ5W/), and write down all solutions.

5. ◦ Which of the following are [elementary row operations](/04XWH28452/) on a matrix with three rows? For each one that is, give the operation that undoes it. (a) $R_1 \leftrightarrow R_3$. (b) $R_2 \leftarrow -R_2$. (c) $R_2 \leftarrow 0 \cdot R_2$. (d) $R_3 \leftarrow R_3 - R_3$. (e) $R_1 \leftarrow R_1 + 2R_3$.

6. ◦ An echelon form of the augmented matrix of a real system is
$$\left[\begin{array}{rrr|r} 1 & 2 & -1 & 3 \\ 0 & 1 & 4 & 2 \\ 0 & 0 & 0 & h \end{array}\right].$$
For which $h$ is the system consistent, and how many solutions does it have then?

7. ◦ A [homogeneous system](/04KGXJG1A2/) over $\R$ has $3$ equations and $5$ unknowns. Can its only solution be $x = 0$? What is the least possible number of free variables?

8. ◦ Is $b = (5, 3)$ a linear combination of $a_1 = (1, 2)$ and $a_2 = (3, -1)$? If so, find the coefficients. (Write the question as a [vector equation](/E7SAHXQEVC/) first.)

9. • Solve $x + 2y - z = 3$, $2x + 5y + z = 10$, $-x + y + 4z = 3$ by [Gaussian elimination](/0JVJ2WCXZH/) and [back substitution](/0ATFVE08MW/), and check the answer.

10. • Find the reduced row echelon form of
$$\begin{pmatrix} 1 & 2 & 1 & 4 \\ 2 & 4 & 0 & 2 \\ 3 & 6 & 1 & 6 \end{pmatrix}$$
by [Gauss–Jordan elimination](/098D6FQN3N/). Which columns are pivot columns, and what is the rank?

11. • Solve $x_1 + 2x_2 - x_3 + x_4 = 1$, $2x_1 + 4x_2 + x_3 + 5x_4 = 8$ over $\R$. Write the solution set in [parametric form](/KQT68YPHD1/) as $p + N$, with $p$ one solution and $N$ the solution set of the homogeneous system, given by a basis.

12. • For which real numbers $a$ and $b$ does the system $x + y + z = 1$, $x + 2y + az = 2$, $2x + 3y + 4z = b$ have no solution, exactly one solution, or infinitely many solutions?

13. • Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 5 \\ 3 & 7 \end{pmatrix}$. Use the [Rouché–Capelli theorem](/0HV1SKWPMS/) to find all $b = (b_1, b_2, b_3) \in \R^3$ for which $Ax = b$ is consistent.

14. • Solve the system $x + y + z = 0$, $x + 2y = 1$ over the field $\F_3$ and list all its solutions. Check the count against the formula $q^k$ of [linear systems over finite fields](/J6A58MEM8R/), where $k$ is the number of free variables.

15. • Let $p$ and $q$ be two different solutions of $Ax = b$ over $\R$, with $b \neq 0$. For which pairs $(s, t)$ of real numbers is $sp + tq$ always a solution? Use the [structure of the solution set](/PDH3HKXWAZ/).

16. • Decide which of these three matrices are [row equivalent](/006BHFWMAP/) to each other:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \end{pmatrix}.$$

17. • A student solves $x + ay = 1$, $ax + y = 1$ as follows: $R_2 \leftarrow R_2 - aR_1$ gives $(1 - a^2)\, y = 1 - a$, so $y = \dfrac{1}{1 + a}$ and $x = \dfrac{1}{1 + a}$. For which values of $a$ is the argument wrong, and what is the solution set for those values?

18. • Find all values of $c$ for which some polynomial $y = a_0 + a_1 x + a_2 x^2$ passes through the four points $(0, 1)$, $(1, 2)$, $(2, 5)$ and $(3, c)$. This is an [overdetermined system](/QJ0P26J9BV/) in $a_0, a_1, a_2$. For such $c$, find the polynomial.

19. ★ Count the $2 \times 3$ matrices over $\F_2$ that are in reduced row echelon form. Use the [uniqueness of the reduced row echelon form](/BF9SMZMJZE/) to explain why the number equals the number of subspaces of $\F_2^3$ of dimension at most $2$.

20. ★ Let $A$ be an $m \times n$ matrix and $b \in \Q^m$ with rational entries. Prove that if $Ax = b$ has a solution in $\R^n$, then it has a solution in $\Q^n$, and that if the real solution is unique, it is rational.

21. ★ Let $A$ be an $n \times n$ matrix over a field $F$. Prove with pivots that $Ax = b$ has a solution for every $b \in F^n$ if and only if $Ax = 0$ has only the solution $x = 0$.

22. ★ Five lights stand in a row, each on or off. Pressing a light switches it and its neighbours (one neighbour at the ends, two in the middle). Model this as a system over $\F_2$. Show that a pattern $(b_1, \ldots, b_5)$ can be switched off completely if and only if $b_1 + b_2 + b_4 + b_5 = 0$ in $\F_2$. Find the presses that switch off the pattern with all five lights on.
