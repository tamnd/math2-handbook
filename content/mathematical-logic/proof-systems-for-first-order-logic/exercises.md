1. ◦ Which of these formulas are logical axioms of Enderton's [Hilbert-style predicate calculus](/N95HV0VWSM/), and of which group? (a) $\forall x\, (P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))$. (b) $\forall x\, \forall y\, R(x,y) \to \forall y\, R(y,y)$. (c) $P(c) \to \forall x\, P(c)$. (d) $\forall z\, (x = y \to (P(x) \to P(y)))$. (e) $P(x) \to \forall x\, P(x)$.

2. ◦ Is the term $f(y)$ [substitutable](/NCDZ969V7X/) for $x$ in each formula? (a) $\forall y\, R(x,y)$. (b) $\forall z\, R(x,z) \wedge \forall y\, Q(y)$. (c) $\forall x\, R(x,y)$. Where it is, write the result of the substitution.

3. ◦ Clearly $\{P(x)\} \vdash P(x)$. Which hypothesis of the [generalization theorem](/VKSK35Y52Z/) fails if you try to conclude $\{P(x)\} \vdash \forall x\, P(x)$ in Enderton's calculus? Give a structure and an assignment that satisfy $P(x)$ but not $\forall x\, P(x)$.

4. ◦ In Mendelson's calculus $\mathsf{H}_G$, the set $\{\forall x\, (P(x) \to Q(x)), \forall x\, P(x)\}$ derives $\forall x\, Q(x)$, with one use of the generalization rule on $x$. Does the restricted [deduction theorem](/8M9ZFDR4DH/) of $\mathsf{H}_G$ allow you to conclude $\{\forall x\, (P(x) \to Q(x))\} \vdash \forall x\, P(x) \to \forall x\, Q(x)$? Say which condition you checked.

5. ◦ Find the wrong step in this tree, which claims to derive $\forall y\, (P(y) \to \forall x\, P(x))$ in [natural deduction](/6KT3BJZ7D1/): (1) assume $[P(y)]^1$; (2) $\forall x\, P(x)$ by ${\forall}\mathrm{I}$ from (1); (3) $P(y) \to \forall x\, P(x)$ by ${\to}\mathrm{I}$, discharging 1; (4) $\forall y\, (P(y) \to \forall x\, P(x))$ by ${\forall}\mathrm{I}$. Give a structure in which the conclusion is false.

6. ◦ For each sentence, give its type ($\alpha$, $\beta$, $\gamma$ or $\delta$) in the [tableau](/WGWBBVE8GX/) rules and the sentences the rule adds: (a) $\neg(P(c) \vee Q(c))$; (b) $P(c) \to Q(c)$; (c) $\neg \exists x\, P(x)$; (d) $\neg \forall x\, Q(x)$; (e) $\neg(P(c) \to Q(c))$.

7. ◦ Let $L$ have one constant $c$, unary relation symbols $P, Q$ and no function symbols. Which of these sets are [Hintikka sets](/RJNDEG07R1/) for $L$? For each one that is not, name the condition that fails. (a) $\{\exists x\, P(x)\}$. (b) $\{\exists x\, P(x), P(c)\}$. (c) $\{\forall x\, (P(x) \vee Q(x)), P(c) \vee Q(c), \neg P(c)\}$. (d) $\{\forall x\, (P(x) \vee Q(x)), P(c) \vee Q(c), Q(c), \neg P(c)\}$.

8. ◦ Find a most general [unifier](/RJJ9D0WF53/) of each pair, or say why none exists. (a) $R(x, g(x))$ and $R(a, y)$. (b) $P(x, f(y))$ and $P(g(z), f(x))$. (c) $Q(x, x)$ and $Q(y, f(y))$.

9. ◦ Put each sentence into [clause](/T3SXVH3ZZC/) form, using a new function or constant symbol for each existential quantifier. (a) $\forall x\, \exists y\, \forall z\, (R(x,y) \vee \neg R(y,z))$. (b) $\neg \forall x\, \exists y\, R(x,y)$.

10. • Show that $\vdash \forall x\, \forall y\, R(x,y) \to \forall y\, \forall x\, R(x,y)$ in Enderton's calculus. Use axiom group 2, the generalization theorem and the deduction theorem, and check the condition of each.

11. • Let $y$ be a variable that does not occur in $\varphi$. Show that $\vdash \forall x\, \varphi \to \forall y\, \varphi[y/x]$ in Enderton's calculus. Which step fails if $y$ occurs free in $\varphi$?

