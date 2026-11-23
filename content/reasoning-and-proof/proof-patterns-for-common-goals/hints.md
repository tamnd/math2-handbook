1. (a) $A = B$: $x^2 \le x$ means $x(x - 1) \le 0$, which holds exactly for $0 \le x \le 1$. (b) $A = B$ for all $X$ and $Y$: a set $C$ satisfies $C \subseteq X \cap Y$ exactly when $C \subseteq X$ and $C \subseteq Y$. (c) $B \subseteq A$ always, since $C \subseteq X$ or $C \subseteq Y$ gives $C \subseteq X \cup Y$. The inclusion $A \subseteq B$ fails for $X = \set{1}$ and $Y = \set{2}$: the set $\set{1, 2}$ lies in $\mathcal{P}(X \cup Y)$ and in neither $\mathcal{P}(X)$ nor $\mathcal{P}(Y)$.

2. (a) Bijective, with inverse $n \mapsto n - 5$. (b) Injective, since $n + 1 = m + 1$ gives $n = m$; not surjective, since $0$ is not a value. (c) Not injective: $h(0) = h(1) = 0$. Surjective: $h(x) - c$ is a cubic, which is negative for large negative $x$ and positive for large positive $x$, so the intermediate value theorem gives a root. (d) Surjective, since $k(2m) = m$; not injective, since $k(0) = k(1) = 0$.

3. (a) An equivalence relation: $x + x = 2x$ is even, the condition is symmetric, and if $x + y$ and $y + z$ are even, so is $x + z = (x + y) + (y + z) - 2y$. The classes are the even and the odd integers. (b) Reflexive and symmetric, not transitive: $1 \cdot 0 \ge 0$ and $0 \cdot (-1) \ge 0$, but $1 \cdot (-1) < 0$. (c) An equivalence relation, since it has the form $h(x) = h(y)$ with $h(x) = x^2$. The classes are $\set{0}$ and $\set{n, -n}$ for $n \ge 1$.

6. (a) $\abs{(5x - 1) - 9} = 5 \abs{x - 2}$, so the condition holds exactly when $\abs{x - 2} < \varepsilon / 5$, and the largest $\delta$ is $\varepsilon / 5$, which is $0.02$ for $\varepsilon = 0.1$. (b) $\delta = 1$ works exactly when $5 \abs{x - 2} < \varepsilon$ for all $\abs{x - 2} < 1$, that is, when $\varepsilon \ge 5$.

9. $252 = 1 \cdot 198 + 54$, $198 = 3 \cdot 54 + 36$, $54 = 1 \cdot 36 + 18$, $36 = 2 \cdot 18$. So $\gcd(252, 198) = 18$, after four divisions. Back substitution: $18 = 54 - 36 = 54 - (198 - 3 \cdot 54) = 4 \cdot 54 - 198 = 4 \cdot (252 - 198) - 198$, so $x = 4$ and $y = -5$.

11. Solve $y = \frac{3x + 1}{x - 2}$ for $x$: $x(y - 3) = 2y + 1$, so $g(y) = \frac{2y + 1}{y - 3}$. The value $3$ is never taken, since $3x + 1 = 3(x - 2)$ has no solution; in the same way $g$ never takes the value $2$. Then compute $g(f(x))$ and $f(g(y))$ by putting each over a common denominator.

13. (a) For transitivity, add $a + d = b + c$ and $c + f = d + e$ and cancel $c + d$ to get $a + f = b + e$. (b) $h(a, b) = a - b$. (c) The class of $(0, 2)$ is $\set{(n, n + 2) : n \in \N}$, and the class of $(3, 1)$ is $\set{(n + 2, n) : n \in \N}$.

17. The bound $\abs{f(x) - f_N(x)} < \varepsilon/3$ for $x \ne c$ has no reason: $N$ was chosen at the point $c$ only, and pointwise convergence gives no control at other points. For the example, $f_n(0) = 1$ for every $n$ and $f_n(x) \to 0$ for $x \ne 0$, so the limit is $1$ at $0$ and $0$ elsewhere, which is not continuous.

