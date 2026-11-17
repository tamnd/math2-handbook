1. ◦ In the [language of arithmetic](/D8SD54M5PN/), write formulas for "$x \le y$", "$x$ is a perfect square" and "$x$ is the remainder of $y$ on division by $3$". Use only bounded quantifiers.

2. ◦ Place each formula in the lowest class $\Delta_0$, $\Sigma_n$ or $\Pi_n$ that contains it as written: (a) $\forall x < y\, \exists z < y\, (x + z = y)$; (b) $\exists x\, \forall y\, (x \cdot y = x)$; (c) $\forall x\, \exists y\, (x < y \land \forall z < y\, (z \cdot z \ne y))$; (d) $\exists x\, (x \cdot x = y)$. See [the classes $\Delta_0$, $\Sigma_n$, $\Pi_n$](/GE43CSZTS9/).

3. ◦ Which of these sentences does [Robinson arithmetic](/3K1AKGXF8A/) prove? (a) $\overline 2 \cdot \overline 3 = \overline 6$; (b) $\neg (\overline 2 + \overline 2 = \overline 5)$; (c) $\forall x\, (x + 0 = x)$; (d) $\forall x\, (0 + x = x)$; (e) $\forall x\, (x < \overline 2 \to x = 0 \lor x = \overline 1)$.

4. ◦ Compute $\beta(1521, 6, i)$ for $i = 0, 1, 2$, where $\beta(c, d, i) = c \bmod (1 + (i+1)d)$ is [Gödel's $\beta$-function](/BM6P0C2AC2/). Explain why no $c$ makes $\beta(c, 1, 0) = 7$.

5. ◦ Write out the instance of the induction schema of [Peano arithmetic](/HACXBCM7SS/) for the formula $\varphi(x) := x + \overline 1 = \overline 1 + x$.

6. ◦ Is [true arithmetic](/DX0KPMH4QZ/) finitely axiomatizable? Computably axiomatizable? Decidable? Does it have models that are not isomorphic to $\N$?

7. ◦ Without writing a proof, say why $\mathsf{Q} \vdash \exists x\, (x \cdot x = \overline 9)$ and why $\mathsf{Q} \vdash \neg \exists x < \overline 5\, (x + x = \overline 7)$. Which theorem do you use?

8. ◦ True or false? (a) Every model of $\mathsf{PA}$ is a model of $\mathsf{Q}$. (b) Every model of $\mathsf{Q}$ is a model of $\mathsf{PA}$. (c) $\N$ is a model of every [fragment](/T70PYM1F36/) $\mathrm{I}\Sigma_n$. (d) $\mathsf{PA}$ is the union of the theories $\mathrm{I}\Sigma_n$.

9. • Show that $\mathsf{Q}$ does not prove $\forall x\, (0 \cdot x = 0)$: add one element $a$ to $\N$ with $Sa = a$ and define the operations on $a$ so that every axiom holds. Then prove $\forall x\, (0 \cdot x = 0)$ in $\mathsf{PA}$.

10. • Show that a relation on $\N$ defined by a $\Sigma_1$ formula is computably enumerable. Assume that $\Delta_0$ formulas define decidable relations.

11. • Use the model of exercise 9 to give a consistent extension of $\mathsf{Q}$ that proves a false $\Sigma_1$ sentence. Why does this not contradict [$\Sigma_1$-completeness](/69234Z1V00/)?

12. • Write "there are infinitely many twin primes" and "there are only finitely many twin primes" as sentences of the language of arithmetic, and place each in the lowest class $\Sigma_n$ or $\Pi_n$ it can be written in with a $\Delta_0$ formula for primality.

13. • Let $T$ be a consistent, computably axiomatized extension of $\mathsf{Q}$, and let the formula $\varphi(x)$ [represent](/BJF29XET83/) a set $A$ in $T$. Show that $A$ is computable.

14. • Use the $\beta$-function to write a $\Sigma_1$ formula $\varphi(n, y)$ that defines the graph of $n \mapsto n!$ in $\N$.

15. • [Parikh's theorem](/2JD80TE553/) says that if $\mathrm{I}\Delta_0 \vdash \forall x\, \exists y\, \theta(x, y)$ with $\theta$ in $\Delta_0$, then some polynomial $p$ has $\N \models \forall x\, \exists y \le p(x)\, \theta(x, y)$. Assume that the graph of $x \mapsto x^x$ is defined by a $\Delta_0$ formula. Show that $\mathrm{I}\Delta_0$ does not prove that this function is total.

16. • Let $T_0 \subsetneq T_1 \subsetneq T_2 \subsetneq \cdots$ be theories, each closed under consequence, and let $T = \bigcup_n T_n$. Show that $T$ is not finitely axiomatizable. Which known fact about [Peano arithmetic](/M5WNB181T7/) follows?

17. • Let $M$ be a non-standard model of true arithmetic. Show that $M$ has an element $x \ne 0$ that is divisible by every standard prime.

18. • Show that $\mathrm{I}\Sigma_1$ proves that $n \mapsto n!$ is total, using your formula from exercise 14.

19. • Show that a non-standard model of $\mathsf{PA}$ has no least non-standard element.

20. ★ Let $d = s!$ with $s \ge n$. Show that the numbers $1 + (i+1)d$ for $i = 0, \dots, n-1$ are pairwise coprime. Conclude that every sequence $a_0, \dots, a_{n-1}$ with all $a_i \le s$ is $\beta(c, d, i)$ for some $c$.

21. ★ Show that $\mathsf{PA}$ proves the least number principle $\exists x\, \varphi(x) \to \exists x\, (\varphi(x) \land \forall y < x\, \neg \varphi(y))$ for every formula $\varphi$.

22. ★ Use the fact that the halting set is defined by a $\Sigma_1$ formula to show that true arithmetic is not computably enumerable.

23. ★ Let $M$ be a non-standard model of $\mathsf{PA}$. Show that no formula, even with parameters from $M$, defines the set of standard elements of $M$.

24. ★ Prove $\forall x\, \forall y\, (x \cdot y = y \cdot x)$ in $\mathsf{PA}$. State each lemma you need, and the formula on which you use induction for each.
