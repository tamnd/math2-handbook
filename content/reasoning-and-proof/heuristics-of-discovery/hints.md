1. (a) A heuristic: it may or may not show a pattern. (b) An algorithm: it always ends with a quotient and a remainder. (c) A heuristic. (d) A proof: each step is justified, and the conclusion is certain.

3. For $n = 1, \ldots, 10$ the values $11, 13, 17, 23, 31, 41, 53, 67, 83, 101$ are all prime. At $n = 11$ the value is $121 = 11^2$.

5. Put $y = x^3$. Then $y^2 - 9y + 8 = (y - 1)(y - 8) = 0$, so $x^3 = 1$ or $x^3 = 8$, and $x = 1$ or $x = 2$. The reduction is bilateral: the real solutions in $x$ and the solutions in $y$ correspond one to one, since $x \mapsto x^3$ is a bijection of $\R$.

6. (a) Local but not global: a diagonal from $V$ runs outside the dart, so the lemma fails, but the angles still add up to $360^\circ$. (b) Global: each point of the star has an angle of $36^\circ$, so the sum is $180^\circ$, not $540^\circ$. The lemma fails as well. One can also bar this "monster" by defining a polygon to be simple.

7. The two evenings are preparation, Saturday is incubation, the bus is illumination, and Sunday is verification. The missing case shows why verification is a stage of its own.

8. The ride takes $\frac{1}{2} + \frac{3}{4} = \frac{5}{4}$ hours for $60$ km, so the average is $48$ km/h. The intuition averages the speeds as if equal *times* were spent at each; here equal *distances* are, and the right mean is the harmonic mean.

11. By the angle bisector theorem, the bisector from $A$ meets $BC$ at $D$ with $BD : DC = AB : AC$. So $D$ is the midpoint exactly when $AB = AC$. For the ratio $1 : 2$, take $AB = 3$, $AC = 6$ and $BC = 6$.

12. From $\sum_{k \le n} 1/k^2 < 2$ you only get $\sum_{k \le n+1} 1/k^2 < 2 + \frac{1}{(n+1)^2}$. For the stronger statement the step needs $\frac{1}{(n+1)^2} \le \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}$, which is true.

14. The first player wins. The totals to reach are those that leave $100$ a multiple of $11$ away: $1, 12, 23, \ldots, 89, 100$. The first player says $1$, and after the opponent adds $k$, adds $11 - k$.

16. $2^{100} \equiv 0 \pmod 4$. Since $2^{10} = 1024 \equiv -1 \pmod{25}$, we get $2^{100} \equiv 1 \pmod{25}$. The only number from $0$ to $99$ that is $0$ modulo $4$ and $1$ modulo $25$ is $76$.

17. Without the second condition, the locus is the circle $x^2 + y^2 = 1$ with $A$ and $B$ removed. Intersecting with the lines $y = \pm\frac{1}{2}$ gives the four points $\left(\pm\frac{\sqrt{3}}{2}, \pm\frac{1}{2}\right)$.

20. Take $n = 6$, $a = 2$, $b = 3$. The refuted lemma is "if $n \nmid a$, then $\gcd(n, a) = 1$", which holds for every $a$ exactly when $n$ is prime. Corrected theorem: if $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$. (Another correct form keeps any $n$ and adds the hypothesis $\gcd(n, a) = 1$.)

21. A square of side $k$ cells can be placed in $(n - k + 1)(m - k + 1)$ ways, so the number is $\sum_{k=1}^{n} (n - k + 1)(m - k + 1)$. For $3 \times 5$ it is $15 + 8 + 3 = 26$.

22. The guess is $1 + n + \binom{n}{2} + \binom{n}{3}$, which gives $2, 4, 8$ for $n = 1, 2, 3$ and $15$ for $n = 4$. For the proof, the $n$-th plane meets the other $n - 1$ planes in $n - 1$ lines in general position, which cut it into $1 + (n - 1) + \binom{n-1}{2}$ pieces; each piece splits one region of space into two.

23. For $\frac{1}{\sqrt{3n}}$ the step needs $(2n+1)^2 (3n+3) \le (2n+2)^2 \cdot 3n$, which reduces to $n + 1 \le 0$. For $\frac{1}{\sqrt{3n+1}}$ it needs $(2n+1)^2(3n+4) \le (2n+2)^2(3n+1)$, which reduces to $19n \le 20n$.

24. Let $I(t) = \int_0^1 \frac{x^t - 1}{\ln x}\, dx$. Then $I'(t) = \int_0^1 x^t\, dx = \frac{1}{t+1}$ and $I(0) = 0$, so $I(t) = \ln(1 + t)$ and the answer is $\ln 6$.

25. If $p_1, \ldots, p_k$ were all the irreducible polynomials, then $p_1 p_2 \cdots p_k + 1$ has degree at least $1$, so it has an irreducible factor. That factor is some $p_i$, and then $p_i$ divides $1$, which is impossible.
