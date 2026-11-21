1. ◦ Which of these are instances of the [naive truth schema](/99XVFR5ZN5/) for a sentence of $\mathcal{L}_T$, and which are axioms of $\mathsf{TB}$? (a) $T(\ulcorner 0 = 0 \urcorner) \leftrightarrow 0 = 0$. (b) $T(\ulcorner \neg T(\ulcorner 0 = 1 \urcorner) \urcorner) \leftrightarrow \neg T(\ulcorner 0 = 1 \urcorner)$. (c) $T(\ulcorner x = x \urcorner) \leftrightarrow x = x$. (d) $\forall x\, (T(\ulcorner \dot x = \dot x \urcorner) \leftrightarrow x = x)$.

2. ◦ Ann says "what Bob says is true", Bob says "what Cleo says is true", and Cleo says "what Ann says is not true". Show that no assignment of true and false to the three claims satisfies their three T-sentences. How many assignments do so if Cleo says "what Ann says is true" instead?

3. ◦ Count the letters of the phrase "the least number not definable in fewer than forty letters". Does it give a [Berry paradox](/MYP4A5VRBA/)? What changes when "forty" is replaced by "fifty"?

4. ◦ Four sentences $S_0, S_1, S_2, S_3$ are given, where $S_n$ says that every $S_k$ with $k \neq n$ is untrue. How many assignments of true and false satisfy all four T-sentences? Compare the finite variants of the [Yablo paradox](/6FJXAN1ND9/), which have exactly one.

5. ◦ Which of these adjectives are [autological](/VFHBYVXPCB/) and which are heterological: "polysyllabic", "monosyllabic", "English", "French", "hyphenated", "unhyphenated"?

6. ◦ In the [Tarskian hierarchy](/Z6MCGB0ZFX/) over arithmetic, find for each sentence the least $n$ with the sentence in $\mathcal{L}_n$, and its value in $\mathcal{N}_n$. (a) $T_0(\ulcorner 1 + 1 = 2 \urcorner)$. (b) $T_1(\ulcorner T_0(\ulcorner 0 = 1 \urcorner) \urcorner)$. (c) $T_0(\ulcorner T_0(\ulcorner 0 = 0 \urcorner) \urcorner)$. (d) $\neg T_1(\ulcorner \neg T_0(\ulcorner 0 = 0 \urcorner) \urcorner)$.

