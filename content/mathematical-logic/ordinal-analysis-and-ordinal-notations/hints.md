2. $(3, 1, 1, 0)$ names $\omega^3 + \omega \cdot 2 + 1$ and $(2, 2, 2, 2, 2)$ names $\omega^2 \cdot 5$. The first is larger, because $3 > 2$ at the first place. $(3, 1, 1)$ is a proper initial segment of $(3, 1, 1, 0)$, so it lies below it; it names $\omega^3 + \omega \cdot 2$. $(1, 3)$ is not non-increasing.

3. $(\omega^{\omega^2} + \omega^3)[2] = \omega^{\omega^2} + \omega^2 \cdot 2$ and $\omega^{\omega^2}[3] = \omega^{\omega \cdot 3}$. The sequence of $\varepsilon_0$ runs $0, 1, \omega, \omega^\omega, \omega^{\omega^\omega}$, so $\varepsilon_0[4] = \omega^{\omega^\omega}$.

4. Gentzen's induction is not a theorem of $\mathrm{PA}$, so his proof is not a proof in $\mathrm{PA}$. If $\mathrm{PA}$ proved the quantifier-free induction along $\varepsilon_0$, it would prove $\operatorname{Con}(\mathrm{PA})$. So, if $\mathrm{PA}$ is consistent, it does not prove that induction.

7. $\psi_0(\Omega + 5) = \omega^{\varepsilon_0 + 5} = \varepsilon_0 \cdot \omega^5$, $\psi_0(\Omega + \varepsilon_0) = \omega^{\varepsilon_0 \cdot 2} = \varepsilon_0^2$ and $\psi_0(\Omega + \varepsilon_0 \cdot 2) = \omega^{\varepsilon_0 \cdot 3} = \varepsilon_0^3$.

9. (a) and (d) are $X$-positive; in (b) and (c) the atom $X(\cdot)$ occurs under one negation. For (a) the least fixed point is the set of multiples of $3$. The number $3k$ enters at stage $k$, and no new element enters at stage $\omega$, so the closure ordinal is $\omega$.

11. Use $\operatorname{TI}(\omega, \varphi^{+++})$ and three jumps: $\omega$, then $\omega^\omega$, then $\omega^{\omega^\omega}$, then $\omega^{\omega^{\omega^\omega}}$. Each proof uses a fixed formula, so it makes only finitely many jumps and reaches a finite tower. $\varepsilon_0$ is the limit of all finite towers.

12. With $\omega^\alpha$ the three steps give $\omega^{\omega + 3}$, then $\omega^{\omega^{\omega + 3}}$, then $\omega^{\omega^{\omega^{\omega + 3}}}$. With $2^\alpha$ they give $2^{\omega + 3} = \omega \cdot 8$, then $2^{\omega \cdot 8} = \omega^8$, then $2^{\omega^8} = \omega^{\omega^7}$.

17. The even number $2k$ enters at stage $k$ and the odd number $2k + 1$ at stage $\omega + k$. The closure ordinal is $\omega \cdot 2$, the order type of $\prec$.

19. The reduction replaces $X$ by $T$ in the left premise, so the new cut formula is $T(a)$, which is $\forall X\, X(a)$ again. An abstract can be as complex as the formula it is substituted into, or more.

20. Embed $\mathrm{PA} + \sigma$ as $\mathrm{PA}$ is embedded. The extra axiom $\sigma$ is true, so it has a cut-free derivation of finite height. Cut elimination and boundedness then give heights and order types below $\varepsilon_0$. The sentence $\neg \operatorname{Con}(\mathrm{PA})$ is false, so it has no derivation in the infinitary system. The lower bound $\varepsilon_0$ comes from $\mathrm{PA}$ itself.

21. Prove $\forall n\, \mathrm{WO}(\omega_n)$, with $\omega_0 = \omega$ and $\omega_{n+1} = \omega^{\omega_n}$, by induction on $n$. Each descending sequence in the notations for $\varepsilon_0$ starts below some $\omega_n$. The formula $\mathrm{WO}(\omega_n)$ has a set quantifier, so $\mathrm{ACA}_0$ cannot use induction on it.

22. If $\gamma < \gamma'$, then $\varphi_{\gamma'}(0)$ is a fixed point of $\varphi_\gamma$ and is larger than $0$, so $\varphi_{\gamma'}(0) = \varphi_\gamma(\varphi_{\gamma'}(0)) > \varphi_\gamma(0)$. For the supremum $g$, use the continuity of $\gamma \mapsto \varphi_\gamma(0)$ at limits.

23. The set of $\gamma$ with $\alpha$ in the range of $\varphi_\gamma$ contains $0$, is closed under limits, and is bounded by $\alpha$, since $\varphi_\gamma(0) \ge \gamma$. Let $\gamma$ be its largest element. If $\gamma = \alpha$ then $\alpha \ge \varphi_\alpha(0) \ge \alpha$, so $\alpha = \varphi_\alpha(0)$, which is impossible below $\Gamma_0$. So $\gamma < \alpha$, and $\delta < \alpha$ because $\alpha$ is not a fixed point of $\varphi_\gamma$.

24. Use transfinite induction along $\prec$. If every $y \prec x$ has stage equal to the order type of its initial segment, then $x$ enters at the least stage above all of these, which is the order type of $\set{y : y \prec x}$.
