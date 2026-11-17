1. ◦ Compute $n!$ and $2^n$ for $n = 0, 1, \ldots, 5$. What is the least natural number $n_0$ such that $n! > 2^n$ holds for $n_0$ and for every larger $n$?

2. ◦ Let $P(n)$ be "$3$ divides $4^n + 1$". Show that $P(n)$ implies $P(n + 1)$ for every natural number $n$. Is $P(n)$ true for any $n$? What does this say about the base case of an induction?

3. ◦ Which of these sets has a least element? (a) The set of natural numbers $n$ with $n^2 > 50$. (b) The set of positive rational numbers. (c) The set of negative integers. (d) The set of natural numbers $n$ such that $n$ divides $0$. Give the least element where there is one, and say why the [well-ordering principle](/01BX15HSRR/) does not apply where there is none.

4. ◦ Which integers from $1$ to $12$ can be written as $3a + 5b$ with natural numbers $a$ and $b$? A proof by [strong induction](/0KMVFSHFGZ/) that every $n \ge 8$ has this form uses the step from $n - 3$ to $n$. Which base cases does it need?

5. ◦ "Claim: for every natural number $n$, if $a$ and $b$ are natural numbers with $\max(a, b) = n$, then $a = b$. The case $n = 0$ is clear. If $\max(a, b) = n + 1$, then $\max(a - 1, b - 1) = n$, so $a - 1 = b - 1$ by the induction hypothesis, and $a = b$." The claim is false. Which step fails, and for which $a$ and $b$?

6. ◦ A descent argument produces a strictly decreasing sequence of sizes. For which of these sets of sizes must every such sequence be finite? (a) $\N$. (b) $\Z$. (c) The positive rationals. (d) The pairs of natural numbers in lexicographic order.

7. ◦ Let $S$ be the smallest set of integers that contains $3$ and contains $x + y$ whenever it contains $x$ and $y$. Describe $S$. Is $12$ in $S$? Is $0$? Is $4$?

8. ◦ A statement $P(n)$ about positive integers satisfies three conditions: $P(1)$ holds; $P(n)$ implies $P(2n)$ for every $n \ge 1$; and $P(n)$ implies $P(n - 1)$ for every $n \ge 5$. For which positive integers $n$ do these conditions prove $P(n)$?

9. ◦ "Claim: $2^n = 1$ for every natural number $n$. Base case: $2^0 = 1$. Step: let $n \ge 0$ and assume $2^k = 1$ for every $k \le n$. Then $2^{n+1} = 2^n \cdot 2^n / 2^{n-1} = 1 \cdot 1 / 1 = 1$." Find the first $n$ for which the step fails, and say why.

10. • Prove by [induction](/0ASJVEFA9J/) that $n! > 2^n$ for every integer $n \ge 4$.

11. • Prove that $1^3 + 2^3 + \cdots + n^3 = \left( \frac{n(n + 1)}{2} \right)^2$ for every $n \ge 1$.

12. • Prove that $7$ divides $3^{2n+1} + 2^{n+2}$ for every natural number $n$.

13. • Prove by strong induction that every positive integer is a sum of distinct powers of $2$.

14. • An induction on $n$ that tries to prove $\sum_{k=1}^n \frac{1}{k(k + 1)} < 1$ directly gets stuck. Say where, then [strengthen the claim](/F94KJC2RXP/) to an exact formula and prove it.

15. • Use a [minimal counterexample](/JGRCNPKNGG/) to prove that every positive integer $n$ can be written as $n = 2^a m$ with $a$ a natural number and $m$ odd.

16. • Prove by [infinite descent](/0EFYCFHYFG/) that the equation $x^3 = 4y^3$ has no solution in positive integers.

17. • Define $a(m, n)$ for natural numbers $m$ and $n$ by $a(m, 0) = a(0, n) = 1$ and $a(m, n) = a(m - 1, n) + a(m, n - 1)$ for $m, n \ge 1$. Prove that $a(m, n) \le 2^{m+n}$ for all $m$ and $n$, by induction on $m + n$.

18. • Use [forward-backward induction](/QC9FKGZH1V/) to prove that $(x_1 + \cdots + x_n) \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right) \ge n^2$ for all positive reals $x_1, \ldots, x_n$. Do not quote Jensen's inequality; prove the case $n = 2$ and the two steps directly.

19. • The formulas of propositional logic are built from the variables $p, q, r, \ldots$ by the rules: if $A$ is a formula, so is $\neg A$; if $A$ and $B$ are formulas, so are $(A \wedge B)$, $(A \vee B)$ and $(A \to B)$. Prove by [structural induction](/12MQ2NJ29A/) that in every formula the number of occurrences of variables is one more than the number of binary connectives.

20. • The sequence $(a_n)$ is defined by $a_0 = 2$, $a_1 = 3$ and $a_{n+1} = 3a_n - 2a_{n-1}$ for $n \ge 1$. Prove that $a_n = 2^n + 1$ for every natural number $n$. How many base cases does your proof use, and why?

21. • A tournament is a finite set of players in which each two players have played once and one of them won. Prove by [induction on size](/B2D8PTFNN1/) that the players of every tournament can be listed as $v_1, v_2, \ldots, v_n$ so that $v_i$ beat $v_{i+1}$ for each $i < n$.

22. • Prove by induction on the number of elements that every finite nonempty set of real numbers has a largest element.

23. ★ Prove that the only integer solution of $x^2 + y^2 + z^2 = 2xyz$ is $x = y = z = 0$.

24. ★ Prove that every rational number $p/q$ with $0 < p/q < 1$ is a sum of distinct unit fractions $1/n$. Take $1/n$ as large as possible with $1/n \le p/q$, and use strong induction on the numerator.

25. ★ Prove that for every integer $n \ge 6$, a square can be cut into exactly $n$ squares, not necessarily of the same size.

26. ★ Using the base theory (B1) to (B4) of the entry on the [equivalence of induction and well-ordering](/J2P9FWBP3Q/), prove that well-ordering implies induction. Say where you use (B3) and (B4).

27. ★ Let $F_0 = 0$, $F_1 = 1$ and $F_{k+1} = F_k + F_{k-1}$. Prove that $F_{m+n} = F_m F_{n+1} + F_{m-1} F_n$ for all $m \ge 1$ and $n \ge 0$, and deduce that $F_m$ divides $F_{2m}$.
