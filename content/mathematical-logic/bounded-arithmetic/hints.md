1. $\abs 0 = 0$, $\abs 5 = 3$, $\abs{1000} = 10$, $\abs{1024} = 11$, $5 \mathbin{\#} 6 = 2^9 = 512$, $12 \mathbin{\#} 7 = 2^{12} = 4096$ and $1000 \mathbin{\#} 1000 = 2^{100}$.

2. (a) $\Sigma^b_1$; (b) $\Sigma^b_0$, since the quantifier is sharply bounded; (c) $\Pi^b_1$, since the inner quantifier is sharply bounded; (d) not bounded.

8. With $2^{\abs x - 1} \le x < 2^{\abs x}$, the left side is $x^{\abs x} < (2^{\abs x})^{\abs x} = 2^{\abs x^2}$ and the right side is $(2x)^{\abs x} \ge (2^{\abs x})^{\abs x}$.

9. The graph $y = x^{\abs x}$ is $\Delta_0$. If $\mathsf{I}\Delta_0$ proved $\Omega_1$, Parikh's theorem would bound $x^{\abs x}$ by a polynomial in $x$, but $x^{\abs x} > x^k$ as soon as $\abs x > k$.

12. The formula after $x > 1 \to$ is $\Sigma^b_1$, so Buss's witnessing theorem gives a polynomial-time function that returns a witness to one of the two disjuncts. For a composite $x$ no certificate exists, so the witness is a factor.

13. There are polynomial-time $f_1, f_2$ with $\varphi(x, f_1(x), z_1) \vee \varphi(x, f_2(x, z_1), z_2)$ for all $x, z_1, z_2$. The student proposes $f_1(x)$; if the teacher answers with a counterexample $z_1$, the student proposes $f_2(x, z_1)$, which must be right. If $\exists y\, \forall z\, \varphi(x, y, z)$ failed for some $x$, choose $z_1$ with $\neg \varphi(x, f_1(x), z_1)$ and then $z_2$ with $\neg \varphi(x, f_2(x, z_1), z_2)$; both disjuncts fail.

14. Only the pairs $(u, v)$ with $u + v = 3$ give non-trivial conjuncts, so the translation is $(p_0 \to p_3) \wedge (p_1 \to p_2) \wedge (p_2 \to p_1) \wedge (p_3 \to p_0)$. It is not a tautology: take $p_0$ true and $p_3$ false.

16. Use $v = 1$, the map $u \mapsto u + 2^{n-1}$ from $[0, 2^{n-1})$ onto $X$, and the map $x \mapsto x - 2^{n-1}$ from $X$ onto $[0, 2^{n-1})$.

17. Induction on $t$, with $\abs{Sx} \le \abs x + 1$, $\abs{x + y} \le \max(\abs x, \abs y) + 1$, $\abs{x \cdot y} \le \abs x + \abs y$, $\abs{x \mathbin{\#} y} = \abs x \abs y + 1$, and the fact that $\floor{x/2}$ and $\abs x$ do not increase lengths.

18. Run the map for $Y \preceq_\delta Z$ on each copy, then the map for $X \preceq_\varepsilon Y$, with multiplier $vw$. The two error intervals $[0, \varepsilon 2^n)$ and $[0, \delta 2^n)$ together have the size of $[0, (\varepsilon + \delta) 2^n)$.

19. Each bounded quantifier $(\forall y \le t)$ becomes a conjunction of at most $t(n) + 1$ formulas, and $t(n) + 1 \le (n + 2)^d$ for some $d$. Each quantifier adds one level of depth, and atomic formulas without $\alpha$ become $\top$ or $\bot$.

20. Evaluate the formula recursively. All bounds are polynomials in $x$, so every quantified variable and every term value takes $O(\abs x)$ bits, and the number of variables is fixed by the formula.