7. ◦ Let $\psi_0 := (0 = 1)$ and $\psi_{n+1} := \neg T(\ulcorner \psi_n \urcorner)$. In the stages of [Kripke's theory of truth](/ES71QTSTNV/), at which stage does $\psi_n$ first get a value other than $\mathrm{u}$, and which value is it?

8. ◦ Decide for each inference whether it is valid in strong Kleene logic $K_3$, with designated value $1$, and in the [logic of paradox](/BXJZG67PX3/) $\mathrm{LP}$, with designated values $1$ and $\mathrm{b}$. (a) $p \wedge \neg p \models q$. (b) $p \models p \vee q$. (c) $p, \neg p \vee q \models q$. (d) $\models p \vee \neg p$. (e) $p \vee q, \neg p \models q$.

9. ◦ Start a revision sequence with $S_0 := \set{\ulcorner 0 = 1 \urcorner}$. At which stages $S_\zeta$ is the code of $T(\ulcorner 0 = 1 \urcorner)$ a member? Is $\neg T(\ulcorner 0 = 1 \urcorner)$ categorically true in the [revision theory](/ZQ4TWM7K6E/)?

10. ◦ Let $S$ be the theory $\mathsf{Q} + \forall x\, \neg T(x)$. Which of the three hypotheses NEC, (D) and (U) of [McGee's theorem](/GQW8RQVZJ4/) does $S$ satisfy? Is $S$ $\omega$-consistent?

11. • A cycle of $n$ claims is given, where claim $i$ says that claim $i + 1$ is not true, and claim $n$ says that claim $1$ is not true. For which $n$ is there an assignment of true and false that satisfies all $n$ T-sentences, and how many are there? What is the rule for a cycle in which some links say "true" and others "not true"?

12. • Let $S_n$ say that some $S_k$ with $k > n$ is untrue, for $n = 0, 1, 2, \ldots$. Show that no assignment of true and false satisfies all the T-sentences. Then take only $S_0, \ldots, S_{N-1}$, where $S_n$ speaks about the $S_k$ with $n < k < N$, and find all assignments that satisfy them.

13. • Let $\lambda$ be the liar of the [proof of the diagonal lemma](/SFPSB6JPTC/). In Kripke's construction, which of these sentences are grounded? For the grounded ones, give the first stage at which they have a value and the value. (a) $T(\ulcorner \lambda \urcorner) \vee 0 = 0$. (b) $T(\ulcorner \lambda \urcorner) \wedge 0 = 1$. (c) $T(\ulcorner \lambda \urcorner) \vee \neg T(\ulcorner \lambda \urcorner)$. (d) $\neg T(\ulcorner \neg T(\ulcorner 0 = 1 \urcorner) \urcorner)$. (e) $\forall x\, T(x)$. (f) $\exists x\, T(x)$.

14. • Let $\sigma$ satisfy $\sigma \leftrightarrow T(\ulcorner \sigma \urcorner) \vee \neg T(\ulcorner \sigma \urcorner)$, built like the [truth-teller](/XADBJH4872/). Show that $\sigma$ has value $0$ in no Kripke fixed point and value $\mathrm{u}$ in the least one. Then show that $\sigma$ is categorically true in the revision theory.

15. • Let $\alpha \leftrightarrow T(\ulcorner \beta \urcorner)$ and $\beta \leftrightarrow \neg T(\ulcorner \alpha \urcorner)$, a liar cycle of length two. Compute the first five stages of the revision sequence with $S_0 = \emptyset$, restricted to the codes of $\alpha$ and $\beta$. Show that in every revision sequence neither $\alpha$ nor $\beta$ is nearly stably true or nearly stably false.

16. • A Curry sentence $\kappa$ satisfies $\kappa \leftrightarrow (T(\ulcorner \kappa \urcorner) \to 0 = 1)$. Derive $0 = 1$ from the naive truth schema for $\kappa$ without using negation, and say which step uses an assumption twice; compare [Curry's paradox uses contraction](/40Q1NK471S/). Then, reading $\to$ as the material conditional, find the value of $\kappa$ in every strong Kleene fixed point and in every $\mathrm{LP}$ fixed point.

17. • Let $Y_n$ say that $Y_k$ is untrue for every $k > n$, as in the Yablo paradox, and give $\forall$ its strong Kleene value. Show that every $Y_n$ has value $\mathrm{u}$ in every Kripke fixed point, not only in the least one.

18. • In the proof of the [knower paradox](/N3BWQRFQCC/), let $\kappa$ satisfy $\mathsf{Q} \vdash \kappa \leftrightarrow \neg K(\ulcorner \kappa \urcorner)$. Show that $\mathsf{Q}$ plus the single instance $K(\ulcorner \kappa \urcorner) \to \kappa$ of factivity, closed under necessitation, is already inconsistent.

19. • Use axiom 9 of the [definition of KF](/VQG258JQAD/) and the results of [the liar in KF](/DN71AAR1R1/) to show that $\mathsf{KF} + \mathsf{Compl}$ proves $T(\ulcorner \lambda \vee \neg \lambda \urcorner)$ and that $\mathsf{KF} + \mathsf{Cons}$ proves $\neg T(\ulcorner \lambda \vee \neg \lambda \urcorner)$. Which classical theorem does $\mathsf{KF} + \mathsf{Cons}$ then call untrue?

20. • Take a sorites series of $100$ grains, with premises $H(100)$, $\neg H(1)$ and $H(n + 1) \to H(n)$ for $1 \le n \le 99$. In a supervaluation whose admissible sharpenings are "$H(n)$ if and only if $n \ge k$" for $20 \le k \le 60$, which conditionals fail to be super-true, and how many are super-true? Is $\forall n\, (H(n + 1) \to H(n))$ super-false?

21. • In the same series, put $v(H(n)) := (n - 1)/99$ and use the Łukasiewicz conditional of [Łukasiewicz infinite-valued logic](/NFCEM44XYH/). Find the value of each conditional, the value of the weak conjunction (minimum) of all $99$ conditionals, and the value of their strong conjunction $\max(0, a + b - 1)$.

22. ★ Formalize Exercise 12 in arithmetic: by the diagonal lemma with parameters, take sentences $S_n$ with $\mathsf{PA} \vdash S_n \leftrightarrow \exists k > \underline{n}\, \neg T(\ulcorner S_k \urcorner)$, in the style of [the Yablo T-sentences](/ASVGQGMW9P/). Show that $\mathsf{PA}$ with induction for $\mathcal{L}_T$ plus all T-sentences $T(\ulcorner S_n \urcorner) \leftrightarrow S_n$ is consistent, but has no model whose numbers are the standard ones.

23. ★ Let $\tau$ be the truth-teller. Show that iterating the Kripke jump from $(\set{\ulcorner \tau \urcorner}, \emptyset)$ gives a fixed point in which $\tau$ has value $1$, and that iterating from $(\emptyset, \set{\ulcorner \tau \urcorner})$ gives one in which it has value $0$. Conclude that $\tau$ has value $\mathrm{u}$ in every intrinsic fixed point.

24. ★ Let $B_A$ be the sentence $T(\ulcorner \neg A \urcorner) \leftrightarrow \neg T(\ulcorner A \urcorner)$. Show that $B_A$ is nearly stably true in every revision sequence, for every sentence $A$, so that it is valid in $\mathsf{T}^{\#}$. Then give a revision sequence over $\mathcal{N}$ in which $B_\lambda$ is not stably true, so that $B_\lambda$ is not valid in $\mathsf{T}^*$.

25. ★ Show that $\mathsf{TB}$ does not prove the single sentence $\forall A\, (T[\neg A] \leftrightarrow \neg TA)$, although it proves each instance $T(\ulcorner \neg \varphi \urcorner) \leftrightarrow \neg T(\ulcorner \varphi \urcorner)$ for $\varphi$ without $T$. See [axiomatic theories of truth](/KE8ZX8KVA3/).

26. ★ In the [sorites paradox](/2BV7KAZG1H/) with $10000$ grains, let $v$ be any assignment of values in $[0, 1]$ with $v(H(10000)) = 1$ and $v(H(1)) = 0$. Show that some conditional $H(n + 1) \to H(n)$ has Łukasiewicz value at most $1 - 1/9999$, and that the linear assignment of the entry is the only one in which every conditional reaches this value.
