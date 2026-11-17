1. (a) EIO in the first figure, Ferio: the middle term "perfect square" is the subject of the major premise and the predicate of the minor. (b) EIO in the second figure, Festino: the middle term "multiple of $3$" is the predicate of both premises.

2. The A sentence is false, so its contradictory O, "some multiple of $6$ is not a multiple of $4$", is true. The square leaves E and I open, since a false A allows either value for its contrary and for its subaltern. In fact E is false and I is true, both because of $12$.

3. Take $p \lor \neg p$. It is a tautology, so $\vdash p \lor \neg p$, but $p$ and $\neg p$ are both false under some valuation, so neither is provable. "$\vdash p \lor \neg p$" says that one object-language formula is a theorem; "$\vdash p$ or $\vdash \neg p$" is a disjunction in the metalanguage, and the two must not be confused.

7. The condition $T \vdash \forall x\, \exists! y\, \psi(x, y)$ fails at $x = 0$, where no $y$ exists. Take $\psi(x, y) := (x \neq 0 \land x \cdot y = 1) \lor (x = 0 \land y = 0)$, the convention $0^{-1} = 0$.

9. A term distributed in the conclusion must be distributed in its premise. The major term $P$ is distributed in "no $S$ is $P$" but not in "every $M$ is $P$": this is an illicit major. Let $M$ be the squares, $P$ the rectangles and $S$ the rectangles that are not squares.

11. (a) From $ab$ get $aabb$ by the first rule, then $aabbab$ by the second rule applied to $aabb$ and $ab$. (b) Induction on derivations: the axiom has the property, wrapping in $a \dots b$ keeps it, and so does concatenation. The initial segment $abb$ of $abba$ has more $b$'s than $a$'s.

13. For cut, suppose $\Gamma$ is finite. Then $\Gamma \vdash \psi$ forces $\psi \in \Gamma$, so $\Delta \subseteq \Gamma$ and $\Gamma \cup \Delta = \Gamma$. For the other two parts, take $\Gamma$ to be the set of all variables, the formula $\neg p_0$, and the substitution that sends every variable to $p_0$.

15. Fix the valuation with $p$ true and $q$ false. All axioms are true under it and modus ponens keeps truth under it, so every theorem is true under it, and $q$ is not. Post completeness speaks of schemas: the schema $p \land \neg q$ has the instance $q \land \neg q$, and with that every formula follows.

16. Check that $a \le (b \to a)$ for all $a, b$, so $a \to (b \to a) = 1$. At $p = \tfrac12$ we get $\neg p = 0$, $\neg\neg p = 1$ and $1 \to \tfrac12 = \tfrac12$. So classical logic is not sound for this algebra, and intuitionistic logic, which is sound for it, does not prove $\neg\neg p \to p$.

17. Over $T$, no: $T + A$ proves "there is a greatest element", which fails in $(\Z, <)$. Over $T_1$, yes: every model of $T_1$ expands to a model of $T_1 + A$ by letting $c$ name its greatest element, and the expansion test applies.

20. Iterate $[Q\ [R]]$ from the sheet into the area of depth $2$ that holds $Q$. Deiterate the inner copy of $Q$, remove the double cut around $R$, then erase $Q$ in the area of depth $2$ and $[Q\ [R]]$ from the sheet. Both erasures act in areas of even depth.

21. A relation is invariant exactly when it is a union of orbits of $D^3$, and the orbit of a triple is fixed by which of its entries are equal: a partition of $\set{1, 2, 3}$. There are $5$ partitions, so $2^5 = 32$ relations when $|D| \ge 3$. When $|D| = 2$ the partition into three singletons gives an empty orbit, so there are $2^4 = 16$.

22. If $\mathrm{PA} + \neg\mathrm{Con}(\mathrm{PA})$ were inconsistent, then $\mathrm{PA} \vdash \mathrm{Con}(\mathrm{PA})$, which the second theorem forbids for consistent PA. The theory is not sound for $\N$: it proves $\neg\mathrm{Con}(\mathrm{PA})$, which is false there.

23. Suppose $T \vdash \forall x\, \delta(x)$ but $\delta(n)$ is false for some $n$. Then $T \vdash \neg\delta(\bar n)$ by hypothesis, and $T \vdash \delta(\bar n)$ by instantiation, so $T$ is inconsistent. A finitary consistency proof for $T$ would therefore make every real statement proved with ideal methods true.

24. Enumerate the formulas $\varphi_0, \varphi_1, \dots$. Let $\Gamma_0 = \Gamma$ and add $\varphi_n$ to $\Gamma_n$ if the result is consistent, and $\neg\varphi_n$ otherwise. If both $\Gamma_n \cup \set{\varphi_n}$ and $\Gamma_n \cup \set{\neg\varphi_n}$ were inconsistent, $\Gamma_n$ would prove $\neg\varphi_n$ and $\neg\neg\varphi_n$. The union of the $\Gamma_n$ is consistent because derivations are finite.
