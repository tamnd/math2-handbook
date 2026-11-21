1. ◦ Which of the following are theorems of [GL](/WJK0YA4GP2/)? (a) $\square p \to \square\square p$; (b) $\square p \to p$; (c) $\square(p \wedge q) \leftrightarrow (\square p \wedge \square q)$; (d) $\square\Diamond p \to \square\bot$; (e) $\neg\square\bot \to \neg\square\square\bot$.

2. ◦ Which of these frames validate Löb's axiom? (a) one reflexive world; (b) $(\set{0, 1, 2}, <)$; (c) $(\N, <)$; (d) $(\N, >)$; (e) two worlds that see each other and not themselves.

3. ◦ Using the [fixed-point theorem](/TDDX1NHG8D/), give a formula without $p$ that is $\mathsf{GL}$-equivalent to the fixed point of each equation: (a) $p \leftrightarrow \Diamond p$; (b) $p \leftrightarrow \square(p \to q)$; (c) $p \leftrightarrow (\neg\square p \wedge \square q)$.

4. ◦ Using [Solovay's theorem](/1ZRWVDYPX0/), decide whether PA proves each sentence: (a) $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$; (b) $\Pr(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner) \to \Pr(\ulcorner 0 = 1 \urcorner)$; (c) $\neg\Pr(\ulcorner \neg\mathrm{Con}(\mathsf{PA}) \urcorner) \to \mathrm{Con}(\mathsf{PA})$.

5. ◦ Which of the following are theorems of the [Grzegorczyk logic](/2Q8E4GQF3B/)? (a) $\square p \to p$; (b) $\square(\square p \to p) \to \square p$; (c) $\square p \to \square\square p$; (d) $p \to \square\Diamond p$; (e) $\Diamond\square p \to \square\Diamond p$.

6. ◦ (a) How many operators $\square$ make the two-element Boolean algebra a [Magari algebra](/PHWAN904PT/), and which? (b) On the frame $W = \set{0, 1, 2}$ with $2R1$, $1R0$ and $2R0$, let $\square X = \set{w : R[w] \subseteq X}$. Compute $\square\emptyset$, $\square\square\emptyset$ and $\square\square\square\emptyset$.

7. ◦ Which of the following are theorems of [interpretability logic](/BGKZTSQN3W/) $\mathsf{IL}$? (a) $p \rhd p$; (b) $\Diamond p \rhd p$; (c) $p \rhd \Diamond p$; (d) $p \rhd q \to (\Diamond p \to \Diamond q)$; (e) $\square\neg p \to (p \rhd \bot)$.

8. • Derive $\Diamond p \to \Diamond(p \wedge \square\neg p)$ in $\mathsf{GL}$ from Löb's axiom with the letter $\neg p$.

9. • Give a Kripke countermodel to $\square(p \vee q) \to (\square p \vee \square q)$ on a finite transitive irreflexive frame, and show that no such frame with at most two worlds is a countermodel.

10. • Give a countermodel to $\square(\square p \to \square q) \vee \square(\square q \to \square p)$ on a finite transitive irreflexive frame with five worlds.

11. • Find $n$ such that each formula is $\mathsf{GL}$-equivalent to $\square^n\bot$: (a) $\square\Diamond\top$; (b) $\square(\square\square\bot \to \square\bot)$; (c) $\square(\Diamond\top \to \Diamond\Diamond\top)$.

12. • Show that PA proves $\mathrm{Con}(\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})) \leftrightarrow \mathrm{Con}(\mathsf{PA})$.

13. • Let $W = \set{w, u}$ with $wRu$ only, $S_w = \set{(u, u)}$ and $S_u = \emptyset$. Check that this is a Veltman frame satisfying the frame condition of M, and that $\top \rhd \Diamond\top$ fails at $w$. What does this say about PA?

14. • In a Magari algebra, let $x = \neg\square x$. Show that $x = \neg\square 0$, and that $\neg\square 0$ is indeed a solution of $x = \neg\square x$.

15. • The translation $t$ leaves letters fixed, commutes with the Boolean connectives and sets $(\square A)^t = A^t \wedge \square A^t$. Compute $(\square p \to \square\square p)^t$ and show that it is a theorem of $\mathsf{GL}$.

16. • In [GLP](/3EDRQJJHMT/), derive (a) $[0]p \to [1][0]p$ and (b) $\langle 2 \rangle\top \to \langle 1 \rangle\langle 1 \rangle\top$.

17. ★ Show that every letter-free modal formula is $\mathsf{GL}$-equivalent to a Boolean combination of formulas $\square^n\bot$, and that $\square A$ is equivalent to $\top$ or to a single $\square^k\bot$ for every letter-free $A$.

18. ★ Show directly from the semantics that the reflexive frame $(\N, \ge)$, in which each number sees itself and every smaller number, validates the Grzegorczyk axiom $\square(\square(p \to \square p) \to p) \to p$.

19. ★ Show that $\neg\square\bot$ is a theorem of $\mathsf{GLS}$ but is false at some world of every finite $\mathsf{GL}$ model, and that $\mathsf{GLS}$ is not closed under necessitation.

20. ★ Show that the rule "from $\square A$ infer $A$" is admissible in $\mathsf{GL}$: if $\mathsf{GL} \vdash \square A$, then $\mathsf{GL} \vdash A$.
