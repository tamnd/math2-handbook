1. $e^x$ is injective but not surjective (it misses $y \le 0$). $x^3 - x$ is surjective (odd degree) but not injective, since $g(0) = g(1) = 0$. $2x + 1$ is a bijection with inverse $(y - 1)/2$.

2. (a) Reflexive and transitive, not symmetric. (b) Symmetric only: $1 \ne 2$ and $2 \ne 1$, but $1 = 1$. (c) All three, so it is an equivalence relation.

4. $p = 0$: a non-zero polynomial of degree at most $3$ has at most three roots.

6. There is an $\varepsilon > 0$ such that for every $\delta > 0$ there is an $x$ with $\abs{x - a} < \delta$ and $\abs{f(x) - f(a)} \ge \varepsilon$.

11. Injective: cross-multiply $f(a) = f(b)$ to get $-3a = -3b$. Surjective: solve $y = (x + 1)/(x - 2)$ to get $x = (2y + 1)/(y - 1)$, then check that $x \ne 2$. The inverse is $y \mapsto (2y + 1)/(y - 1)$.

13. For transitivity, multiply $ad = bc$ by $f$ and $cf = de$ by $b$ to get $d(af - be) = 0$, then cancel $d \ne 0$.

15. Every $x$ with $x^3 < 8$ has $x < 2$, so the supremum is at most $2$. For $0 < \varepsilon < 2$, the number $2 - \varepsilon$ lies in the set, so the supremum is at least $2 - \varepsilon$ for every such $\varepsilon$.

16. The left side is a polynomial of degree at most $2$, and it equals $1$ at $x = 0, 1, 2$. Its difference from $1$ has degree at most $2$ and three roots, so it is $0$.

18. $\abs{x^2 + x - 2} = \abs{x - 1}\abs{x + 2}$, and $\abs{x - 1} < 1$ gives $\abs{x + 2} < 4$. Take $\delta = \min(1, \varepsilon/4)$.

21. The set where $g - f \ge 0$ is closed, because $g - f$ is continuous, and it contains the dense set $\Q$.

22. With $S$ the sum, replacing $k$ by $n - k$ gives $S = \sum (n - k)\binom{n}{k}$. Add the two forms: $2S = n \sum_k \binom{n}{k} = n \, 2^n$.

24. Fix $x_0 \in U$ and let $S = \set{x \in U : f(x) = f(x_0)}$. It is closed in $U$ by continuity, and open because on any ball inside $U$ the mean value theorem along segments makes $f$ constant. On $U = (0, 1) \cup (2, 3)$ the function equal to $0$ on the first interval and $1$ on the second has zero derivative and is not constant.

25. If $u(t) \le 5$, the hypothesis gives $u(t) \le 2 + 125/100 = 13/4$. So no value of $u$ lies in $(13/4, 5]$. Since $u$ is continuous and $u(0) = 0$, the intermediate value theorem stops $u$ from reaching any value above $5$ without passing through that interval, so $u(t) \le 13/4$ for all $t$.

26. Take the largest $F_k \le n$ and repeat with $n - F_k$. Since $n < F_{k+1}$, the remainder satisfies $n - F_k < F_{k-1}$, so the next term chosen has index at most $k - 2$. The remainder strictly decreases, so the procedure stops.

27. The map is well defined because cosine and sine have period $2\pi$. It is injective on classes because equal points on the circle force $2\pi(x - y) \in 2\pi\Z$, and surjective because every point of the circle is $(\cos\theta, \sin\theta)$ for some $\theta$.

28. The inclusion $f(A \cap B) \subseteq f(A) \cap f(B)$ always holds. If $f$ is injective, an element $f(a) = f(b)$ with $a \in A$, $b \in B$ has $a = b \in A \cap B$. Conversely, if $f(a) = f(b)$ with $a \ne b$, take $A = \set{a}$ and $B = \set{b}$.
