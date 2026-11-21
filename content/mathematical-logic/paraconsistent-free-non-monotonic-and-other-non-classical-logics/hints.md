1. K3 is paracomplete and not paraconsistent. LP is paraconsistent and not paracomplete. FDE is both. Intuitionistic logic is paracomplete and not paraconsistent. $D_2$ is paraconsistent, and not paracomplete, since $\Diamond(A \lor \neg A)$ is valid in S5.

2. In K3 both steps are valid, and K3 is explosive. In LP disjunctive syllogism fails: take $v(A) = \mathsf{B}$ and $v(B) = \mathsf{F}$. In $D_2$ the first step is a classical inference from one premise and is valid, while disjunctive syllogism fails, because $A \lor B$ and $\neg A$ can hold at different worlds.

3. Both values are $\mathsf{B}$. They are designated in LP and not in K3. So $p \supset p$ is not a K3 tautology. In fact K3 has no tautologies at all, since the valuation that gives every atom the value $\mathsf{B}$ gives every formula the value $\mathsf{B}$.

4. Strong Kleene with $v(p) = \mathsf{T}$: $\mathsf{T}$, undefined, undefined. Strong Kleene with $v(p) = \mathsf{F}$: undefined, $\mathsf{F}$, $\mathsf{T}$. Weak Kleene: all six values are undefined.

5. (b), (d) and (e). Formulas (a) and (c) fail when $t$ denotes nothing in the inner domain. Formula (e) is one direction of Hintikka's law $E!t \leftrightarrow \exists x\, (x = t)$.

6. (a) Cautious Monotony, which is in $\mathbf{P}$. (b) Right Weakening, which is in $\mathbf{P}$. (c) Monotony, which is not in $\mathbf{P}$ and fails in most preferential models. Penguins are the standard counterexample.

9. (a) Computable: on input $m$, move $m^2$. (b) Not computable: whatever $n$ the machine chooses, an environment that waits for it and then moves $n + 1$ wins. (c) Not computable: a winning machine would decide $h$. (d) Computable with no moves, since after the input $m$ the elementary game $\exists y\, (h(m) \leftrightarrow y = 1)$ is true.

10. In LP the conclusion is designated under every valuation. In K3 the premise is never designated. In FDE take $p$ both true and false and $q$ neither: the premise is both, so designated, and the conclusion is neither. So FDE validates strictly fewer inferences than the intersection of LP and K3.

12. (a) If disjunctive syllogism held, then $A, \neg A \vdash A \lor B$ and $A \lor B, \neg A \vdash B$ would give $A, \neg A \vdash B$, so $C_1$ would be explosive. But $C_1$ is paraconsistent. (b) In the case $A$, gentle explosion $A^\circ, A, \neg A \vdash B$ gives $B$, and in the case $B$ there is nothing to prove.

14. The only minimal Dab-consequence is $p \land \neg p$, so $p$ is the only unreliable atom. The formula $s$ is derived on the condition $\set{r \land \neg r}$, which stays reliable, so $s$ is finally derivable. The formula $q$ needs the condition $\set{p \land \neg p}$, so the line is marked and $q$ is not finally derivable.

23. The induction step uses that $\neg$, $\min$ and $\max$ respect $\sqsubseteq$: if one argument moves to $\mathsf{B}$, the value either stays or becomes $\mathsf{B}$. Every LP valuation $w$ lies above a classical valuation $v$: put $v(p) = w(p)$ when $w(p) \neq \mathsf{B}$, and anything otherwise. If $\varphi$ is a tautology, then $v(\varphi) = \mathsf{T}$, so $w(\varphi) \in \set{\mathsf{T}, \mathsf{B}}$.

24. The minimal Dab-consequence is $(p \land \neg p) \lor (q \land \neg q)$, so both $p$ and $q$ are unreliable. Show that $r$ is not a CLuN consequence of $\Gamma$, so under reliability it cannot be derived on any condition that avoids both abnormalities. The minimally abnormal models make exactly one of the two abnormalities true. If only $p \land \neg p$ holds, then $q$ is false, and $q \lor r$ gives $r$. If only $q \land \neg q$ holds, then $p$ is false, and $p \lor r$ gives $r$.

25. If $E$ is inconsistent, then $\neg\theta \in E$ for every justification $\theta$, so no default applies when $\Gamma(E)$ is built. So $E = \Gamma(E)$ is the deductive closure of $W$, and $W$ is inconsistent. For the converse, every extension contains $W$.

26. Every minimal $\alpha$-state satisfies $\beta$, so it is an $\alpha \land \beta$-state. Let $s$ be a minimal $\alpha \land \beta$-state. If $s$ were not minimal among the $\alpha$-states, finiteness would give a minimal $\alpha$-state $t \prec s$. Then $t$ satisfies $\beta$, which contradicts the minimality of $s$. So $s$ is a minimal $\alpha$-state and satisfies $\gamma$.

27. Take three distinct lines in one plane $\pi$. Any two of them meet in $0$ and join to $\pi$. If $h(\pi) = 1$, exactly one line of each pair gets the value $1$, which is impossible for three lines. So $h(\pi) = 0$ for every plane. But two distinct planes join to $\R^3$, and then $\max(0, 0) = 1$, a contradiction.
