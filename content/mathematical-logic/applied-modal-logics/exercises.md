1. ◦ For each of the frames $(\N, <)$, $(\Q, <)$ and the three-point order $0 < 1 < 2$, say which of $\mathbf{G}p \to \mathbf{G}\mathbf{G}p$, $\mathbf{G}p \to \mathbf{F}p$ and $\mathbf{F}p \to \mathbf{F}\mathbf{F}p$ are valid, using the frame conditions of [temporal logic](/8XB117FKKV/). For each failure, give a valuation and a point that refute the formula.

2. ◦ Let $w$ be the infinite word $\set{p}\,\set{p, q}\,\emptyset\,(\set{q}\,\set{p})^\omega$. Decide which of these [LTL](/RMJ56ZPA63/) formulas hold at position $0$: $p\,\mathbf{U}\,q$, $q\,\mathbf{U}\,p$, $\mathbf{GF}p$, $\mathbf{FG}p$, $\mathbf{XX}(p\,\mathbf{U}\,q)$, $\mathbf{G}(p \to \mathbf{X}q)$ and $\mathbf{G}(p \to \mathbf{F}q)$.

3. ◦ Which of these LTL equivalences and implications are valid? For each one that is not, give a word that refutes it. (a) $\mathbf{G}(p \wedge q) \leftrightarrow \mathbf{G}p \wedge \mathbf{G}q$. (b) $\mathbf{G}(p \vee q) \to \mathbf{G}p \vee \mathbf{G}q$. (c) $\mathbf{F}(p \vee q) \leftrightarrow \mathbf{F}p \vee \mathbf{F}q$. (d) $\mathbf{F}p \wedge \mathbf{F}q \to \mathbf{F}(p \wedge q)$. (e) $\mathbf{FG}(p \wedge q) \leftrightarrow \mathbf{FG}p \wedge \mathbf{FG}q$. (f) $\mathbf{GF}p \wedge \mathbf{GF}q \to \mathbf{GF}(p \wedge q)$.

4. ◦ A transition system has states $0, 1, 2, 3$ and transitions $0 \to 1$, $0 \to 2$, $1 \to 1$, $1 \to 3$, $2 \to 0$ and $3 \to 3$. The atom $p$ holds at $0$, $1$ and $2$, and $q$ holds at $3$ only. Compute the sets of states where the [CTL](/F6JA5C5BJX/) formulas $\mathbf{E}[p\,\mathbf{U}\,q]$, $\mathbf{A}[p\,\mathbf{U}\,q]$, $\mathbf{EG}\,p$ and $\mathbf{AF}\,q$ hold.

5. ◦ An [epistemic](/EA34W4ERRE/) $\mathrm{S5}$ model has worlds $u, v, w$. Agent $a$ cannot tell $u$ from $v$, agent $b$ cannot tell $v$ from $w$, and there are no other confusions. The atom $p$ is true at $u$ and $v$. Decide at $u$: $K_a p$, $K_b p$, $K_a K_b p$, $K_b K_a p$, $E p$, $E E p$ and the [common knowledge](/7BCMKF2P7X/) $C p$, where $E$ and $C$ refer to the group $\set{a, b}$.

6. ◦ A deontic frame has worlds $a, b, c$ and relation $R = \set{(a, b), (a, c), (b, b), (c, c)}$. The atom $p$ is true at $b$ and $c$, and $q$ at $c$ only. Is the frame serial? At $a$, which of $\mathbf{O}p$, $\mathbf{O}q$, $\mathbf{P}q$, $\mathbf{O}p \to p$ and $\mathbf{O}(\mathbf{O}p \to p)$ hold in the semantics of [deontic logic](/7B74J6J5JV/)?

7. ◦ In the [muddy children puzzle](/BG9TYCJ7HP/) with $5$ children of whom $3$ are muddy, how many worlds remain after the father's announcement, after one round of "no" and after two rounds of "no"? In which round do the muddy children answer "yes", and in which round do the clean children first know their state?

8. ◦ In [inquisitive logic](/EX0ND8DCTN/) over two atoms there are four worlds and sixteen information states, the empty state included. How many states support (a) $?p$, (b) $?p \wedge ?q$, (c) $p \vee q$, (d) $\neg\neg(p \vee q)$?

9. ◦ Translate the [description logic](/TXQ80B8ZSA/) concept $\exists \mathsf{hasChild}.(\mathsf{Doctor} \sqcap \forall \mathsf{hasChild}.\neg\mathsf{Doctor})$ into multimodal logic. Then decide whether $\exists r.(A \sqcap B) \sqsubseteq \exists r.A \sqcap \exists r.B$ and whether the converse subsumption holds; for a failure give an interpretation with three elements.

10. • Write LTL formulas for these properties of a run. (a) $p$ holds at infinitely many positions and $q$ at only finitely many. (b) Every position where $p$ holds is followed, strictly later, by a position where $q$ holds. (c) $p$ never holds at two consecutive positions. (d) $q$ holds at some position, and $p$ holds at no earlier position.

