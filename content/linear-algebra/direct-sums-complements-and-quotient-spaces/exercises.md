1. ◦ Let $U = \operatorname{span}\set{(1, 0, 1), (0, 1, 1)}$ and $W = \R(1, 1, 1)$ in $\R^3$. Show that $\R^3 = U \oplus W$ and write $(2, 3, 4)$ as $u + w$ with $u \in U$ and $w \in W$.

2. ◦ Find the error: "If $U$ and $W$ are subspaces of a finite-dimensional space $V$ with $\dim U + \dim W = \dim V$, then $V = U \oplus W$." Give a counterexample in $\R^2$.

3. ◦ Decide which of the matrices
$$A = \begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 0 \\ 3 & 0 \end{pmatrix}$$
are [projections](/033DA1WE8Y/). For each projection, give its image and its kernel.

4. ◦ Let $U = \R(1, 1, 1)$ in $\R^3$. Decide whether $(1, 2, 3) + U = (3, 4, 5) + U$ and whether $(1, 2, 3) + U = (0, 0, 1) + U$.

5. ◦ Find $\dim M_3(\R)/S$, where $S$ is the subspace of symmetric matrices, and $\dim M_3(\R)/Z$, where $Z$ is the subspace of matrices of trace $0$.

6. ◦ Find the error: "Let $U = \R(1, 2)$ in $\R^2$. The rule $(x, y) + U \mapsto x + y$ is a linear map $\R^2/U \to \R$." Then describe all linear forms $\ell$ on $\R^2$ for which $(x, y) + U \mapsto \ell(x, y)$ is well defined.

7. ◦ Let $f \colon \R \to \R^2$, $f(t) = (t, t)$. Decide whether $0 \to \R \xrightarrow{f} \R^2 \xrightarrow{g} \R \to 0$ is exact for $g(x, y) = x + y$ and for $g(x, y) = x - y$.

8. ◦ In the space $P_4$ of real polynomials of degree at most $4$, let $U = \set{p : p(1) = p'(1) = 0}$. Find the [codimension](/JJCGJ1EGCQ/) and the dimension of $U$.

9. • Find the matrix of the projection of $\R^2$ onto the line $y = 2x$ along the line $y = -x$, and the matrix of the complementary projection $I - P$.

10. • Find the matrix $P$ of the projection of $\R^3$ onto the plane $x + y + z = 0$ along the line $\R(1, 0, 0)$. Check that $P^2 = P$ and that $\operatorname{tr} P = \operatorname{rank} P$.

11. • Let $P$ and $Q$ be projections on $V$ with $PQ = QP$. Show that $PQ$ is a projection with image $\operatorname{im} P \cap \operatorname{im} Q$. Then show by an example in $\R^2$ that the product of two projections that do not commute need not be a projection.

12. • Let $F$ be a field and $n \ge 1$. Show that $M_n(F) = \mathfrak{sl}_n(F) \oplus F I$, where $\mathfrak{sl}_n(F)$ is the subspace of matrices of trace $0$, if and only if $n \cdot 1 \ne 0$ in $F$. Give a field and an $n$ for which it fails.

13. • Let $U$ be the subspace of $\R[x]$ of multiples of $(x - 1)(x - 2)$. Use the [first isomorphism theorem](/0MTBGVZ4XJ/) with $p \mapsto (p(1), p(2))$ to show $\R[x]/U \cong \R^2$, and find the polynomial $a + bx$ with $x^3 + U = (a + bx) + U$.

14. • In $\R^4$ let $U = \operatorname{span}\set{(1, 0, 1, 0), (0, 1, 0, 1)}$ and $W = \operatorname{span}\set{(1, 1, 1, 1), (1, 0, 0, 0)}$. Find $U \cap W$ and $U + W$, and check the [second isomorphism theorem](/0APN65D6Y6/) by computing both sides of $(U + W)/W \cong U/(U \cap W)$.

15. • In $\R^5$ let $U = \set{x_1 + x_2 + x_3 = 0}$ and $W = \set{x_3 + x_4 + x_5 = 0}$. Find $\operatorname{codim}(U \cap W)$ and decide whether $U + W = \R^5$. Then find subspaces $U' \supseteq W'$ of $\R^5$, each of codimension at least $1$, with $\operatorname{codim}(U' \cap W') < \operatorname{codim} U' + \operatorname{codim} W'$.

16. • Show that $0 \to \R \xrightarrow{f} \R^3 \xrightarrow{g} \R^2 \to 0$ with $f(t) = (t, 2t, 3t)$ and $g(x, y, z) = (2x - y, 3x - z)$ is exact. Find a splitting $s \colon \R^2 \to \R^3$ with $g \circ s = \operatorname{id}$, and write $(1, 1, 1)$ as $f(t) + s(a, b)$.

17. • Let $V = F[x]$ and $U = xF[x]$. Show that $U \cong V$ and $V/U \cong F$. Explain why this does not contradict the formula $\dim V/U = \dim V - \dim U$.

18. • Let $V = M_2(\R)$, let $U$ be the upper triangular matrices and $W = \R E_{12}$, where $E_{12}$ has a $1$ in position $(1, 2)$ and $0$ elsewhere. Write down the isomorphism $(V/W)/(U/W) \to V/U$ of the [third isomorphism theorem](/07RB3EMBWW/) explicitly, using the $(2, 1)$ entry, and give the dimensions of $V/W$, $U/W$ and $V/U$.

19. • Let $T \colon P_3 \to P_1$, $T(p) = p''$, and $U = \operatorname{span}\set{1}$. Show that $T$ passes to a linear map $\bar T \colon P_3/U \to P_1$ by the [universal property](/0ZERJX6PH6/). Is $\bar T$ injective, and is it surjective? Find $\dim \ker \bar T$.

20. ★ Let $P$ and $Q$ be projections on a vector space over a field in which $2 \ne 0$. Show that $P + Q$ is a projection if and only if $PQ = QP = 0$. Show that the "only if" direction fails over $\mathbb{F}_2$.

21. ★ Let $T$ be a linear map on a finite-dimensional space $V$. Show that $V = \ker T \oplus \operatorname{im} T$ if and only if $\ker T = \ker T^2$. Give a $2 \times 2$ matrix for which both fail.

22. ★ For subspaces $U$ and $W$ of $V$, show that
$$0 \to U \cap W \xrightarrow{f} U \oplus W \xrightarrow{g} U + W \to 0, \quad f(x) = (x, -x), \quad g(u, w) = u + w,$$
is exact, where $U \oplus W$ is the [external direct sum](/0S7W6EG32V/). Deduce $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$ when $U$ and $W$ are finite-dimensional.

23. ★ Let $U$ be a subspace of dimension $k$ of $\mathbb{F}_q^n$, where $\mathbb{F}_q$ is the field with $q$ elements. Show that $U$ has exactly $q^{k(n - k)}$ complements. (Fix one complement $W_0$ and describe the others as graphs of linear maps $W_0 \to U$.)

24. ★ Let $T \colon V \to W$ be linear. Show that
$$0 \to \ker T \to V \xrightarrow{T} W \to W/\operatorname{im} T \to 0$$
is exact, with the inclusion and the quotient map at the ends. Deduce that $\dim V - \dim W = \dim \ker T - \dim(W/\operatorname{im} T)$ when $V$ and $W$ are finite-dimensional.
