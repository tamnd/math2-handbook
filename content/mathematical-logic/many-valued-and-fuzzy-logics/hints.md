1. $\mathrm{Ł}_3$ gives $1$, and $\mathsf{K}_3$ and $\mathrm{B}_3$ give $\tfrac12$. Yes: the value is $\min(1, x + \min(1, 1 - x + y))$ with $x = v(p)$, $y = v(q)$, and $x + \min(1, 1 - x + y) = \min(1 + x, 1 + y) \ge 1$. The same computation shows that it is a tautology of $\mathrm{Ł}_\infty$.

3. In $\mathrm{B}_3$, $v(p \land q) = 1$ forces $v(p) = v(q) = 1$. In $\mathsf{PWK}$, take $v(p) = 0$ and $v(q) = \tfrac12$: the premise has the designated value $\tfrac12$, and the conclusion has $0$.

4. (a) $\mathbf{N}$, (b) $\mathbf{T}$, (c) $\mathbf{T}$. Here $p \land q = \mathbf{F}$ and $\neg q = \mathbf{N}$, so (b) and (c) are designated and (a) is not.

9. $0.3 \le P(p \land q) \le 0.6$ and $0.7 \le P(p \lor q) \le 1$. Both pairs of bounds are reached, by the weights of the four valuations of $(p, q)$.

11. In $\mathrm{Ł}_3$ both sides are $0$ at $p = 0$ and $1$ otherwise. On $[0, 1]$ the value is $1 - x$ on $[0, \tfrac13]$, $2x$ on $[\tfrac13, \tfrac12]$ and $1$ above $\tfrac12$, so the least value is $\tfrac23$, at $p = \tfrac13$.

13. In $\mathsf{K}_3$ the premise is never designated, and in $\mathsf{LP}$ the conclusion always is. In FDE take $v(p) = \mathbf{B}$ and $v(q) = \mathbf{N}$. So the FDE consequence relation is strictly smaller than the intersection of those of $\mathsf{K}_3$ and $\mathsf{LP}$.

15. Try $((p \oplus p) \odot p) \oplus (p \odot p)$. The first term is $\max(0, 3x - 1)$ for $x \le \tfrac12$ and $x$ for $x \ge \tfrac12$; the second is $0$ for $x \le \tfrac12$ and $2x - 1$ above.

19. The degree is $0.9 \odot 0.8 \odot 0.7 = 0.4$, attained by $e(p) = 0.9$, $e(q) = 0.7$, $e(r) = 0.4$. Each axiom of $T$ forces $e(r) \ge e(q) - 0.3 \ge e(p) - 0.5 \ge 0.4$. The minimum rule would claim $0.7$, which this model refutes.

21. (a) Six questions, since $2^5 = 32 < 6 \cdot 6$ and $2^6 = 64 \ge 6 \cdot 7$. (b) Each element in $Q$ keeps its value, and each element outside $Q$ is combined with $\tfrac12$ by $\odot$. The new state is $(1, \tfrac12, \tfrac12, 0, 0, \tfrac12)$, and the weights are $7 + 10 = 17$.

23. (a) $\set{0, \tfrac12, 1}$ is closed under the operations of the five-element chain, so $\mathrm{Ł}_3$ is a submatrix of $\mathrm{Ł}_5$. (b) On the four-element chain, $p \leftrightarrow \neg p$ takes only the values $0$ and $\tfrac23$, and $\tfrac23 \odot \tfrac23 = \tfrac13$, so $k = 3$. At $p = \tfrac12$ the formula $p \leftrightarrow \neg p$ has value $1$, so every power has value $1$.

24. If a valuation gives every formula of $\Gamma$ the value $1$, then no variable of $\Gamma$ has the value $\tfrac12$, so its restriction to these variables is classical. For the converse, give a variable of $\varphi$ that does not occur in $\Gamma$ the value $\tfrac12$. If $\Gamma$ is classically unsatisfiable, no valuation designates all of $\Gamma$, so every $\varphi$ follows.

25. $f(x, x) = x + 1$, so the shift $S$ is a term, and $\min(x, y) = S(S(f(x, y)))$. The map $\sigma(x) = 2 - x$ turns $\max$ into $\min$ and the Post negation $x - 1$ into $S$. Conjugation by $\sigma$ sends terms in Post's connectives to terms in $S$ and $\min$.

26. If $0$ is isolated, an infimum $0$ over values in $V$ must be attained, so some element has $P$-value $0$. If $0$ is a limit of values $v_n > 0$ in $V$, take the domain $\N$ with $P(n) = v_n$: the antecedent has value $1$ and the consequent $0$. So the sentence is not in $\mathrm{G}_{[0, 1]}$.

27. The start weight is $3 \cdot 5 = 15 \le 2^4$. A fixed strategy gives each element a code word, and it works exactly when any two code words differ in at least $3$ places. After a shift, one code word is $0000$; the others then have at least three ones, so any two of them differ in at most $2$ places. With five questions, the code words $00000$, $11100$, $00111$ work.