12. • Derive $\exists x\, \neg P(x) \vdash \neg \forall x\, P(x)$ in natural deduction without RAA. Check the eigenvariable condition at the ${\exists}\mathrm{E}$ step.

13. • Derive $\forall x\, (P(x) \to Q(x)), \exists x\, P(x) \vdash \exists x\, Q(x)$ in natural deduction. Then explain why the same steps do not derive $\forall x\, (P(x) \to Q(x)), \exists x\, P(x) \vdash \forall x\, Q(x)$.

14. • Give a [Fitch-style](/2B6XC7XJA8/) proof of $\exists x\, \exists y\, R(x,y) \vdash \exists y\, \exists x\, R(x,y)$ with boxed constants. Explain why the two boxes must use two different constants.

15. • Give a cut-free derivation in the [sequent calculus](/W72CA3R9MP/) LK of $\neg \exists x\, P(x) \Rightarrow \forall x\, \neg P(x)$. Name the rule at each step and check the eigenvariable condition.

16. • Give a closed tableau for the negation of $\exists x\, (P(x) \vee Q(x)) \to (\exists x\, P(x) \vee \exists x\, Q(x))$. Why is it best to apply the $\delta$ rule before the $\gamma$ rules?

17. • Build a tableau for the negation of $(\forall x\, P(x) \to \forall x\, Q(x)) \to \forall x\, (P(x) \to Q(x))$. Show that it has a finished open branch, and read off a structure in which the sentence is false.

18. • Use [first-order resolution](/DEB3CF4Z2D/) to show that a relation that is symmetric, transitive and serial ($\forall x\, \exists y\, R(x,y)$) is reflexive. Write the clauses, each resolution step and each unifier.

19. • The clause set $\{\{P(a)\}\}$ implies the clause $\{P(a), Q(a)\}$. Show that resolution cannot derive $\{P(a), Q(a)\}$ from $\{\{P(a)\}\}$. How does a resolution prover establish this consequence instead?

20. • Using only the [rules for equality](/Y90Z13AXY8/) ${=}\mathrm{I}$ and ${=}\mathrm{E}$ of natural deduction, derive $a = b \vdash f(a) = f(b)$ and $a = b \vdash g(a,a) = g(b,b)$. How many uses of ${=}\mathrm{E}$ does the second need?

21. • Show that in the structure $(\Q, <)$, any two rationals $a$ and $b$ satisfy the same first-order formulas $\varphi(x)$ in one free variable. Explain why this shows that no set of such formulas can play the role of the [identity of indiscernibles](/SCGE8NF69Q/) in first-order logic.

22. ★ Prove that the rule ${\exists}\mathrm{E}$ is sound. Suppose that every model of $\Gamma \cup \{\varphi[y/x]\}$ satisfies $\chi$ (under every assignment), where $y$ is not free in $\exists x\, \varphi$, in $\chi$ or in any member of $\Gamma$, and $y$ is substitutable for $x$ in $\varphi$. Show that $\Gamma \cup \{\exists x\, \varphi\} \models \chi$.

23. ★ Let $\Sigma$ consist of $\forall x\, \exists y\, R(x,y)$, $\forall x\, \neg R(x,x)$ and $\forall x\, \forall y\, \forall z\, ((R(x,y) \wedge R(y,z)) \to R(x,z))$. Show that every finished tableau for $\Sigma$ has an infinite open branch.

24. ★ Show that the sequent $\Rightarrow P \vee \neg P$, with $P$ a propositional variable, has no derivation in LJ. You may use that LJ has cut elimination and that every LJ derivation is an LK derivation.

25. ★ Let $L$ be a language without the symbol $=$, with a binary relation symbol $E$. Let $\mathcal{M}$ be an $L$-structure in which $E^{\mathcal{M}}$ is a [congruence](/DCSXXT4SER/) for every symbol of $L$. Define the quotient $\mathcal{M}/E$ and prove that $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{M}/E \models \varphi[\bar{s}]$ for every formula $\varphi$ of $L$, where $\bar{s}(x)$ is the class of $s(x)$.

26. ★ Give a closed tableau for the negation of $\forall x\, (P(x) \to P(f(x))) \to (P(c) \to P(f(f(c))))$. Then show that no tableau for it closes if the $\gamma$ rule may be applied only once to each $\gamma$ sentence on a branch.
