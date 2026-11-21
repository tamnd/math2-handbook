1. (a), (e) and (f) are linear. (b) sends $0$ to $(1, 0)$. (c) fails homogeneity: $T(2, 2) = (4, 0) \ne 2T(1, 1)$. (d) fails at $T(-1, 0) = (1, 0) \ne -T(1, 0)$.

4. The rank is $1$: the second row is twice the first. The kernel has basis $(1, 1, 0)$, $(-2, 0, 1)$, the image is spanned by $(1, 2)$, and $1 + 2 = 3$.

6. $T(e_1) = \frac12\big(T(1, 1) + T(1, -1)\big) = (2, 0)$ and $T(e_2) = \frac12\big(T(1, 1) - T(1, -1)\big) = (1, 1)$. So $T(x, y) = (2x + y, y)$, with matrix $\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$.

7. No. The values on the basis $(1, 0)$, $(0, 1)$ fix $T$, and then $T(1, 1) = (1, 1) + (2, 0) = (3, 1) \ne (3, 2)$.

10. A polynomial with $p(0) = p(1) = 0$ is divisible by $x(x - 1)$, so $\ker T$ has basis $x^2 - x$, $x^3 - x^2$. The image contains $T(1) = (1, 1)$ and $T(x) = (0, 1)$, so $T$ is onto. Then $2 + 2 = 4 = \dim P_3(\R)$.

15. One answer is $T(v) = v - \frac{x + y + z}{3}(1, 1, 1)$ for $v = (x, y, z)$, with matrix $I - \frac13 J$, where $J$ is the matrix of ones. Its values have coordinate sum $0$, it fixes the plane, and it kills $(1, 1, 1)$.

16. If $w = T(v)$, then $T(w) = T(T(v)) = 0$. So $\operatorname{rank} T \le \operatorname{nullity} T = n - \operatorname{rank} T$. For $n = 2$, take $T(x, y) = (y, 0)$.

17. On $P_n(\R)$, $D$ kills the constants and its image is $P_{n-1}(\R)$, so it is neither injective nor surjective, and its rank is $n$. On $\R[x]$, $D$ is surjective (every polynomial has an antiderivative) but not injective. The theorem needs finite dimension.

22. The image of $S \circ T$ is $S(\operatorname{im} T)$, which lies in $\operatorname{im} S$ and has dimension at most $\dim \operatorname{im} T$. For the lower bound, apply rank-nullity to $S$ restricted to $\operatorname{im} T$: its kernel lies in $\ker S$, so $\operatorname{rank}(S \circ T) \ge \operatorname{rank} T - (\dim V - \operatorname{rank} S)$.

23. Choose a basis $u_{r+1}, \dots, u_n$ of $\ker T$ and extend it by $u_1, \dots, u_r$ to a basis of $V$. Then $T(u_1), \dots, T(u_r)$ are a basis of $\operatorname{im} T$; extend them to a basis of $W$.

24. Pick a basis containing a sequence $b_1, b_2, \dots$ of distinct vectors, and fix the other basis vectors. The map $b_k \mapsto b_{k+1}$ is injective and misses $b_1$; the map $b_1 \mapsto 0$, $b_{k+1} \mapsto b_k$ is surjective with $b_1$ in its kernel.

25. $\operatorname{End}(V)$ has dimension $n^2$, so the $n^2 + 1$ maps $\mathrm{id}, T, T^2, \dots, T^{n^2}$ are linearly dependent. A dependence relation is a nonzero polynomial in $T$ equal to $0$.

26. Additivity gives $f(0) = 0$, $f(-v) = -f(v)$ and $f(kv) = kf(v)$ for integers $k$. For $q = k/l$, $l\,f(qv) = f(kv) = kf(v)$, so $f(qv) = qf(v)$.
