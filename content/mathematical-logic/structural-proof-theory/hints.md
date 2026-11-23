1. (a) Context-splitting with $\Gamma = p$, $\Delta$ empty, $\Pi = s$ and $\Lambda = t$ gives $p, s \Rightarrow t$; the degree is $1$. (b) With $\Delta = p \vee q$, $\Pi = r$ and $\Lambda = s$ it gives $r \Rightarrow p \vee q, s$; the degree is $0$. The context-sharing form applies to neither pair, since its two premises must have the same contexts.

2. With $\neg$ primitive there are $7$: the whole formula, $p \to q$, $\neg q \to \neg p$, $\neg q$, $\neg p$, $q$ and $p$. With $\neg A = A \to \bot$ there are $8$: the whole formula, $p \to q$, $(q \to \bot) \to (p \to \bot)$, $q \to \bot$, $p \to \bot$, $p$, $q$ and $\bot$. A cut-free derivation uses only these.

4. The final sequents are $p \Rightarrow p$, $p \Rightarrow q$, $q \Rightarrow p$ and $q \Rightarrow q$. Two are not axioms, so the sequent is not derivable. From $p \Rightarrow q$: make $p$ true and $q$ false. Then $p \vee q$ is true and $p \wedge q$ is false.

7. The interpretations are $(p \to q) \vee (q \to p)$ and $((\bot \to \bot) \to p) \vee (p \to \bot)$, which is equivalent to $p \vee \neg p$. Take two worlds $0 \le 1$ with $p$ true only at $1$. At $0$ neither $p$ nor $\neg p$ holds, so $p \vee \neg p$ fails, and HLC is sound for total orders.

9. Under $S_0$, $A(5)$ is $2 < 5$, true, and $A(0)$ is $2 < 0$, false, so the critical formula is false. The least $m \le 5$ with $2 < m$ is $3$, so $S_1$ gives $\varepsilon x\, A(x)$ the value $3$. Then $A(4)$ is true and $\neg(4 < 3)$ is true, so the second critical formula holds.

12. Each premise of a G3cp rule has exactly one connective fewer than the conclusion, and each rule has at most two premises. Use induction on $n$. For the example, each L${\vee}$ step doubles the number of branches and leaves the other disjunctions in place.

15. Read upwards: R${\to}$, then ${\Box}$R with a new label $y$ and the atom $x R y$, then Sym to add $y R x$, then ${\Diamond}$R at $y$ along $y R x$. The top sequent contains $x : p$ on both sides. For the model, take $w R v$ with $p$ true at $w$ and $v$ without successors.

17. Store both formulas, decide on $a \oplus b$, apply ${\oplus}_1$ and close with $\vdash a^{\perp} \Downarrow a$. For $a \otimes b$ the only positive formula to decide on is $a \otimes b$, and each split of $a^{\perp}$ leaves a premise $\vdash \cdot \Downarrow a$ or $\vdash \cdot \Downarrow b$ with no rule.

22. The only possible last rule is L${\to}$, with left premise $(p \to \bot) \to \bot \Rightarrow p \to \bot$. Invert R${\to}$: then $p, (p \to \bot) \to \bot \Rightarrow \bot$ would be derivable. It is false when $p$ is true.

23. By inversion it is enough to rule out $(p \to q) \to p \Rightarrow p$. Its last rule must be L${\to}$, so $p, (p \to q) \to p \Rightarrow q$ would be derivable. That sequent again needs L${\to}$, whose right premise $p, p \Rightarrow q$ is false when $p$ is true and $q$ false.

24. From $q \Rightarrow q$ and $p \Rightarrow p$, the communication rule gives $p \Rightarrow q \mid q \Rightarrow p$. External weakening of $r \Rightarrow r$ gives $p \Rightarrow q \mid r \Rightarrow r$. Apply the communication rule to these two, with side hypersequent $p \Rightarrow q$, to the components $r \Rightarrow r$ and $q \Rightarrow p$. This gives $p \Rightarrow q \mid q \Rightarrow r \mid r \Rightarrow p$, and R${\to}$, R${\vee}$ and EC finish.

25. A normal, fully expanded term of atomic type $p$ is a variable applied to arguments. With $f : p \to p$ and $x : p$ in the context, it is $x$ or $f N$ with $N$ of type $p$. Distinct normal forms are distinct proofs.

26. For an atom or a negated atom use $\mathsf{ai}{\uparrow}$, and for a unit $\mathsf{t} \wedge \mathsf{f} = \mathsf{f}$ follows from the equations. For $B \wedge C$, write $(B \wedge C) \wedge (\bar{B} \vee \bar{C})$ as $C \wedge (B \wedge (\bar{B} \vee \bar{C}))$; switch inside gives $C \wedge ((B \wedge \bar{B}) \vee \bar{C})$, and a second switch gives $(C \wedge \bar{C}) \vee (B \wedge \bar{B})$. For $B \vee C$ the same two switches turn $\bar{B} \wedge (\bar{C} \wedge (C \vee B))$ into $(\bar{B} \wedge B) \vee (\bar{C} \wedge C)$. Then use the induction hypothesis inside the positive contexts, and $\mathsf{f} \vee \mathsf{f} = \mathsf{f}$.

27. The antecedent is empty and the sequent is not an axiom, so the last rule is R${\vee}$. Now $\Rightarrow \neg p$ fails by inversion and soundness. For $\Rightarrow \neg\neg p$ invert to $\neg p \Rightarrow \bot$, whose last rule must be L${\to}$ with left premise $\neg p \Rightarrow p$, false when $p$ is false.
