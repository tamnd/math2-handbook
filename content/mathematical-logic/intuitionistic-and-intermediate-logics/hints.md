1. $r$ forces only $\neg\neg p \to p$. It fails to force $p \vee \neg p$ and $\neg p \vee \neg\neg p$, since $b$ forces $\neg p$ and $a$ forces $p$; $p \to q$ fails at $a$ and $q \to p$ at $b$; and $\neg\neg(p \vee q)$ holds at $r$ while neither $\neg\neg p$ nor $\neg\neg q$ does.

2. $\neg a = 0$, $\neg\neg a = 1$, $a \to b = 1$, $b \to a = a$ and $a \vee \neg a = a$. So $\neg\neg p \to p$ is not valid, as $p = a$ gives $1 \to a = a$. The formula $(p \to q) \vee (q \to p)$ is valid, as in every chain.

3. For $(0, 1)$: $\neg p = (-\infty, 0) \cup (1, \infty)$, $\neg\neg p = (0, 1)$ and $p \vee \neg p = \R \setminus \set{0, 1}$. Then $p \to q = (-\infty, 0) \cup (1, \infty)$, $q \to p = (-\infty, 1) \cup (2, \infty)$, and their union is $\R \setminus \set{1}$, so prelinearity fails at $1$.

4. (a), (b) and (c) are provable, since the formulas under the double negation are classical tautologies. (d) is not, since $p \to q$ is not a tautology. The theorem says nothing about predicate formulas with $\forall$, and in fact $\mathsf{IQC}$ does not prove $\neg\neg\forall x\,(Px \vee \neg Px)$.

5. $D_2 = (p_0 \leftrightarrow p_1) \vee (p_0 \leftrightarrow p_2) \vee (p_1 \leftrightarrow p_2)$. On the chain $u \le v$, give $p_0$, $p_1$ and $p_2$ the three up-sets $\emptyset$, $\set{v}$ and $\set{u, v}$. In the two-element algebra two of the three values coincide, and then their biconditional is $1$.

6. For the first rule substitute $\bot$ for $p$ and $\top$ for $q$: $\bot \vee \top$ is a theorem and $\bot$ is not. For the second substitute $\top$ for $p$ and $\bot$ for $q$.

7. $\mathsf{LC}$: $(p \to q) \vee (q \to p)$. $\mathsf{KC}$: $\neg p \vee \neg\neg p$. $\mathsf{CPC}$: $p \vee \neg p$. In each case neither disjunct is a classical tautology, so the logic, which lies inside $\mathsf{CPC}$, does not prove it.

8. $F_3 \mapsto \set{0, 1}$, $F_7 \mapsto \set{0, 1, 2, 3}$ and $F_8 \mapsto \set{0, 1, 2, 4}$. $F_6 \mapsto \set{0, 1, 3}$, so $F_6$ implies $F_7$. $F_5 \mapsto \set{0, 1, 2}$, which is not contained in $\set{0, 1, 3}$, so $F_5$ does not imply $F_6$.

9. Use $T(\neg\varphi) = \square(T(\varphi) \to \bot) = \square\neg T(\varphi)$. The translations are $\square\neg\square p \vee \square\neg\square\neg\square p$ and $\square(\square p \to \square q) \vee \square(\square q \to \square p)$.

10. $2^n - 1$ worlds, the non-empty subsets of $\set{1, \ldots, n}$; $n$ maximal worlds, the singletons; a longest chain has $n$ worlds. $M_3$ has a root $\set{1, 2, 3}$, three worlds with two elements and three maximal worlds.

12. Peirce's law fails at $u$ in the chain $u \le v$ with $p$ true at $v$ only and $q$ nowhere. The De Morgan law fails at the root of the fork with $p$ true at one maximal world and $q$ at the other.

13. With $\bot$ as an atom $f$, both laws are still theorems of the positive logic. For the failures take one world where $f$ and $p$ are true and $q$ is false.

