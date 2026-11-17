1. Contrapositive: if $4 \nmid n^2$, then $6 \nmid n$. Converse: if $4 \mid n^2$, then $6 \mid n$. Inverse: if $6 \nmid n$, then $4 \nmid n^2$. The statement and its contrapositive are true, because $6 \mid n$ makes $n$ even and then $4 \mid n^2$. The converse and the inverse are false: take $n = 2$.

3. The proof fixes one element, so it proves the claim for $x = 2$ only. For arbitrary real $x$, $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1 > 0$.

4. Only $n = 4$, since $21 = 3 \cdot 7$. For $n = 1, 2, 3$ the values $3, 7, 13$ are prime. The value $1$ at $n = 0$ is not prime, but $0$ is not a positive integer, so it fails the hypothesis and is not a counterexample.

5. The case $-1 < x < 1$. There $\abs{x - 1} + \abs{x + 1} = (1 - x) + (x + 1) = 2$.

6. $x^3 = x$ has the solutions $-1$, $0$ and $1$: existence holds and uniqueness fails. Among positive reals, $x^3 = x$ means $x^2 = 1$, so $x = 1$ is the only solution: both hold.

8. The first arrow holds only from left to right, since squaring loses the sign. The other two hold both ways. Checking: $x = 5$ gives $2 = 2$, while $x = 2$ gives $-1 = 1$. The only solution is $x = 5$.

11. Prove the contrapositive: if $n = 2k + 1$, then $n^2 - 1 = 4k(k + 1)$, and $k(k + 1)$ is even.

13. If $s = \sqrt 2 + \sqrt 3$ were rational, then so would be $s^2 = 5 + 2\sqrt 6$, and so $\sqrt 6 = (s^2 - 5)/2$.

14. Factor $n^5 - n = n(n - 1)(n + 1)(n^2 + 1)$. If $n \equiv 0, 1, 4$ modulo $5$, one of the first three factors is divisible by $5$; if $n \equiv 2$ or $3$, then $n^2 + 1 \equiv 0$.

17. Existence: $x^3 + x - 1$ is $-1$ at $0$ and $1$ at $1$, so the intermediate value theorem gives a root in $(0, 1)$. Uniqueness: if $x < y$, then $x^3 + x < y^3 + y$. The existence part is not constructive, though bisection makes it so.

23. Let $p_1, \ldots, p_k$ be any finite list of such primes and let $N = 4 p_1 \cdots p_k - 1$. Then $N \equiv 3 \pmod 4$ and $N$ is odd. A product of numbers that are $1$ modulo $4$ is $1$ modulo $4$, so $N$ has a prime factor $q \equiv 3 \pmod 4$, and $q$ is not in the list, since every prime in the list divides $N + 1$ and $q$ cannot divide both $N$ and $N + 1$.

24. Prove the contrapositive. If $n = ab$ with $1 < a < n$, then $2^a - 1$ divides $2^{ab} - 1$, because $x - 1$ divides $x^b - 1$; and $1 < 2^a - 1 < 2^n - 1$. For the converse, $2^{11} - 1 = 2047 = 23 \cdot 89$.

25. Suppose $\sqrt n = a/b$ in lowest terms, so $a^2 = n b^2$. If a prime $p$ divides $b$, then $p \mid a^2$, so $p \mid a$, against lowest terms. So $b = 1$ and $n = a^2$.

26. For integers $u \ne v$, $u - v$ divides $u^k - v^k$ for each $k$, so $u - v$ divides $p(u) - p(v)$. Here $3 - 1 = 2$ would have to divide $5 - 2 = 3$.

27. The right side is cyclic, not symmetric: exchanging $b$ and $c$ changes it to $a^2 c + c^2 b + b^2 a$. By the inequality of arithmetic and geometric means, $a^3 + a^3 + b^3 \ge 3a^2 b$. Add the three cyclic versions of this inequality.
