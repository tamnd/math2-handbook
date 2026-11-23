1. The translation is $\neg(\neg\neg \forall x\, \neg\neg\neg P(x) \wedge \neg\neg\neg Q)$. Since $\neg\neg\neg B \leftrightarrow \neg B$ and $\neg(\neg\neg X \wedge Y) \leftrightarrow \neg(X \wedge Y)$ intuitionistically, it is equivalent to $\neg(\forall x\, \neg P(x) \wedge \neg Q)$.

3. (a) $\bar 6$. (b) $n \mapsto 2n$. (c) $R_{\N}\, 0\, (\lambda k\, r.\, k)$, since $R_{\N}\, 0\, (\lambda k\, r.\, k)\, (Sn) \rightsquigarrow n$.

7. (a) True: PA interprets it, and $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ contains PA. (b) False: PA interprets $\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$, so by composing PA would interpret $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$. (c) True: compose the translations. (d) True: a proof of $\bot$ in $T$ translates to a proof of $\bot$ in $S$.

9. Kuroda gives $\neg\neg \forall x\, \neg\neg \exists y\, P(x, y)$; Gödel–Gentzen gives $\forall x\, \neg \forall y\, \neg\neg\neg P(x, y)$, and $\neg \forall y\, \neg B \leftrightarrow \neg\neg \exists y\, B$. For the Kuroda form, the formula $\forall x\, \neg\neg B$ is stable: from $\neg\neg \forall x\, \neg\neg B$ one gets $\neg\neg\neg\neg B$ for each $x$, which is $\neg\neg B$.

12. Both sides satisfy the same recursion in $n$. Take $a = S$ and $f = \lambda k\, g.\, \lambda n.\, \mathrm{It}\, g\, (Sn)\, \bar 1$. Then $A_1(n) = n + 2$, $A_2(n) = 2n + 3$, $A_3(n) = 2^{n+3} - 3$ and $A_3(2) = 29$.

13. The interpretation is $\exists U, Y\, \forall f, k\, \bigl(\varphi(Y f k, f(Y f k)) \to \psi(k, U f k)\bigr)$. For $\psi(k, l) = \varphi(k + 1, l)$ take $Y f k = k + 1$ and $U f k = f(k + 1)$.

14. Put $n_0 = 0$ and $n_{i+1} = F(n_i)$, and take the first $n_i$ with $f(F(n_i)) \le f(n_i)$. If $n_0, \dots, n_c$ all fail, then $f(n_0) < f(n_1) < \cdots < f(n_{c+1})$ are $c + 2$ distinct values in $\set{0, \dots, c}$. To stay within $c + 1$ evaluations, evaluate $f(n_0), f(n_1), \dots$ in turn, and answer $n_i$ as soon as $f(n_{i+1}) \le f(n_i)$ or $f(n_i) = c$. Until then the values strictly increase, so $f(n_i) \ge i$, and at the latest $f(n_c) = c$.

15. If all $K$ candidates fail, $a$ increases by more than $\varepsilon$ on each of $K$ consecutive intervals, so by more than $K\varepsilon \ge c$ in total. Here $\tilde g(n) = 2n + 1$ and $K = 6$; the candidates are $0, 1, 3, 7, 15, 31$, so the largest is $31$.

17. Take $r(0) = 0$, and $r(x + 1) = r(x) + 1$ if $(r(x) + 1)^3 \le x + 1$, otherwise $r(x + 1) = r(x)$. Then $r(26) = 2$, $r(27) = 3$ and $r(63) = 3$.

18. Let node $k$ force $P(i)$ exactly when $i < k$. Every node forces $\neg\neg P(i)$ for every $i$, but node $k$ does not force $P(k)$, so no node forces $\forall x\, (\neg\neg P(x) \to P(x))$. The second formula is $\forall x$ applied to an instance of exercise 8.

19. If $\sigma$ is $\Pi_1$ and $\mathsf{PA} \rhd \mathsf{PA} + \sigma$, then every $\Pi_1$ theorem of $\mathsf{PA} + \sigma$ is a theorem of PA. So PA proves $\sigma$, and $\mathsf{PA} + \neg\sigma$ is inconsistent; a consistent theory cannot interpret it. For a $\Sigma_1$ sentence, apply the same argument to the $\Pi_1$ sentence $\neg\sigma$.

20. For fixed $k$, the matrix $\forall i, j \in [n, n + m]\, \abs{a_i - a_j} \le 2^{-k}$ is bounded, hence decidable, and the formula has the form $\exists n\, \forall m\, \theta(n, m)$. Its no-counterexample interpretation replaces $m$ by $g(n)$.

21. Atoms are decidable, so $\neg\neg P \to P$. Use $\neg\neg(B \wedge C) \to \neg\neg B \wedge \neg\neg C$, $\neg\neg(B \to C) \to (B \to \neg\neg C)$ and $\neg\neg \forall x\, B \to \forall x\, \neg\neg B$, and note that the clauses for $\vee$ and $\exists$ produce negations, which are always stable.
