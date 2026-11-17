1. Any three of: introduce the two integers with their types ("let $m$ be even and $n$ odd"); say that $a$ and $b$ are integers given by the definitions of even and odd; say that $a + b$ is an integer; state the conclusion that $m + n$ is odd.

5. The text starts from the conclusion and ends at a true statement, which proves nothing as written. Reverse it: $(x - 1)^2 \ge 0$, so $x^2 - 2x + 1 \ge 0$, so $x^2 + 1 \ge 2x$; every step is an implication in this direction.

6. $\exists M \in \R \; \forall x \in \R \; \abs{f(x)} \le M$. Negation: $\forall M \in \R \; \exists x \in \R \; \abs{f(x)} > M$.

7. (a) and (b) are acceptable: true, known to the reader and needing no new idea. (c) is not: it is the twin prime conjecture, which is open, so the step is not known to be true.

8. Fermat's theorem says that a local extremum of a differentiable function has $f' = 0$; the proof uses the converse, which is false. For $f(x) = x^3$, $f'(0) = 0$ and $0$ is not a local extremum.

18. Induction. The cases $n = 0$ and $n = 1$ hold. If $2^n > n$ with $n \ge 1$, then $2^{n+1} = 2 \cdot 2^n > 2n \ge n + 1$. The step uses $n \ge 1$, which is why the case $n = 0$ is checked separately.

19. Writing $n = 2k + 1$ with $k$ an integer uses that $n$ is an odd integer, and the conclusion "odd" uses that $2k^2 + 2k$ is an integer. Contrapositive: if $n$ is odd, then $n^2$ is odd, which is exactly the computation.

20. Wrong. Take $A = \set{1}$, $B = \set{1}$, $C = \emptyset$: then $A \cup B = A \cup C = \set{1}$ and $B \ne C$. Union has no cancellation law.

21. Here $r = 0$. The step "$r - b$ is rational" is false: $r - b = \sqrt 2$. The difference of a rational and an irrational number is always irrational, so the argument derives nothing.

22. Level 1: $\langle 1 \rangle 1$ $g \circ f$ is injective; $\langle 1 \rangle 2$ $g \circ f$ is surjective; $\langle 1 \rangle 3$ $(f^{-1} \circ g^{-1}) \circ (g \circ f)$ and $(g \circ f) \circ (f^{-1} \circ g^{-1})$ are identities; Q.E.D. Prove each by its own short list of steps.

23. $p^2 = 3q^2$ gives $3 \mid p^2$, and since $3$ is prime, $3 \mid p$. Write $p = 3m$; then $9m^2 = 3q^2$, so $q^2 = 3m^2$, and the same argument gives $3 \mid q$. Then $3$ divides both $p$ and $q$, which contradicts lowest terms.

24. Every prime fails, for example $n = 7$: then $p = 7$, $m = 1$, and "$p \le m$" is false because $m = 1$ has no prime factor. Corrected claim: every composite $n$ has a prime factor $p \le \sqrt n$. Then $m \ge 2$, every prime factor of $m$ is a prime factor of $n$, so $m \ge p$, and $p^2 \le n$.

25. Scratch: compare each factor with a geometric mean. Final proof: $a + b \ge 2\sqrt{ab}$, $b + c \ge 2\sqrt{bc}$, $c + a \ge 2\sqrt{ca}$, each from $(\sqrt a - \sqrt b)^2 \ge 0$; multiply the three inequalities of positive numbers to get $8abc$.

26. Let $x \in B$. If $x \in A$, then $x \in A \cap B = A \cap C$, so $x \in C$. If $x \notin A$, then $x \in A \cup B = A \cup C$ and $x \notin A$, so $x \in C$. By symmetry $C \subseteq B$. Examples: $A = \emptyset$, $B = \set{1}$, $C = \emptyset$ for the first hypothesis alone, and $A = B = \set{1}$, $C = \emptyset$ for the second.
