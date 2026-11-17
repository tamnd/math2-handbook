1. ◦ For each map $\R \to \R$, say whether it is injective and whether it is surjective: $f(x) = e^x$, $g(x) = x^3 - x$, $h(x) = 2x + 1$.

2. ◦ For each relation on $\Z$, say which of reflexive, symmetric and transitive it is: (a) $x \le y$; (b) $x \ne y$; (c) $x - y$ is even.

3. ◦ A student writes: "For all real $x$, $\dfrac{x^2 - 1}{x - 1} = x + 1$, since $x^2 - 1 = (x - 1)(x + 1)$." What is wrong with the statement, and what is the correct claim?

4. ◦ A polynomial $p$ with real coefficients has degree at most $3$ and satisfies $p(0) = p(1) = p(2) = p(3) = 0$. What is $p$?

5. ◦ Using the [epsilon-delta pattern](/RXG5JTZ2PZ/), give a $\delta$, in terms of $\varepsilon$, that proves $\lim_{x \to 1} (5x - 2) = 3$.

6. ◦ Write the [negation](/K930V33BSC/) of "$f$ is continuous at $a$" in the form that starts "there is an $\varepsilon > 0$ such that".

7. ◦ Real numbers $a$ and $b$ satisfy $b \le a$ and $a \le b + 1/n$ for every integer $n \ge 1$. Show that $a = b$.

8. ◦ Find $\displaystyle\int_{-2}^{2} x^5 \cos x \, dx$ without computing an antiderivative.

9. ◦ Euclid's algorithm replaces a pair $(a, b)$ of natural numbers with $b > 0$ by $(b, r)$, where $r$ is the remainder of $a$ on division by $b$. Which natural number decreases at every step, and why does that prove termination?

10. • Prove by [double inclusion](/MKHVRNW68H/) that $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$ for all sets $A$, $B$, $C$.

11. • Prove that $f \colon \R \setminus \set{2} \to \R \setminus \set{1}$, $f(x) = \dfrac{x + 1}{x - 2}$, is a bijection, and find its inverse.

12. • Let $f \colon X \to Y$ and $g \colon Y \to Z$. Prove that if $g \circ f$ is injective then $f$ is injective. Give an example in which $g \circ f$ is injective and $g$ is not.

13. • On the set of pairs $(a, b)$ with $a \in \Z$ and $b \in \Z \setminus \set{0}$, define $(a, b) \sim (c, d)$ when $ad = bc$. Prove that $\sim$ is an [equivalence relation](/RGNF33GVHX/), and say where the condition $b \ne 0$ is used.

14. • Give a relation on $\set{1, 2, 3}$ that is reflexive and symmetric but not transitive, and one that is reflexive and transitive but not symmetric.

15. • Prove that $\sup \set{x \in \R : x^3 < 8} = 2$ by proving two inequalities.

16. • Prove that for every real $x$,
$$\frac{(x - 1)(x - 2)}{2} - x(x - 2) + \frac{x(x - 1)}{2} = 1,$$
by checking only three values of $x$. Say why three values are enough.

17. • Prove that $\cos^4 x - \sin^4 x = \cos 2x$ for every real $x$.

18. • Prove from the definition that $\lim_{x \to 1} (x^2 + x) = 2$.

19. • Prove that $f(x) = x^2$ is uniformly continuous on $[0, 5]$: give one $\delta$ that works for every point.

20. • Let $f_n \to f$ uniformly on a set $S$, and suppose that each $f_n$ is bounded on $S$. Prove that $f$ is bounded on $S$.

21. • Let $f, g \colon \R \to \R$ be continuous with $f(q) \le g(q)$ for every rational $q$. Prove that $f(x) \le g(x)$ for every real $x$.

22. • Use the [symmetry](/H840D9TM2X/) $k \mapsto n - k$ to prove that $\sum_{k=0}^{n} k \binom{n}{k} = n \, 2^{n-1}$.

23. • Prove that $\dfrac{a + b}{2} \ge \sqrt{ab}$ for all $a, b > 0$ by [reducing to the special case](/DX2H7AD66G/) $b = 1$.

24. ★ Let $U \subseteq \R^n$ be open and connected, and let $f \colon U \to \R$ be differentiable with $\nabla f = 0$ at every point. Prove with the [open-closed argument](/1JJCDJB7FM/) that $f$ is constant. Show by an example that the conclusion fails if $U$ is not connected.

25. ★ Let $u \colon [0, T) \to [0, \infty)$ be continuous with $u(0) = 0$ and
$$u(t) \le 2 + \frac{u(t)^3}{100} \quad \text{for all } t.$$
Use [bootstrapping](/YKA0ADKYFR/) to prove that $u(t) \le 13/4$ for all $t$.

26. ★ Let the Fibonacci numbers be $F_1 = 1$, $F_2 = 2$ and $F_{k+1} = F_k + F_{k-1}$. Prove with a greedy [algorithm](/X5HG1RNWQX/) that every positive integer is a sum of distinct terms $F_k$, no two with consecutive indices.

27. ★ On $\R$, let $x \sim y$ when $x - y \in \Z$. Prove that $\sim$ is an equivalence relation, and that $x \mapsto (\cos 2\pi x, \sin 2\pi x)$ gives a well-defined bijection from the set of equivalence classes onto the unit circle.

28. ★ Let $f \colon X \to Y$. Prove that $f(A \cap B) = f(A) \cap f(B)$ for all subsets $A, B \subseteq X$ if and only if $f$ is injective.
