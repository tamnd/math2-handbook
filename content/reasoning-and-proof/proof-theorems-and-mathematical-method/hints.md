1. (a) Deductive. (b) Enumerative induction. (c) Abductive. All three conclusions are true: $(10^k + 1)^2 = 10^{2k} + 2 \cdot 10^k + 1$ has the digits $1$, then $k - 1$ zeros, $2$, $k - 1$ zeros, $1$; and $\frac1k - \frac{1}{k+1} = \frac{1}{k(k+1)}$, so the sum of the first $n$ terms is $1 - \frac{1}{n+1} = \frac{n}{n+1}$. The truth of (b) and (c) comes from these deductions, not from the arguments given.

4. For $n = 0, \dots, 15$ the values $17, 19, 23, \dots, 227, 257$ are all prime. At $n = 16$ the value is $289 = 17^2$, and this is forced: $16^2 + 16 + 17 = 16 \cdot 17 + 17 = 17 \cdot 17$.

5. (a) Open. (b) Theorem: Andrew Wiles, proved in 1994 and published in 1995, with one step done jointly with Richard Taylor. (c) Refuted by Euler: $2^{32} + 1 = 641 \cdot 6700417$. (d) Refuted by Lander and Parkin in 1966: $27^5 + 84^5 + 110^5 + 133^5 = 144^5$. (e) Theorem: Grigori Perelman, in work posted in 2002 and 2003. (f) Theorem: Appel and Haken, 1976, with a computer check. (g) Open.

9. $6 \mid 2 \cdot 3$, but $6 \nmid 2$ and $6 \nmid 3$. The statement holds for all $a, b$ exactly when $n$ is prime: for prime $n$ it is Euclid's lemma, and a composite $n = cd$ with $1 < c, d < n$ divides $cd$ but neither $c$ nor $d$.

10. Each line contains $\binom32 = 3$ pairs of points, and each of the $\binom42 = 6$ pairs lies on exactly one line, so there are exactly $6/3 = 2$ lines. Two $3$-element subsets of a $4$-element set share at least two points, and those two points would lie on two lines.

12. Not reflexive: the empty relation on $\set{1, 2}$. Not symmetric: $\le$ on $\set{1, 2}$. Not transitive: on $\set{1, 2, 3}$, the relation containing every $(x, x)$ and $(1,2), (2,1), (2,3), (3,2)$. The argument assumes that some $b$ with $a \mathrel{R} b$ exists; for an element related to nothing there is no such $b$, as the first example shows.

14. (a) $p \mid a^2 - b^2 = (a - b)(a + b)$, and Euclid's lemma gives $p \mid a - b$ or $p \mid a + b$. (b) $3^2 \equiv 1^2 \pmod 8$ with $3 \not\equiv \pm 1$; $4^2 = 16 \equiv 1^2 \pmod{15}$ with $4 \not\equiv \pm 1$. The proof used that the modulus is prime, through Euclid's lemma. (c) $n = 4$: $2^2 \equiv 0^2$ but $2 \not\equiv 0$.

17. The formula gives $31$ for $n = 6$ and $57$ for $n = 7$, not $32$ and $64$, so the conjecture is refuted at $n = 6$. It came from enumerative induction on five cases.

18. An even square is $4k^2$ and an odd square is $4k^2 + 4k + 1$. So a sum of two squares is $0$, $1$ or $2$ modulo $4$, never $3$; and $2023 = 4 \cdot 505 + 3$. The converse is false; the smallest counterexample is $6$, since $6 - 0$, $6 - 1$ and $6 - 4$ are not squares.

23. Fix a point $P$. Each of the other $v - 1$ points lies on exactly one line with $P$, and each line through $P$ contains exactly two of them, so $P$ lies on $r = (v - 1)/2$ lines. Counting pairs (point, line through it) in two ways gives $vr = 3b$, so $b = v(v-1)/6$. Then $v$ is odd and $6 \mid v(v - 1)$, which excludes $v \equiv 5 \pmod 6$. From $6$ to $13$ only $7$, $9$ and $13$ pass. The values $7$ and $9$ do have models: Exercise 11, and the $9$ points of $(\Z/3)^2$ with its $12$ lines.

24. By Exercise 23 there are $7$ lines and each point lies on $3$ of them. Fix a line $L = \set{a, b, c}$. Each of $a, b, c$ lies on two lines other than $L$, which gives $6$ pairs (point of $L$, other line through it). No other line meets $L$ in two points, by the first axiom, and there are exactly $6$ other lines, so each of them meets $L$ in exactly one point.

25. If $f(0)$ is not prime, you are done; otherwise let $p = f(0)$. For every integer $k$, $f(kp) - f(0)$ is a sum of multiples of $kp$, so $p \mid f(kp)$. A polynomial of positive degree takes the value $p$ at only finitely many points, so for some $k \ge 1$ the number $f(kp)$ is a multiple of $p$ other than $p$, and it is not prime. For $f(n) = n^2 + n + 17$ this gives $f(17) = 17 \cdot 19$.

26. Number the rows and columns $0$ to $9$ and give the square $(i, j)$ the colour $(i + j) \bmod 4$. Each $1 \times 4$ tile covers one square of each colour, so $25$ tiles cover $25$ squares of each colour. The colours occur $25$, $26$, $25$ and $24$ times.

27. The values are $3 > 1$, $9 > 8$, $27 = 27$, $81 > 64$, $243 > 125$, $729 > 216$. Conjecture: $3^n \ge n^3$ for all $n \ge 1$, with equality only at $n = 3$. For $n \ge 4$, if $3^n > n^3$ then $3^{n+1} > 3n^3 \ge (n+1)^3$, because $\left(\frac{n+1}{n}\right)^3 \le \left(\frac54\right)^3 = \frac{125}{64} < 3$.
