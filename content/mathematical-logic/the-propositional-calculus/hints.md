1. It contains $14$ brackets, twice the number of connectives. So no official formula has $9$ brackets: the number is always even.

3. $CKpqr$ is $(p \land q) \to r$ and $NCpNq$ is $\neg (p \to \neg q)$. $KCpq$ is not a formula, since $K$ has only one argument, $Cpq$. $CpqNr$ is not a formula, since $Cpq$ is already complete and $Nr$ is left over.

5. $p \lor \neg q$ is in both forms: one clause, or two terms of one literal each. $\neg \neg p$ is in neither, since $\neg \neg p$ is not a literal. $(p \lor q) \land \neg r$ is in CNF only. $p \land q$ is in both: one term, or two unit clauses.

7. There are $2^{2^3} = 256$ functions. Fixing the values at $(0,0,0)$ and $(1,1,1)$ leaves $6$ free inputs, so $2^6 = 64$ functions preserve both constants.

8. Both $p$ and $p \lor \neg p$ are satisfiable. The formula $\neg p$ is satisfiable, but $\neg (p \lor \neg p)$ is not. So replacing a formula by an equisatisfiable one inside a larger formula can change satisfiability.

10. De Morgan's laws give the CNF $(\neg p \lor \neg q) \land (p \lor \neg r)$. Its value is $\neg q$ when $p$ is true and $\neg r$ when $p$ is false, which is the DNF $(p \land \neg q) \lor (\neg p \land \neg r)$: "if $p$ then not $q$, else not $r$".

11. The marking goes $p$, then $q$ and $r$, then $s$, then $t$, and the goal clause $\neg t \lor \neg q$ has both its variables marked, so the set is unsatisfiable. Without $\neg p \lor r$ only $p$ and $q$ are marked; the goal clause is satisfied, and the least model makes $p$ and $q$ true and all other variables false.

13. Take $(p_1 \lor p_2 \lor x) \land (\neg x \lor p_3 \lor y) \land (\neg y \lor p_4 \lor p_5)$. If $p_1$ or $p_2$ is true, make $x$ and $y$ false; if $p_3$ is true, make $x$ true and $y$ false; if $p_4$ or $p_5$ is true, make both true. If all $p_i$ are false, the clauses force $x$, then $y$, and the last clause fails.

16. Under this reading every instance of A1 and A2 takes the value $1$, and modus ponens keeps the value $1$. The instance $(\neg p \to \neg p) \to ((\neg p \to p) \to p)$ of A3 becomes $(0 \to 0) \to ((0 \to p) \to p)$, which is $p$, and it takes the value $0$ when $p$ is $0$.

19. Suppose a valuation $v$ makes $\varphi$ true and a valuation $w$ makes $\psi$ false. Since the variables are disjoint, one valuation can agree with $v$ on the variables of $\varphi$ and with $w$ on those of $\psi$, and it makes $\varphi$ true and $\psi$ false.

21. Assume $\neg \neg \varphi$. From A1 and modus ponens get $\neg \varphi \to \neg \neg \varphi$. The instance $(\neg \varphi \to \neg \neg \varphi) \to ((\neg \varphi \to \neg \varphi) \to \varphi)$ of A3 then gives $(\neg \varphi \to \neg \varphi) \to \varphi$, and $\vdash \neg \varphi \to \neg \varphi$ gives $\varphi$. Discharge the assumption with the deduction theorem.

22. Use induction on formulas, with $\neg x = 1 \oplus x$ and $x \leftrightarrow y = 1 \oplus x \oplus y$. A function of this form in two variables is true at $0$, $2$ or $4$ of the four inputs, while $p \land q$ is true at exactly one.

23. A complete connective $f$ must have $f(0,0) = 1$, or every formula built from it preserves $0$, and likewise $f(1,1) = 0$. That leaves four connectives: NAND, NOR, $\neg p$ and $\neg q$. The last two give only functions that depend on one variable, so they cannot express $p \land q$.

25. If $\varphi$ had the same models as $\Gamma$, then $\Gamma \models \varphi$, and by compactness $\gamma_1, \ldots, \gamma_n \models \varphi$ for some $n$. Since the $\gamma_i$ get stronger, this says $\gamma_n \models \varphi$, and $\varphi \models \gamma_{n+1}$, which contradicts $\gamma_n \not\models \gamma_{n+1}$.
