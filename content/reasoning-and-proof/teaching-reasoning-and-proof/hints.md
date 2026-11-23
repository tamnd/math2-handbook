1. Turn the $8$, which must be red on the back, and the blue card, which must not have an even number. The $3$ and the red card cannot break the rule. Matching bias predicts the $8$ and the red card, the two named in the rule.

3. (a) Empirical, inductive. (b) External conviction, authoritarian. (c) Deductive, transformational. (d) External conviction, non-referential symbolic: the step $a + b + c = 3a$ is false for numbers, since $1 + 3 + 5 \ne 3$. (e) External conviction, ritual.

5. Questions (a), (b) and (c) are local: they ask about the logical status of a statement, the justification of a step and the meaning of a term. Questions (d) to (g) are holistic: summary, modules, transfer and illustration. The answer to (f) is yes, with $n(n + 1) + 2(n + 1) = (n + 1)(n + 2)$.

11. The student proved the converse, "if $3 \mid n$ then $3 \mid n^2$", a difficulty with logic. Prove the contrapositive. If $3 \nmid n$, then $n = 3k + 1$ or $n = 3k + 2$, and $n^2 = 3(3k^2 + 2k) + 1$ or $n^2 = 3(3k^2 + 4k + 1) + 1$, so $3 \nmid n^2$.

13. The correct negation is $\exists \varepsilon > 0\ \forall N\ \exists n \ge N\ \abs{a_n - L} \ge \varepsilon$. For $a_n = (-1)^n$ and $L = 1$, the student's statement is false, since every even $n$ gives $\abs{a_n - 1} = 0$. The correct negation is true with $\varepsilon = 1$: for any $N$, an odd $n \ge N$ gives $\abs{-1 - 1} = 2$.

14. The data are the four computations and the claim is "for every prime $p$". The unstated warrant is "a pattern that holds in the cases checked holds in all cases". A rebuttal is $p = 11$: $2^{11} - 1 = 2047 = 23 \cdot 89$. The scheme is empirical, inductive.

16. Argument (a) is generic: with $a$ and $b$ for the digits, $10a + b = 9a + (a + b)$, and every step stays true. Argument (b) only checks cases. Its suggested claim is false: $99 = 11 \cdot 9$ has digit sum $18$.

17. (a) True: $b = ak$ and $c = bl$ give $c = a(kl)$. (b) True: $b + c = a(k + l)$. (c) False: $2 \mid 1 + 1$ but $2 \nmid 1$. (d) False: $2 \mid -2$ and $-2 \mid 2$. It becomes true for positive $a$, $b$. (e) False: $2 \mid -2$ but $2 > -2$. It becomes true for positive $b$.

19. (a) An assumption made for contradiction; it is never proved. (b) $\log_2 3 > 0$ because $3 > 1 = 2^0$. (c) $a \ge 1$, so $2^a$ is even, and $3^b$ is a product of odd numbers. (d) Yes, since $2^a = 5^b$ fails in the same way. (e) The equation $4^a = 8^b$ becomes $2^{2a} = 2^{3b}$, where both sides are even, and it holds for $a = 3$, $b = 2$, so $\log_4 8 = \tfrac32$. Questions (a) to (c) are local, and (d) and (e) are holistic: transfer and illustration.

20. (a) Valid. (b) Not valid: dividing by $x$ keeps the direction of the inequality only when $x > 0$. The claim is false, since $x = -1$ gives $1 > -1$.

23. (a) False, with $x = -3$. (b) True. (c) True, with $x = 0$, since the hypothesis is false. (d) True, since no real $x$ has $x^2 < 0$. (e) False. Under the defective reading the instance $x = 1$ of (b), "if $1 > 2$ then $1 > 4$", is neither true nor false. A universal statement is true only if every instance is true, so if (b) is a theorem, this instance must count as true. This is the reading of conditionals as universally quantified open sentences.

24. Add the circles one at a time. The first gives $2$ regions. The $k$-th circle meets the earlier ones in $m \le 2(k - 1)$ points. If $m \ge 1$, these points cut it into $m$ arcs, and each arc splits one region into two; if $m = 0$, it adds one region. So the total is at most $2 + \sum_{k=2}^{n} 2(k - 1) = n^2 - n + 2$. The bound gives $2, 4, 8, 14$ for $n = 1, 2, 3, 4$, so the largest $n$ is $3$. For $n \ge 4$, induction shows $2^n > n^2 - n + 2$: going from $n$ to $n + 1$ adds $2^n$ on the left and $2n$ on the right, and $2^n > 2n$ for $n \ge 3$.

25. Let $c = N^2 + N + 41$ and $p(n) = n^2 + n + 41 + c \cdot n(n - 1) \cdots (n - N + 1)$. The product vanishes at $n = 0, \dots, N - 1$, so $p$ agrees with $n^2 + n + 41$ there. At $n = N$ the product is $N!$, so $p(N) = c\,(1 + N!)$, a product of two integers greater than $1$. However many cases a class checks, some formula fits all of them and fails at the next.

26. The scheme is empirical, inductive. Put $m = n^2 + 3n + 1$. Then $n(n + 3) = m - 1$ and $(n + 1)(n + 2) = m + 1$, so the product plus $1$ is $(m - 1)(m + 1) + 1 = m^2$. Generically: $3 \cdot 6 = 18$ and $4 \cdot 5 = 20$ differ by $2$, so $18 \cdot 20 + 1 = (19 - 1)(19 + 1) + 1 = 19^2$. With letters the outer and inner products always differ by $2$, which is the step to check.

27. Let $a_n = 1 + \tfrac1n$. Each term is closer to $0$ than the last, but $\abs{a_n - 0} > 1$ for all $n$, so $\varepsilon = 1$ defeats every $N$; the limit is $1$. Let $a_n = 0$ for even $n$ and $a_n = \tfrac1n$ for odd $n$. Each odd $n \ge 3$ gives a term farther from $0$ than the term before, yet $\abs{a_n} \le \tfrac1n < \varepsilon$ for all $n > \tfrac1\varepsilon$.
