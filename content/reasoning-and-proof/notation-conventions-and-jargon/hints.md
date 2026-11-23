2. (a) Free: $n$ and $x$; bound: $k$; the value is $2 + 8 + 24 = 34$. (b) Free: $x$; bound: $t$; the value is $9$. (c) Free: $a$; bound: $y$. (d) Free: $x$, $a$ and $f$; bound: $\varepsilon$ and $\delta$. The letter $x$ in (d) is free because no quantifier binds it.

7. (a) Eventually, with least threshold $51$; at $n = 50$ the two sides are equal. (b) Frequently, not eventually: every fifth number satisfies it and the others do not. (c) Neither, since it fails for every $n \ge 1000$. (d) The last digits of $2^1, 2^2, 2^3, 2^4, \dots$ repeat as $2, 4, 8, 6$, so the property holds exactly for $n \ge 4$ with $4 \mid n$: frequently, not eventually.

8. (a) Strictly stronger; $x = -3$ satisfies the second and not the first. (b) Equivalent: if $16 \mid n^2$, then $n = 2m$ and $4 \mid m^2$, so $m$ is even and $4 \mid n$. (c) Strictly stronger; $9$ is odd and not prime. (d) Strictly stronger; $x = \sqrt2$.

9. (a) True, since $\tfrac13 - x + x^2 = (x - \tfrac12)^2 + \tfrac1{12} > 0$, but not sharp. The sharp constant is $\tfrac14$, attained at $x = \tfrac12$. (b) $C = \tfrac12$: the function $x/(1 + x)$ is increasing and tends to $\tfrac12$ as $x \to 1$, so every smaller constant fails near $1$, and the value $\tfrac12$ is not attained on $(0, 1)$.

10. (a) Both: the exceptions are $0, \dots, 9$. (b) Density only: the powers of $2$ are infinite, but at most $\log_2 n + 1$ of them lie in $\set{1, \dots, n}$. (c) Neither: the exceptions are infinite and have density $\tfrac14$. (d) True in all three senses, because the exceptions $k\pi$, $k \in \Z$, form a countable set.

11. (a) and (d) use only the given data, so they are canonical. (b) Another basis changes the matrix $A$ into $P^{-1} A P$, and $\det(P^{-1} A P) = \det A$, so the number does not depend on the basis. (c) The two bases give the matrices $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(4, 1)$, with traces $2$ and $5$, so the construction is not canonical.

13. The inequality holds for $n = 0, 1$ and for every $n \ge 17$; it fails for $2 \le n \le 16$, with equality $2^{16} = 16^4 = 65536$ at $n = 16$. For the step, $(n + 1)^4 / n^4 = (1 + 1/n)^4 \le (18/17)^4 = 104976/83521 < 2$.

15. (a) Yes: $(a + tn)^2 = a^2 + n(2at + t^2 n)$. (b) Yes: $3^4 = 81 \equiv 1 \pmod 5$, so $3^{a + 4t} \equiv 3^a$. (c) No: $[0] = [4]$ in $\Z/4$, but $2^0 = 1$ and $2^4 = 16 \equiv 2 \pmod 7$.

16. The exceptions are the $n$ with $\gcd(n, 210) = 1$. Each block of $210$ consecutive integers contains exactly $1 \cdot 2 \cdot 4 \cdot 6 = 48$ of them, so the share in $\set{0, \dots, n}$ tends to $48/210 = 8/35$. The exceptions have positive density, and the statement is false.

22. If $10^k \le n < 10^{k+1}$, every number in $\set{0, \dots, n}$ without the digit $7$ has at most $k + 1$ digits, so there are at most $9^{k+1}$ of them, and their share is at most $9^{k+1}/10^k = 9 \cdot (0.9)^k$, which tends to $0$. The cofinite sense fails because the numbers $10^m$ are infinitely many exceptions.

23. Fix $k$. For $n \ge 2k + 2$, each factor of $n(n - 1) \cdots (n - k)$ is at least $n/2$, so $2^n > \binom{n}{k+1} \ge (n/2)^{k+1}/(k+1)!$, and this exceeds $n^k$ once $n > 2^{k+1}(k+1)!$. For the second statement, every $n \ge 2$ fails with $k = n$, since $n^n \ge 2^n$. The first is $\forall k \, \exists N \, \forall n \ge N$, the second $\exists N \, \forall n \ge N \, \forall k$.

24. At $0$, the difference quotient is $h \sin(1/h)$, and $\abs{h \sin(1/h)} \le \abs h$, so $f'(0) = 0$. For $x \ne 0$, $f'(x) = 2x \sin(1/x) - \cos(1/x)$. At $x_k = 1/(2k\pi)$ this is $-1$, and $x_k \to 0$, so $f'(x)$ does not tend to $f'(0)$.

25. Transitivity: add $a + d = b + c$ and $c + f = d + e$ and cancel $c + d$. The form depends only on the integer $a - b$, and $(a, b) \sim (c, d)$ says exactly that $a - b = c - d$. Then $c(3, 8) = c(10, 15) = (0, 5)$, so these are equivalent, while $c(7, 2) = (5, 0) \ne (0, 5) = c(2, 7)$.

26. $C = 9$. Expand the product as $3 + (a/b + b/a) + (a/c + c/a) + (b/c + c/b)$, and use $t + 1/t \ge 2$ for $t > 0$, which is $(t - 1)^2 \ge 0$, with equality only at $t = 1$. Equality holds exactly when $a = b = c$, so $9$ is attained and no larger constant works.
