1. ◦ For each pair of sets, decide whether $A \subseteq B$, whether $B \subseteq A$, and whether $A = B$. Here $X$ and $Y$ are any sets and $\mathcal{P}$ denotes the [power set](/00E0YZCERH/). (a) $A = \set{x \in \R : x^2 \le x}$ and $B = [0, 1]$. (b) $A = \mathcal{P}(X \cap Y)$ and $B = \mathcal{P}(X) \cap \mathcal{P}(Y)$. (c) $A = \mathcal{P}(X \cup Y)$ and $B = \mathcal{P}(X) \cup \mathcal{P}(Y)$. Where an inclusion can fail, give sets $X$ and $Y$ for which it fails.

2. ◦ For each function, say whether it is injective and whether it is surjective. When a property fails, give a witness: two inputs with the same value, or a value that is never taken. (a) $f \colon \Z \to \Z$, $f(n) = n + 5$. (b) $g \colon \N \to \N$, $g(n) = n + 1$, where $\N = \set{0, 1, 2, \dots}$. (c) $h \colon \R \to \R$, $h(x) = x^3 - x$. (d) $k \colon \Z \to \Z$, $k(n) = \floor{n/2}$.

3. ◦ For each relation on $\Z$, decide whether it is reflexive, symmetric and transitive. For each property that fails, give elements that show it. For each equivalence relation, describe its classes. (a) $x \mathrel{R} y$ when $x + y$ is even. (b) $x \mathrel{R} y$ when $xy \ge 0$. (c) $x \mathrel{R} y$ when $x^2 = y^2$.

4. ◦ Find the error. "Claim: $\sqrt{x^2 + 2x + 1} = x + 1$ for every real $x$. Proof: squaring both sides gives $x^2 + 2x + 1 = (x + 1)^2$, which is true for every $x$." Give a value of $x$ at which the claim fails, and state the correct identity.

5. ◦ (a) The polynomials $(x + 1)^3 - x^3$ and $3x^2 + 3x + 1$ take the same values at $x = 0, 1, 2$. Explain why this proves that they are equal for every real $x$. (b) Check that $x^3$ and $6x^2 - 11x + 6$ take the same values at $x = 1, 2, 3$, and that they differ at $x = 0$. Why does the argument of (a) not apply?

6. ◦ For the limit $\lim_{x \to 2} (5x - 1) = 9$: (a) find, as a function of $\varepsilon$, the largest $\delta$ such that $0 < \abs{x - 2} < \delta$ implies $\abs{(5x - 1) - 9} < \varepsilon$, and give its value for $\varepsilon = 0.1$; (b) find all $\varepsilon > 0$ for which $\delta = 1$ works.

7. ◦ Use symmetry, not an antiderivative, to find (a) $\int_{-2}^{2} (x^5 - 4x^3 + 3x + 1) \, dx$ and (b) $\int_{-\pi}^{\pi} x^2 \sin x \, dx$.

8. ◦ Say whether each subset of $[0, 1]$ is open in $[0, 1]$, closed in $[0, 1]$, both, or neither: (a) $[0, \tfrac12)$; (b) $[\tfrac12, 1]$; (c) $\Q \cap [0, 1]$; (d) $[0, 1]$. Which of them could be the set $S$ at the end of an open-closed argument on $[0, 1]$?

9. ◦ Run the [Euclidean algorithm](/0TRNT4X7J0/) on $252$ and $198$. Write each division, give $\gcd(252, 198)$ and the number of divisions, and then work back through the divisions to find integers $x$ and $y$ with $252x + 198y = \gcd(252, 198)$.

10. • Let $A$, $B$, $C$ and $D$ be sets. (a) Prove by double inclusion that $A \times (B \cap C) = (A \times B) \cap (A \times C)$. (b) Prove that $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$, and give sets for which the two sides differ.

11. • Let $f \colon \R \setminus \set{2} \to \R \setminus \set{3}$ be given by $f(x) = \dfrac{3x + 1}{x - 2}$. Check that $f$ takes values in $\R \setminus \set{3}$. Find a function $g \colon \R \setminus \set{3} \to \R \setminus \set{2}$ with $g \circ f = \mathrm{id}$ and $f \circ g = \mathrm{id}$, and conclude that $f$ is a [bijection](/0SNQEF7Z53/).

12. • Let $f \colon A \to B$ and $g \colon B \to C$ be functions. (a) Prove that if $g \circ f$ is surjective, then $g$ is surjective. (b) Give an example in which $g \circ f$ is surjective and $f$ is not surjective.

13. • On $\N \times \N$, define $(a, b) \sim (c, d)$ when $a + d = b + c$. (a) Prove that $\sim$ is an equivalence relation by checking the three properties directly, using only addition in $\N$. (b) Prove it again with a function $h \colon \N \times \N \to \Z$ such that $(a, b) \sim (c, d)$ exactly when $h(a, b) = h(c, d)$. (c) Describe the classes of $(0, 2)$ and of $(3, 1)$.

