1. (a) Not direct: $(1, -1, 0)$ lies in the plane. (b) Direct, and the sum is $\R^3$, since $1 + 0 + 0 \ne 0$ and the dimensions add up to $3$. (c) Direct, and the sum is $\R^3$: the three vectors are independent, since the matrix with columns $(1,0,0)$, $(0,1,0)$, $(1,1,1)$ has determinant $1$.

3. $P^2 = P$ by direct multiplication. The image is $\R(1, 1)$, the kernel is $\R(1, 2)$ and the trace is $1$, the rank.

5. (a) $9 - 6 = 3$. (b) The subspace has dimension $3$, so the quotient has dimension $5 - 3 = 2$. (c) $0$.

6. The first is exact: $f$ is injective, $g$ is surjective, and $\ker g = \R(2, 1) = \operatorname{im} f$. The second is not, since $g(f(1)) = 1 - 4 = -3 \ne 0$.

7. $2$. The map $p \mapsto (p(1) - p(0), p(2) - p(1))$ from $\R[x]$ to $\R^2$ has kernel $U$ and is surjective (try $p = x$ and $p = x^2$), so $\R[x]/U \cong \R^2$.

8. Matrices can multiply to $0$ without either factor being $0$. The matrix $\operatorname{diag}(1, 0)$ is a projection that is neither $0$ nor $I$.

11. Write $v = u + t(1, 2, 3)$ with $u$ in the plane. Applying $x + y + z$ gives $t = (x + y + z)/6$, so $P = I - \frac16 \begin{pmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{pmatrix}$.

13. Lagrange interpolation gives surjectivity, and $\ker T$ is the set of multiples of $x(x - 1)(x - 2)$. So $\R[x]/\ker T \cong \R^3$, and each coset contains exactly one polynomial of degree at most $2$, the remainder on division by $x(x - 1)(x - 2)$.

15. They correspond to the subspaces of $\F_2^4/U \cong \F_2^2$: the zero space, three lines and the whole space. So there are $5$.

19. A complement $W$ is the graph $\set{w + \varphi(w) : w \in W_0}$ of a unique linear $\varphi \colon W_0 \to U$: project $W$ onto $W_0$ along $U$. There are $q^{k(n-k)}$ linear maps from a space of dimension $n - k$ to one of dimension $k$.

20. Choose a basis of $\operatorname{im} P$ and a basis of $\ker P$. Together they form a basis of $V$ in which $P$ has matrix $\operatorname{diag}(I_r, 0)$, where $r$ is the rank.

21. Split $\N$ into infinitely many disjoint infinite sets $A_1, A_2, \ldots$, for instance by the power of $2$ dividing $n + 1$. The cosets of the indicator sequences of the $A_k$ are independent, because a nonzero finite combination of the indicators is nonzero at infinitely many places.

22. $\bar T$ is well defined by the universal property applied to $\pi \circ T$, which vanishes on $U$. The first columns are $T$ of the basis of $U$, which lie in $U$, and the images of the last basis vectors in $V/U$ give $C$.

23. Hyperplanes containing $U$ correspond to hyperplanes of $V/U \cong \F_q^k$, that is, to the kernels of nonzero linear forms on $\F_q^k$, taken up to a nonzero scalar. There are $(q^k - 1)/(q - 1)$ of them.
