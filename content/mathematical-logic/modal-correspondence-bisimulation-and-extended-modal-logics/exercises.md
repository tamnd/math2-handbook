1. ◦ Let $\mathfrak{M}$ have worlds $r, s, t$ with $R = \set{(r, s), (r, t), (s, s)}$, and let $\mathfrak{M}'$ have worlds $r', s'$ with $R' = \set{(r', s'), (s', s')}$, with every variable false in both. Find the largest [bisimulation](/X27BR4YP2Y/) between $\mathfrak{M}$ and $\mathfrak{M}'$. Are $r$ and $r'$ bisimilar? Give a modal formula that is true at one of them and false at the other.

2. ◦ Let $C_n$ be the cycle with worlds $0, 1, \dots, n - 1$ and $i \mathrel{R} i + 1 \pmod n$. (a) With every variable false, show that $C_2$, $C_3$ and $C_4$ are pairwise bisimilar. (b) Make $p$ true at $0$ only, in $C_2$ and in $C_3$, and find a formula that is true at $0$ in $C_2$ and false at $0$ in $C_3$. (c) In $C_4$ make $p$ true at $0$ and $2$, and give a bisimulation between this model and $C_2$ with $p$ true at $0$ only. (d) Use (a) to show that the first-order formula $\exists y \, (R x y \wedge R y x)$ is not equivalent to the standard translation of any modal formula, as the [van Benthem characterization theorem](/Y89MGMWE4H/) predicts.

3. ◦ Let $W = \set{1, \dots, 6}$, $R = \set{(1,2), (1,3), (2,4), (3,5), (4,4), (5,6), (6,5)}$ and $V(p) = \set{4, 5, 6}$. Find the classes of mutually bisimilar worlds of this model and draw its bisimulation contraction. Which world of the contraction satisfies the same formulas as world $1$, and why does the [Hennessy–Milner theorem](/DBDNYXA7ME/) apply?

