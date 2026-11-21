1. ◦ Which of these sums in $\R^3$ are direct? (a) The plane $x + y + z = 0$ plus the line $\R(1, -1, 0)$. (b) The plane $x + y + z = 0$ plus the line $\R(1, 0, 0)$. (c) The three lines $\R(1, 0, 0)$, $\R(0, 1, 0)$ and $\R(1, 1, 1)$. For each direct sum, say whether it is all of $\R^3$.

2. ◦ Let $U$ be the plane $x + 2y - z = 0$ in $\R^3$ and $W = \R(1, 0, 0)$. Check that $\R^3 = U \oplus W$, and write $v = (2, 1, 3)$ as $u + w$ with $u \in U$ and $w \in W$.

3. ◦ Show that $P = \begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix}$ is a [projection](/033DA1WE8Y/). Find its image, its kernel and its trace.

4. ◦ Let $U = \R(1, 1, 1)$ in $\R^3$. Which of the cosets $(1, 2, 3) + U$, $(0, 1, 2) + U$ and $(3, 2, 1) + U$ are equal?

5. ◦ Find the dimension of each quotient. (a) $M_3(\R)$ modulo the symmetric matrices. (b) $P_4$, the polynomials of degree at most $4$, modulo $\set{p : p(1) = p(2) = 0}$. (c) $\R^5$ modulo $\R^5$.

6. ◦ Is $0 \to \R \xrightarrow{f} \R^2 \xrightarrow{g} \R \to 0$ exact for $f(t) = (2t, t)$ and $g(x, y) = x - 2y$? And for $f(t) = (t, 2t)$ with the same $g$?

7. ◦ Find the [codimension](/JJCGJ1EGCQ/) of $U = \set{p \in \R[x] : p(0) = p(1) = p(2)}$ in $\R[x]$.

8. ◦ Find the error: "Let $P$ be a projection. From $P^2 = P$ we get $P(P - I) = 0$, so $P = 0$ or $P = I$." Give a projection of $\R^2$ that is neither.

9. • Show that $M_n(\R)$ is the direct sum of the upper triangular matrices (diagonal included) and the strictly lower triangular matrices. Give the dimension of each summand.

10. • Show that the [complements](/0M83V17KHX/) of the plane $z = 0$ in $\R^3$ are exactly the lines $\R(a, b, 1)$ with $(a, b) \in \R^2$, and that different pairs $(a, b)$ give different complements.

11. • Find the matrix of the projection of $\R^3$ onto the plane $x + y + z = 0$ along the line $\R(1, 2, 3)$, and check that its trace is $2$.

12. • Let $P$ and $Q$ be projections on $V$ with $PQ = QP = 0$. Show that $P + Q$ is a projection and that its image is $\operatorname{im} P \oplus \operatorname{im} Q$.

13. • Let $T \colon \R[x] \to \R^3$ be $T(p) = (p(0), p(1), p(2))$. Show that $T$ is surjective, find its kernel, and use the [first isomorphism theorem](/0MTBGVZ4XJ/) to describe $\R[x]/\ker T$. Which polynomials give one representative of each coset?

14. • In $\R^4$ let $U = \set{x_1 + x_2 + x_3 + x_4 = 0}$ and $W = \operatorname{span}\set{e_1, e_2}$. Find $U \cap W$ and $U + W$, and check the [second isomorphism theorem](/0APN65D6Y6/) by computing $\dim U/(U \cap W)$ and $\dim (U + W)/W$.

15. • Let $U$ be a $2$-dimensional subspace of $\F_2^4$. Use the [third isomorphism theorem](/07RB3EMBWW/) and the correspondence of subspaces to count the subspaces of $\F_2^4$ that contain $U$.

16. • Let $H_1 \ne H_2$ be hyperplanes of a vector space $V$, that is, subspaces of codimension $1$. Show that $\operatorname{codim}(H_1 \cap H_2) = 2$.

17. • Let $0 \to V_1 \to V_2 \to V_3 \to V_4 \to 0$ be an [exact sequence](/946YAZNYKX/) with $\dim V_1 = 2$, $\dim V_2 = 5$ and $\dim V_4 = 4$. Find $\dim V_3$ and the rank of the map $V_2 \to V_3$.

18. • Let $V$ be the space of continuous functions $[-1, 1] \to \R$ and $U = \set{f : f(0) = 0}$. Show that $V = U \oplus \R \cdot 1$, where $1$ is the constant function, and that $V/U \cong \R$ through $f + U \mapsto f(0)$.

19. ★ Let $U$ be a $k$-dimensional subspace of $\F_q^n$. Fix one complement $W_0$. Show that the complements of $U$ correspond one to one to the linear maps $W_0 \to U$, and deduce that $U$ has exactly $q^{k(n - k)}$ complements.

20. ★ Show that two projections on a finite-dimensional space are [similar](/0E89HQATM8/) if and only if they have the same rank.

21. ★ Let $V = \R^{\N}$ be the space of real sequences and $U = \R^{(\N)}$ the subspace of sequences with finitely many nonzero terms. Show that $V/U$ is infinite-dimensional.

22. ★ Let $T \colon V \to V$ be linear with $T(U) \subseteq U$, where $V$ is finite-dimensional. Show that $T$ induces a linear map $\bar T$ on $V/U$ with $\bar T(v + U) = T(v) + U$. In a basis of $V$ that extends a basis of $U$, show that the matrix of $T$ is $\begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$, where $A$ is the matrix of $T$ restricted to $U$ and $C$ is the matrix of $\bar T$. Deduce that $\operatorname{tr} T = \operatorname{tr}(T|_U) + \operatorname{tr} \bar T$.

23. ★ Let $U$ be a subspace of codimension $k$ in $\F_q^n$. Show that exactly $(q^k - 1)/(q - 1)$ hyperplanes of $\F_q^n$ contain $U$.
