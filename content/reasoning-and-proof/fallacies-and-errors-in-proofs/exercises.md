1. ◦ Find the error. "Let $x = 2$. Then $x^2 = 2x$, so $x^2 - 4 = 2x - 4$, that is, $(x - 2)(x + 2) = 2(x - 2)$. Cancelling $x - 2$ gives $x + 2 = 2$, so $x = 0$ and $2 = 0$." Name the step that fails and the value of the expression it divides by.

2. ◦ A student solves $x(x - 1)(x + 2) = 3x(x - 1)$ by cancelling $x(x - 1)$ on both sides and finds $x = 1$. Find all real solutions, and say which solution the cancellation lost.

3. ◦ Find the error in
$$-2 = (-8)^{1/3} = (-8)^{2/6} = \left((-8)^2\right)^{1/6} = 64^{1/6} = 2,$$
and state the rule for powers that the faulty step uses, with its hypothesis.

4. ◦ A student computes $\int_0^{\pi} \sec^2 x \, dx = \tan \pi - \tan 0 = 0$, and a second student objects that $\sec^2 x \ge 1$, so the integral is at least $\pi$. Decide what the integral is, and say which hypothesis of the [fundamental theorem of calculus](/0NHGY0N0JB/) fails.

5. ◦ Take the true conditional "if $6$ divides $n$, then $3$ divides $n$". For each argument, name its form, say whether it is valid, and give a counterexample if it is not. (a) $3$ divides $n$, so $6$ divides $n$. (b) $6$ does not divide $n$, so $3$ does not divide $n$. (c) $3$ does not divide $n$, so $6$ does not divide $n$. (d) $6$ divides $42$, so $3$ divides $42$.

6. ◦ Write each statement with quantifiers, and decide whether it is true. (a) For every natural number $n$ there is a prime $p$ with $p > n$. (b) There is a prime $p$ with $p > n$ for every natural number $n$. Which of the two implies the other?

7. ◦ Let $q(n) = n^2 - n + 11$. Say which claims the given evidence proves. (a) "Some $q(n)$ with $n \ge 1$ is a prime greater than $50$", with the evidence $q(7) = 53$. (b) "$q(n)$ is prime for $n = 1, 2, 3, 4, 5$", with the five values computed. (c) "$q(n)$ is prime for every $n \ge 1$", with the values for $n = 1, \dots, 10$ computed and found prime. For the claim that is not proved, find the smallest counterexample and explain, without testing primality, why that $n$ must fail.

8. ◦ A student solves
$$\frac{x}{x - 2} = \frac{2}{x - 2} + 3$$
by multiplying both sides by $x - 2$, and gets $x = 2$. Find all real solutions, and name the step that is not reversible.

9. ◦ Each claim was introduced with "clearly". Decide which are true; give a counterexample to each false one and a one-line proof of each true one. (a) The product of two irrational numbers is irrational. (b) The sum of a rational number and an irrational number is irrational. (c) If $f \colon \R \to \R$ and $f^2$ is continuous, then $f$ is continuous. (d) If $f$ is continuous at $0$ and $g$ is not, then $f + g$ is not continuous at $0$.

10. • Check that $\sqrt{3 + \frac{3}{8}} = 3\sqrt{\frac{3}{8}}$, as if the $3$ could be moved out of the root. For a fixed integer $n \ge 2$, find every positive integer $d$ with
$$\sqrt{n + \frac{n}{d}} = n\sqrt{\frac{n}{d}}.$$
Is the step "move $n$ out of the root" a valid rule?

11. • Use the principal square root on all of $\R$: $\sqrt{a}$ is the nonnegative root for $a \ge 0$, and $\sqrt{a} = i\sqrt{-a}$ for $a < 0$. Prove that $\sqrt{a}\sqrt{b} = \sqrt{ab}$ for all real $a, b$ except when $a < 0$ and $b < 0$, and that in that case $\sqrt{a}\sqrt{b} = -\sqrt{ab}$. Which step of "$-1 = i \cdot i = \sqrt{-1}\sqrt{-1} = \sqrt{1} = 1$" does this rule out?

12. • A student writes $\int_{-1}^{2} \frac{dx}{x} = \ln\abs{2} - \ln\abs{-1} = \ln 2$. (a) Show that the [improper integral](/05KQ3F99BQ/) does not exist. (b) Compute
$$\lim_{\varepsilon \to 0^+} \left( \int_{-1}^{-\varepsilon} \frac{dx}{x} + \int_{\varepsilon}^{2} \frac{dx}{x} \right) \quad \text{and} \quad \lim_{\varepsilon \to 0^+} \left( \int_{-1}^{-\varepsilon} \frac{dx}{x} + \int_{2\varepsilon}^{2} \frac{dx}{x} \right),$$
and explain why the two answers show that no value can be assigned in a natural way.

13. • A $13 \times 13$ square is cut into four pieces: a $13 \times 8$ strip is cut into two congruent right trapezoids with parallel sides $8$ and $5$ and height $8$, and the remaining $13 \times 5$ strip is cut along a diagonal into two right triangles with legs $13$ and $5$. The pieces are then laid out to look like an $8 \times 21$ rectangle, with the slanted edges along its diagonal. (a) Compare the two areas. (b) Find the slope of the triangles' hypotenuse and of the trapezoids' slanted side, both measured along the long side of the rectangle, and the slope of the diagonal of the $8 \times 21$ rectangle. (c) Explain where the missing unit of area is.

