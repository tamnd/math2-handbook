1. ◦ The fork has a root $r$ and two worlds $a$ and $b$ above it, which are incomparable. Let $p$ be true at $a$ only and $q$ at $b$ only. Using the clauses of [Kripke semantics](/5GTQ69W47T/), decide which of these formulas $r$ forces: $p \vee \neg p$, $\neg p \vee \neg\neg p$, $\neg\neg p \to p$, $(p \to q) \vee (q \to p)$ and $\neg\neg(p \vee q) \to \neg\neg p \vee \neg\neg q$.

2. ◦ In the four-element chain $0 < a < b < 1$, viewed as a Heyting algebra as in the [algebraic semantics](/JM1XJXWZYH/), compute $\neg a$, $\neg\neg a$, $a \to b$, $b \to a$ and $a \vee \neg a$. Is $\neg\neg p \to p$ valid in this algebra? Is $(p \to q) \vee (q \to p)$?

3. ◦ In the [topological semantics](/RKFTMQNWRC/) on $\R$, let $V(p) = (0, 1)$. Compute the open sets of $\neg p$, $\neg\neg p$ and $p \vee \neg p$. Then also let $V(q) = (1, 2)$ and compute $p \to q$, $q \to p$ and $(p \to q) \vee (q \to p)$.

4. ◦ Use [Glivenko's theorem](/B9M3P61ZVA/) to decide which of these formulas $\mathsf{IPC}$ proves: (a) $\neg\neg(\neg\neg p \to p)$, (b) $\neg\neg((p \to q) \vee (q \to p))$, (c) $\neg\neg(((p \to q) \to p) \to p)$, (d) $\neg\neg(p \to q)$. Does the theorem tell you whether $\mathsf{IQC}$ proves $\neg\neg\forall x\,(Px \vee \neg Px)$?

5. ◦ Write out Gödel's formula $D_2$ from [Gödel's theorem on finite matrices](/CFCPJA1QF5/). Give a valuation on the two-world chain that refutes it at the bottom world, and explain in one line why it holds in the two-element Boolean algebra.

6. ◦ Show that neither of the rules "from $p \vee q$ infer $p$" and "from $p$ infer $q$" is an [admissible rule](/C5K35H0R4Y/) of $\mathsf{IPC}$, by giving for each a substitution that makes the premise a theorem and the conclusion a non-theorem.

7. ◦ For each of $\mathsf{LC}$, $\mathsf{KC}$ and $\mathsf{CPC}$, give a disjunction that the logic proves while it proves neither disjunct, so that the logic fails the [disjunction property](/YTRVX6F3FX/).

8. ◦ In the [Rieger–Nishimura ladder](/KAB6KM98ZZ/), compute the truth sets of $F_3$, $F_7$ and $F_8$ from the recursion. Does $F_6$ imply $F_7$ in $\mathsf{IPC}$? Does $F_5$ imply $F_6$?

9. ◦ Compute the [Gödel–McKinsey–Tarski translations](/BXVNEN55MR/) of $\neg p \vee \neg\neg p$ and of $(p \to q) \vee (q \to p)$.

