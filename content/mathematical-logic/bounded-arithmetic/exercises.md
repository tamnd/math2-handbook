1. ◦ With $\abs{x} = \ceil{\log_2(x + 1)}$ and $x \mathbin{\#} y = 2^{\abs x \abs y}$, compute $\abs 0$, $\abs 5$, $\abs{1000}$, $\abs{1024}$, $5 \mathbin{\#} 6$, $12 \mathbin{\#} 3$ and $1000 \mathbin{\#} 1000$.

2. ◦ Classify each formula as $\Sigma^b_0$, $\Sigma^b_1$, $\Pi^b_1$ or not bounded, where the inner parts are open: (a) $(\exists y \le x)(y \cdot y = x)$; (b) $(\forall i \le \abs x)(i \cdot i \le x)$; (c) $(\forall y \le x)(\exists z \le \abs y)(z \cdot z = y)$; (d) $\exists y\, (y \cdot y = x)$.

3. ◦ Which of the following does [$\mathsf{I}\Delta_0$](/A2CFPP8JMN/) prove? Answer yes, no or open. (a) $\forall x\, \exists y\, (x = 2y \vee x = 2y + 1)$; (b) $\forall x\, \exists y\, (y = 2^x)$, with the $\Delta_0$ graph of exponentiation; (c) there are infinitely many primes. (d) Does $\mathsf{I}\Delta_0 + \Omega_1$ prove (c)?

4. ◦ Write a $\Delta_0$ formula that defines the set $\set{1, 4, 16, 64, \dots}$ of powers of $4$.

5. ◦ In dyadic notation with digits $1$ and $2$, the successor functions are $s_1(x) = 2x + 1$ and $s_2(x) = 2x + 2$. Write $10$ and $13$ in dyadic notation and as terms in $s_1$, $s_2$ and $0$, and compute the value of $13$ with its last dyadic digit removed.

6. ◦ Write out the [Paris–Wilkie translation](/ZVD982MVST/) at $n = 2$ of (a) $(\forall x \le n)(\alpha(x) \vee \alpha(x + 1))$ and (b) $(\exists y \le n)(y + y = 3)$, with $p_i$ the variable for $\alpha(i)$.

7. ◦ Answer yes, no or open: (a) $S^1_2 \subseteq T^1_2$; (b) $T^1_2 \subseteq S^2_2$; (c) $S^1_2 = T^1_2$; (d) $S_2 = T_2$; (e) $S^0_2 = T^0_2$.

8. • Show that $x^{\abs x} < x \mathbin{\#} x \le (2x)^{\abs x}$ for every $x \ge 1$.

9. • Use [Parikh's theorem](/YPQPC1WJMV/) to show that $\mathsf{I}\Delta_0$ does not prove $\Omega_1$, the statement that $x^{\abs x}$ exists for every $x$.

10. • Show that the set of numbers whose binary expansion is a palindrome is $\Delta_0$-definable, and list its elements below $40$.

11. • Define the function $x \mapsto \abs x$ by limited recursion on notation from $0$, the successor and $\floor{x/2}$, as in [Cook's PV](/FMM44KFZQT/), and give the bound that the recursion needs.

12. • Let $\mathrm{Cert}(x, c)$ be a polynomial-time predicate saying that $c$ is a valid certificate of the primality of $x$. Suppose $S^1_2$ proves $\forall x\, (x > 1 \to (\exists y \le x)(1 < y < x \wedge y \mid x) \vee (\exists c \le t(x))\, \mathrm{Cert}(x, c))$ for a term $t$. Show that some polynomial-time algorithm finds a nontrivial factor of every composite number.

13. • Write the conclusion of the [Krajíček–Pudlák–Takeuti theorem](/YP7KE8E6DC/) for $\forall x\, \exists y\, \forall z\, \varphi(x, y, z)$ with $k = 2$ rounds, and describe the corresponding student–teacher game. What does the case $k = 1$ say?

14. • Let $A(x) = (\forall u \le x)(\forall v \le x)(\neg(\alpha(u) \wedge u + v = x) \vee \alpha(v))$. Compute the Paris–Wilkie translation of $A$ at $x = 3$, simplify it, and decide whether it is a tautology.

15. • The propositional pigeonhole formula $\mathrm{PHP}^m_n$ has a variable $p_{ij}$ for each pigeon $i < m$ and hole $j < n$, a clause saying that each pigeon is in some hole, and a clause saying that no two pigeons share a hole. Count the variables and clauses of $\mathrm{PHP}^4_3$ and of $\mathrm{PHP}^9_3$.

16. • In the notation of [approximate counting](/65K2S22DGZ/), show that the set of odd numbers below $2^n$ satisfies $X \approx_0 2^{n-1}$.

17. ★ Show that for every term $t(x_1, \dots, x_k)$ of Buss's language there is a polynomial $p$ with $\abs{t(\vec x)} \le p(\abs{x_1}, \dots, \abs{x_k})$ for all $\vec x$.

18. ★ Show that if $X \preceq_\varepsilon Y$ and $Y \preceq_\delta Z$, then $X \preceq_{\varepsilon + \delta} Z$, with the maps given explicitly from the ones for the two hypotheses.

19. ★ Show by induction on the formula that the Paris–Wilkie translation of a $\Delta_0(\alpha)$ formula $\varphi(x)$ at $x = n$ has depth bounded by a constant and size at most $(n + 2)^c$, for a constant $c$ that depends only on $\varphi$.

20. ★ Show that every $\Delta_0$-definable set is decidable in space $O(\abs x)$ on input $x$.
