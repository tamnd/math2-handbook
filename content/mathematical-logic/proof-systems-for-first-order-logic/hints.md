1. (a) Group 3, distribution. (b) Not an axiom: $y$ is not substitutable for $x$ in $\forall y\, R(x,y)$, because the free $x$ lies in the scope of $\forall y$. (c) Group 4, since $x$ is not free in $P(c)$. (d) A generalization of a group 6 axiom, with $\alpha = P(x)$ and $\alpha' = P(y)$, so it is an axiom. (e) Not an axiom: $x$ is free in $P(x)$.

3. The theorem needs $x$ not free in any member of $\Gamma$, and $x$ is free in $P(x)$. Take the domain $\{0, 1\}$, let $P$ hold of $0$ only, and let $s(x) = 0$.

5. Step (2) is wrong: its eigenvariable $y$ is free in the open assumption $P(y)$. In the domain $\{0, 1\}$ with $P$ true of $0$ only, $y = 0$ makes $P(y) \to \forall x\, P(x)$ false.

7. (a) No: condition (5) fails, since no instance $P(t)$ is in the set. (b) Yes. (c) No: condition (3) fails, since neither $P(c)$ nor $Q(c)$ is in the set. (d) Yes: the only closed term is $c$, the $\gamma$ instance and the $\beta$ choice $Q(c)$ are present, and no atomic sentence occurs with its negation.

8. (a) $\{x \mapsto a, y \mapsto g(a)\}$. (b) $\{x \mapsto g(z), y \mapsto g(z)\}$; both atoms become $P(g(z), f(g(z)))$. (c) None: $x = y$ gives $x \mapsto y$, and then $y = f(y)$ fails the occurs check.

10. From the hypothesis $\forall x\, \forall y\, R(x,y)$, two instances of group 2 (with $t = x$, then $t = y$) and modus ponens give $R(x,y)$. Generalize on $x$ and then on $y$; neither is free in the hypothesis. The deduction theorem then moves the hypothesis across the arrow.

12. Assume $[\forall x\, P(x)]^1$ and $[\neg P(y)]^2$. Then ${\forall}\mathrm{E}$ gives $P(y)$ and ${\neg}\mathrm{E}$ gives $\bot$. The ${\exists}\mathrm{E}$ step discharges 2 and concludes $\bot$; $y$ is not free in $\exists x\, \neg P(x)$, in $\bot$ or in $\forall x\, P(x)$. Finally ${\neg}\mathrm{I}$ discharges 1.

14. Open a box with a new constant $a$ and the line $\exists y\, R(a,y)$; inside it open a box with a new constant $b$ and the line $R(a,b)$. Two uses of ${\exists}\mathrm{I}$ give $\exists x\, R(x,b)$ and $\exists y\, \exists x\, R(x,y)$, which leaves both boxes. The inner constant must be new to its box, and $a$ already occurs there; using $a$ twice would assume $R(a,a)$, a stronger claim than $\exists y\, R(a,y)$ gives.

17. The open branch contains $P(a)$, $\neg Q(a)$ (from the $\delta$ step on $\neg \forall x\, (P(x) \to Q(x))$) and $\neg P(b)$ (from the $\delta$ step on $\neg \forall x\, P(x)$); the other side of the $\beta$ split, with $\forall x\, Q(x)$, closes against $\neg Q(a)$. The structure has domain $\{a, b\}$, $P = \{a\}$ and $Q = \emptyset$.

18. The clauses are $\{\neg R(x_1,y_1), R(y_1,x_1)\}$, $\{\neg R(x_2,y_2), \neg R(y_2,z_2), R(x_2,z_2)\}$, $\{R(x_3, f(x_3))\}$ and, from the negated goal, $\{\neg R(c,c)\}$. Resolve the goal with transitivity to get $\{\neg R(c,y_2), \neg R(y_2,c)\}$, then use seriality with $x_3 \mapsto c$ to get $\{\neg R(f(c), c)\}$. Symmetry and seriality give $\{R(f(x), x)\}$, which refutes it.

21. The map $q \mapsto q + (b - a)$ is an automorphism of $(\Q, <)$ that sends $a$ to $b$, and automorphisms preserve the truth of every formula. So $a \neq b$, yet no first-order formula in one variable separates them.

22. Let $\mathcal{M}, s$ satisfy $\Gamma$ and $\exists x\, \varphi$, and pick $d$ with $\mathcal{M} \models \varphi[s(d/x)]$. Put $s' = s(d/y)$. Since $y$ is not free in $\Gamma$, $\mathcal{M}, s'$ satisfies $\Gamma$; by the substitution lemma and the conditions on $y$, it satisfies $\varphi[y/x]$. So $\mathcal{M} \models \chi[s']$, and since $y$ is not free in $\chi$, also $\mathcal{M} \models \chi[s]$.

23. $\Sigma$ has a model, $(\N, <)$, so by soundness no tableau for it closes. Every model of $\Sigma$ is infinite: following $R$-successors in a finite model must repeat an element, and transitivity then gives $R(x,x)$. If a finished open branch were finite, its sentences would form a Hintikka set for the finitely many parameters on it, and Hintikka's lemma would give a finite model of $\Sigma$.

24. In a cut-free LJ derivation of $\Rightarrow P \vee \neg P$, the last step is ${\vee}$R from $\Rightarrow P$ or from $\Rightarrow \neg P$, or weakening from the empty sequent; contraction on the right is impossible with one formula there. Each of the sequents $\Rightarrow P$, $P \Rightarrow$ (the only premise of $\Rightarrow \neg P$ by ${\neg}$R) and the empty sequent is false in some valuation, so LK, which is sound, does not derive them.

25. Let the domain of $\mathcal{M}/E$ be the set of classes, and interpret each symbol on representatives; the congruence condition makes this well defined, and $E$ becomes identity. Prove the claim by induction on $\varphi$. The atomic case is the definition; the quantifier case uses that every class is the class of some element.

26. Use the $\gamma$ sentence twice on the same branch, with $t = c$ and then $t = f(c)$, and split each instance by $\beta$. With only one instance $P(t) \to P(f(t))$, the branch through $\neg P(t)$ closes only if $t = c$, and the branch through $P(f(t))$ closes only if $t = f(c)$; both cannot hold.