14. • Prove that $\gcd(a, b) = \gcd(a, a + b)$ for all positive integers $a$ and $b$, by showing that each of the two numbers divides the other.

15. • (a) Prove the identity
$$\frac{1}{n(n + 1)(n + 2)} = \frac12 \left( \frac{1}{n(n + 1)} - \frac{1}{(n + 1)(n + 2)} \right)$$
for every integer $n \ge 1$, by a chain of equalities from the right side. (b) Deduce that $\sum_{n=1}^{N} \frac{1}{n(n + 1)(n + 2)} = \frac14 - \frac{1}{2(N + 1)(N + 2)}$, and check the case $N = 3$.

16. • Prove from the definition that $\lim_{x \to -1} (x^2 + 3x) = -2$. Show the scratch work that finds $\delta$, then write the proof forward.

17. • Find the error. "Claim: if continuous functions $f_n \colon \R \to \R$ converge at every point to $f$, then $f$ is continuous. Proof: fix $c$ and $\varepsilon > 0$. Choose $N$ with $\abs{f_N(c) - f(c)} < \varepsilon/3$, and $\delta > 0$ with $\abs{f_N(x) - f_N(c)} < \varepsilon/3$ for $\abs{x - c} < \delta$. Then for $\abs{x - c} < \delta$, $\abs{f(x) - f(c)} \le \abs{f(x) - f_N(x)} + \abs{f_N(x) - f_N(c)} + \abs{f_N(c) - f(c)} < \varepsilon$." Name the step that has no reason, and show that the claim is false with $f_n(x) = \dfrac{1}{1 + n x^2}$.

18. • Let $D = \set{k / 2^m : k \in \Z, \ m \in \N}$ be the set of dyadic rationals. (a) Prove that $D$ is dense in $\R$: for each real $x$, the numbers $d_m = \floor{2^m x} / 2^m$ lie in $D$ and $d_m \to x$. (b) Let $f \colon \R \to \R$ be continuous with $f(d) = d^2$ for every $d \in D$. Prove that $f(x) = x^2$ for every real $x$. (c) Give a function, not continuous, with $f(d) = d^2$ on $D$ and $f(\sqrt2) \ne 2$.

19. • Prove that $x^4 + y^4 \ge x^3 y + x y^3$ for all real $x$ and $y$, by reducing to the case $y = 1$. Explain why the reduction is valid also when $y < 0$, and find when equality holds.

20. • Let $I$ be an interval and let $f, g \colon I \to \R$ be continuous, with $f(x)^2 = g(x)^2$ and $g(x) \ne 0$ for every $x \in I$. Suppose $f(a) = g(a)$ for one $a \in I$. Prove with the [open-closed argument](/1JJCDJB7FM/) that $f = g$ on $I$. Then show by an example that the conclusion can fail if $g$ is allowed to vanish.

21. • Let $T > 0$ and let $u \colon [0, T] \to [0, \infty)$ be continuous with $u(0) = 0$ and $u(t) \le 2 + \tfrac{1}{16} u(t)^2$ for every $t$. (a) Show that $u(t) \le 4$ implies $u(t) \le 3$, and conclude that $u \le 3$ on $[0, T]$. (b) Show that in fact $u \le 8 - 4\sqrt2$ on $[0, T]$. (c) Show that the conclusion fails without continuity, using a function that takes only the values $0$ and $14$.

22. ★ Let $A$ and $B$ be non-empty sets of real numbers that are bounded above, and let $A + B = \set{a + b : a \in A, \ b \in B}$. Prove that $\sup (A + B) = \sup A + \sup B$ by two inequalities.

23. ★ Let $f_n \colon [0, 1] \to \R$ satisfy $\abs{f_n(x) - f_n(y)} \le \abs{x - y}$ for all $n$, $x$ and $y$, and suppose $f_n(x) \to f(x)$ for every $x \in [0, 1]$. (a) Prove that $\abs{f(x) - f(y)} \le \abs{x - y}$. (b) Prove that $f_n \to f$ uniformly on $[0, 1]$, by an epsilon over three argument through finitely many grid points.

24. ★ Let $f \colon \R \to \R$ be continuous with $f(x + 1) = f(x)$ and $f(x + \sqrt2) = f(x)$ for every $x$. Prove that $f$ is constant. You may use that $\sqrt2$ is irrational.

25. ★ The improper integral $I = \int_0^{\pi/2} \ln (\sin x) \, dx$ converges; take this as known. Use the substitutions $x \mapsto \frac{\pi}{2} - x$ and $x \mapsto \pi - x$ to prove that $I = -\frac{\pi}{2} \ln 2$.

26. ★ Let $1, 2, 3, 5, 8, 13, \dots$ be the Fibonacci numbers $F_1 = 1$, $F_2 = 2$, $F_{k+1} = F_k + F_{k-1}$. Consider the greedy procedure: while $n > 0$, subtract from $n$ the largest $F_k \le n$. Prove that it stops for every integer $n \ge 1$, and that it writes $n$ as a sum of distinct $F_k$, no two with consecutive indices. Find the representations of $100$ and $2026$.
