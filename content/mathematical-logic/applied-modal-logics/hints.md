1. $(\N, <)$: the first two are valid, since the order is transitive and every point has a later point; the third fails at $0$ with $p$ true at $1$ only, because no point lies strictly between $0$ and $1$. $(\Q, <)$: all three are valid. On $0 < 1 < 2$ only the first is valid; $\mathbf{G}p \to \mathbf{F}p$ fails at $2$, where $\mathbf{G}p$ is vacuously true, and $\mathbf{F}p \to \mathbf{F}\mathbf{F}p$ fails at $0$ with $p$ true at $1$ only.

2. True: $p\,\mathbf{U}\,q$, $q\,\mathbf{U}\,p$ (as $p$ holds at $0$), $\mathbf{GF}p$ and $\mathbf{G}(p \to \mathbf{F}q)$. False: $\mathbf{FG}p$, $\mathbf{XX}(p\,\mathbf{U}\,q)$, since position $2$ has neither $p$ nor $q$, and $\mathbf{G}(p \to \mathbf{X}q)$, which fails at position $1$.

3. (a), (c) and (e) are valid. (b), (d) and (f) fail on the word $(\set{p}\,\set{q})^\omega$, where $p$ and $q$ alternate and never hold together.

4. $\mathbf{E}[p\,\mathbf{U}\,q]$ holds at all four states. $\mathbf{A}[p\,\mathbf{U}\,q]$ holds at $3$ only, because of the path that stays at $1$ forever. $\mathbf{EG}\,p$ holds at $0$, $1$ and $2$, and $\mathbf{AF}\,q$ at $3$ only.

5. True at $u$: $K_a p$, $K_b p$, $K_b K_a p$ and $E p$. False: $K_a K_b p$, since $K_b p$ fails at $v$; hence also $E E p$ and $C p$. The world $w$, where $p$ is false, is reached from $u$ in two steps.

6. Yes, every world has a successor. At $a$: $\mathbf{O}p$, $\mathbf{P}q$ and $\mathbf{O}(\mathbf{O}p \to p)$ hold; $\mathbf{O}q$ and $\mathbf{O}p \to p$ fail. The last one holds at $a$ because every successor of $a$ sees itself.

7. $31$, $26$ and $16$ worlds: after $r$ rounds of "no", the worlds left are those with at least $r + 1$ muddy children. The muddy children answer "yes" in round $3$, and the clean children know in round $4$.

8. (a) $7$, (b) $5$: the empty state and the four singletons, (c) $6$, (d) $8$: all subsets of the three worlds where $p \vee q$ is classically true.

9. $\langle \mathsf{hasChild}\rangle(\mathsf{Doctor} \wedge [\mathsf{hasChild}]\neg\mathsf{Doctor})$. The first subsumption holds. The converse fails in $\set{x, y, z}$ with $r = \set{(x, y), (x, z)}$, $A = \set{y}$ and $B = \set{z}$: $x$ has an $r$-successor in $A$ and one in $B$, but none in both.

10. (a) $\mathbf{GF}p \wedge \mathbf{FG}\neg q$. (b) $\mathbf{G}(p \to \mathbf{XF}q)$. (c) $\mathbf{G}(p \to \mathbf{X}\neg p)$. (d) $\neg p\,\mathbf{U}\,q$.

11. $\varphi\,\mathbf{U}\,\psi \equiv \psi \vee (\varphi \wedge \varphi\,\mathbf{U}^{s}\psi)$ and $\varphi\,\mathbf{U}^{s}\psi \equiv \mathbf{X}(\varphi\,\mathbf{U}\,\psi)$. In each case split on whether the witness $j$ for $\psi$ is the current position or a later one.

12. A suffix of a path from a reachable state is a path from that state, and a finite path to a state followed by any path from it is a path from the start. Both directions use only these two facts. For $\mathbf{AF}\,\mathbf{AG}$ the first $\mathbf{F}$ must find one state from which every continuation satisfies $\mathbf{G}p$, and different paths may reach their stable region at points that no single state controls.

13. In a Euclidean frame, $wRv$ and $wRv$ give $vRv$. So every world $v$ that $w$ considers possible sees itself, and $Bp \to p$ holds at $v$. For the failure of $Bp \to p$ take worlds $a, b$ with $R = \set{(a, b), (b, b)}$ and $p$ true at $b$ only.

