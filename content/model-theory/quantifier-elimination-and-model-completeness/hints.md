1. $b \ne 0 \lor c \ne 0$. The product of the two roots is $c$, so if $c \ne 0$ both roots are nonzero. If $c = 0$ the roots are $0$ and $-b$.

3. Without constants the only quantifier-free sentences are $\top$ and $\bot$, so each sentence is equivalent modulo $T$ to one of them. (a) Yes. (b) No: it is not complete, since $\exists x \exists y \exists z \, (x \ne y \land y \ne z \land x \ne z)$ is not decided. (c) Yes: the only model is a five-element set, and two tuples with the same pattern of equalities are moved onto each other by a permutation, so every definable set of tuples is a union of equality patterns.

5. Yes: both are real closed fields, and real closed fields are model complete in the ring signature. No: $\Q$ is not a model, and $\exists y \, (y \cdot y = 1 + 1)$ holds in $\R$ and fails in $\Q$.

7. (a) Yes, it is universal. (b) Yes, it is axiomatized by $\forall\exists$ sentences. (c) No: the orders $\set{-n, -n + 1, \ldots}$ of integers form a chain whose union $\Z$ has no least element. (d) Yes, with the axiom $\forall x \, \exists y \, E(x, y)$.

8. Seven cells: $(-\infty, -1)$, $\set{-1}$, $(-1, 0)$, $\set{0}$, $(0, 1)$, $\set{1}$, $(1, \infty)$, on which $p$ is $-$, $0$, $+$, $0$, $-$, $0$, $+$.

10. $c < 0 \lor (b < 0 \land b^2 - 4c \ge 0)$. If $c < 0$ the roots are real with product $c$, so one is positive. If $c \ge 0$ the real roots have the same sign or one is $0$, and a positive root needs a real root and sum $-b > 0$.

12. Each $D_n(t)$ is the existential formula $\exists y \, (t = n y)$, and $\neg D_n(t)$ is equivalent to the disjunction of $D_n(t - k)$ for $0 < k < n$. So every formula becomes existential. A quantifier-free formula in $x$ alone is a Boolean combination of conditions $n x + k = 0$ and $n x + k > 0$ with integers $n, k$. Each condition has a constant truth value for all large $x$, so the set defined contains all large integers or none of them; the even numbers do neither.

13. For models $M, N$ the embeddings of $M_0$ are elementary, so $M \equiv M_0 \equiv N$. For $\mathrm{ACF}_0$ take the algebraic closure of $\Q$, and for real closed fields take $\R_{\mathrm{alg}}$, the real closure of $\Q$.

18. Over $x < 0$ there is no root and one cell; over $x = 0$ the root $y = 0$ gives three cells; over $x > 0$ the roots $\pm \sqrt{x}$ give five cells. That makes nine cells: one of dimension $0$ (the origin), four of dimension $1$ (the two open half-lines of the $y$-axis and the two branches $y = \pm\sqrt{x}$ over $x > 0$), and four of dimension $2$.

19. For the extension test, $A$ is a subgroup and its divisible hull sits in both models. A new element $b$ is determined, over $A$, by the cut it makes in the divisible hull, and an $\omega$-saturated model realizes every such cut over finitely many parameters. For the definable sets, an atomic formula in $x$ says $n x + t > 0$ or $n x + t = 0$ for a term $t$ in the parameters.

20. A finitely generated Boolean algebra is finite. For each atom $a$ of $A$, the element $b \land a$ is $0$, $a$, or strictly between; in an atomless $N$ the image of $a$ has an element strictly between $0$ and it. Take the join of the chosen pieces.

21. Embed $B$ and $C$ into models $B^*$ and $C^*$ of $T^*$. Both are models of $T^* \cup \mathrm{Diag}(A)$, which is complete, so they are elementarily equivalent over $A$, and the [elementary amalgamation theorem](/P2VMSM4H4Y/) gives a common elementary extension; embed it in a model of $T$. For the second part, real closed fields in the ring signature: $\Q(t)$ lies in $\Q(\sqrt t)$ and in $\Q(\sqrt{-t})$, both formally real, and no formally real domain contains both, since $-1$ would be a square of a fraction.

22. A proper ideal lies in a maximal ideal $\mathfrak m$, and $L = K[\bar x]/\mathfrak m$ is a field extension of $K$ in which the classes of the $x_i$ are a common zero. Embed $\bar K$ over $K$ into an algebraically closed field $F \supseteq L$. The existential formula $\exists \bar x \, \bigwedge_j f_j(\bar x) = 0$, with parameters in $K$, holds in $F$, so it holds in $\bar K$ by model completeness.
