1. ◦ The numbers $11$, $111$, $11111$ and $1111111$ consist of $2$, $3$, $5$ and $7$ ones. Someone notices that
$11$ is prime and that $2$ is prime, and conjectures that a number written with $p$ ones is prime whenever $p$ is
prime. Test the conjecture on the case $p = 3$, and say which of Pólya's patterns settles it.

2. ◦ A tempting rule says that $n > 1$ is prime exactly when $n$ divides $2^n - 2$. Show that $341 = 11 \cdot 31$
breaks the rule by computing $2^{10}$ modulo $341$ and deducing $2^{341} \equiv 2 \pmod{341}$.

3. ◦ Goldbach conjectured that every odd number greater than $1$ is a prime or a prime plus twice a square,
$p + 2k^2$ with $k \ge 1$. The first exception is $5777$. Check that $5777$ is not prime, and that
$5777 - 2k^2$ is composite for $k = 1, 2, 3$, by giving a factor of each number.

4. ◦ The first four primes are $2, 3, 5, 7$. Find, by finite differences, the value at $n = 5$ of the polynomial of
degree at most $3$ that takes the values $2, 3, 5, 7$ at $n = 1, 2, 3, 4$. Compare it with the fifth prime.

5. ◦ A computation returns $\alpha = 0.7320508075688772\ldots$. Find integers $a, b, c$, not all zero, with
$a + b\alpha + c\alpha^2 = 0$ (to the precision shown), and state the conjectured closed form of $\alpha$.

6. ◦ Compute $\ln \ln x$ for $x = 10^{100}$ and $x = 10^{1000}$, to two decimal places. If a pattern can only fail
where $\ln \ln x > 10$, how much closer to a failure does a check up to $10^{1000}$ get than a check up to
$10^{100}$, on this scale?

7. ◦ Count the primes up to $100$ of the form $4k + 1$ and of the form $4k + 3$. The count of the second kind stays
at least the count of the first kind for every $x$ up to $26860$, and falls behind at $x = 26861$. What does the
table up to $100$ prove about the inequality "$\#\{p \le x : p \equiv 3 \pmod 4\} \ge \#\{p \le x : p \equiv 1 \pmod 4\}$
for all $x$"?

8. ◦ For each item, say whether the support given proves the claim or only makes it more credible.
(a) A program checks $n = 0, 1, \ldots, 39$; claim: $n^2 + n + 41$ is prime for every integer $n$ with
$0 \le n \le 39$. (b) The same program; claim: $n^2 + n + 41$ is prime for every $n \ge 0$. (c) An integer
relation search finds a relation that holds to $200$ digits; claim: the relation is exact. (d) The expected number
of single-coloured copies of $K_k$ in a random red-blue colouring of the edges of $K_n$ is less than $1$; claim:
some colouring of $K_n$ has no single-coloured $K_k$. (e) Soap films between pins always meet in threes at
angles of $120^\circ$; claim: a shortest road network joining the pins has only such junctions.

9. ◦ A line in the plane is the zero set of $ax + by + c$ with $(a, b, c) \neq 0$, and two points in general
position determine one line. Use the same dimension count to predict how many points in general position determine
a curve of degree at most $3$, the zero set of a nonzero polynomial of degree at most $3$ in $x$ and $y$.

10. • Count the ways to write $126$ and $128$ as $p + q$ with primes $p \le q$. The Hardy–Littlewood prediction for
the number of such sums of an even number $n$ contains the factor $\prod (p - 1)/(p - 2)$ over the odd primes $p$
dividing $n$. Compute this factor for $126$ and $128$, and say whether it accounts for the direction of the
difference between the two counts.

11. • List the primes below $60$ that can be written as $x^2 + 2y^2$ with integers $x, y$. Form a conjecture that
describes these primes by their residue modulo $8$, and prove one half of it: an odd prime of the form
$x^2 + 2y^2$ is congruent to $1$ or $3$ modulo $8$.

12. • A naive random model treats "$p$ is prime", "$p + a$ is prime" and "$p + b$ is prime" as independent events.
Show that $p, p + 2, p + 4$ are all prime only for $p = 3$, so the model is wrong for this pattern. Show that no
prime blocks the patterns $(p, p + 2, p + 6)$ and $(p, p + 4, p + 6)$ in the same way, and find the least $p$ for
each.

13. • A computation gives $(1 + \sqrt 2)^{10} = 6725.99985\ldots$. Explain the near-integer: show that
$a_n = (1 + \sqrt 2)^n + (1 - \sqrt 2)^n$ is an integer for every $n \ge 0$, compute $a_{10}$, and bound the
distance from $(1 + \sqrt 2)^{10}$ to $a_{10}$.

14. • Compute $s_n = \sum_{k=0}^{n} \binom{n}{k}^2$ for $n = 1, \ldots, 5$, recognise the values as a known
sequence of binomial coefficients, and prove the resulting formula by counting.

15. • Compute the partial sums $S_N = \sum_{n=1}^{N} \frac{1}{n(n+1)(n+2)}$ for $N = 1, 2, 3, 4$ as fractions.
Guess the limit and a closed form for $S_N$, and prove the closed form.

16. • Erdős's counting argument shows: if $\binom{n}{k} 2^{1 - \binom{k}{2}} < 1$, then some red-blue colouring of
the edges of $K_n$ has no single-coloured $K_k$, so the Ramsey number satisfies $R(k, k) > n$. For $k = 5$, find
the largest $n$ for which the inequality holds, and state the resulting lower bound.

17. • Four pins stand at the corners of a unit square. A soap film between two plates joined by the pins forms a
network with two junctions on the line through the midpoints of two opposite sides, where three segments meet at
$120^\circ$. Compute the total length of this network and compare it with the two diagonals and with three sides
of the square.

18. • A random model says that an odd number near $N$ is prime with probability about $2/\ln N$. Using
$\ln F_n \approx 2^n \ln 2$ for the Fermat numbers $F_n = 2^{2^n} + 1$, estimate the expected number of primes
among $F_5, F_6, F_7, \ldots$ under this model, to two decimal places.

19. • Let $t_n$ be the number of ways to tile a $2 \times n$ rectangle with $1 \times 2$ dominoes. Find
$t_1, \ldots, t_5$ by drawing, form a conjecture, and prove it with a recurrence. What is $t_6$?

20. ★ Prove that no non-constant polynomial $f$ with integer coefficients has $f(n)$ prime for every integer
$n \ge 1$.

21. ★ Fermat studied $2^{2^n} + 1$ rather than $2^m + 1$ for all $m$. Prove that if $2^m + 1$ is prime with
$m \ge 1$, then $m$ is a power of $2$.

22. ★ A conic is the zero set of a nonzero polynomial $ax^2 + bxy + cy^2 + dx + ey + f$. Prove that any five points
of the plane lie on some conic. Then find the conic through $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ and $(2,3)$, and
say what kind of curve it is.

23. ★ Let $g(n)$ be the number of ways to write $n$ as $p + q$ with primes $p \le q$. The Cramér model, with
independent events of probability $1/\ln m$, predicts that $g(n)$ grows like $n/(\ln n)^2$ for all large $n$,
even or odd. Show that $g(n) \le 1$ for every odd $n$, and explain which assumption of the model fails.

24. ★ Prove that if a polynomial $f$ of degree $d$ takes integer values at $x = 0, 1, \ldots, d$, then $f(n)$ is
an integer for every integer $n$, positive or negative. Use the forward differences $\Delta f(x) = f(x+1) - f(x)$
and the polynomials $\binom{x}{k} = x(x-1)\cdots(x-k+1)/k!$.