14. $\neg K_b p$ holds at $w_1$ and $w_3$, so the updated model is $\set{w_1, w_3}$, where $a$ can tell the two worlds apart and $b$ cannot. Before the announcement $a$ does not know $q$ at $w_1$, since $w_2$ is possible; after it $a$ does. $q$ holds at both remaining worlds, so it is common knowledge.

15. For the first, the sphere $\set{w}$ contains the $\varphi$-world $w$, and $\varphi \to \psi$ holds there. For the second, take spheres $S_1$ and $S_2$ that witness the two conditionals; one is contained in the other, and the smaller one still contains a $\varphi$-world and satisfies both $\varphi \to \psi$ and $\varphi \to \chi$.

16. $K * \neg q = \mathrm{Cn}(\neg p \wedge \neg q)$, since $00$ is the lowest $\neg q$-valuation. $K * \neg(p \wedge q) = \mathrm{Cn}(\neg p \wedge q)$. $K \div q$ has models $\set{11, 00}$, so it is $\mathrm{Cn}(p \leftrightarrow q)$, and adding $q$ gives back $\mathrm{Cn}(p \wedge q)$.

17. $x{:}(p \wedge q) \to (a \cdot x){:}p \wedge (b \cdot x){:}q$, with $a{:}(p \wedge q \to p)$ and $b{:}(p \wedge q \to q)$ from axiom necessitation, and $x{:}p \to {!x}{:}(x{:}p)$, an instance of the checker axiom.

18. In $\mathrm{K}$, $\mathbf{O}(p \wedge \neg p) \leftrightarrow \mathbf{O}p \wedge \mathbf{O}\neg p$, and $\mathbf{O}\bot \leftrightarrow \mathbf{O}(p \wedge \neg p)$ by the rule of replacing provable equivalents. Since $\mathbf{P}p = \neg\mathbf{O}\neg p$, the first formula is a rewriting of the third.

19. Take $\psi = C_G\varphi$ in the induction rule. You need $C_G\varphi \to E_G(C_G\varphi \wedge C_G\varphi)$, which follows from the fixed point axiom because each $K_a$ is monotone: $K_a(\varphi \wedge C_G\varphi) \to K_a C_G\varphi$.

20. $\langle B\rangle\langle E\rangle p$ asks for $c$ with $a < c < b$ and then $d$ with $a < d < c$ such that $p$ holds at $[d, c]$. The formula $\langle B\rangle\langle B\rangle\top$ asks for $a < d < c < b$, which is possible in $\N$ exactly when $b - a \ge 3$.

21. In round $k - 1$. Prove by induction on $k \ge 2$ that after the announcement and $k - 2$ rounds of "no" the worlds left are those with at least $k$ muddy children. A muddy child in a world with exactly $k$ muddy children then sees that flipping her own coordinate leads to a deleted world.

22. If $K(p \wedge \neg Kp)$ held at $w$, distribution would give $Kp$ and $K\neg Kp$ at $w$, and reflexivity would turn the second into $\neg Kp$. So $\neg K(p \wedge \neg Kp)$ is valid, and by necessitation $\neg\lozenge K(p \wedge \neg Kp)$ is too. Knowability then gives $\neg(p \wedge \neg Kp)$, which is classically equivalent to $p \to Kp$.

23. The automaton guesses the point after which $p$ holds forever: state $0$ loops on both letters and moves to the accepting state $1$ on $\set{p}$, and state $1$ loops on $\set{p}$ only. A deterministic automaton would reach an accepting state on some prefix $\set{p}^{n_1}$ of $\set{p}^\omega$, then on some prefix $\set{p}^{n_1}\emptyset\set{p}^{n_2}$, and so on; the limit word has infinitely many letters $\emptyset$ and is accepted.

24. In $\mathrm{S5}$, $\square\varphi$ and $\neg\square\varphi$ are true at every world of an equivalence class or at none, so they behave like constants under $\square$. Put the formula under each box in conjunctive normal form, distribute the box over conjunctions and pull the depth-one parts out of the disjunctions with the first equivalence. Induction on depth then removes nested boxes.

25. Use the chain of worlds $w_0, w_1, \ldots, w_{d+1}$ in which consecutive worlds are linked alternately by $a$ and by $b$, with $p$ false only at $w_{d+1}$, and the one-world model where $p$ is true. At $w_0$ and at the single world, $C p$ differs. The points are $d$-bisimilar, since a play of length $d$ from $w_0$ never reaches $w_{d+1}$, so they agree on formulas of depth at most $d$.
