1. $111 = 3 \cdot 37$, so the conjecture is false. The prime $11$ only made it more credible; the false case $111$
refutes it by the demonstrative pattern "$A$ implies $B$, $B$ false, so $A$ false", which is deduction. (Also
$11111 = 41 \cdot 271$ and $1111111 = 239 \cdot 4649$.)

3. $5777 = 53 \cdot 109$, $5775 = 3 \cdot 5^2 \cdot 7 \cdot 11$, $5769 = 3^2 \cdot 641$ and $5759 = 13 \cdot 443$.
The remaining cases $k = 4, \ldots, 53$ are also composite, which is what makes $5777$ an exception.

5. $\alpha^2 + 2\alpha - 2 = 0$, that is $(a, b, c) = (-2, 2, 1)$; the positive root is $\alpha = \sqrt 3 - 1$. The
relation is a conjecture until it is checked to more digits or proved.

6. $\ln \ln 10^{100} \approx 5.44$ and $\ln \ln 10^{1000} \approx 7.74$. The larger check covers $10^{900}$ times
as many numbers but moves only $2.30$ on the scale, and still stops well short of $10$.

7. There are $11$ primes of the form $4k + 1$ and $13$ of the form $4k + 3$ up to $100$. The table proves the
inequality for $x \le 100$ and nothing beyond; the statement for all $x$ is false, with $26861$ as the first
counterexample.

8. (a) Proof: the claim is about finitely many cases, and all were checked. (b) Only more credible, and in fact
false at $n = 40$. (c) Only more credible. (d) Proof: if every colouring had a single-coloured $K_k$, the
expected number would be at least $1$. (e) Only more credible; it is a physical argument.

10. $126$ has $10$ representations and $128$ has $3$ ($19 + 109$, $31 + 97$, $61 + 67$). Since
$126 = 2 \cdot 3^2 \cdot 7$, the factor is $\frac{2}{1} \cdot \frac{6}{5} = 2.4$, while $128 = 2^7$ gives $1$. The
factor predicts more sums for $126$, in the observed direction; the rest of the gap is the noise of small numbers.

12. One of $p, p + 2, p + 4$ is divisible by $3$, so it equals $3$. For $(0, 2, 6)$ and $(0, 4, 6)$ the residues
modulo $3$ are $\{0, 2\}$ and $\{0, 1\}$, which miss a class, and three numbers cannot fill all classes modulo a
prime $q \ge 5$. The least examples are $5, 7, 11$ and $7, 11, 13$.

13. Expand by the binomial theorem: the odd powers of $\sqrt 2$ cancel, or use $a_0 = a_1 = 2$ and
$a_n = 2a_{n-1} + a_{n-2}$, since $1 \pm \sqrt 2$ are the roots of $t^2 = 2t + 1$. Then $a_{10} = 6726$, and
$a_{10} - (1 + \sqrt 2)^{10} = (\sqrt 2 - 1)^{10} < 0.42^{10} < 2 \cdot 10^{-4}$.

16. $2^{1 - \binom{5}{2}} = 2^{-9}$, so the condition is $\binom{n}{5} < 512$. Since $\binom{11}{5} = 462$ and
$\binom{12}{5} = 792$, the largest $n$ is $11$ and $R(5,5) > 11$. The bound is far from the truth; much larger
lower bounds come from explicit colourings.

18. The sum is $\sum_{n \ge 5} \frac{2}{2^n \ln 2} = \frac{2}{\ln 2} \cdot \frac{1}{16} = \frac{1}{8 \ln 2}
\approx 0.18$. The model ignores the known structure of the prime factors of $F_n$, so it is a heuristic and
proves nothing.

20. Suppose $p = f(1)$ is prime. For every integer $k$, $f(1 + kp) \equiv f(1) \equiv 0 \pmod p$, so $f(1 + kp)$
is a prime divisible by $p$, hence equal to $p$. A non-constant polynomial takes the value $p$ only finitely
often.

21. If $m$ has an odd factor $b > 1$, write $m = ab$. Since $x + 1$ divides $x^b + 1$ for odd $b$, the number
$2^a + 1$ divides $2^m + 1$, and $1 < 2^a + 1 < 2^m + 1$.

22. Each point gives one linear equation in the six coefficients, and five homogeneous linear equations in six
unknowns have a nonzero solution. For the given points, $f = 0$, $d = -a$, $e = -c$, $b = 0$ and $a = -3c$, so the
conic is $3x(x - 1) = y(y - 1)$, a hyperbola.

23. If $n = p + q$ is odd, exactly one of $p, q$ is even, so it is $2$ and the other is $n - 2$; hence
$g(n) \le 1$. The model treats "$p$ is prime" and "$n - p$ is prime" as independent, but the parity of $n - p$ is
fixed by that of $p$. A correct model needs a factor for the prime $2$: it is $0$ for odd $n$ and $2$ for even $n$,
which is why the predictions are made for even $n$ only.

24. Write $f(x) = \sum_{k=0}^{d} c_k \binom{x}{k}$ with $c_k = \Delta^k f(0)$ (Newton's forward formula, proved by
comparing values at $0, \ldots, d$). The $c_k$ are integers because they are integer combinations of
$f(0), \ldots, f(d)$. Each $\binom{n}{k}$ is an integer for $n \ge 0$, and
$\binom{-m}{k} = (-1)^k \binom{m + k - 1}{k}$ for $m > 0$.