11. • Let $\varphi\,\mathbf{U}^{s}\psi$ be the strict until: it holds at $i$ when $\psi$ holds at some $j > i$ and $\varphi$ holds at every $k$ with $i < k < j$. Show that over $\N$ the strict and the reflexive until define each other with the help of $\mathbf{X}$: give a formula for $\varphi\,\mathbf{U}\,\psi$ in terms of $\mathbf{U}^{s}$ and one for $\varphi\,\mathbf{U}^{s}\psi$ in terms of $\mathbf{U}$ and $\mathbf{X}$, and prove both.

12. • On total transition systems, show that the CTL formula $\mathbf{AG}\,\mathbf{AF}\,p$ is equivalent to the CTL* formula $\mathbf{A}\,\mathbf{GF}\,p$. Explain why the same argument does not show that $\mathbf{AF}\,\mathbf{AG}\,p$ is equivalent to $\mathbf{A}\,\mathbf{FG}\,p$.

13. • Show that $B(Bp \to p)$ is valid on every $\mathrm{KD45}$ frame of [doxastic logic](/RTP4HTZYK3/), although $Bp \to p$ is not. Which of the three frame conditions does the proof use?

14. • A model has worlds $w_1, w_2, w_3$, with $p, q$ true at $w_1$, only $p$ at $w_2$ and only $q$ at $w_3$. Agent $a$ cannot tell $w_1$ from $w_2$, and agent $b$ cannot tell $w_1$ from $w_3$. The formula $\neg K_b p$ is announced in public, as in [dynamic epistemic logic](/9465T2PWZT/). Find the worlds where it is true and the updated model. At $w_1$, does $a$ know $q$ before the announcement, and after it? Is $q$ common knowledge after it?

15. • In a centered sphere model of [conditional logic](/ZGYG7WN7EC/), show that $(\varphi \wedge \psi) \to (\varphi > \psi)$ and $((\varphi > \psi) \wedge (\varphi > \chi)) \to (\varphi > (\psi \wedge \chi))$ are valid. Where does the second proof use that the spheres are nested?

16. • Let $K = \mathrm{Cn}(p \wedge q)$, and revise with the faithful ranking $11 < 01 < 00 < 10$ of the valuations, written as in [AGM belief revision](/Y05YQN7HGQ/). Compute $K * \neg q$, $K * \neg(p \wedge q)$ and, by the Harper identity, $K \div q$. Check the recovery postulate $K \subseteq (K \div q) + q$.

17. • In the logic of proofs of [justification logic](/5HKWCXEFG1/), give realizations of the $\mathrm{S4}$ theorems $\square(p \wedge q) \to \square p \wedge \square q$ and $\square p \to \square\square p$, and derive them from the axioms. Name the constants you use and the formulas they justify.

18. • Show that over the logic $\mathrm{K}$ each of the formulas $\mathbf{O}p \to \mathbf{P}p$, $\neg\mathbf{O}\bot$ and $\neg(\mathbf{O}p \wedge \mathbf{O}\neg p)$ derives the other two, so that each axiomatizes standard deontic logic.

19. • Use the fixed point axiom and the induction rule for [common knowledge](/7BCMKF2P7X/) to derive $C_G\varphi \to C_G C_G\varphi$. Which property of $K_a$ do you need besides the two principles?

20. • In the strict semantics of [interval temporal logic](/991B5RR6X4/) over $\N$, show that $\langle B\rangle\langle E\rangle p$ holds at $[a, b]$ if and only if $p$ holds at some $[c, d]$ with $a < c < d < b$. Then give a formula without atoms that holds at $[a, b]$ exactly when $b - a \ge 3$.

21. ★ In the muddy children puzzle with $n$ children of whom $k \ge 2$ are muddy, suppose the father says "at least two of you are muddy" instead of "at least one". In which round do the muddy children first answer "yes"? Prove your answer in the style of the induction of the puzzle.

22. ★ Show that $K(p \wedge \neg Kp)$ is false at every world of every model in which $K$ is normal and reflexive. Deduce, following [Fitch's paradox](/HVCW7QYXSW/), that the knowability principle $\varphi \to \lozenge K\varphi$, applied to $p \wedge \neg Kp$, gives $p \to Kp$ in classical logic.

23. ★ Over the alphabet $\set{\emptyset, \set{p}}$, give a nondeterministic Büchi automaton with two states for $\mathbf{FG}p$. Then show that no deterministic Büchi automaton accepts exactly the words satisfying $\mathbf{FG}p$.

24. ★ Show that in $\mathrm{S5}$ with one agent every formula is equivalent to a formula of modal depth at most $1$. Start by proving $\mathrm{S5} \vdash \square(\square\varphi \vee \psi) \leftrightarrow \square\varphi \vee \square\psi$ and $\mathrm{S5} \vdash \square\square\varphi \leftrightarrow \square\varphi$.

25. ★ Show that the common knowledge operator $C_{\set{a,b}}$ is not definable in the language of $K_a$ and $K_b$: for each formula $\varphi$ of modal depth $d$ without $C$, find two pointed models that agree on all formulas of depth at most $d$ and disagree on $C_{\set{a,b}}p$.