14. • A book proves [Euclid's lemma](/051VYKA1EX/) ("if a prime $p$ divides $ab$, then $p$ divides $a$ or $b$") from the uniqueness of prime factorization, and proves the [fundamental theorem of arithmetic](/084HH1NDCB/) from Euclid's lemma. (a) Explain why the two proofs together prove neither statement. (b) Give a proof of Euclid's lemma that does not use unique factorization, from [Bézout's identity](/0DQVHMYAGA/): if $\gcd(p, a) = 1$, then $px + ay = 1$ for some integers $x, y$.

15. • A student argues: "$f(x) = x^2$ is continuous on $\R$, so for $\varepsilon = 1$ there is a $\delta > 0$ with $\abs{f(y) - f(x)} < 1$ whenever $\abs{y - x} < \delta$, for all $x$ at once." Write the claim with quantifiers, name the fallacy, and show that the claim is false by finding, for each $\delta > 0$, points $x$ and $y$ with $\abs{y - x} < \delta$ and $\abs{f(y) - f(x)} \ge 1$.

16. • Let $X$ be a set and $P(x, n)$ a property of $x \in X$ and $n \in \N$. (a) Prove that if $X$ is finite and nonempty and for every $x \in X$ there is $N_x$ with $P(x, n)$ for all $n \ge N_x$, then there is one $N$ with $P(x, n)$ for all $x \in X$ and all $n \ge N$. (b) Show by an example with $X = \N$ that the conclusion can fail when $X$ is infinite.

17. • Solve $\sin x = \cos x$ on $[0, 2\pi)$ by squaring both sides, and list the candidates that squaring produces. Which candidates are solutions, and which are extraneous?

18. • Find the error. "Let $x$ be a real number with $x^2 + x + 1 = 0$. Then $x \ne 0$, and dividing by $x$ gives $x + 1 + \frac{1}{x} = 0$. From the equation, $x + 1 = -x^2$, so $-x^2 + \frac{1}{x} = 0$, that is, $x^3 = 1$. Hence $x = 1$, and putting $x = 1$ into the equation gives $3 = 0$."

19. • In $\Z[\sqrt{-5}]$, show that
$$21 = 3 \cdot 7 = (1 + 2\sqrt{-5})(1 - 2\sqrt{-5}),$$
and that the four factors are irreducible and the two factorizations are different. Use the norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$. Which step of a proof copied from the integers would break here?

20. ★ Rearrange the alternating harmonic series so that two positive terms are followed by one negative term:
$$1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \frac{1}{9} + \frac{1}{11} - \frac{1}{6} + \cdots.$$
Prove that the new series converges to $\frac{3}{2}\ln 2$, while the original one has sum $\ln 2$. You may use $H_m = 1 + \frac{1}{2} + \dots + \frac{1}{m} = \ln m + \gamma + o(1)$.

21. ★ Find the error. "Let $a_n$ and $b_n$ be nonzero with $a_n / b_n \to 1$, and let $\sum a_n$ converge. For large $n$ we have $\frac{1}{2} \abs{b_n} \le \abs{a_n} \le 2\abs{b_n}$, so by comparison $\sum b_n$ converges." Show that the conclusion fails for $a_n = \frac{(-1)^n}{\sqrt{n}}$ and $b_n = \frac{(-1)^n}{\sqrt{n}} + \frac{1}{n}$, with $n \ge 2$, and state a correct version of the claim, in the spirit of the [limit comparison test](/0HW7BNHHGF/).

22. ★ Let $f_n(x) = n x e^{-n x^2}$ on $[0, 1]$. (a) Show that $f_n(x) \to 0$ for every $x \in [0, 1]$. (b) Compute $\int_0^1 f_n(x) \, dx$ and its limit. (c) Find $\max_{[0, 1]} f_n$, and explain which hypothesis is missing for the exchange $\lim \int f_n = \int \lim f_n$.

23. ★ A student proves that every continuous $f \colon [0, 1] \to \R$ is bounded: "For each $x$, continuity with $\varepsilon = 1$ gives $\delta_x > 0$ with $\abs{f(y)} < \abs{f(x)} + 1$ whenever $\abs{y - x} < \delta_x$. So $f$ is bounded near every point, and hence bounded." (a) Show that the same words apply to $g(x) = \frac{1}{x}$ on $(0, 1]$, which is unbounded, so the argument proves too much. (b) Name the missing step and the property of $[0, 1]$ that supplies it. (c) For $g$, show that every admissible $\delta_x$ is less than $x$, and explain why finitely many of the intervals $(x - \delta_x, x + \delta_x)$ cannot cover $(0, 1]$.

24. ★ Let $f(x) = x + 2x^2 \sin\frac{1}{x}$ for $x \ne 0$ and $f(0) = 0$. A text says: "Clearly, since $f'(0) > 0$, $f$ is increasing on some interval around $0$." Show that $f'(0) = 1$, that $f'\left(\frac{1}{2k\pi}\right) = -1$ for every positive integer $k$, and conclude that $f$ is increasing on no interval $(-h, h)$. What does $f'(0) > 0$ correctly imply?
