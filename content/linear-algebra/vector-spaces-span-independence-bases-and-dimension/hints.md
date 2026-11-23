1. The map $v \mapsto v - 3$ carries the new operations to the usual ones, so every axiom follows from the axiom for $\R$. The zero vector is $3$, and the negative of $5$ is $1$, since $5 \oplus 1 = 3$.

4. $(3, 1, 5) = 2 v_1 + v_2$. The vector $(1, 2, 4)$ is not in the span: the first two coordinates force $-v_1 + 2 v_2 = (1, 2, 0)$.

5. (a) Dependent: $2 (1, 2, 0) - 3 (0, 1, 3) - (2, 1, -9) = 0$. (b) Dependent: the four vectors add up to $0$.

7. (a) $6$. (b) $8$. (c) $3$. (d) $12$.

10. The pivot columns are the first, third and fifth, so $v_1, v_3, v_5$ is a basis. Also $v_2 = 2 v_1$ and $v_4 = v_1 - v_3$.

12. $\dim U = 3$. A vector $(a, a, b, b)$ of $W$ lies in $U$ exactly when $b = 0$, so $U \cap W$ is spanned by $(1, 1, 0, 0)$. Then $\dim(U + W) = 3 + 2 - 1 = 4$ and $U + W = \R^4$.

14. The determinant is $1 + t^3$, so all $t \ne -1$.

18. The determinant of the coefficient matrix is $1 - c$, so all $c \ne 1$. For $c = 1$, the alternating sum of the four polynomials is $0$.

21. Writing $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the condition gives $c = 0$ and $a = d$. Dimension $2$, basis $I$ and $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

22. (a) $27$. (b) $26 / 2 = 13$. (c) $26 \cdot 24 \cdot 18 = 11232$.

23. Suppose the union is $V$ with $n$ minimal. Take $u \in U_1$ outside the other $U_i$ and $v \notin U_1$. None of the $\abs{F}$ vectors $v + tu$, $t \in F$, lies in $U_1$, and each $U_i$ with $i \ge 2$ contains at most one of them, since two would put $u$ in $U_i$. For sharpness, take the $q + 1$ lines through $0$ of $\F_q^2$.

24. Clear denominators to get integers $a_i$ with $\sum a_i \log p_i = 0$, so $\prod p_i^{a_i} = 1$. Move the negative exponents to the other side and use unique factorization. Since there are infinitely many primes, no finite family spans $\R$ over $\Q$.

25. There are $15 \cdot 14$ ordered pairs of independent vectors, and each plane has $3 \cdot 2$ ordered bases, so the answer is $35$. In general the count is $\frac{(q^n - 1)(q^n - q) \cdots (q^n - q^{k-1})}{(q^k - 1)(q^k - q) \cdots (q^k - q^{k-1})}$.

26. If $k < n$, the proper subspaces $U$ and $W$ do not cover $V$, so there is a $v$ outside both. Replace $U$, $W$ by $U + Fv$, $W + Fv$, which have dimension $k + 1$, and repeat. The chosen vectors $v_1, \ldots, v_{n-k}$ span $X$, and $\dim(U + X) = n$ gives $U \cap X = \set{0}$ by Grassmann's formula.

27. In a relation $\sum c_i \abs{x - a_i} = 0$ with distinct $a_i$, every term except the $i$-th is differentiable at $a_i$, and $\abs{x - a_i}$ is not, so $c_i = 0$. The $f_a$ are continuous. In a space with a countable basis every independent family extends to a basis, and by the dimension theorem all bases are countable, so no uncountable independent family exists there.
