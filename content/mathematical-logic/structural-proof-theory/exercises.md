1. ◦ Apply the [cut rule](/HGVMPZ2DXA/) where you can, and give the degree of each cut. (a) Premises $p \Rightarrow q \to r$ and $q \to r, s \Rightarrow t$, cut formula $q \to r$. (b) Premises $\Rightarrow p \vee q, p$ and $p, r \Rightarrow s$, cut formula $p$. In each case say whether the context-sharing form also applies to the premises as given.

2. ◦ List the distinct subformulas of $(p \to q) \to (\neg q \to \neg p)$, first with $\neg$ as a primitive connective, then with $\neg A$ read as $A \to \bot$. By the [subformula property](/Z2NXKDK06G/), which formulas can occur in a cut-free derivation of $\Rightarrow (p \to q) \to (\neg q \to \neg p)$?

3. ◦ In implicational natural deduction, let $D$ be the derivation that applies ${\to}$E to the assumptions $w : p \to q$ and $u : p$ to get $q$, then ${\to}$I discharging $u$ to get $p \to q$, then ${\to}$E with a new assumption $v : p$ to get $q$. Find the detour and its degree, and carry out the reduction step of the [normalization theorem](/W33WAE1XTC/).

4. ◦ Run backward search in G3cp, the [contraction-free calculus](/KP5KA51FC4/), on $\Rightarrow (p \vee q) \to (p \wedge q)$. List the final sequents, decide whether the sequent is derivable, and read off a valuation that falsifies the formula.

5. ◦ Derive $(p \vee q) \wedge r \Rightarrow (p \wedge r) \vee (q \wedge r)$ in G3ip and give the height. Then show that a derivation cannot end with R${\vee}$.

6. ◦ A connective $\star$ has one introduction rule, from $A$ and $B$ infer $A \star B$, and one elimination rule: from $A \star B$ and a derivation of $C$ from the assumptions $A$ and $B$, infer $C$ and discharge $A$ and $B$. Show that the rules are in harmony in the sense of [proof-theoretic semantics](/K97KZB5R7N/): give the reduction of an introduction followed by the elimination, and rebuild $A \star B$ from itself with an elimination followed by an introduction.

7. ◦ Give the formula interpretation of the hypersequents $p \Rightarrow q \mid q \Rightarrow p$ and $\Rightarrow p \mid p \Rightarrow$ of the [hypersequent calculus](/3PR9PEMXJ4/). Show with a Kripke model on a total order that the second one is not derivable in HLC.

8. ◦ In the [display calculus](/1X7D5CBXB7/) $\mathrm{DK_t}$: (a) display $q$ in $p \circ q \vdash r \circ s$; (b) decide whether $s$ is an antecedent or a succedent part of $p \vdash q \circ {*}s$, and display it.

9. ◦ Run the [epsilon substitution method](/F5HTHB46SH/) on the critical formula $A(5) \to A(\varepsilon x\, A(x))$, where $A(x)$ is $2 < x$. Start from the substitution that gives every $\varepsilon$-term the value $0$. Then check the critical formula of the second kind, $A(4) \to \neg(4 < \varepsilon x\, A(x))$, under the new substitution.

10. ◦ A derivation has cuts on $p \wedge q$ and on $(p \vee q) \wedge r$ and no others. Give its cut rank. Compute $2_3(2)$, and the values of the terms $s_4$ and $s_5$ in the [lower bound for cut elimination](/B5F5HB4YK7/).

11. • In LK, let $D_1$ derive $p \Rightarrow p \vee p$ by ${\vee}$R from an axiom, and let $D_2$ derive $p \vee p \Rightarrow p$ by ${\vee}$L from two axioms. Cut $D_1$ against $D_2$. Carry out the reduction of the principal cut from the proof of the [cut-elimination theorem](/AYRZ98Y0NW/) until no cut is left.

