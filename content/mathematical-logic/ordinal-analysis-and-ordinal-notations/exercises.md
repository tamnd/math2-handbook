1. ◦ Put these ordinals in increasing order, using the [comparison of Cantor normal forms](/DXKWBFWCE0/): $\omega^{\omega+2} \cdot 3 + \omega$, $\omega^{\omega^2}$, $\omega^{\omega \cdot 2} + \omega^{\omega+5}$ and $\omega^{\omega+3}$.

2. ◦ In the [notation system](/7MBX59Y7N9/) of finite non-increasing sequences of natural numbers, which ordinals do $(3, 1, 1, 0)$ and $(2, 2, 2, 2, 2)$ name? Which is larger, and how does the lexicographic rule decide it? Where does $(3, 1, 1)$ lie relative to $(3, 1, 1, 0)$, and why is $(1, 3)$ not a notation?

3. ◦ With the fundamental sequences of [epsilon nought](/KT50SMH3EC/), $\varepsilon_0[0] = 0$, $\varepsilon_0[n+1] = \omega^{\varepsilon_0[n]}$, $(\gamma + \omega^{\delta+1})[n] = \gamma + \omega^\delta \cdot n$ and $(\gamma + \omega^\beta)[n] = \gamma + \omega^{\beta[n]}$ for a limit $\beta$, compute $(\omega^{\omega^2} + \omega^3)[2]$, $\omega^{\omega^2}[3]$ and $\varepsilon_0[4]$.

4. ◦ [Gentzen's consistency proof](/QPV0HNP22S/) shows that $\mathrm{PRA}$ together with quantifier-free transfinite induction along $\varepsilon_0$ proves $\operatorname{Con}(\mathrm{PA})$. Why does this not contradict [Gödel's second incompleteness theorem](/4PZM5GJTR5/)? What does it show about quantifier-free transfinite induction along $\varepsilon_0$ in $\mathrm{PA}$, if $\mathrm{PA}$ is consistent?

5. ◦ In the infinitary system of the [ω-rule](/XAMKAB1BZM/), give a cut-free derivation of $\forall x\, \exists y\, (y = x + x)$ and state its height. Then give the height of a cut-free derivation of $\exists y\, \forall x\, (x + y = x)$.

6. ◦ Compare each pair of [Veblen](/JQFAE9S2F4/) terms, and say which is larger or whether they are equal: (a) $\varphi_2(\varepsilon_0)$ and $\varphi_1(\varphi_2(\omega))$; (b) $\varphi_\omega(1)$ and $\varphi_5(\varphi_\omega(0) + 1)$; (c) $\varphi_3(0)$ and $\varphi_2(\varphi_3(0))$.

