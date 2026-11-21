1. (a) Commutativity and $x \le 1$ hold; $x \le x \cdot x$ fails at $x = 1/2$, where $x \cdot x = 0$. This models exchange and weakening without contraction, as in affine logic. (b) Only commutativity holds: $x \le 0$ fails at $x = 1$, and $x \le 2x$ fails at $x = -1$. This models exchange alone. (c) All three hold, since $x \wedge y = y \wedge x$, $x \le \top$ and $x = x \wedge x$; this is intuitionistic logic.

2. (a) Yes. (b) No: $np/n$ looks for its $n$ on the right, and there is nothing there. (c) Yes. (d) No: $(np \backslash s)/np$ takes the $np$ on its right and gives $np \backslash s$, which then needs an $np$ on its left, and there is none.

5. Four axiom links, since a cut-free proof net with $k$ tensor links has $k + 1$ axiom links, and so eight atom occurrences. There are $2^2 = 4$ switchings. The graph has $8 + 5 = 13$ vertices, so each correction graph, being a tree, has $12$ edges: $4$ axiom edges, $6$ tensor edges and $2$ par edges.

6. For a group with $\bot = \set{0}$, $\set{x}^\perp = \set{-x}$, a set with two or more elements has $\emptyset$ as its orthogonal, and $\emptyset^\perp = \Z/3$. So the facts are $\emptyset$, $\set{0}$, $\set{1}$, $\set{2}$ and $\Z/3$. The sets $\set{0, 1}$, $\set{0, 2}$ and $\set{1, 2}$ are not facts; each has $\Z/3$ as its double orthogonal.

8. (c) and (e) pass; (a), (b) and (d) fail, since antecedent and consequent have no variable in common. Passing is not enough: (e) is not a theorem of $\mathbf{R}$, by the two-point Routley–Meyer model.

10. For the first sequent, $A, A \backslash B \Rightarrow B$ and then ${\backslash}\mathrm{L}$ with $B \backslash C$ give $A, A \backslash B, B \backslash C \Rightarrow C$, and ${\backslash}\mathrm{R}$ ends the derivation. For the second, run the cut-free search on $a, b \backslash c, a \backslash b \Rightarrow c$: the formula left of $b \backslash c$ is $a$, not $b$, and no nonempty block left of $a \backslash b$ derives $a$.

13. (a) Affine only. (b) Neither: the valuation $v(a) = v(b) = 1/2$ gives the sum $1/2 + 0 < 1$. (c) Both, by the rule for $\oplus$ on an axiom. (d) Affine only: weakening discards one $a$, and a cut-free MALL search ends in $\vdash a^\perp, a^\perp, a$, which has three atoms.

15. Compute $(p^{\perp *})^\perp = \set{1}$ and $((p \otimes p)^*)^\perp = \set{2}^\perp = \set{1}$. The first sequent gives $1 + 1 = 2 \notin \bot$, so it is not valid; the second gives $1 + 1 + 1 = 0 \in \bot$, so it is valid. It is still not derivable: in $\Z/2$ with $\bot = \set{0}$ and $p^* = \set{1}$ the sum is $1 \notin \bot$.

18. $T_0$ sends $!!p \multimap !p$ to $\neg p_2 \vee p_1$, which fails at $p_2$ true and $p_1$ false. In ELL, functorial promotion on $\vdash p^\perp, p$ gives $\vdash ?p^\perp, !p$ twice, the tensor rule and $?C$ give $\vdash ?p^\perp, {!p} \otimes {!p}$. In full linear logic, two derelictions and one promotion take $\vdash p^\perp, p$ to $\vdash ??p^\perp, !p$.

20. (d) and (e) hold. (a) fails with $p$ true at $0$ only and $q$ true nowhere. (b) fails with $p$ true at both points and $q$ true at $0$ only, since then $q \rightarrow q$ fails at $1$ and $R011$ holds. (c) fails with the valuation of (a); this is disjunctive syllogism.

23. For the first, join the axioms on $A$ and $B$ by $\otimes$, then join $B^\perp$ with $C^\perp$ by $\otimes$, and finish with three $\mathbin{\wp}$ rules. For the converse, each atom occurs once with its dual, so there is only one proof structure. The switching that keeps $a^\perp$ in $a^\perp \mathbin{\wp} b^\perp$ and $c$ in $b \mathbin{\wp} c$ gives a cycle through $a$, $a^\perp$, $c^\perp$ and $c$, and leaves $b - b^\perp$ apart.

24. $!\mathbf{Bool}$ has $6$ cliques, since $\set{t}$ and $\set{f}$ do not cohere and $\emptyset$ coheres with both. $!\mathbf{Bool} \multimap \mathbf{Bool}$ has $11$. They match the $11$ stable functions: the two constant functions with value $\set{t}$ or $\set{f}$, and the $9$ functions with $F(\emptyset) = \emptyset$, which choose $F(\set{t})$ and $F(\set{f})$ freely.

25. Tokens $(t_1, b)$ and $(t_2, b')$ have coherent inputs, so the outputs must cohere and then be equal, and equal outputs from coherent but distinct inputs are forbidden. So each nonempty clique lies in one component and is one of the $8$ nonempty cliques of $\mathbf{Bool} \multimap \mathbf{Bool}$, which gives $1 + 8 + 8 = 17$. A linear function reads at most one argument, and the left-sequential and has $\set{t_1, t_2}$ in its trace, so it is stable but not linear.

26. The truth set of any formula is hereditary, so it is $\emptyset$, $\set{0}$ or $W$, and the truth of $A \rightarrow (A \rightarrow A)$ at $0$ depends only on this set. Check the three cases. So the model cannot show that mingle is not a theorem of $\mathbf{R}$.

27. Take $v(p) = v(q) = v(r) = 1/2$. The negated antecedent $(p \otimes q^\perp) \mathbin{\wp} (p \otimes r^\perp)$ has value $0$ and $p^\perp \mathbin{\wp} (q \otimes r)$ has value $1/2$, so the sequent is not good. For the additive version, the rule for $\mathbin{\&}$ gives both premises the same context, so the one hypothesis $p$ serves both branches.
