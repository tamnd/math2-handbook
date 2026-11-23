1. The cancellation of $x - 2$ fails, because $x - 2 = 0$ when $x = 2$. The line $(x - 2)(x + 2) = 2(x - 2)$ is true, since both sides are $0$, and the next line, $4 = 2$, is the first false one.

3. For a negative base, a rational power is defined only from a fraction in lowest terms with odd denominator, so $(-8)^{2/6}$ can only mean $(-8)^{1/3} = -2$. The step to $\left((-8)^2\right)^{1/6}$ uses $(a^m)^n = a^{mn}$, which holds for $a > 0$ (and for $a \ne 0$ when $m$ and $n$ are integers); here $a = -8$ and $n = \frac{1}{6}$.

4. The integral diverges: $\int_0^b \sec^2 x \, dx = \tan b \to \infty$ as $b \to \frac{\pi}{2}^-$. The theorem needs an antiderivative on the whole interval $[0, \pi]$, and $\tan x$ is not defined at $\frac{\pi}{2}$, where $\sec^2 x$ is unbounded. The second student is right that the answer is not $0$, and the bound $\pi$ is not the answer either.

7. (a) is proved, since one example proves an existential claim. (b) is proved by checking every case: $11, 13, 17, 23, 31$. (c) is not proved, and it is false: $q(n)$ is prime for $n = 1, \dots, 10$, and $q(11) = 121 = 11^2$. The failure is forced, since $q(11) = 11 \cdot 10 + 11 = 11 \cdot 11$.

9. (a) False: $\sqrt{2} \cdot \sqrt{2} = 2$. (b) True: if $r + s = t$ with $r$ and $t$ rational, then $s = t - r$ is rational. (c) False: let $f(x) = 1$ for rational $x$ and $f(x) = -1$ otherwise; then $f^2 = 1$ is continuous and $f$ is continuous nowhere. (d) True: if $f + g$ were continuous at $0$, then so would be $g = (f + g) - f$.

11. Split into cases by signs. If $a < 0 \le b$, then $\sqrt{a}\sqrt{b} = i\sqrt{-a}\sqrt{b} = i\sqrt{-ab} = \sqrt{ab}$, since $ab \le 0$; the case $b < 0 \le a$ is the same. If $a, b < 0$, then $\sqrt{a}\sqrt{b} = i^2\sqrt{-a}\sqrt{-b} = -\sqrt{ab}$. The step $\sqrt{-1}\sqrt{-1} = \sqrt{(-1)(-1)}$ is exactly the excluded case.

13. (a) $169$ against $168$. (b) The hypotenuse has slope $\frac{5}{13}$ and the slanted side of a trapezoid has slope $\frac{3}{8}$, while the diagonal has slope $\frac{8}{21}$, and $\frac{3}{8} < \frac{8}{21} < \frac{5}{13}$. (c) The slanted edges do not lie on one line, so the pieces do not fit edge to edge: they overlap in a thin parallelogram along the diagonal, of area $169 - 168 = 1$.

14. (a) Each proof assumes the conclusion of the other, so together they show only that the two statements are equivalent. (b) If $p \nmid a$, then $\gcd(p, a) = 1$, since the only positive divisors of $p$ are $1$ and $p$. Write $px + ay = 1$ and multiply by $b$: $b = pbx + aby$. Both terms are divisible by $p$, so $p \mid b$.

15. The claim is $\exists \delta > 0\ \forall x\ \forall y\ (\abs{y - x} < \delta \Rightarrow \abs{y^2 - x^2} < 1)$, obtained from the true $\forall x\ \exists \delta\ \forall y \ldots$ by a quantifier shift. Given $\delta$, take $x = \frac{1}{\delta}$ and $y = x + \frac{\delta}{2}$. Then $y^2 - x^2 = x\delta + \frac{\delta^2}{4} = 1 + \frac{\delta^2}{4} \ge 1$.

