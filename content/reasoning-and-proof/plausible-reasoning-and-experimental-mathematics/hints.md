2. $f(80) = 6400 - 6320 + 1601 = 1681 = 41^2$. With $m = n - 40$, $f(n) = m^2 + m + 41$. As $n$ runs over $0, \ldots, 79$, $m$ runs over $-40, \ldots, 39$, and $m^2 + m + 41$ takes the same value at $m$ and $-1 - m$, so the $80$ values are the $40$ primes of $m^2 + m + 41$ for $m = 0, \ldots, 39$, each taken twice.

5. $128 = 19 + 109 = 31 + 97 = 61 + 67$, three ways. Powers of $2$ have few partitions because $128$ is not divisible by small odd primes, so $128 - p$ is less often prime. The conjecture asks only for one partition.

6. $L(n) = 1, 0, -1, 0, -1, 0, -1, -2, -1, 0$. Haselgrove proved in 1958 that the conjecture fails, and the least counterexample, $n = 906150257$, was found by Tanaka in 1980.

10. The partial sums are $\frac{1}{6}, \frac{5}{24}, \frac{9}{40}, \frac{7}{30}, \frac{5}{21}$. Write the term as $\frac{1}{2}\left(\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right)$; the sum telescopes to $\frac{1}{4}$.

11. From $5 \cdot 2^7 \equiv -1 \pmod{641}$, raising to the fourth power gives $5^4 \cdot 2^{28} \equiv 1$. Since $5^4 \equiv -2^4$, this gives $-2^{32} \equiv 1$.

12. Use Pascal's rule twice: $\binom{n}{4} = \binom{n-1}{4} + \binom{n-1}{3}$ and $\binom{n}{2} = \binom{n-1}{2} + \binom{n-1}{1}$. The sum equals $2^{n-1} = \sum_{k=0}^{n-1} \binom{n-1}{k}$ exactly when no terms with $k \ge 5$ are missing.

14. Each $F_n$ is prime with probability about $1/\ln F_n \approx 1/(2^n \ln 2)$. The sum over $n \ge 5$ is $\frac{1}{16 \ln 2} \approx 0.09$.

16. It assumes that a curve of largest area exists. The integer argument makes the same assumption, and there it is false.

17. The recurrence $a_n = 2a_{n-1} + a_{n-2}$ with $a_0 = a_1 = 2$ shows that each $a_n$ is an integer; $a_{10} = 6726$. Since $\abs{1 - \sqrt{2}} < 1/2$, the second term is tiny, about $1.5 \cdot 10^{-4}$.

19. If $p(n_0) = q$ is prime, then $q$ divides $p(n_0 + kq)$ for every $k$, since $p(n_0 + kq) \equiv p(n_0) \pmod q$. A nonconstant polynomial takes the values $\pm q$ only finitely often.

20. Since $2^{2^n} \equiv -1 \pmod p$, the order of $2$ modulo $p$ is exactly $2^{n+1}$, and it divides $p - 1$. For $F_5$ the primes allowed are $193, 257, 449, 577, 641$. Since $p \equiv 1 \pmod 8$, $2$ is a square mod $p$, which improves the condition to $p \equiv 1 \pmod{128}$, leaving $257$ and $641$.

21. $1, 2, 6, 20, 70, 252$ are the central binomial coefficients $\binom{2n}{n}$. Sort the choices by the number $k$ of women chosen and use $\binom{n}{n-k} = \binom{n}{k}$.

22. Each term is at least $1/(\ln n)^2$ and there are $n - 3$ terms. For odd $n$ one of $k$ and $n - k$ is even, so at most one partition exists. The model must take account of divisibility by small primes, which leads to the singular series of Hardy and Littlewood.
