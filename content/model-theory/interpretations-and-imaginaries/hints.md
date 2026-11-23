1. (a) $(-3, -10)$. (b) $\set{2, -2}$, the roots of $t^2 - 4$. (c) The roots of $t^2 - t + 1$, that is $\set{(1 + i\sqrt 3)/2, (1 - i\sqrt 3)/2}$. No real pair has this code, since a real pair has $(a + b)^2 - 4ab = (a - b)^2 \ge 0$, while $1 - 4 < 0$. (d) $(4, 6, 3, 14, 8)$ and $(1, 1, 0, 1, 0)$.

4. (a) An equivalence relation; the class $\set{a, -a}$ is coded by $a^2$. (b) An equivalence relation with three classes, coded by $-1$, $0$ and $1$, which are $\emptyset$-definable. (c) Not transitive: $0$ is related to $0.6$, and $0.6$ to $1.2$, but $0$ is not related to $1.2$. (d) The class of $0$ would be the definable set $\Q$, but every definable subset of $\R$ is a finite union of points and intervals.

6. (a) True, since $\operatorname{dcl} \subseteq \operatorname{acl}$. (b) False: an unordered pair has no real code. (c) True, by Poizat's theorem. (d) True. (e) True.

7. (a), (c) and (e) follow; (e) because $N$ is the image of a subset of $M^n$. (b) fails for the reduct $(\Z, +)$ of $(\Z, +, \cdot)$, by Presburger's theorem. (d) fails for the reduct $(\Q, =)$ of $(\Q, <)$.

9. An $n$-tuple of $N$ is $(f \bar a_1, \dots, f \bar a_n)$ with $\bar a_i \in M^d$, and automorphisms of $M$ in the same orbit on $M^{dn}$ give tuples of $N$ in the same orbit of the induced group. So $\operatorname{Aut}(N)$ has finitely many orbits on $N^n$, and $N$ is countable.

13. (a) Only $(0, 0, -1)$ itself: a circle of positive radius determines its centre $(-u/2, -v/2)$ and its squared radius $(u^2 + v^2)/4 - w$. (b) When $u^2 + v^2 \ge 4w$ the class is a single tuple, since a point also determines $(u, v, w)$; all tuples with $u^2 + v^2 < 4w$ define the empty set and form one class. (c) $g(u, v, w) = (u, v, w)$ if $u^2 + v^2 \ge 4w$, and $g(u, v, w) = (0, 0, 1)$ otherwise.

14. In the monster model, the automorphisms fixing $e$ include all permutations of each class, so no real element is algebraic over $e$. A weak code would then be the empty tuple, which needs $e \in \operatorname{dcl}(\emptyset)$, but the automorphism that swaps the two classes moves $e$.

17. Each $E_n$ has exactly $n!$ classes, so a class of $E$ is determined by a sequence of classes, one for each $n$, and there are at most $\prod_n n! = 2^{\aleph_0}$ such sequences. If one formula $\psi$ defined $E$, compactness would give $E_m \subseteq E \subseteq E_{m+1}$ for some $m$. Take $a$ not divisible by $m + 1$: then $m! \, a$ is $E_m$-related to $0$ but not $E_{m+1}$-related to it.

18. Let $E(\bar x, \bar y, \bar a)$ be an equivalence relation over $\bar a \in A$. Form the $\emptyset$-definable relation $F$ on pairs $(\bar x \bar z, \bar y \bar w)$ that says $\bar z = \bar w$ and $E(\bar x, \bar y, \bar z)$ when $E(-, -, \bar z)$ is an equivalence relation, and $\bar x = \bar y$ otherwise. The class of $\bar c \bar a$ under $F$ is interdefinable over $A$ with the class of $\bar c$ under $E(-, -, \bar a)$, and $T$ gives it a real code.

19. A formula $\exists z \, \theta(\bar x, z)$ with $z$ of sort $M^k/E$ is equivalent in $M^{\mathrm{eq}}$ to $\exists \bar y \, \theta(\bar x, \pi_E(\bar y))$, and an equation $\pi_E(\bar y) = \pi_E(\bar y')$ is equivalent to $E(\bar y, \bar y')$. Prove by induction that every formula $\theta(\bar x, \pi_{E_1}(\bar y_1), \dots)$ with home-sort variables is equivalent to an $L$-formula in $\bar x, \bar y_1, \dots$.

20. For each tuple $\bar a$, elimination gives a formula $\theta(\bar x, \bar y)$ such that, for $\bar x$ in the class of $\bar a$, $\theta(\bar x, -)$ picks out one real tuple that defines the class. By compactness finitely many formulas $\theta_1, \dots, \theta_k$ cover all tuples. Pad the tuples to one length and add a tag made of the two definable elements to record the least $i$ that applies; the result is one $\emptyset$-definable map.

21. The coefficients are symmetric polynomial expressions in the points, so any automorphism or definable bijection that fixes $S$ setwise fixes them. Conversely, $\bar a \in S$ exactly when substituting $Y = -(a_1 X_1 + \dots + a_n X_n)$ into the polynomial gives $0$, and this is a finite set of polynomial equations in $\bar a$ and the coefficients.

22. For $\sigma \in \operatorname{Aut}(M)$, the composite coordinate map $h$ is $\emptyset$-definable and so commutes with $\sigma$; since $h$ is onto $M$, the automorphism of $M$ induced by the induced automorphism of $N$ is $\sigma$ again. For continuity, the stabilizer of finitely many elements $f(\bar a_1), \dots, f(\bar a_k)$ of $N$ contains the image of the stabilizer of $\bar a_1, \dots, \bar a_k$ in $\operatorname{Aut}(M)$.
