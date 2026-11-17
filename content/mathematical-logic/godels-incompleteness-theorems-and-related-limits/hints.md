1. $\#(S0) = 2^{15} 3^{13}$ and $\#(v_0 = v_0) = 2^{21} 3^{7} 5^{21}$. The string is $SS0$. No: a string code has positive odd exponents on an initial run of primes, and the exponent of $3$ here is $0$.

3. (a) and (d). True arithmetic is not computably axiomatizable, Presburger arithmetic does not contain $\mathsf{Q}$, and the theory of all sentences is inconsistent.

4. Yes, if $\mathsf{PA}$ is consistent. Yes, it is equivalent to $\neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$. Yes: $\mathsf{PA}$ proves $G \leftrightarrow \mathrm{Con}(\mathsf{PA})$.

6. No. It proves $\exists x\, (0 \cdot x \ne 0)$, and $\mathsf{Q}$ proves $0 \cdot \overline n = 0$ for every $n$.

7. (a) and (b) exist. (c) does not, since the true $\Pi_3$ sentences are not $\Sigma_3$; (d) does not, by Tarski's theorem.

8. D1 is a rule. D3 is formalized $\Sigma_1$-completeness for the sentence $\square\varphi$. No: the theory $T$ proves $\neg\mathrm{Con}(\mathsf{PA})$ and hence $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, but it does not prove $0 = S0$, since it is consistent if $\mathsf{PA}$ is.

10. Enumerate the theorems until $\sigma$ or $\neg\sigma$ appears. A consistent, complete, c.e. extension of $\mathsf{Q}$ would then be a decidable consistent extension.

11. A false $\Sigma_1$ sentence $\exists x\, \theta(x)$ with $\theta$ in $\Delta_0$ has every $\theta(\overline n)$ false, so $\mathsf{Q}$ proves each $\neg\theta(\overline n)$.

12. Take $T = \mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$. Since $T$ extends $\mathsf{PA}$, $\mathsf{PA}$ proves $\mathrm{Con}(T) \to \mathrm{Con}(\mathsf{PA})$, so $T \vdash \neg\mathrm{Con}(T)$.

13. A Henkin sentence $H$ has $\mathsf{PA} \vdash \square H \to H$, so Löb's theorem makes it provable. Any two provable sentences are equivalent.

14. For $\delta \to \mathrm{Con}$: $\square(0 = S0) \to \square\delta$ by D1 and D2. For the converse: $\square\delta$ gives $\square\square\delta$ by D3 and $\square\neg\square\delta$ from the fixed point, so $\square(0 = S0)$.

16. By D1, $T \vdash \square\neg\varphi$. With $\square\varphi$ and D2 this gives $\square(0 = S0)$, which $\mathrm{Con}(T)$ denies, so $T + \mathrm{Con}(T) \vdash \neg\square\varphi$.

17. The proof of the second theorem formalizes: $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \neg\square\mathrm{Con}(\mathsf{PA})$. By the formalized deduction theorem, $\neg\square\mathrm{Con}(\mathsf{PA})$ is $\mathrm{Con}(\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA}))$.

19. If $T \nvdash \varphi$, then $T + \neg\varphi$ is consistent. From $\square\varphi \to \varphi$ it proves $\neg\square\varphi$, which is equivalent over $T$ to $\mathrm{Con}(T + \neg\varphi)$.

20. $T$ proves $\neg\, 0 = S0$ with some proof of code $p$, so $T \vdash \mathrm{Prf}_T(\overline p, \mathrm{neg}(\ulcorner 0 = S0 \urcorner))$. A Rosser proof $y$ of $0 = S0$ would need $y \le \overline p$, and $\mathsf{Q}$ checks the finitely many $y \le p$ one by one. The Rosser predicate fails D2 or D3, which the second theorem needs.

21. Let $\chi := \square(\square\varphi \to \varphi) \to \square\varphi$ and show $\mathsf{PA} \vdash \square\chi \to \chi$ with D2 and D3. Then Löb's theorem gives $\mathsf{PA} \vdash \chi$.

22. Let $\gamma(x)$ represent the set $C$, and take $\delta$ with $\mathsf{Q} \vdash \delta \leftrightarrow \neg\gamma(\ulcorner\delta\urcorner)$. If $\ulcorner\delta\urcorner \in C$, then $T$ refutes $\delta$; if not, $T$ proves $\delta$. Both contradict the choice of $C$.
