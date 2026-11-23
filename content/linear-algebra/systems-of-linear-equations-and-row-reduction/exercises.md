1. ◦ Which of the following are [linear equations](/0Q3ZT8J05R/) in the unknowns $x$, $y$, $z$ over $\R$? (a) $3x - 2y + z = \sin 1$. (b) $xy + z = 1$. (c) $\tfrac12 x + \sqrt{3}\, y = z$. (d) $2^x + y = 3$. (e) $(x - y)^2 = x^2 + y^2$.

2. ◦ Write the coefficient matrix and the augmented matrix of the system $x + 2y - z = 3$, $2x + 5y + z = 10$, $-x + y + 4z = 3$, and solve it by Gaussian elimination and back substitution.

3. ◦ Give the elementary row operation that undoes each of $R_2 \leftarrow R_2 - 4R_1$, $R_1 \leftrightarrow R_3$ and $R_2 \leftarrow \tfrac15 R_2$. Then explain why $R_1 \leftarrow 0 \cdot R_1$ is not allowed as a row operation on an augmented matrix, with a system whose solution set it changes.

4. ◦ Decide for each matrix whether it is in reduced row echelon form, in row echelon form but not reduced, or in neither:
$$\text{(a) } \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \end{pmatrix}, \quad \text{(b) } \begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}, \quad \text{(c) } \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \text{(d) } \begin{pmatrix} 1 & 3 & 1 \\ 0 & 2 & 4 \end{pmatrix}, \quad \text{(e) } \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$

5. ◦ Find the reduced row echelon form of
$$\begin{pmatrix} 1 & 2 & 1 & 4 \\ 2 & 4 & 0 & 2 \\ 3 & 6 & 1 & 6 \end{pmatrix},$$
its pivot columns and its rank.

6. ◦ A system in $x_1, x_2, x_3, x_4$ has the augmented matrix
$$\left(\begin{array}{rrrr|r} 1 & -2 & 0 & 3 & 1 \\ 0 & 0 & 1 & -1 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right).$$
Name the basic and the free variables and write all solutions in parametric form.

7. ◦ Decide whether $b = (5, 3)$ is a linear combination of $v_1 = (1, 2)$ and $v_2 = (3, -1)$ by solving the [vector equation](/E7SAHXQEVC/) $x_1 v_1 + x_2 v_2 = b$.

8. ◦ Without solving anything, answer: (a) must a homogeneous system of $3$ equations in $5$ unknowns over $\R$ have a nonzero solution? (b) Must a homogeneous system of $5$ equations in $3$ unknowns over $\R$ have one? Justify (a) and give an example for (b).

9. ◦ Solve $x + y + z = 0$, $x + 2y = 1$ over the field $\F_3$ and list all its solutions.

10. • Solve $x_2 + x_3 = 3$, $x_1 + x_2 + x_3 = 4$, $2x_1 + 2x_2 + 3x_3 = 11$ by Gaussian elimination. Say where a row swap is needed and why.

11. • For which real $a$ and $b$ does the system $x + y + z = 1$, $x + 2y + az = 2$, $2x + 3y + 4z = b$ have exactly one solution, no solution, or infinitely many?

12. • Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 5 \\ 3 & 7 \end{pmatrix}$. Find the condition on $b = (b_1, b_2, b_3)$ for $Ax = b$ to be consistent, and solve the system for $b = (1, 3, 4)$.

13. • Which two of the following matrices are [row equivalent](/006BHFWMAP/)?
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \end{pmatrix}.$$

14. • Find the error. To solve $x + ay = 1$, $ax + y = 1$ over $\R$, a student subtracts $a$ times the first equation from the second, gets $(1 - a^2)y = 1 - a$, divides to get $y = \tfrac{1}{1 + a}$ and then $x = \tfrac{1}{1 + a}$, and concludes that the system has exactly one solution for every $a \neq -1$. Correct the conclusion for every real $a$.

15. • Find the error. To reduce the augmented matrix of $x + y = 2$, $x - y = 0$, a student performs $R_1 \leftarrow R_1 - R_2$ and $R_2 \leftarrow R_2 - R_1$ in one step, both computed from the original rows. Find the solution sets before and after this step, and say what went wrong.

16. • For which real $c$ does a polynomial $y = a_0 + a_1 x + a_2 x^2$ pass through the four points $(0, 1)$, $(1, 2)$, $(2, 5)$ and $(3, c)$? Find the polynomial in that case.

17. • Let $A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix}$ and $b = (1, 2, c)$. Find $\operatorname{rank} A$ and $\operatorname{rank}\,[A \mid b]$ for each real $c$. Use the [Rouché-Capelli theorem](/0HV1SKWPMS/) to say for which $c$ the system $Ax = b$ is consistent, and write its solutions in parametric form in that case.

18. • Use Gauss-Jordan elimination on $[A \mid I]$ to find the inverse of $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 1 & 2 & 4 \end{pmatrix}$, and check one entry of $A A^{-1}$.

19. • Let $p$ and $q$ be solutions of $Ax = b$ over $\R$ with $b \neq 0$. For which real $s$ and $t$ is $sp + tq$ a solution of $Ax = b$? Show also that $p - q$ solves $Ax = 0$.

20. • How many $2 \times 3$ matrices over $\F_2$ are in reduced row echelon form? Sort them by their pivot columns.

21. • For each item give an example over $\R$ or prove that none exists. (a) A system of $3$ equations in $2$ unknowns with exactly one solution. (b) A system of $2$ equations in $3$ unknowns with exactly one solution. (c) A system of $2$ equations in $3$ unknowns with no solution.

22. ★ Show that the system $x + 2y + 3z = 1$, $4x + 5y + 6z = 2$, $7x + 8y + 9z = 8$ has no solution over $\Q$. For which primes $p$ does it have a solution over $\F_p$, and how many solutions does it have then?

23. ★ Let $A$ be an $m \times n$ matrix and $b \in \Q^m$, all with rational entries. Prove that if $Ax = b$ has a solution in $\R^n$, then it has a solution in $\Q^n$.

24. ★ Let $A$ be an $n \times n$ matrix over a field $F$. Prove with pivots that $Ax = b$ has a solution for every $b \in F^n$ if and only if $Ax = 0$ has only the solution $x = 0$.

25. ★ Five lights stand in a row, each on or off. Pressing a light switches it and its neighbours, so pressing light $1$ switches lights $1$ and $2$ and pressing light $3$ switches lights $2$, $3$ and $4$. Work over $\F_2$. Show that a pattern $b = (b_1, \dots, b_5)$ of lights to switch can be produced by pressing some lights if and only if $b_1 + b_2 + b_4 + b_5 = 0$. Find all ways to switch on all five lights, starting with all of them off.

26. ★ Let $F$ be a field and let $x_0, x_1, x_2 \in F$ be distinct. Prove by row reduction, without determinants, that for every $y_0, y_1, y_2 \in F$ there is exactly one polynomial $a_0 + a_1 x + a_2 x^2$ over $F$ that takes the value $y_i$ at $x_i$ for $i = 0, 1, 2$.
