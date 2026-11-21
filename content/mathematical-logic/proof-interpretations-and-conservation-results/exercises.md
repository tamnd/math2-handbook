1. ◦ Let $P$ and $Q$ be atomic formulas of pure predicate logic. Compute the Gödel–Gentzen [translation](/HGJVM49PA4/) of $\exists x\, P(x) \vee Q$, and simplify it to an intuitionistically equivalent formula with no triple negations and no $\neg\neg$ in front of a conjunct.

2. ◦ In Heyting arithmetic, write $\neg B$ for $B \to \bot$. Write out the [A-translation](/6CCK0TT69P/) of $\forall x\, (x = 0 \vee \neg\, x = 0)$ for an arbitrary formula $A$.

3. ◦ In [system T](/A4WR995XZP/), with $R_0\, a\, f\, 0 \rightsquigarrow a$ and $R_0\, a\, f\, (Sn) \rightsquigarrow f\, n\, (R_0\, a\, f\, n)$: (a) find the normal form of $R_0\, 0\, (\lambda k\, r.\, S(Sr))\, \bar 3$; (b) say which function $n \mapsto R_0\, 0\, (\lambda k\, r.\, S(Sr))\, n$ is; (c) give a term of the form $R_0\, a\, f$ for the predecessor function, with $0 \mapsto 0$.

4. ◦ Let $\varphi(n, m, k)$ be quantifier-free. Write the [Dialectica interpretation](/HZ17ES9PDY/) $\exists x\, \forall y\, A_D(x, y)$ of $A = \forall n\, \exists m\, \forall k\, \varphi(n, m, k)$, naming the types of $x$ and $y$.

5. ◦ For the same $A = \forall n\, \exists m\, \forall k\, \varphi(n, m, k)$, write the [no-counterexample interpretation](/4BCD1EM542/), and say which arguments the witnessing functional takes.

6. ◦ True or false, with $\varphi$ quantifier-free: (a) if $\mathsf{PA} \vdash \forall x\, \exists y\, \varphi(x, y)$, then $\mathsf{HA} \vdash \forall x\, \exists y\, \varphi(x, y)$; (b) PA and HA prove the same $\Pi^0_3$ sentences; (c) $\mathsf{ACA}_0$ proves some arithmetic sentence that PA does not prove; (d) every $\Pi^1_1$ sentence provable in $\mathsf{WKL}_0$ is provable in $\mathsf{RCA}_0$; (e) $\mathrm{I}\Sigma_1$ proves that the Ackermann function is total.

7. ◦ True or false, using the facts on [interpretability](/8H03GRMDYG/) that PA interprets $\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$ and does not interpret $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$: (a) $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ interprets $\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$; (b) $\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$ interprets $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$; (c) if $S \rhd T$ and $T \rhd U$, then $S \rhd U$; (d) if $S \rhd T$ and $T$ is inconsistent, then $S$ is inconsistent.

8. • Give an intuitionistic proof of $\neg\neg(\neg\neg A \to A)$ for an arbitrary formula $A$.

9. • Let $P(x, y)$ be atomic. Compute the Kuroda translation and the Gödel–Gentzen translation of $\forall x\, \exists y\, P(x, y)$, and show that both are intuitionistically equivalent to $\forall x\, \neg\neg \exists y\, P(x, y)$.

10. • Show that the A-translation of an instance $\varphi(0) \wedge \forall x\, (\varphi(x) \to \varphi(Sx)) \to \forall x\, \varphi(x)$ of the induction schema is again an instance of the induction schema.

11. • Write closed terms of system T for (a) the iteration functional $\mathrm{It}$ of type $(0 \to 0) \to 0 \to 0 \to 0$ with $\mathrm{It}\, f\, n\, x = f^n(x)$, (b) addition, and (c) the function $n \mapsto 2^n$, using only the recursor $R_0$.

12. • Let $A_0(n) = n + 1$, $A_{m+1}(0) = A_m(1)$ and $A_{m+1}(n+1) = A_m(A_{m+1}(n))$. Show that $A_{m+1}(n) = A_m^{n+1}(1)$, and use it to write $m \mapsto A_m$ as a term $R_{0 \to 0}\, a\, f$ of system T. Then compute $A_1(n)$, $A_2(n)$, $A_3(n)$ in closed form and the value $A_3(2)$.

13. • Compute the Dialectica interpretation of $\forall n\, \exists m\, \varphi(n, m) \to \forall k\, \exists l\, \psi(k, l)$ for quantifier-free $\varphi$ and $\psi$. Then take $\psi(k, l) = \varphi(k + 1, l)$ and give explicit witnessing terms.

14. • Let $c \in \N$ and let $f : \N \to \set{0, 1, \dots, c}$. The maximum principle $\exists n\, \forall k\, f(k) \le f(n)$ has the no-counterexample interpretation $\forall F\, \exists n\, f(F(n)) \le f(n)$. Give a witness $n$ that is found after at most $c + 1$ evaluations of $f$ at points of the form $F^i(0)$.

15. • Let $(a_n)$ be a nondecreasing sequence in $[0, c]$, let $\varepsilon > 0$, $K = \ceil{c / \varepsilon}$, $g : \N \to \N$ and $\tilde g(n) = n + g(n)$. Show that some $n \in \set{\tilde g^i(0) : i < K}$ satisfies $\abs{a_i - a_j} \le \varepsilon$ for all $i, j \in [n, n + g(n)]$. For $c = 2$, $\varepsilon = 1/3$ and $g(n) = n + 1$, list the candidates and give the largest.

16. • Use [Parsons's theorem](/2VYJXZZDGB/) to show that $\mathrm{I}\Sigma_1$ does not prove the totality of the Ackermann function.

17. • $\mathrm{I}\Sigma_1$ proves $\forall x\, \exists r\, (r^3 \le x < (r + 1)^3)$ by induction on $x$. Read off from that proof, in the manner of [Herbrand analysis](/MESZ87G9ET/), a primitive recursive function $r(x)$ that witnesses the statement, given by $r(0)$ and a step $r(x + 1)$ from $r(x)$. Compute $r(26)$, $r(27)$ and $r(63)$.

18. ★ Show that $\neg\neg \forall x\, (\neg\neg P(x) \to P(x))$ is not provable in intuitionistic predicate logic, with a Kripke model whose nodes are the natural numbers and whose domains are all equal to $\N$. Show also that $\forall x\, \neg\neg(\neg\neg P(x) \to P(x))$ is provable.

19. ★ A sentence $\sigma$ is an Orey sentence for PA if PA interprets both $\mathsf{PA} + \sigma$ and $\mathsf{PA} + \neg\sigma$. Using the Orey–Hájek characterization, show that no $\Pi_1$ sentence and no $\Sigma_1$ sentence is an Orey sentence for PA.

20. ★ Write the Cauchy property of a sequence $(a_n)$ of rationals as $\forall k\, \exists n\, \forall m\, \forall i, j \in [n, n + m]\, \abs{a_i - a_j} \le 2^{-k}$. Show that its no-counterexample interpretation is the statement of metastability: for every $k$ and every $g : \N \to \N$ there is $n$ with $\abs{a_i - a_j} \le 2^{-k}$ for all $i, j \in [n, n + g(n)]$.

21. ★ Let atomic formulas of arithmetic be decidable in HA, and let the Gödel–Gentzen translation leave arithmetic atoms unchanged. Show by induction on $A$ that $\mathsf{HA} \vdash \neg\neg A^N \to A^N$ for every formula $A$.