4. ◦ Check that $\square p \to \lozenge p$ and $(\lozenge p \wedge \lozenge q) \to \lozenge(p \wedge q)$ are Sahlqvist formulas, and compute their first-order correspondents by the minimal valuations of [Sahlqvist's theorem](/S4SSDMETJM/). Then check the second answer by hand, in the sense of [correspondence theory](/3RYBWYPJVD/), on a world with exactly two successors.

5. ◦ Let $\circ$ be the reflexive one-point frame and $\bullet$ the irreflexive one. Decide which of the formulas $\square p \to p$, $\square p \to \lozenge p$, $\square p \leftrightarrow \lozenge p$, $\square \bot$, $p \to \square p$ and $\square p \to \square\square p$ are valid on each. Deduce that neither of $\mathrm{Log}(\circ)$ and $\mathrm{Log}(\bullet)$ contains the other, as two coatoms of the [lattice of normal modal logics](/EZ011FT3GT/) must.

6. ◦ In [propositional dynamic logic](/VJ78A0Q22R/), let $W = \set{0, 1, 2, 3}$, $R_a = \set{(0,1), (1,2), (2,0)}$, $R_b = \set{(2,3)}$ and $V(p) = \set{3}$. Compute the relations of $a ; b$ and $a^*$, and the sets of worlds at which $\langle a^* ; b \rangle p$ and $[a^*] \neg p$ hold.

7. ◦ Let $W = \set{0, \dots, 5}$, $R = \set{(0,1), (0,2), (1,3), (2,3), (3,4), (5,5), (5,1)}$ and $V(p) = \set{3}$. Compute the iterates $T_0 = \emptyset$, $T_{k+1} = V(p) \cup \set{w : \text{every successor of } w \text{ is in } T_k}$ and the set of worlds where the [modal $\mu$-calculus](/MZ0M2KR9S0/) formula $\mu X . (p \vee \square X)$ holds. Explain why world $4$ is in the set and world $5$ is not.

8. ◦ In [hybrid logic](/NVPQ9W9DED/), let $W = \set{0, 1, 2}$ and $R = \set{(0,1), (1,1), (1,2)}$. Find the worlds at which each of $\downarrow x . \lozenge x$, $\downarrow x . \lozenge\lozenge x$, $\downarrow x . \square\square x$ and $\downarrow x . \square\lozenge x$ holds.

9. ◦ Write out the [Gödel–McKinsey–Tarski translations](/BXVNEN55MR/) $T(p \vee \neg p)$ and $T(\neg\neg p \to p)$, where $\neg A$ is $A \to \bot$, and simplify them in $\mathsf{S4}$. Evaluate both on the reflexive two-world chain $0 \le 1$ with $p$ true at $1$ only, and deduce that neither $p \vee \neg p$ nor $\neg\neg p \to p$ is a theorem of intuitionistic logic.

10. ◦ In the [topological semantics](/HWJXMBNHQ0/) on $\R$, let $V(p) = \Q$. Find the truth sets of $\lozenge p$, $\square\lozenge p$, $\square p$ and $\lozenge\square p$. Deduce from the [McKinsey–Tarski theorem](/2VF0546VXK/) that the [McKinsey formula](/4N4ZNWZRE2/) $\square\lozenge p \to \lozenge\square p$ is not a theorem of $\mathsf{S4}$.

11. • Compute the first-order correspondents of the Sahlqvist formulas $\square p \to \lozenge\lozenge p$ and $\lozenge\square p \to \square\square p$. Show that the second is valid on every frame whose relation is an equivalence relation.

12. • Prove that $\square p \vee \square(p \to q) \vee \square((p \wedge q) \to r)$ is valid on a frame if and only if every world has at most two successors.

13. • For each class of frames, decide whether it is modally definable. If it is not, name a closure condition of the [Goldblatt–Thomason theorem](/GX5E3GNRCS/) that fails, with frames that show it; if it is, give a defining formula. (a) $\exists x \, R x x$. (b) $\forall x \forall y \, (R x y \to \neg R y x)$. (c) $\forall x \forall y \, (x = y)$. (d) $\forall x \exists y \, (R x y \wedge \forall z \, \neg R y z)$.

14. • Show that the pure formulas $\lozenge i \to \square i$, $\lozenge\lozenge j \to \neg\lozenge j$ and $@_i \lozenge j \vee @_i j \vee @_j \lozenge i$ define, respectively, the frames in which each world has at most one successor, the frames with $\forall x \forall y \forall z \, (R x y \wedge R y z \to \neg R x z)$, and the frames with $\forall x \forall y \, (R x y \vee x = y \vee R y x)$. Which of the three classes is defined by a formula of basic modal logic?

15. • Let $W = \set{0, 1, 2}$, let $R_1$ be the equivalence relation with classes $\set{0, 1}$ and $\set{2}$, and let $R_2$ be the one with classes $\set{0}$ and $\set{1, 2}$. Show that $(W, R_1, R_2)$ is a frame for the fusion $\mathsf{S5} \otimes \mathsf{S5}$. With $V(p) = \set{2}$, compute the truth sets of $\lozenge_1 \lozenge_2 p$ and $\lozenge_2 \lozenge_1 p$, and deduce that the frame does not validate $\mathsf{S5} \times \mathsf{S5}$, in the sense of [products of modal logics](/JA2EBWVW8A/).

16. • In Kripke's models with non-normal worlds, the [impossible worlds](/8PAJMAN8DM/) of his semantics for $\mathsf{S2}$ and $\mathsf{S3}$, show that $\square(p \to q) \to \square(\square p \to \square q)$ is valid on all models whose relation is reflexive and transitive. Give a model with a reflexive relation, and all worlds normal, in which it fails.

17. • List the elements of the Fischer–Ladner closures $\mathrm{FL}([(a ; b)^*] p)$ and $\mathrm{FL}([(p ? ; a)^*] q)$. What bound on the size of a model does the small model theorem give for each formula?

18. • Prove that $[a^*] p \leftrightarrow (p \wedge [a][a^*] p)$ and $[a^*](p \to [a] p) \to (p \to [a^*] p)$ are valid in every model of propositional dynamic logic.

19. • Prove that $R_{(a \cup b)^*} = R_{a^* ; (b ; a^*)^*}$ in every model, and deduce that $\langle (a \cup b)^* \rangle p \leftrightarrow \langle a^* \rangle \langle (b ; a^*)^* \rangle p$ is valid.

20. • Let $W = \set{0, \dots, 4}$, $R = \set{(0,1), (1,2), (0,3), (3,3), (2,4)}$, $V(p) = \set{0, 1, 3}$ and $V(q) = \set{2}$. Compute the truth sets of $\mu X . (q \vee (p \wedge \lozenge X))$, which says that some path keeps $p$ until it reaches $q$, and of $\mu X . (q \vee (\lozenge\top \wedge \square X))$, which says that every path reaches $q$ and none ends before.

21. • Let $T(\neg p \vee \neg\neg p)$ be the translation of the weak excluded middle. Show that on a reflexive and transitive frame it is equivalent to $\lozenge\square p \to \square\lozenge\square p$, and that it is valid exactly when the frame is directed: any two successors of a world have a common successor. Relate this to the remark in the [Blok–Esakia theorem](/BB9TA5Q9PN/) that every extension of $\mathsf{S4.2}$ proves $T(\neg p \vee \neg\neg p)$.

22. • In [quantified modal logic](/D2H3S12V7X/) with varying domains, let $E x$ be $\exists y \, (y = x)$. Show that $\square \forall x \, E x$ is valid on every frame with domains and that $\forall x \, \square E x$ is valid on a frame with domains exactly when its domains increase. Deduce that the converse [Barcan formula](/9PYDNBA5X4/) fails on every frame whose domains do not increase.

23. ★ Let $\mathfrak{M}$ be a finite model. Let $Z_0$ be the set of pairs of worlds that agree on all variables, and let $Z_{k+1}$ be the set of pairs in $Z_k$ that satisfy the forth and back conditions with respect to $Z_k$. Prove that the sequence becomes constant, that its limit is the largest bisimulation on $\mathfrak{M}$, and that $(w, v) \in Z_k$ exactly when $w$ and $v$ satisfy the same formulas of modal depth at most $k$.

24. ★ Prove that on a finite transitive frame the McKinsey formula $\square\lozenge p \to \lozenge\square p$ is valid at a world $x$ under all valuations if and only if $x$ has a successor $y$ with $R(y) \subseteq \set{y}$, where $R(y)$ is the set of successors of $y$.

25. ★ Let $\mathsf{Ver} = \mathsf{K} \oplus \square\bot$ and $\mathsf{Triv} = \mathsf{K} \oplus (p \leftrightarrow \square p)$. Prove that $\mathsf{Ver} = \mathrm{Log}(\bullet)$ and $\mathsf{Triv} = \mathrm{Log}(\circ)$.

26. ★ Show that the $\mu$-calculus formula $\nu X . (p \wedge \square X)$, which says that $p$ holds at every world reachable in zero or more steps, is not equivalent to any formula of basic modal logic.

27. ★ Show that the class of frames with $\forall x \exists y \, (R x y \wedge R y y)$ is closed under generated subframes, disjoint unions and bounded morphic images, but is not modally definable. Use the ultrafilter extension of $(\N, <)$ and the Goldblatt–Thomason theorem.
