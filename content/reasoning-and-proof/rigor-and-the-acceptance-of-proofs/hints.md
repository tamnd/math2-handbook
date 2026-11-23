1. $f(0) = 0$ and $f(x) = 1$ for $0 < x \le 1$, since $x^{1/n} = e^{(\ln x)/n} \to 1$. The limit is not
continuous at $0$. The convergence cannot be uniform, because a uniform limit of continuous functions is
continuous.

2. A common point has $2x^2 = 1$, so $x = \pm 1/\sqrt 2$, which is irrational. The plane $\Q^2$ satisfies many
axioms of geometry but not the continuity that guarantees that a line through an inside point meets the circle.

3. $f(1) = -1$ and $f(2) = 6$. A rational zero $p/q$ in lowest terms would need $p \mid 2$ and $q \mid 1$, so it
would be $\pm 1$ or $\pm 2$, and none is a zero. The domain is not an interval of $\R$: completeness fails.

4. $1 \le a_n \le 2$, and $\abs{a_n - \sqrt 2} < 10^{-n}$, so $a_n \to \sqrt 2$ in $\R$ and so does every
subsequence. A limit is unique and $\sqrt 2 \notin \Q$, so no subsequence has a rational limit.

5. Each semicircle has length $\pi \cdot \frac{1}{2n}$, so the total is $\pi/2$ for every $n$. Every point of the
curve lies within $\frac{1}{2n}$ of the segment, but arc length is not continuous under this kind of convergence:
the limit of the lengths need not be the length of the limit.

6. (a) $1001 = 7 \cdot 143$ (indeed $7 \cdot 11 \cdot 13$); multiplying checks it. (b) Every integer is congruent
to one of $0, \ldots, 6$, whose squares are $0, 1, 4, 2, 2, 4, 1$ modulo $7$. The reader must check all seven
cases; a claim that no solution exists has no one-line certificate here.

7. Kempe (1879), Heawood (1890), Appel and Haken (1976), Robertson, Sanders, Seymour and Thomas (1997),
Gonthier and Werner (2005).

8. Modus ponens takes $P$ and $P \to Q$ to $Q$; line 3 runs it backwards (affirming the consequent). With $P$
false and $Q$ true both hypotheses are true and $P$ is false.

9. $f(x) = 1/x$ is continuous and unbounded on $(0, 1)$. The theorem needs a closed bounded interval $[a, b]$.

11. 1. $P \to (Q \to R)$ (assumption). 2. $Q$ (assumption). 3. $P$ (assumption). 4. $Q \to R$ ($\to$E, 1, 3).
5. $R$ ($\to$E, 4, 2). 6. $P \to R$ ($\to$I, 3–5). 7. $Q \to (P \to R)$ ($\to$I, 2–6). 8. The whole formula
($\to$I, 1–7).

12. $f_n'(x) = x^{n-1}(n - (n+1)x)$, so the maximum is at $x = n/(n+1)$ and equals
$\frac{n^n}{(n+1)^{n+1}} \le \frac{1}{n+1}$. Hence $\sup_{[0,1]} f_n \to 0$.

13. Divide the square into four quarters, shade one, leave two white, and repeat the division inside the fourth;
at each stage three equal squares of area $4^{-k}$ appear, one of them shaded, so a third of the divided area is
shaded. Algebraically $\sum_{k=1}^{n} 4^{-k} = \frac13 (1 - 4^{-n})$. The picture leaves
out the limit: the undivided square at stage $n$ has area $4^{-n}$, which tends to $0$.

15. In a split of $\set{1, 2, 3, 4}$, $1$ and $2$ must be in different sets ($1 + 1 = 2$), and so must $2$ and $4$;
so $1$ and $4$ go together, and $3$ cannot join $1$ ($1 + 3 = 4$), so the split is $\set{1, 4}$, $\set{2, 3}$.
Adding $5$: it cannot join $\set{1, 4}$ ($1 + 4 = 5$) or $\set{2, 3}$ ($2 + 3 = 5$). A program would check
$2^5 = 32$ colourings, or $16$ up to swapping the colours.

16. Resolve $x \lor y$ with $\lnot x \lor y$ to get $y$; resolve $x \lor \lnot y$ with $\lnot x \lor \lnot y$ to
get $\lnot y$; resolve $y$ with $\lnot y$ to get the empty clause. Each step can be checked mechanically, much
more easily than the derivation was found.

18. If a prime $p \le n$ divided $n! + 1$, it would divide $n!$ and hence $1$. So for every $n$ there is a prime
greater than $n$. But $5! + 1 = 121 = 11^2$ is not prime.

19. If $u \in S$ then $v^2 < 3$ and $v > u$, so $u$ is not largest. If $u > 0$ and $u^2 > 3$ then $v^2 > 3$ and
$v < u$, so $u$ is not least among the upper bounds. And $u^2 = 3$ has no rational solution.

20. 1. $(p \to ((p \to p) \to p)) \to ((p \to (p \to p)) \to (p \to p))$ (second axiom). 2.
$p \to ((p \to p) \to p)$ (first axiom). 3. $(p \to (p \to p)) \to (p \to p)$ (modus ponens, 2, 1). 4.
$p \to (p \to p)$ (first axiom). 5. $p \to p$ (modus ponens, 4, 3).

21. Induction on $n$; $p_1 = 2 = 2^{2^0}$. The number $p_1 p_2 \cdots p_n + 1$ has a prime factor not among
$p_1, \ldots, p_n$, so $p_{n+1} \le p_1 \cdots p_n + 1 \le 2^{1 + 2 + \cdots + 2^{n-1}} + 1 = 2^{2^n - 1} + 1
\le 2^{2^n}$.

22. For $x \ne 0$ the series is geometric with ratio $1/(1 + x^2) < 1$, and its sum is
$x^2 \cdot \frac{1 + x^2}{x^2} = 1 + x^2$. At $x = 0$ every term is $0$. The sum jumps at $0$, so the convergence
is not uniform on any interval containing $0$. This contradicts Cauchy's claim that a convergent series of
continuous functions has a continuous sum.

23. With $1 < \sqrt 2 < 2$ we get $b < a < 2b$. From $a^2 = 2b^2$ one checks
$(2b - a)^2 = 2(a - b)^2$, so $\sqrt 2 = (2b - a)/(a - b)$ with $0 < a - b < b$, contradicting the choice of $b$.

24. One answer: $\set{1, 4, 10, 13}$, $\set{2, 3, 11, 12}$, $\set{5, 6, 7, 8, 9}$. In the third set every sum is at
least $10$; in the first two, list the sums $x + y$ with $x \le y$ and check that none lies in the set. No split of
$\set{1, \ldots, 14}$ into three such sets exists.
