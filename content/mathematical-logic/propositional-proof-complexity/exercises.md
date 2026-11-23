1. ◦ Write out the [pigeonhole formula](/RJ571F7FF0/) $\mathrm{PHP}^4_3$. How many variables, pigeon clauses and hole clauses does it have, what is its largest clause width, and how many rows does a truth table for it have? Check your count against the general formula $m + n\binom{m}{2}$ for the number of clauses of $\mathrm{PHP}^m_n$.

2. ◦ Which of the following functions $f$ are [propositional proof systems](/3V24CYWDT6/)? In each case $f$ sends every string not covered by the rule to $p \vee \neg p$. (a) $f(w) = w$ if $w$ is a formula of the form $\varphi \vee \neg\varphi$. (b) $f(w)$ is the last line of $w$ if $w$ is a proof in a fixed [Frege system](/J2BAR09TPF/). (c) $f(\tau \# 1^k) = \tau$ if $k \ge \abs{\tau}^2$ and $\tau$ is a tautology. (d) $f(w) = w$ if $w$ is a formula. For (c), show that it is a proof system if and only if $\mathrm{P} = \mathrm{NP}$.

3. ◦ Let $F = \set{a \vee b, \ \neg a \vee b, \ a \vee \neg b, \ \neg a \vee \neg b}$. Consider the [resolution](/6JSH907W5R/) refutation with the lines (1) $a \vee b$, (2) $\neg a \vee b$, (3) $b$ from 1 and 2, (4) $a \vee \neg b$, (5) $a$ from 3 and 4, (6) $\neg a \vee \neg b$, (7) $\neg a$ from 3 and 6, (8) $\square$ from 5 and 7. Find its size in clauses and its width, and decide whether it is tree-like and whether it is regular. Then give a refutation of $F$ with fewer clauses.

4. ◦ Translate the clause $x \vee \neg y \vee \neg z$ into a line of [cutting planes](/KKCX2HQP2K/) and into a polynomial of the [algebraic proof systems](/ZERBQSTZB5/), with $1$ read as true. Check on all eight $0$-$1$ points that the clause is true exactly when the inequality holds and exactly when the polynomial vanishes.

5. ◦ Let $C_4$ be the cycle on the vertices $1, 2, 3, 4$ with charge $\chi = (1, 0, 0, 0)$, and let $K_4$ be the complete graph on the same vertices with charge $(1, 1, 0, 0)$. For each, count the clauses of the [Tseitin formula](/JXTCC6KXNG/) and give their width. Decide which of the two formulas is satisfiable, and for that one give a satisfying assignment.

6. ◦ A proof of a tautology $\tau$ in the variables $p, q$ is being written in [extended Frege](/5YSE04SHFH/). Which of these lines are allowed as extension axioms? (a) $r \leftrightarrow (p \wedge q)$ as the first line. (b) $r \leftrightarrow (r \vee p)$ as the first line. (c) $s \leftrightarrow (r \wedge \neg p)$ after line (a). (d) $p \leftrightarrow (q \vee q)$. (e) $r \leftrightarrow \neg q$ after line (a).

7. ◦ With the convention of [bounded-depth Frege](/41QJ1WEMJ3/), in which literals have depth $0$, find the depth of $(x_1 \wedge x_2) \vee \neg\bigl(x_3 \vee (x_4 \wedge x_5)\bigr)$. What is the depth of a CNF with at least two clauses, each of at least two literals?

8. ◦ Each argument has an error. Find it. (a) "By Haken's theorem resolution is not polynomially bounded, so by the [Cook-Reckhow theorem](/YS1T29B00B/), $\mathrm{NP} \ne \mathrm{coNP}$." (b) "Every $\tau_n$ in a family has a Frege proof with $n$ lines, so Frege systems prove the family in polynomial size." (c) "Cutting planes p-simulates resolution, and the pigeonhole formulas need exponential-size resolution refutations, so they also need exponential-size cutting-planes refutations."

9. ◦ Apply the division rule of cutting planes to each line with the largest possible divisor $c \ge 2$, or say why the rule does not apply. (a) $2x + 4y - 6z \ge 1$. (b) $3x + 6y \ge 2$. (c) $2x + 3y \ge 1$. (d) $4x - 2y \ge -1$.

10. ◦ A CNF $F$ in $n = 1000$ variables has $w(F) = 3$ and refutation width $w(F \vdash \square) = 203$. What lower bounds do the two parts of the [size-width relation](/GWDGRPAQSM/) give for $S_T(F \vdash \square)$ and for $S(F \vdash \square)$? What is the least refutation width for which part 2 gives a bound of at least $2^{100}$?

11. • Let $F_n$ be the CNF whose clauses are all $2^n$ clauses that contain each of the variables $x_1, \dots, x_n$ exactly once, positive or negative. Prove that the least size of a resolution refutation of $F_n$, tree-like or not, is exactly $2^{n+1} - 1$ clauses.

12. • Show that deleting any one of the nine clauses of $\mathrm{PHP}^3_2$ leaves a satisfiable CNF, and deduce that every resolution refutation of $\mathrm{PHP}^3_2$ has at least $17$ clauses. Compare with the width-$2$ refutation in the [pigeonhole formulas](/RJ571F7FF0/) entry.

13. • Let $G$ be a finite graph that need not be connected. Show that $T(G, \chi)$ is unsatisfiable if and only if some connected component of $G$ has odd total charge. Give an example in which the total charge is even and the formula is unsatisfiable.

14. • Let $e = \set{u, v}$ be an edge of $G$, where $u$ and $v$ both have degree at least $2$, and let $b \in \set{0, 1}$. Show that setting $x_e = b$ in $T(G, \chi)$ and simplifying gives exactly $T(G - e, \chi')$, where $\chi'$ agrees with $\chi$ except that $\chi'(u) = \chi(u) \oplus b$ and $\chi'(v) = \chi(v) \oplus b$.

15. • Let $C_n$ be the cycle with $n \ge 3$ vertices and let $\chi$ have odd total charge. Give a resolution refutation of $T(C_n, \chi)$ of width $2$ with $4n - 1$ clauses. Why does no refutation have width $1$?

16. • Resolve $x \vee y$ and $\neg x \vee \neg z$ on $x$. Derive the cutting-planes line of the resolvent from the lines of the two premises, using linear combinations, Boolean axioms and one division.

17. • The parity of $p_1, \dots, p_n$ can be written without extension variables as $P_1 = p_1$ and $P_{i+1} = (P_i \wedge \neg p_{i+1}) \vee (\neg P_i \wedge p_{i+1})$. Find the number of occurrences of variables in $P_n$. Then write extension axioms $q_1 \leftrightarrow p_1$ and $q_{i+1} \leftrightarrow \ldots$ that name the same parities, check that each is allowed, and count the occurrences of variables in all of them together.

18. • Find a [Nullstellensatz](/ZERBQSTZB5/) refutation of degree $2$ of the clauses $x$, $\neg x \vee y$ and $\neg y$, and prove that no refutation of degree $1$ exists.

19. • Take the triangle Tseitin formula with charge $(1, 0, 0)$ and its six clauses, as in the [Tseitin formulas](/JXTCC6KXNG/) entry. Show that over $\F_2$ the sum of the six clause polynomials is $1$, so that all multipliers $g_i = 1$ give a Nullstellensatz refutation of degree $2$. Compute the same sum over $\Q$.

20. • Let $A(p_1, p_2, q) = \set{q \vee p_1, \ \neg q \vee p_2}$ and $B(p_1, p_2, r) = \set{\neg p_1 \vee r, \ \neg p_2 \vee r, \ \neg r}$. Give a resolution refutation of $A \wedge B$ with $10$ clauses, run the construction of [feasible interpolation](/59GJCM8C66/) for resolution on it with the general and with the monotone rule, and show that the circuit you get is the only interpolating function for this pair.

21. • Let $A(p, q)$ and $B(p, r)$ be CNFs with $A \wedge B$ unsatisfiable, and suppose that no variable of $p$ occurs negatively in $A$. Show that the set $U = \set{a : A(a, q) \text{ is satisfiable}}$ is closed upwards in the order of $\set{0,1}^{\abs{p}}$, and that the indicator function of $U$ is a monotone interpolating function. Explain why this does not prove monotone feasible interpolation.

22. • Treat the [truth-table system](/67MYPBSHCJ/) as a refutation system: a refutation of a CNF $F$ in $N$ variables is $F \# 1^{2^N}$. Show that resolution p-simulates it and that it does not p-simulate resolution.

23. ★ Let $L$ be a nonempty set of strings. Call a polynomial-time function onto $L$ a proof system for $L$. Prove that $L$ has a polynomially bounded proof system if and only if $L \in \mathrm{NP}$, and deduce the Cook-Reckhow theorem.

24. ★ Prove part 1 of the size-width relation: if $F$ has a tree-like resolution refutation with at most $2^b$ clauses, then $F$ has a refutation of width at most $w(F) + b$.

25. ★ Prove that every tree-like resolution refutation of least size is regular.

26. ★ Show that for $3$-CNFs in $n$ variables a resolution refutation can be found in time $n^{O(\log S_T)}$, where $S_T = S_T(F \vdash \square) \ge 2$. You may use part 1 of the size-width relation.

27. ★ Let $\mathcal F_1$ and $\mathcal F_2$ be Frege systems over the same connectives. Show that every $\mathcal F_1$-proof with $m$ lines and size $s$ can be turned in polynomial time into an $\mathcal F_2$-proof of the same formula with at most $cm$ lines and size $O(s^2)$, for a constant $c$ that depends only on the two systems.
