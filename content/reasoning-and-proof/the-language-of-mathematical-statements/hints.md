1. (a) A true statement: $2^{10} = 1024$. (b) An open sentence: true for $x = 3$, false for $x = 0$. (c) A question, so neither; the statement "$2^{11} - 1$ is prime" is false, since $2047 = 23 \cdot 89$. (d) A statement whose truth value is not known: it is the twin prime conjecture. (e) A command, so neither.

3. (a) $1, 2, 3, 5, 7, 9$. (b) $4, 6, 8, 10$. (c) $2$. (d) $1, 9$. Sentence (b) is $\neg P \land \neg Q$, the negation of $P \lor Q$ by De Morgan's law, so (a) and (b) are negations of each other; their lists split the range.

5. Converse: for every integer $n$, if $5 \mid n$ then $10 \mid n$; false, as $n = 5$ shows. Inverse: if $10 \nmid n$ then $5 \nmid n$; false, again at $n = 5$. Contrapositive: if $5 \nmid n$ then $10 \nmid n$; true. Negation: some integer $n$ has $10 \mid n$ and $5 \nmid n$; false. The original statement is true.

9. Turn the square, to see whether a prime is behind it, and the $9$, to see whether a square is behind it, since $9$ is not prime. The $5$ is prime, so the rule is satisfied whatever shape is behind it: the rule says nothing about what stands behind a prime. The circle cannot break the rule either.

11. (a) True, with $y = x$; false, since $y$ odd fails at $x = 2$ and $y$ even fails at $x = 1$. (b) False, since $x = 4$ has no larger $y$ in $D$; true, with $x = 1$. (c) True: $1 \cdot 1$, $2 \cdot 3$, $3 \cdot 2$ and $4 \cdot 4$ all leave remainder $1$ on division by $5$; false, since the partner $y$ changes with $x$ and $y$ must be the inverse of every $x$ at once.

12. (a) Sufficient, not necessary ($n = 4$). (b) Necessary, not sufficient ($n = 2$). (c) Necessary, not sufficient ($n = 2$, with $n^2 = 4$). (d) Both: if $4 \mid n$ then $16 \mid n^2$; if $n$ is odd then $n^2$ is odd, and if $n = 2m$ with $m$ odd then $n^2 = 4m^2$ with $m^2$ odd, so $8 \nmid n^2$. (e) Neither: $n = 4$ shows it is not necessary and $n = 6$ that it is not sufficient.

14. Not injective: there are integers $m \ne n$ with $f(m) = f(n)$. Not surjective: there is an integer $k$ with $f(n) \ne k$ for every integer $n$. For $g$, $g(0) = g(1) = 0$, and $n^2 - n = n(n - 1)$ is always even, so $k = 1$ is missed: $g$ is neither. For $h$, $h(0) = h(1) = 0$, so $h$ is not injective, and $h(2k) = k$ for every $k$, so $h$ is surjective.

18. The student assumed $3 \mid n$ and proved $3 \mid n^2$, which is the converse. For the statement asked for, assume $3 \nmid n$, so $n = 3k + 1$ or $n = 3k - 1$. Then $n^2 = 9k^2 \pm 6k + 1 = 3(3k^2 \pm 2k) + 1$, so $3 \nmid n^2$.

20. (a) True: $x = 0$ has three partners, $x = 1$ has two and only $x = 2$ has exactly one; $6$ pairs. (b) False, since every $x$ has exactly one partner $2 - x$; $3$ pairs. (c) False, since $x = 1$ and $x = 2$ each have exactly one partner, $y = 0$; $5$ pairs. The number of pairs does not decide the statement.

23. Dividing by $x$ assumes $x \ne 0$, and $x = 0$ is a solution. The existence half is fine; uniqueness, the claim that there are no others, is false. The solutions are $-3$, $0$ and $3$, from $x^3 - 9x = x(x - 3)(x + 3)$.

24. (a) There is an $\varepsilon > 0$ such that for every $\delta > 0$ there are real $x$ and $y$ with $\abs{x - y} < \delta$ and $\abs{f(x) - f(y)} \ge \varepsilon$. (b) Take $\varepsilon = 1$; given $\delta$, take $x = 1/\delta$ and $y = x + \delta/2$. Then $y^2 - x^2 = (y - x)(y + x) = 1 + \delta^2/4 \ge 1$. (c) Continuity reads $\forall x \, \forall \varepsilon > 0 \, \exists \delta > 0 \, \forall y$: the $\forall x$ stands before $\exists \delta$, so $\delta$ may depend on $x$, and in uniform continuity it does not.

25. Existence: $3, 5, 7$ are prime. Uniqueness: $p$, $p + 2$ and $p + 4$ leave the three different remainders on division by $3$, since $p + 4 = (p + 1) + 3$, so one of them is divisible by $3$; being prime, it equals $3$. Then $p = 3$, as $p + 2 = 3$ and $p + 4 = 3$ give $p = 1$ and $p = -1$, which are not prime.

26. One answer is
$$\exists x \, \exists y \, \bigl(x \ne y \land f(x) = 0 \land f(y) = 0 \land \forall z \, (f(z) = 0 \Rightarrow z = x \lor z = y)\bigr).$$
Its negation is $\forall x \, \forall y \, \bigl(x = y \lor f(x) \ne 0 \lor f(y) \ne 0 \lor \exists z \, (f(z) = 0 \land z \ne x \land z \ne y)\bigr)$: $f$ has at most one zero or at least three. The formula holds for $x^2 - 1$ (zeros $\pm 1$) and fails for $x^3 - x$ (three zeros) and $x^2 + 1$ (none).

27. Suppose the sequence converges to $L$ and to $M$ with $L \ne M$, and take $\varepsilon = \abs{L - M}/2$. For $n$ beyond both thresholds, $\abs{L - M} \le \abs{L - a_n} + \abs{a_n - M} < 2\varepsilon = \abs{L - M}$, which is impossible. This is uniqueness; "the limit" also needs existence, which is the hypothesis that the sequence converges.

28. Existence: let $t = \abs{a} + 1$. Then $t^3 - a > 0$ and $(-t)^3 - a < 0$, and the intermediate value theorem applied to $x^3 - a$ on $[-t, t]$ gives a zero. Uniqueness: if $x < y$ then $y^3 - x^3 = (y - x)(x^2 + xy + y^2)$, and $x^2 + xy + y^2 = (x + y/2)^2 + 3y^2/4 > 0$ unless $x = y = 0$, so $x^3 < y^3$.

29. (a) If $(a, b)$ is the only pair, then $b$ is the only partner of $a$, and every other $x$ has no partner. (b) On $\set{0, 1, 2}$, the condition $x \le y$ makes the statement true, and six pairs satisfy it: only $x = 2$ has exactly one partner. (c) Only $x = 1$ has exactly one partner, so the first statement is true; but $y = 0$, $y = 1$ and $y = 2$ each have exactly one partner ($2$, $2$ and $1$), so the second is false.
