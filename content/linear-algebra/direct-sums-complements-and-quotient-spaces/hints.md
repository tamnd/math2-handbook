1. $U$ is the plane $x + y - z = 0$, and $(1, 1, 1)$ is not on it, so $U \cap W = \set{0}$ and the dimensions add up to $3$. Since $2 + 3 - 4 = 1$ and $1 + 1 - 1 = 1$, take $w = (1, 1, 1)$: $(2, 3, 4) = (1, 2, 3) + (1, 1, 1)$.

3. $A^2 = A$, with image $\R(1, 1)$ and kernel $\R(1, 2)$. $B^2 = 2B \ne B$, so $B$ is not a projection. $C^2 = C$, with image $\R(1, 3)$ and kernel $\R(0, 1)$.

5. Both quotients have dimension $\dim M_3(\R)$ minus the dimension of the subspace: $9 - 6 = 3$ and $9 - 8 = 1$.

6. The representatives $(0, 0)$ and $(1, 2)$ give the same coset but the values $0$ and $3$. The form $\ell$ passes to the quotient exactly when $\ell(1, 2) = 0$, so $\ell(x, y) = c(2x - y)$ for some $c \in \R$.

8. The map $p \mapsto (p(1), p'(1))$ from $P_4$ to $\R^2$ is onto (it sends $1$ to $(1, 0)$ and $x - 1$ to $(0, 1)$) and has kernel $U$. So $\operatorname{codim} U = 2$ and $\dim U = 5 - 2 = 3$.

9. Write $v = a(1, 2) + b(1, -1)$ and keep $a(1, 2)$. Then $P = \frac{1}{3}\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ and $I - P = \frac{1}{3}\begin{pmatrix} 2 & -1 \\ -2 & 1 \end{pmatrix}$.

11. $(PQ)^2 = PQPQ = PPQQ = PQ$. A vector in the image of $PQ$ is fixed by $P$ and by $Q$, since $P(PQv) = PQv$ and $Q(PQv) = PQQv = PQv$; conversely $PQ$ fixes every vector of $\operatorname{im} P \cap \operatorname{im} Q$. For the example, $P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $Q = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$ are projections, and $QP = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ squares to $0$.

13. The map is onto, since $2 - x \mapsto (1, 0)$ and $x - 1 \mapsto (0, 1)$, and its kernel is $U$. The class of $x^3$ is the linear polynomial with the same values at $1$ and $2$, namely $7x - 6$; indeed $x^3 - 7x + 6 = (x - 1)(x - 2)(x + 3)$.

14. $U$ is $\set{x_1 = x_3, x_2 = x_4}$, so $U \cap W = \R(1, 1, 1, 1)$, and $U + W = \set{x_2 = x_4}$ has dimension $3$. Both quotients have dimension $1$.

16. $s(a, b) = (0, -a, -b)$ works, since $g(0, -a, -b) = (a, b)$; its image is the plane $x = 0$. Then $(1, 1, 1) = (1, 2, 3) + (0, -1, -2)$, so $t = 1$ and $(a, b) = (1, 2)$.

20. Expand $(P + Q)^2 = P + Q + PQ + QP$, so $P + Q$ is a projection exactly when $PQ + QP = 0$. Multiply $PQ = -QP$ on the left by $P$, and then on the right by $P$, to get $PQ = -PQP = QP$; with $PQ = -QP$ and $2 \ne 0$ this gives $PQ = 0$. Over $\mathbb{F}_2$, take $P = Q = I$ on $\mathbb{F}_2$: then $P + Q = 0$ is a projection but $PQ = I$.

21. If $\ker T = \ker T^2$ and $v = T(w) \in \ker T$, then $T^2 w = 0$, so $w \in \ker T$ and $v = 0$; the dimensions add up by rank-nullity. Conversely, if $T^2 v = 0$ then $Tv \in \ker T \cap \operatorname{im} T = \set{0}$. The nilpotent matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has $\ker T = \operatorname{im} T = \R e_1$.

22. $f$ is injective because its first component is the identity, and $g$ is onto by the definition of $U + W$. The pair $(u, w)$ lies in $\ker g$ exactly when $w = -u$, and then $u \in U \cap W$. Take dimensions in the exact sequence.

23. A complement $W$ meets $U$ only in $0$ and has dimension $n - k$, so the projection onto $W_0$ along $U$ maps $W$ isomorphically onto $W_0$. Hence $W = \set{w + A w : w \in W_0}$ for exactly one linear map $A \colon W_0 \to U$, and every $A$ gives a complement. There are $q^{k(n - k)}$ such maps.

24. Exactness at $V$ and at $W$ restates the definitions of kernel and of the quotient map. The alternating sum of the dimensions in a finite exact sequence is $0$; this follows from rank-nullity at each map.
