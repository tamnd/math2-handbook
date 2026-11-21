1. (a) An instance, and an axiom of $\mathsf{TB}$. (b) An instance, but not an axiom of $\mathsf{TB}$, since the sentence on the right contains $T$. (c) Not an instance: $x = x$ is not a sentence. (d) Not an instance of the schema; it is an axiom of $\mathsf{UTB}$.

3. The phrase has $49$ letters. With "forty" there is no paradox: the phrase has $40$ or more letters, so it is not one of the short definitions it speaks about. "Fifty" also has five letters, so the new phrase has $49 < 50$ letters, and the Berry argument goes through.

4. Four. If $S_i$ is true, every other sentence is false, and then each $S_j$ with $j \neq i$ is false, as it must be, because $S_i$ is true. If all four are false, then each one is true. If two are true, each of them is false. So the assignments are those with exactly one true sentence.

7. $\psi_n$ first gets a value at stage $n$. Its value is $0$ for even $n$ and $1$ for odd $n$: $\psi_0$ is false at every stage, its code enters the anti-extension at stage $1$, so $\psi_1$ is true from stage $1$, and so on.

8. (a) $K_3$ yes, $\mathrm{LP}$ no. (b) Yes in both. (c) $K_3$ yes, $\mathrm{LP}$ no. (d) $K_3$ no, $\mathrm{LP}$ yes. (e) $K_3$ yes, $\mathrm{LP}$ no. The counterexamples in $\mathrm{LP}$ take $v(p) = \mathrm{b}$ and $v(q) = 0$; for (d) in $K_3$ take $v(p) = \mathrm{u}$.

11. Going once round the cycle, the value of claim $1$ is reversed once for each "not true" link. So an assignment exists exactly when the number of such links is even, and then the value of claim $1$ fixes all the others: there are exactly two. With every link "not true", this means $n$ even.

13. (a) and (b) have values at stage $0$, namely $1$ and $0$, by the strong Kleene tables. (c) is ungrounded, since $T(\ulcorner \lambda \urcorner)$ is $\mathrm{u}$ at every stage. (d) has value $0$ from stage $2$. At stage $1$ the anti-extension contains every number that is not a sentence code, so (e) has value $0$ from stage $1$; and the extension contains $\ulcorner 0 = 0 \urcorner$, so (f) has value $1$ from stage $1$.

15. The stages are $\emptyset$, $\set{\beta}$, $\set{\alpha, \beta}$, $\set{\alpha}$, $\emptyset$. On the four subsets of $\set{\alpha, \beta}$ the rule $\rho$ is a single cycle of length four, so from any stage the next four stages contain $\alpha$ twice and omit it twice, and the same for $\beta$. No limit choice can stop this.

17. In a fixed point, $Y_n$ has value $1$ exactly when every $Y_k$ with $k > n$ has value $0$, and value $0$ exactly when some $Y_k$ with $k > n$ has value $1$. Now repeat the classical Yablo argument for the values $1$ and $0$: a sentence with value $1$ leads to a contradiction, and a sentence with value $0$ needs a later one with value $1$.

19. Axiom 9 gives $T(\ulcorner \lambda \vee \neg \lambda \urcorner) \leftrightarrow T(\ulcorner \lambda \urcorner) \vee T(\ulcorner \neg \lambda \urcorner)$. $\mathsf{Compl}$ for $\lambda$ makes the right side true. Under $\mathsf{Cons}$ both disjuncts are false, by the equivalence $T(\ulcorner \lambda \urcorner) \leftrightarrow T(\ulcorner \neg \lambda \urcorner)$. So $\mathsf{KF} + \mathsf{Cons}$ proves $\lambda \vee \neg \lambda$ and calls it untrue.

22. For a finite set of the T-sentences, with indices at most $m$, interpret $T$ by $\set{\ulcorner S_n \urcorner : n \le m}$. Each $S_n$ with $n \le m$ is then true, because $S_{m+1}$ is not in the extension, and so it agrees with $T(\ulcorner S_n \urcorner)$; apply compactness. In an expansion of $\mathcal{N}$, the T-sentences would give an assignment that the argument of Exercise 12 rules out.

23. Under $(\set{\ulcorner \tau \urcorner}, \emptyset)$ the sentence $\tau$ already has value $1$, so the pair lies below its own jump. By monotonicity the iteration then increases, and it reaches a fixed point that keeps $\ulcorner \tau \urcorner$ in the extension. An intrinsic fixed point is compatible with both fixed points, so $\ulcorner \tau \urcorner$ is in neither its extension nor its anti-extension.

24. By the successor rule, $\ulcorner \neg A \urcorner \in S_{\zeta + 1}$ exactly when $\ulcorner A \urcorner \notin S_{\zeta + 1}$. So $B_A$ is true in every successor stage, and its code is in $S_{\zeta + 2}$ for every $\zeta$. For the second part, $\ulcorner \lambda \urcorner$ and $\ulcorner \neg \lambda \urcorner$ are both unstable, so at every limit the limit rule allows both into $S_\eta$; then $B_\lambda$ fails at every limit stage.

25. A proof uses only finitely many T-sentences, for $\varphi_1, \ldots, \varphi_k$. Interpret $T$ in $\mathcal{N}$ by the codes of the true sentences among them. This model satisfies $\mathsf{PA}$ with full induction and those T-sentences, but the general sentence fails for any $\psi$ such that neither $\psi$ nor $\neg \psi$ is in the list.

26. The differences $d_n := v(H(n + 1)) - v(H(n))$ for $1 \le n \le 9999$ add up to $1$, so some $d_n \ge 1/9999$, and that conditional has value $1 - d_n$. Every conditional has value at least $1 - 1/9999$ only if every $d_n \le 1/9999$; since the $9999$ differences add up to $1$, each one is then exactly $1/9999$.