12. • Show that if $\Gamma \Rightarrow \Delta$ has $n$ occurrences of connectives, then every backward search tree in G3cp has height at most $n$ and at most $2^n$ final sequents. Show that the bound $2^n$ is reached by $p_1 \vee q_1, \dots, p_n \vee q_n \Rightarrow$.

13. • Reduce the lambda term $(\lambda f.\, \lambda x.\, f x)(\lambda y.\, y)$ to normal form, and count the steps. Write the natural deduction derivation that the term codes, with $p$ as the only variable, and point to each detour.

14. • Derive $\Rightarrow (p \to q) \vee (q \to p)$ in HLC, naming every rule. Which rule of HLC is not in HLJ, and where is it used?

15. • In the [labeled sequent calculus](/VW8XP95XCB/) G3KB, with the rule Sym for symmetry, derive $\Rightarrow x : p \to \Box \Diamond p$. Then give a Kripke model that shows that the formula is not valid on all frames.

16. • Derive $\Rightarrow x : \Box p \to \Diamond p$ in G3KD, the calculus with the rule Ser for seriality.

17. • In focused MALL, as in the entry on [focusing](/AMMKNENT3R/), find a focused proof of $\vdash \cdot \Uparrow a \oplus b, a^{\perp}$. Show that $\vdash \cdot \Uparrow a \otimes b, a^{\perp}$ has no focused proof, and conclude from Andreoli's theorem that $\vdash a \otimes b, a^{\perp}$ is not provable in MALL.

18. • Show that the rules ${\vee}$I$_1$, ${\vee}$I$_2$ and ${\vee}$E of natural deduction are in harmony: give the reduction of each introduction followed by ${\vee}$E, and an expansion of a derivation of $A \vee B$.

19. • Under the normalization criterion for the [identity of proofs](/G7B4XWMS7Q/), with both detour reductions and expansions, how many distinct proofs does $p \to (p \to p)$ have? Give a normal, fully expanded derivation for each.

20. • In SKS, as in [deep inference](/4ZW0SHW2RG/), derive $a \vee b$ from $(a \vee b) \vee (a \vee b)$, and derive $(a \vee b) \wedge c$ from $((a \vee b) \wedge c) \vee ((a \vee b) \wedge c)$. Name each rule and each use of the equations.

21. • For the sequent $\Rightarrow \exists x\, (P(x) \to P(f x))$, with a constant $c$, show that no single instance $P(t) \to P(f t)$ is a tautology, find a tautological Herbrand disjunction of two instances, and write the [midsequent](/1FPWTGE14W/) of a cut-free derivation.

22. • Show that G3ip does not derive $(p \to \bot) \to \bot \Rightarrow p$. Use the [inversion lemma](/EXMS77F2XN/) and the soundness of G3ip for classical truth tables.

23. ★ Show that G3ip does not derive Peirce's law $\Rightarrow ((p \to q) \to p) \to p$, although G3cp does.

24. ★ Derive $\Rightarrow (p \to q) \vee (q \to r) \vee (r \to p)$ in HLC. Use the communication rule twice.

25. ★ Show that the normal, fully expanded derivations of $(p \to p) \to (p \to p)$ correspond to the terms $\lambda f.\, \lambda x.\, f^n x$ with $n \ge 0$. Conclude that this formula has infinitely many distinct proofs under the normalization criterion.

26. ★ Show by induction on $A$ that general cut, from $A \wedge \bar{A}$ to $\mathsf{f}$, is derivable in SKS from atomic cut $\mathsf{ai}{\uparrow}$, switch and the equations, for every formula $A$ built from atoms, negated atoms, units, $\wedge$ and $\vee$. Here $\bar{A}$ is the negation of $A$ by the De Morgan laws.

27. ★ Show that if G3ip derives $\Rightarrow A \vee B$, then it derives $\Rightarrow A$ or $\Rightarrow B$. Use this to show that G3ip does not derive $\Rightarrow \neg p \vee \neg \neg p$, although HLC does.
