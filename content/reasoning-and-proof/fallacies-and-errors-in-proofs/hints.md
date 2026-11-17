1. The solution $x = 0$ is lost, in the division by $x$. Factor instead: $x(x - 2)(x + 2) = 0$.

2. The step $(-8)^{2/2} = \bigl((-8)^2\bigr)^{1/2}$. The law $(a^b)^c = a^{bc}$ holds for $a > 0$, but not for a negative base with a fractional exponent.

8. All ten values are prime: $11, 13, 17, 23, 31, 41, 53, 67, 83, 101$. But $n = 11$ gives $121 = 11^2$.

10. $x^3 = 1$ is correct, since $x^3 - 1 = (x - 1)(x^2 + x + 1)$. The false step is $x^3 = 1 \Rightarrow x = 1$: the equation has no real roots, and its roots are the two non-real cube roots of unity.

15. The step "the length of the limit curve is the limit of the lengths". Arc length is not continuous under uniform convergence of curves.

16. Each proof uses the other's conclusion. Bézout's identity breaks the circle: if $p \nmid a$ then $1 = px + ay$ for some integers $x, y$, so $b = pbx + aby$ is divisible by $p$.

18. From $5 \cdot 2^7 \equiv -1 \pmod{641}$, raise to the fourth power: $5^4 \cdot 2^{28} \equiv 1$. Since $5^4 \equiv -2^4$, this gives $-2^{32} \equiv 1$, so $641 \mid 2^{32} + 1$.

19. Pointwise: $\forall x \, \forall \varepsilon > 0 \, \exists N \, \forall n \ge N \, \abs{x}/n < \varepsilon$. Uniform: $\forall \varepsilon > 0 \, \exists N \, \forall x \, \forall n \ge N \, \abs{x}/n < \varepsilon$. The second fails for $\varepsilon = 1$: whatever $N$ is, $x = N$ and $n = N$ give $\abs{x}/n = 1$; the shift moves $\exists N$ in front of $\forall x$.

23. The first $3n$ terms contain the odd reciprocals up to $1/(4n - 1)$ and the even ones up to $1/(2n)$, so $S_{3n} = H_{4n} - \tfrac12 H_{2n} - \tfrac12 H_n$. Substituting the asymptotic form gives $\ln 4 - \tfrac12 \ln 2 = \tfrac32 \ln 2$. The partial sums $S_{3n+1}$ and $S_{3n+2}$ differ from $S_{3n}$ by terms that tend to $0$.

24. Take $N = \max_{x \in X} N_x$, which exists because $X$ is finite (any $N$ works if $X$ is empty). For $X = \N$ and $P(x, n)$: "$n \ge x$", each $x$ has $N_x = x$, but no single $N$ works for all $x$.

25. Let $M$ be the midpoint of the arc $BC$ not containing $A$. The inscribed angles $BAM$ and $MAC$ stand on equal arcs, so $AM$ is the bisector, and the equal arcs give $MB = MC$, so $M$ is on the perpendicular bisector. The two lines coincide only if $A$ is on the perpendicular bisector, that is, $AB = AC$; otherwise they meet only at $M$.

26. $f_n(x) \to 0$ for every $x \in [0, 1]$, but $\int_0^1 f_n = \tfrac12(1 - e^{-n}) \to \tfrac12$. The convergence is not uniform: $f_n(1/\sqrt{2n}) = \sqrt{n/2}\, e^{-1/2} \to \infty$.

27. Write $\sqrt a \, \sqrt b = \sqrt{\abs{ab}} \, e^{i(\operatorname{Arg} a + \operatorname{Arg} b)/2}$ and $\sqrt{ab} = \sqrt{\abs{ab}} \, e^{i \operatorname{Arg}(ab)/2}$. The sum $\operatorname{Arg} a + \operatorname{Arg} b$ lies in $(-2\pi, 2\pi]$ and differs from $\operatorname{Arg}(ab)$ by $0$ or $\pm 2\pi$; the two roots agree exactly when the difference is $0$.
