1. (a) "Let $n$ be an integer"; the last sentence says that $n^2 + n$ is even. (b) "Take $n = 4$" (or $n = -2$); the last sentence checks that $4^2 = 2 \cdot 4 + 8$. (c) "Let $g \colon B \to A$ satisfy $g \circ f = \mathrm{id}_A$, and let $a, a' \in A$ with $f(a) = f(a')$"; the last sentence says that $a = a'$. (d) The statement is the negation of a universal statement, so it needs one example: "Consider $f(x) = \abs{x}$"; the last sentence says that $f$ is continuous and not differentiable at $0$.

2. (a) There is a real $M$ such that $\abs{a_n} \le M$ for every $n$. (b) There is $\varepsilon > 0$ such that for every $\delta > 0$ there is $x$ with $\abs{x} < \delta$ and $\abs{f(x) - f(0)} \ge \varepsilon$. (c) There is $x$ with $x \in A$ and $x \notin B$. (d) There are $x, y, z \in X$ with $x \mathrel{R} y$, $y \mathrel{R} z$ and not $x \mathrel{R} z$.

5. Step $\langle 1 \rangle 2$ is wrong. Its proof uses $\abs{x} = x$, which was known only inside the proof of $\langle 1 \rangle 1$, under the assumption $x \ge 0$; that assumption ends with its step, and in the case $x < 0$ it is false. Repair: for $x < 0$, $\abs{x} = -x > 0 > x$.

6. (a) Acceptable: a routine expansion. (b) Acceptable: it names the extreme value theorem, whose hypotheses hold. (c) A gap, and the step is false: at $x = -\tfrac12$, $x^3 = -\tfrac18 > -\tfrac12 = x$. It holds only for $x < -1$. (d) A gap, and the step is false: the identity matrix has determinant $1$, and the sum of it with itself has determinant $4$.

9. Multiplying $x < y$ by $x$ keeps the direction only when $x > 0$. Counterexample: $x = -2$ and $y = 1$, where $x^2 = 4 > 1 = y^2$. Under the extra hypothesis $x \ge 0$, the claim holds: $x^2 \le xy$ with equality only at $x = 0$, and $xy < y^2$ since $y > x \ge 0$.

12. Scratch: squaring gives $x + 5 = x^2 - 2x + 1$, so $x^2 - 3x - 4 = 0$ and $x = 4$ or $x = -1$. Squaring is not reversible, so check: $x = -1$ gives $\sqrt4 = 2 \ne -2$. For the final proof, show that a solution satisfies $x - 1 \ge 0$ and $x^2 - 3x - 4 = 0$, hence $x = 4$; and check directly that $x = 4$ is a solution.

14. (a) The goal says a set is empty, that is, a negated existence statement: suppose $x \in A \cap C$ and reach a contradiction, since then $x \in B \cap C$. (b) The goal has the form "for every $n$ there is $m$": let $n$ be arbitrary, then name $m$ in terms of $n$. The choice $m = 2\abs{n} + 2$ is even and $m > \abs{n} \ge n$.

17. Suppose, for contradiction, that $x + y$ is rational. Write $x = p/q$ and $x + y = r/s$ with integers $p, q, r, s$ and $q, s \ne 0$; then $y = (rq - ps)/(qs)$ with $qs \ne 0$, so $y$ is rational, which contradicts the hypothesis. The column omits that $p, q, r, s$ are integers, that $q$, $s$ and $qs$ are not $0$, where $r/s$ comes from, and which line is the assumption to be contradicted.

19. Short version: $(n - 1) n (n + 1)$ is a product of three consecutive integers, so it is divisible by $2$ and by $3$, hence by $6$, and so is $6n$. The long version must show the identity by expanding, explain why one of two consecutive integers is even and one of three is a multiple of $3$, and say why a number divisible by $2$ and by $3$ is divisible by $6$: if $m = 2a$ and $3 \mid m$, then $3 \mid a$ by Euclid's lemma.

21. The claim fails first at $k = 6$: $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \cdot 509$. The step from "no $p_i$ divides $N$" to "$N$ is prime" is wrong. The argument proves that every prime factor of $N$ is larger than $p_k$; since $N > 1$ has a prime factor, there is a prime larger than $p_k$ for every $k$.

23. (a) For $x, y \in [0, 1]$, $\abs{x^2 - y^2} = \abs{x - y} \, \abs{x + y} \le 2 \abs{x - y}$, so $\delta = \varepsilon / 2$ works. (b) The negation: there is $\varepsilon > 0$ such that for every $\delta > 0$ there are $x, y \ge 0$ with $\abs{x - y} < \delta$ and $\abs{x^2 - y^2} \ge \varepsilon$. Take $\varepsilon = 1$, and for a given $\delta$ take $x = 1/\delta$ and $y = x + \delta/2$; then $y^2 - x^2 = 1 + \delta^2/4 \ge 1$.

24. Lemma $\langle 1 \rangle 1$: a product of integers each $\equiv 1 \pmod 4$ is $\equiv 1 \pmod 4$, since $(4a + 1)(4b + 1) = 4(4ab + a + b) + 1$. Main step: assume the list is non-empty (it may contain $3$). $N$ is odd and $N \equiv 3 \pmod 4$, so its prime factors are odd and, by the lemma, not all $\equiv 1 \pmod 4$; so some prime factor $q$ has $q \equiv 3 \pmod 4$. If $q = p_i$, then $q$ divides $4 p_1 \cdots p_k - N = 1$. So $q$ is not in the list, and no finite list contains all such primes.

25. (a) The definition of $D$ uses only $f$ and $X$; the case split uses that $d \in D$ or $d \notin D$, and each case unpacks the definition of $D$ at the element $d$. (b) $1 \in f(1)$, $2 \notin f(2)$ and $3 \in f(3)$, so $D = \set{2}$, which differs from $\set{1, 2}$, $\varnothing$ and $\set{1, 3}$. (c) No: the proof works for every set $X$, finite or infinite.

26. Summary: the proof uses $\varepsilon = 1$ to bound the tail of the sequence. Verdict: the claim is true, but the last line is wrong. The bound $\abs{a_n} < \abs{a_N} + 1$ was proved only for $n \ge N$, and it fails for the sequence $100, 0, 0, \dots$ with $N = 2$. Repair: $M = \max\set{\abs{a_1}, \dots, \abs{a_{N-1}}, \abs{a_N} + 1}$ bounds every term.

27. The claim is true, but the proof checks one case only. Symmetry lets you assume an order such as $a \ge b \ge c$, not that the three numbers are equal. A correct proof: $a^2 + b^2 + c^2 - (ab + bc + ca) = \tfrac12 \left[ (a - b)^2 + (b - c)^2 + (c - a)^2 \right] \ge 0$, so $9 = (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \ge 3(ab + bc + ca)$.