10. ◦ How many worlds does the Medvedev frame $M_n$ of [Medvedev's logic](/R2FD01J3PC/) have, how many of them are maximal, and how many worlds does its longest chain have? Draw $M_3$.

11. • Show that $\mathsf{IPC}$ proves $\neg\neg(p \to q) \leftrightarrow (\neg\neg p \to \neg\neg q)$. Give derivations in natural deduction, or argue with Kripke models and the completeness theorem.

12. • Give Kripke countermodels to [Peirce's law](/GMSZ75D5WE/) $((p \to q) \to p) \to p$ and to the [De Morgan law](/09PKJKA6J0/) $\neg(p \wedge q) \to \neg p \vee \neg q$. Use as few worlds as you can, and check each clause.

13. • Show that [minimal logic](/V7MTF4P01E/) proves $(p \to \neg p) \to \neg p$ and $\neg\neg\neg p \to \neg p$, and that it proves neither $\neg p \to (p \to q)$ nor the disjunctive syllogism $(p \vee q) \wedge \neg p \to q$. For the second part, treat $\bot$ as an atom.

14. • Show that $\mathsf{LC}$ proves $\neg p \vee \neg\neg p$, so that $\mathsf{KC} \subseteq \mathsf{LC}$. Then find a frame with four worlds that validates $\neg p \vee \neg\neg p$ but not $(p \to q) \vee (q \to p)$, so that the inclusion is strict.

15. • Show that $(p \to q) \vee (q \to p)$ is valid on every linearly ordered frame, and that on a finite rooted frame it is valid only if the frame is a chain, as in the definition of [Gödel–Dummett logic](/FA88H7FDPY/).

16. • Find a Kripke model with four worlds whose root refutes the axiom of [Kreisel–Putnam logic](/X0C1NC7FXX/).

17. • Using the [Kleene slash](/YRRKEEHNCD/), show that $\set{p \to q \vee r}$ is self-slashing, although $p \to q \vee r$ is not a Harrop formula. Deduce that if $p \to q \vee r \vdash \varphi \vee \psi$ in $\mathsf{IPC}$, then $p \to q \vee r$ proves $\varphi$ or proves $\psi$. Show that $\set{p,\ p \to q \vee r}$ is not self-slashing.

18. • Show that every [intermediate logic](/H5NSKEP3P2/) $L$ proves the same negated formulas $\neg\varphi$ as $\mathsf{CPC}$. Use Glivenko's theorem and $\neg\neg\neg\varphi \to \neg\varphi$.

19. • In the topological semantics on $\R$, let $V(p) = (0, 1) \cup (1, 2)$. Compute the open sets of $\neg p$, $\neg\neg p$, $\neg\neg p \to p$ and $\neg p \vee \neg\neg p$, and name the points where each formula fails.

20. • Show that $\square(p \to q) \to (\lozenge p \to \lozenge q)$ and $\neg\lozenge\bot$ are valid on every birelational frame, with the forcing clauses of [intuitionistic modal logic](/J57YRDWX3G/). Does your proof use condition F1 or F2?

21. • Give a Kripke model of [intuitionistic predicate logic](/MW0RVDRFTA/) with two worlds that refutes $(\forall x\,Px \to Q) \to \exists x\,(Px \to Q)$, where $Q$ is a sentence letter. Show that the formula is classically valid in every non-empty domain.

22. ★ Build a Kripke model on the worlds $0 \le 1 \le 2 \le \cdots$ that refutes the double negation shift $\forall x\,\neg\neg Px \to \neg\neg\forall x\,Px$. Show that the same model refutes $\neg\neg\forall x\,(Px \vee \neg Px)$, and explain why no model on a finite frame can refute the double negation shift.

23. ★ Prove that $D_n$ holds in every Heyting algebra with at most $n$ elements and fails on the chain of $n$ worlds. Deduce that no finite Heyting algebra validates exactly the theorems of $\mathsf{IPC}$.

24. ★ Prove Glivenko's theorem with Kripke models. Show first that in a finite model, $w \Vdash \neg\neg\varphi$ if and only if every maximal world above $w$ forces $\varphi$, and use that a maximal world forces formulas as a classical valuation does.

25. ★ Show that $\neg p \vee \neg\neg p$ is valid on a finite rooted frame if and only if the frame has a greatest element, as the theorem on the [weak excluded middle](/CX032ACTMZ/) predicts for directed frames.

26. ★ Play the [dialogue](/ZCEBYYP67J/) for $p \to \neg\neg p$ and for $\neg\neg p \to p$ under the formal rule, with each move attacked at most once. Show that $\mathbf{P}$ wins the first under the intuitionistic rule, that $\mathbf{P}$ has no winning strategy for the second under the intuitionistic rule, and that $\mathbf{P}$ wins the second under the classical rule. Would it help $\mathbf{P}$ in the second dialogue to be allowed to attack each move of $\mathbf{O}$ twice?
