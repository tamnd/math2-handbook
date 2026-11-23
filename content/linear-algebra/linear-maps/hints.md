1. (a), (d) and (e) are linear. (b) is not, since $T(0) \ne 0$. (c) is not, since $T(-1, 0) \ne -T(1, 0)$. (f) is not, since $\det(2I) = 4 \ne 2 \det I$.

4. $\ker T$ is spanned by $(1, 1, 1)$. The image is the plane $x + y + z = 0$: every column has coordinate sum $0$, and the rank is $2$.

5. (a) Injective. (b) Injective: if $p \ne 0$ then $p + p'$ has the same degree as $p$. (c) Not injective, since $\dim P_2 = 3 > 2$. (d) Not injective: $A (1, -2, 1)^T = 0$.

6. (a) Rank $3$, nullity $2$. (b) Rank $1$, nullity $3$, the kernel being the symmetric matrices. (c) Rank $2$, nullity $2$. (d) Rank $2$, nullity $2$, since the third row is the sum of the first two.

10. $\ker T$ has basis $(1, -1, 1, 0)$, $(-1, -1, 0, 1)$. The first two columns are the pivot columns, so $\operatorname{im} T$ has basis $(1, 0, 1)$, $(1, 1, 2)$ and equation $z = x + y$. Then $2 + 2 = 4$.

11. $T(1) = (1, 0)$ and $T(x - 1) = (0, 1)$, so $T$ is surjective and the nullity is $4 - 2 = 2$. A basis of the kernel is $(x - 1)^2$, $x(x - 1)^2$: the kernel is the set of $p \in P_3$ divisible by $(x - 1)^2$.

13. A subspace can avoid $e_1$, $e_2$, $e_3$ and still be nonzero. For $\begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ the columns are nonzero and $(1, -1, 0)$ is in the kernel.

15. $T(T(v)) = 0$ puts $T(v)$ in $\ker T$, so $\operatorname{rank} T \le \dim \ker T = n - \operatorname{rank} T$. Example: $T(x_1, x_2, x_3, x_4) = (x_3, x_4, 0, 0)$.

20. $T^2(x, y) = (y, -x - y)$ and $T^3(x, y) = (-x, -y)$. From $T \circ (-T^2) = -T^3 = \mathrm{id}$ and $(-T^2) \circ T = \mathrm{id}$.

21. (a) $\C$-linear. (b) Antilinear. (c) $\R$-linear and neither: $T(i) = -i$, while $i T(1) = 3i$ and $-i T(1) = -3i$. (d) None: $(2z)^2 \ne 2 z^2$.

23. $\operatorname{End}(V)$ has dimension $n^2$, so the $n^2 + 1$ maps $\mathrm{id}, T, T^2, \ldots, T^{n^2}$ are dependent.

24. Additivity gives $f(kv) = k f(v)$ for integers $k$, then $q f(\tfrac{p}{q} v) = f(pv) = p f(v)$. Over $\R$ the argument reaches only rational scalars, and a Hamel basis of $\R$ over $\Q$ gives additive maps $\R \to \R$ that are not $\R$-linear.

25. For $i \ne j$, $\varphi(E_{ij}) = \varphi(E_{ii} E_{ij}) = \varphi(E_{ij} E_{ii}) = \varphi(0) = 0$. Also $\varphi(E_{ii}) = \varphi(E_{ij} E_{ji}) = \varphi(E_{ji} E_{ij}) = \varphi(E_{jj})$. Take $c = \varphi(E_{11})$.

26. Take a basis of $V$ whose first $k$ vectors are a basis of $U$. In this basis the condition says that the lower left $(n - k) \times k$ block of the matrix is $0$.

27. All columns are multiples of one nonzero column $u$; let $w_j$ be the multiple for column $j$. Then $A^2 = u (w^T u) w^T$ and $w^T u = \operatorname{tr} A$. For the example, $A^2 = 4A$ and $\operatorname{tr} A = 4$.