19. If $y = 0$ the claim is $x^4 \ge 0$. If $y \ne 0$, divide by $y^4 > 0$, which keeps the direction of the inequality whatever the sign of $y$, and put $t = x/y$: the claim becomes $t^4 - t^3 - t + 1 = (t - 1)^2 (t^2 + t + 1) \ge 0$, and $t^2 + t + 1 > 0$. Equality holds exactly when $x = y$.

21. (a) If $u(t) \le 4$, then $u(t) \le 2 + \frac{16}{16} = 3$. The set $S = \set{t : u(t) \le 4}$ contains $0$, is closed since $u$ is continuous, and is open since $u(t) \le 3 < 4$ keeps $u < 4$ near $t$. (b) The hypothesis says $u^2 - 16u + 32 \ge 0$, that is, $u \le 8 - 4\sqrt2$ or $u \ge 8 + 4\sqrt2$, and the second is excluded by $u \le 3$. (c) Take $u = 0$ on $[0, T/2]$ and $u = 14$ on $(T/2, T]$; since $2 + \frac{196}{16} = 14.25$, the inequality holds everywhere.

22. Every $a + b$ is at most $\sup A + \sup B$, so $\sup(A + B) \le \sup A + \sup B$. For the other inequality, let $\varepsilon > 0$ and pick $a \in A$ and $b \in B$ with $a > \sup A - \varepsilon/2$ and $b > \sup B - \varepsilon/2$. Then $\sup(A + B) \ge a + b > \sup A + \sup B - \varepsilon$ for every $\varepsilon > 0$.

23. (a) Let $n \to \infty$ in $\abs{f_n(x) - f_n(y)} \le \abs{x - y}$. (b) Given $\varepsilon > 0$, pick an integer $m > 3/\varepsilon$ and the grid points $x_i = i/m$ for $0 \le i \le m$. Since there are finitely many, one $N$ gives $\abs{f_n(x_i) - f(x_i)} < \varepsilon/3$ for all $i$ and all $n \ge N$. For any $x$, take the nearest grid point $x_i$ and pass from $f_n(x)$ to $f_n(x_i)$, to $f(x_i)$, to $f(x)$; the outer two steps are at most $\abs{x - x_i} \le \frac{1}{2m} < \varepsilon/3$.

24. Let $G = \set{m + n\sqrt2 : m, n \in \Z}$; then $f(x + g) = f(x)$ for every $g \in G$, so $f = f(0)$ on $G$. Show that $G$ is dense. Let $c$ be the infimum of the positive elements of $G$. If $c > 0$, then $c \in G$ (otherwise two elements of $G$ in $(c, 2c)$ would differ by a positive element below $c$), and every element of $G$ is an integer multiple of $c$, so $1 = pc$ and $\sqrt2 = qc$ with integers $p$ and $q$, and $\sqrt2 = q/p$ would be rational. So $G$ has positive elements below any $\ell > 0$, and their multiples meet every interval of length $\ell$. Then use continuity.

25. The substitution $x \mapsto \frac{\pi}{2} - x$ gives $I = \int_0^{\pi/2} \ln(\cos x) \, dx$, so $2I = \int_0^{\pi/2} \ln\left(\tfrac12 \sin 2x\right) dx = \int_0^{\pi/2} \ln(\sin 2x) \, dx - \frac{\pi}{2} \ln 2$. With $u = 2x$, the last integral is $\frac12 \int_0^{\pi} \ln(\sin u) \, du$, and $u \mapsto \pi - u$ shows that this equals $I$. So $2I = I - \frac{\pi}{2} \ln 2$.

26. Termination: $n$ decreases by at least $1$ at each step. Correctness: if $F_k \le n < F_{k+1}$, the remainder is $n - F_k < F_{k+1} - F_k = F_{k-1}$, so the next number taken is at most $F_{k-2}$, smaller than $F_k$ and not adjacent to it. So $100 = 89 + 8 + 3$ and $2026 = 1597 + 377 + 34 + 13 + 5$.