7. ◦ In [Buchholz's system](/E7WEFRMQTB/), $\psi_0(\Omega + \eta) = \omega^{\varepsilon_0 + \eta}$ for every $\eta \le \varepsilon_1$. Compute $\psi_0(\Omega + 5)$, $\psi_0(\Omega + \varepsilon_0)$ and $\psi_0(\Omega + \varepsilon_0 \cdot 2)$, and write each as a product or power of $\varepsilon_0$ times a power of $\omega$.

8. ◦ Put these theories in order of their [proof-theoretic ordinals](/C72RBH0CDR/), and name each ordinal: $\mathrm{ID}_1$, $\mathrm{ACA}$, $\mathrm{I}\Sigma_1$, $\Pi^1_1\text{-}\mathrm{CA}_0$, $\mathrm{PA}$, $\mathrm{ATR}_0$, $\mathrm{ID}_2$, $\mathrm{ACA}_0$. Which two have the same ordinal?

9. ◦ Which of these formulas are $X$-positive, so that they define an [inductive definition](/5VNT564Y2W/)? (a) $x = 0 \vee \exists y\, (x = y + 3 \wedge X(y))$; (b) $\neg \forall y\, X(y)$; (c) $X(x) \to x = 0$; (d) $\forall y\, (X(y) \vee y \ne x + 1)$. For (a), find the least fixed point, the stage of each of its elements and the closure ordinal, with the stages $I^\alpha = \Gamma(I^{<\alpha})$.

10. • Write $\varepsilon_0 \cdot \omega$, $\varepsilon_0^\omega$ and $\varepsilon_0^{\varepsilon_0}$ as powers of $\omega$, with exponents in Cantor normal form over $\varepsilon_0$. Show that all three lie strictly between $\varepsilon_0$ and $\varepsilon_1$.

11. • Take as given that $\mathrm{PA}$ proves $\operatorname{TI}(\omega, \psi)$ for every formula $\psi$, and the [jump lemma](/ZE54ABPMJ0/): for each formula $\varphi$ there is a formula $\varphi^+$ such that $\mathrm{PA} \vdash \operatorname{TI}(a, \varphi^+) \to \operatorname{TI}(\omega^a, \varphi)$ for every notation $a$. From which instance of $\operatorname{TI}(\omega, \cdot)$ and how many jumps do you get $\operatorname{TI}(\omega^{\omega^{\omega^\omega}}, \varphi)$? Why does the method not give $\operatorname{TI}(\varepsilon_0, \varphi)$?

12. • Suppose $\vdash^{\omega+3}_3 \Gamma$ in the [infinitary system](/XAMKAB1BZM/), so the cuts have rank at most $2$. Bound the height of a cut-free derivation of $\Gamma$ by repeated cut elimination, first with $\vdash^\alpha_{\rho+1} \Rightarrow \vdash^{\omega^\alpha}_\rho$ and then with $\vdash^\alpha_{\rho+1} \Rightarrow \vdash^{2^\alpha}_\rho$. Write the second bound in Cantor normal form.

13. • Prove the case $\alpha < \gamma$ of the comparison rule for the [Veblen function](/JQFAE9S2F4/): if $\alpha < \gamma$, then $\varphi_\alpha(\beta) < \varphi_\gamma(\delta)$ if and only if $\beta < \varphi_\gamma(\delta)$, and $\varphi_\alpha(\beta) = \varphi_\gamma(\delta)$ if and only if $\beta = \varphi_\gamma(\delta)$.

14. • Show that $\varphi_\alpha(\beta) < \Gamma_0$ whenever $\alpha, \beta < \Gamma_0$, and that the ordinals below the [Feferman–Schütte ordinal](/CNN7BK5YAW/) are closed under addition. Conclude that $\Gamma_0$ is not of the form $\varphi_\alpha(\beta)$ with $\alpha, \beta < \Gamma_0$.

15. • For the [collapsing function](/8S6CT4TMB7/) $\psi$ with generators $0, 1, \omega, \Omega$, compute $\psi(\omega + 1)$ and $\psi(\Omega + \omega)$. Compare them with the values of Buchholz's $\psi_0$ at the same arguments, $\psi_0(\omega + 1) = \omega^{\omega+1}$ and $\psi_0(\Omega + \omega) = \omega^{\varepsilon_0 + \omega}$.

16. • In [Buchholz's system](/E7WEFRMQTB/), show that $\psi_1(2) = \omega^{\Omega + 2}$. Then adapt the proof that $\psi_0(\Omega \cdot 2) = \varepsilon_1$ to show $\psi_0(\Omega \cdot 2 + 1) = \varepsilon_1 \cdot \omega$ and $\psi_0(\Omega \cdot 3) = \varepsilon_2$.

17. • Let $\prec$ be the order on $\N$ that puts all even numbers, in their usual order, below all odd numbers, in their usual order. Compute the stages of the accessible-part operator $A(X, x) = \forall y\, (y \prec x \to X(y))$, with $I^\alpha = \Gamma(I^{<\alpha})$, and its closure ordinal. Compare it with the order type of $\prec$.

18. • In the tree class $\mathcal{O}_1$ of [iterated inductive definitions](/5VNT564Y2W/), the codes $s_0 = 0$, $s_{n+1} = \langle 1, s_n \rangle$ name the natural numbers, and $\langle 2, e \rangle$ with $\set{e}(n) = s_n$ names $\omega$. Give codes in $\mathcal{O}_1$ for $\omega + 1$ and $\omega \cdot 2$, and compute the stages at which the operator $A_1$ puts them into $\mathcal{O}_1$, with $I^0 = \Gamma(\emptyset)$.

19. • In [Takeuti's](/W560YMCPA3/) calculus $\mathrm{LK}^2$, consider a cut on $\forall X\, X(a)$, where the left premise ends with $(\forall^2\mathrm{R})$ and the right premise with $(\forall^2\mathrm{L})$ for the abstract $T = \lambda z.\, \forall X\, X(z)$. What is the cut formula after the usual reduction step? Explain why cut elimination for $\mathrm{LK}^2$ cannot be proved by induction on the complexity of the cut formula.

20. ★ Let $\sigma$ be a true arithmetical sentence. Show that $\abs{\mathrm{PA} + \sigma} = \varepsilon_0$, using the embedding and cut elimination for the [ω-rule](/XAMKAB1BZM/). Apply this to $\sigma = \operatorname{Con}(\mathrm{PA})$, and say why the argument fails for $\neg\operatorname{Con}(\mathrm{PA})$.

21. ★ Over $\mathrm{RCA}_0$, the statement "if $X$ is a well-order, then $\omega^X$ is a well-order" is equivalent to $\mathrm{ACA}_0$. Use this to show that $\mathrm{ACA}$, which has induction for all formulas of second-order arithmetic, proves that the standard notation system for $\varepsilon_0$ is well-ordered. Why does the same argument not work in $\mathrm{ACA}_0$?

22. ★ Show that $\gamma \mapsto \varphi_\gamma(0)$ is strictly increasing, so $\varphi_\gamma(0) \ge \gamma$ for all $\gamma$. Let $g_0 = 0$ and $g_{n+1} = \varphi_{g_n}(0)$. Show that $\sup_n g_n$ is the least $\gamma$ with $\varphi_\gamma(0) = \gamma$, which is $\Gamma_0$.

23. ★ Let $0 < \alpha < \Gamma_0$ be additively indecomposable. Show that $\alpha = \varphi_\gamma(\delta)$ for some $\gamma, \delta < \alpha$. Conclude that every ordinal below $\Gamma_0$ is named by a term built from $0$, $+$ and the binary function $(\gamma, \delta) \mapsto \varphi_\gamma(\delta)$.

24. ★ Let $\prec$ be a well-order on $\N$, and let $\Gamma(S) = \set{x : \forall y\, (y \prec x \to y \in S)}$, with stages $I^\alpha = \Gamma(I^{<\alpha})$. Show that the stage of each $x$ is the order type of $\set{y : y \prec x}$, and that the closure ordinal is the order type of $\prec$.
