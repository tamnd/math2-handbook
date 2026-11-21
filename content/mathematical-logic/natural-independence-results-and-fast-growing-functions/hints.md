1. $G_1 = 2^{2^1} + 1 = 5$, $G_2 = 3^{3^1} = 27$, $G_3 = 3 \cdot 4^3 + 3 \cdot 4^2 + 3 \cdot 4 + 3 = 255$ and $G_4 = 3 \cdot 5^3 + 3 \cdot 5^2 + 3 \cdot 5 + 2 = 467$. The ordinals are $\omega^\omega + 1 > \omega^\omega > \omega^3 \cdot 3 + \omega^2 \cdot 3 + \omega \cdot 3 + 3 > \omega^3 \cdot 3 + \omega^2 \cdot 3 + \omega \cdot 3 + 2$.

3. The ordinal is $\omega^2 + 1$, with $5$ nodes. After the cut, the root has the head, $p$ with one head, and three copies of $p$ with one head each. The ordinal is $\omega \cdot 4 + 1$, and there are $10$ nodes.

4. $L(10) = 5$, through $10, 1, 000, 00, 0$. $L(01) = 4$, through $01, 000, 00, 0$. The worm sequence of $2$ starts $2, 11, 101010, 10101, 101000000$.

6. (a) No: $f(\set{1, 3}) = 2 \ge 1$. (b) $f(s) < \min s$ when $0 \notin s$, and $f$ depends only on $\min s$. (c) No: on $\set{x, y, z}$ with $1 \le x < y < z$ the pair $\set{y, z}$ has value $y - 1 \ne x - 1$. The homogeneous $3$-sets are exactly the sets $\set{0, 1, z}$.

7. $H_{\omega^2 + \omega + 2}(3) = H_{\omega^2 + \omega}(5) = H_{\omega^2}(10) = 2^{10} \cdot 10 = 10240$. The substitution rule gives $g_{\omega^2 + \omega + 2}(3) = 9 + 3 + 2 = 14$. Also $f_2(3) = 2^3 \cdot 3 = 24$ and $f_3(1) = f_2(1) = 2$.

9. (a) No: it is a finite conjunction of true $\Sigma_1$ sentences, each provable in $\mathsf{PA}$ by running the sequence. (b) Yes. (c) No: it codes provability. (d) No: it is a statement about infinite sequences, not an arithmetic sentence. (e) Yes.

10. The ordinals are $\omega^\omega$, then $\omega^2$, $\omega \cdot 3$ and $\omega \cdot 2 + 4$ after steps $1$ to $3$. They reach $\omega \cdot 2$ after step $7$, $\omega + 9$ after step $8$, $\omega$ after step $17$ and $19$ after step $18$, so the battle ends at step $18 + 19 = 37$.

16. On $\set{1, \dots, 5}$ the values $f(\set{2, y})$ with $y = 3, 4, 5$ lie in $\set{0, 1}$, so two agree, say for $y = a, b$, and $\set{1, 2, a, b}$ is min-homogeneous. For $m = 5$, let $f(\set{0, y}) = y$, $f(\set{2, 3}) = 0$ and $f(\set{2, 4}) = 1$. Every $4$-set that contains $0$ fails, and so does $\set{1, 2, 3, 4}$.

17. The least $m$ is $7$, with the bad sequence $K_2$, four isolated vertices, three, two, one, and the empty graph. If $G_1 = K_2$, every later graph has no edge, and edgeless graphs must lose vertices at each step. Every other choice of $G_1$ allows at most $5$ graphs.

20. The tree $T_1$ needs a path of $4$ vertices, and $T_2$ needs a vertex with $4$ children; no later tree has either. $T_3$ needs a vertex with three children one of which has two children, and $T_4$ needs a vertex with three children that each have a child. So the least $m$ is at least $6$; a full search shows that it is exactly $6$.

21. Order the colour classes by their least elements, and let $t_i$ be the number of points in the first $i$ classes. The least element of class $i + 1$ is at most $t_i + 1$. If no class is large with at least $m$ elements, class $i + 1$ has at most $\max(m - 1, t_i)$ points, so $t_{i+1} \le t_i + \max(m - 1, t_i)$ and $t_k \le (m - 1) 2^{k-1}$. Build a colouring that meets the bound with classes of sizes $m - 1, m - 1, 2m - 2, 4m - 4, \dots$.

22. Split by $T_1$, which has at most $3$ vertices. A single vertex or a single edge as $T_1$ forces a short sequence. If $T_1$ is the path with $3$ vertices, all later trees are stars, which must lose leaves; if $T_1$ is the root with two children, all later trees are paths, which must get shorter. The second case gives the cherry and then the paths with $4, 3, 2, 1$ vertices.

23. If the head is $0$, the last summand $\omega^0$ is removed. If the head is $1$, the last block of $r_t$ ones is replaced by $k + 1$ blocks of $r_t - 1$ ones and an empty block, so $\omega^{r_t}$ becomes $\omega^{r_t - 1} \cdot (k + 1) + 1$. Ordinal addition is strictly increasing in its right argument, so the ordinal decreases.

24. If $I$ is closed under squaring and $a \in I < b$, then $a^{2^c} \in I$ for each standard $c$, so $Y(a, b)$ is non-standard. Conversely, if $Y(a, b)$ is non-standard, the set of $x$ below some $a^{2^c}$ with $c$ standard is a cut closed under squaring that contains $a$ and omits $b$. For a non-standard $c$, $Y(c, c^c)$ is non-standard, but every model of $\mathsf{PA}$ that contains $c$ contains $c^c$.

25. Each $f_n$ has a primitive recursive definition, so it is provably total in $\mathrm{I}\Sigma_1$ by the theorem of Parsons and Mints. The map $(n, x) \mapsto f_n(x)$ eventually dominates every primitive recursive function along the diagonal $n = x$, so it is not provably total there. In $\mathsf{PA}$ prove $\forall x\, \exists y\; f_n(x) = y$ by induction on $n$; the formula is $\Pi_2$.