18. Each step is a correct implication, so the argument shows: if $x$ is a real root, then $x = 1$. Putting $x = 1$ back fails, so the right conclusion is that the equation has no real root, which agrees with $x^2 + x + 1 = \left(x + \frac{1}{2}\right)^2 + \frac{3}{4} > 0$. The step from $x^2 + x + 1 = 0$ to $x^3 = 1$ cannot be reversed; over $\C$, the cube roots of $1$ other than $1$ are exactly the two roots of $x^2 + x + 1$.

20. The first $3n$ terms contain the first $2n$ odd reciprocals and the first $n$ even ones, so the partial sum is
$$S_{3n} = \left(H_{4n} - \tfrac{1}{2}H_{2n}\right) - \tfrac{1}{2}H_n = \ln 4 - \tfrac{1}{2}\ln 2 + o(1) \to \tfrac{3}{2}\ln 2.$$
The constant $\gamma$ cancels. The partial sums $S_{3n+1}$ and $S_{3n+2}$ differ from $S_{3n}$ by at most $\frac{2}{4n+1}$, so the whole series converges to $\frac{3}{2}\ln 2$.

21. The comparison test is for series with nonnegative terms: the bounds give $\sum \abs{b_n} \le 2 \sum \abs{a_n}$, which needs $\sum \abs{a_n} < \infty$, and only $\sum a_n$ converges. In the example, $b_n / a_n = 1 + \frac{(-1)^n}{\sqrt{n}} \to 1$, $\sum a_n$ converges by the alternating series test, and $\sum b_n = \sum a_n + \sum \frac{1}{n}$ diverges. Correct version: if $a_n, b_n > 0$ and $a_n / b_n \to 1$, the two series converge or diverge together; and if $\sum a_n$ converges absolutely and $a_n / b_n \to 1$, then $\sum b_n$ converges absolutely.

22. (a) $f_n(0) = 0$, and for $x > 0$, $n e^{-n x^2} \to 0$. (b) $\int_0^1 f_n = \frac{1 - e^{-n}}{2} \to \frac{1}{2}$. (c) The maximum is at $x = \frac{1}{\sqrt{2n}}$, with value $\sqrt{\frac{n}{2}}\, e^{-1/2} \to \infty$, so the convergence is not uniform. Nor is there an integrable bound for all $f_n$, since $\sup_n f_n(x)$ is about $\frac{1}{ex}$ near $0$. Either hypothesis would allow the exchange, and both are missing.

23. (a) $g$ is continuous on $(0, 1]$, so every sentence of the argument holds for $g$. (b) The step from "bounded near each point" to "bounded" needs finitely many of the intervals to cover the domain; then $\abs{f} < \max_i \abs{f(x_i)} + 1$. Compactness of $[0, 1]$, the [Heine–Borel theorem](/07PFYV65MB/), supplies the finite cover. (c) If $\frac{1}{y} < \frac{1}{x} + 1$ for every $y$ in $(x - \delta_x, x + \delta_x) \cap (0, 1]$, then every such $y$ is at least $\frac{x}{1 + x}$, so $\delta_x \le \frac{x^2}{1 + x} < x$. Finitely many intervals around $x_1, \dots, x_k$ then miss every point below $\min_i (x_i - \delta_{x_i}) > 0$.

24. $f'(0) = \lim_{h \to 0} \left(1 + 2h \sin\frac{1}{h}\right) = 1$. For $x \ne 0$, $f'(x) = 1 + 4x \sin\frac{1}{x} - 2\cos\frac{1}{x}$, which is $1 + 0 - 2 = -1$ at $x = \frac{1}{2k\pi}$. Since $f'$ is continuous away from $0$, $f' < 0$ on an interval around each such point, and $f$ decreases there; every $(-h, h)$ contains such points. What $f'(0) > 0$ does imply is $f(x) > f(0)$ for small $x > 0$ and $f(x) < f(0)$ for small $x < 0$.
