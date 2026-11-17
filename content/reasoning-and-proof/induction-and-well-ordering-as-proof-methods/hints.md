1. The values of $n!$ are $1, 1, 2, 6, 24, 120$ and of $2^n$ are $1, 2, 4, 8, 16, 32$. So $n_0 = 4$; Exercise 10 proves that the inequality holds from there on.

2. $4^{n+1} + 1 = 4(4^n + 1) - 3$, so the step holds. But $4^n + 1$ leaves remainder $2$ on division by $3$ for every $n$, so $P(n)$ is never true. A valid step proves nothing without a base case.

4. The numbers $3, 5, 6, 8, 9, 10, 11, 12$ have this form and $1, 2, 4, 7$ do not. The step from $n - 3$ to $n$ needs the three base cases $8$, $9$ and $10$.

5. The step fails when $a = 0$ or $b = 0$, for example $a = 0$ and $b = 1$: then $a - 1 = -1$ is not a natural number, so the induction hypothesis does not apply.

8. Doubling from $1$ gives $2, 4, 8, 16, \ldots$, and stepping down from $2^k$ reaches every $n \ge 4$. The number $3$ is reached by neither rule, since stepping down to $3$ would need the step from $4$. So the conditions give $P(n)$ for every $n \ne 3$.

9. It fails at $n = 0$: the step uses $2^{n-1} = 2^{-1}$, which is not a case of the hypothesis, and $2^{-1} \ne 1$. So the step from $0$ to $1$ is never proved.

14. From "the sum up to $n$ is less than $1$" nothing stops the next term from pushing it past $1$. Prove instead that the sum equals $1 - \frac{1}{n + 1}$; the step is $1 - \frac{1}{n + 1} + \frac{1}{(n + 1)(n + 2)} = 1 - \frac{1}{n + 2}$.

16. If $x^3 = 4y^3$, then $x$ is even, $x = 2x_1$, and $y^3 = 2x_1^3$, so $y = 2y_1$ and $x_1^3 = 4y_1^3$. This is a solution with a smaller $x$.

18. The case $n = 2$ is $4xy \le (x + y)^2$. Write the claim as $\frac{n}{x_1 + \cdots + x_n} \le \frac{1}{n} \sum \frac{1}{x_i}$. For the step down from $n$ to $n - 1$, apply the claim for $n$ numbers with $x_n$ equal to the mean of $x_1, \ldots, x_{n-1}$.

21. Remove one player $v$ and list the others as $v_1, \ldots, v_n$. If $v$ beat $v_1$, put $v$ first; if $v_n$ beat $v$, put $v$ last. Otherwise let $i$ be the least index with $v$ beating $v_i$; then $i \ge 2$, $v_{i-1}$ beat $v$, and $v$ fits between them.

23. Prove the stronger claim that $x^2 + y^2 + z^2 = 2^k xyz$ with $k \ge 1$ has only the zero solution. The right side is even, so an even number of $x, y, z$ are odd. If two are odd, the left side is $2$ modulo $4$ and the right side is divisible by $4$. So all three are even, and halving them gives a solution of the equation with $2^{k+1}$, with smaller $\abs{x} + \abs{y} + \abs{z}$ unless all are $0$.

24. If $n$ is least with $1/n \le p/q$, then $p(n - 1) < q$, so $p/q - 1/n = (pn - q)/(qn)$ has a numerator less than $p$. Also $p/q - 1/n < \frac{1}{n - 1} - \frac{1}{n} \le \frac{1}{n}$, so the unit fractions for the remainder are all smaller than $1/n$, and the denominators are distinct.

25. Cutting one square into four adds $3$, so it is enough to do $6$, $7$ and $8$. For $6$, take a $3 \times 3$ grid and merge four cells into one square. For $7$, cut one quarter of a $2 \times 2$ grid into four. For $8$, take a $4 \times 4$ grid and merge nine cells.

26. Suppose $0 \in A$, $A$ is closed under $S$, and $A \ne N$. The complement has a least element $b$, and $b \ne 0$. By (B4), $b = S(k)$, and by (B3), $k < b$, so $k \in A$ by the choice of $b$. Then $b = S(k) \in A$, a contradiction.

27. Induct on $m$ for all $n$ at once, with base cases $m = 1$ and $m = 2$. The step adds the identities for $m$ and $m - 1$. For the divisibility, take $n = m$: $F_{2m} = F_m (F_{m+1} + F_{m-1})$.