14. Substitute $\neg p$ for $q$ in $(p \to q) \vee (q \to p)$; then $p \to \neg p$ gives $\neg p$ and $\neg p \to p$ gives $\neg\neg p$. The frame is the diamond: a root, two incomparable middle worlds and a top above both.

15. If $p \to q$ fails at $w$ through $v \ge w$ and $q \to p$ fails through $u \ge w$, compare $u$ and $v$ and use persistence. For the converse, let $p$ and $q$ be true above two incomparable worlds.

16. Take a root with three maximal worlds $1$, $2$ and $3$ above it, $p$ true at $3$, $q$ at $1$ and $r$ at $2$. At the root, $\neg p \to q \vee r$ holds, but $\neg p \to q$ fails at $2$ and $\neg p \to r$ fails at $1$.

17. $\Gamma \mid p \to q \vee r$ needs $\Gamma \vdash p \to q \vee r$ and that $\Gamma \mid p$ imply $\Gamma \mid q \vee r$. Since $\Gamma \nvdash p$ (make every atom false), the second condition is vacuous. For $\set{p, p \to q \vee r}$ the set proves $p$ but neither $q$ nor $r$.

19. $\neg p = (-\infty, 0) \cup (2, \infty)$, $\neg\neg p = (0, 2)$, $\neg\neg p \to p = \R \setminus \set{1}$ and $\neg p \vee \neg\neg p = \R \setminus \set{0, 2}$.

20. If $w \Vdash \square(p \to q)$, $w' \ge w$ and $w' R v$ with $v \Vdash p$, then $v \Vdash p \to q$, so $v \Vdash q$ and $w' \Vdash \lozenge q$. No world forces $\lozenge\bot$. Neither condition is used.

21. Worlds $0 \le 1$ with domains $\set{a}$ and $\set{a, b}$, $Pa$ true at both worlds, $Pb$ and $Q$ false everywhere. $\forall x\,Px$ fails at both worlds, so the antecedent holds at $0$, but $Pa \to Q$ fails at $0$.

22. Let world $n$ have domain $\set{0, \ldots, n}$, and let $Pk$ be true at the worlds $m > k$. Every $Pk$ becomes true later, so $\forall x\,\neg\neg Px$ holds everywhere, while $Pm$ fails at $m$, so $\forall x\,Px$ holds nowhere. On a finite frame every world lies below a maximal world, where $\neg\neg Px$ means $Px$.

23. Among $n + 1$ values in an algebra with $n$ elements two coincide, and then $p_i \leftrightarrow p_j$ is $1$. The chain of $n$ worlds has $n + 1$ up-sets; give the $p_i$ different ones, and no biconditional holds at the bottom. An algebra with $n$ elements would validate $D_n$, which $\mathsf{IPC}$ does not prove.

24. In a finite model every world lies below a maximal world, and the worlds above a maximal world are itself only. If $\mathsf{CPC} \vdash \varphi$, every maximal world forces $\varphi$, so every world forces $\neg\neg\varphi$; finite completeness of $\mathsf{IPC}$ does the rest.

25. With a top $t$: if $t \Vdash p$, every world forces $\neg\neg p$; otherwise no world forces $p$, and every world forces $\neg p$. Without a top, a finite rooted frame has two maximal worlds $a \ne b$; make $p$ true at $a$ only.

26. For $p \to \neg\neg p$: $\mathbf{O}$ asserts $p$, $\mathbf{P}$ defends with $\neg\neg p$, $\mathbf{O}$ attacks it with $\neg p$, and $\mathbf{P}$ attacks $\neg p$ with $p$, which $\mathbf{O}$ has asserted; $\mathbf{O}$ has no move left. For $\neg\neg p \to p$: $\mathbf{O}$ asserts $\neg\neg p$, $\mathbf{P}$ may not yet assert $p$ and attacks with $\neg p$, and $\mathbf{O}$ attacks $\neg p$ with $p$. That attack has no defence and is the latest unanswered one, so the intuitionistic rule forbids $\mathbf{P}$ to answer the first attack with $p$; the classical rule allows it. A second attack with $\neg p$ only provokes $\mathbf{O}$ to assert $p$ again, and the position repeats.
