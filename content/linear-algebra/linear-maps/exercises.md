1. ◦ Which of these maps are [linear](/0NRYHJPQG2/)? (a) $T(x, y) = (2x - y, 3y)$ on $\R^2$. (b) $T(x, y) = (x + 1, y)$. (c) $T(x, y) = (xy, 0)$. (d) $T(x, y) = (\abs{x}, y)$. (e) $T(x, y, z) = x + y + z$, from $\R^3$ to $\R$. (f) $T(p) = p(2)$, from the real polynomials of degree at most $2$ to $\R$.

2. ◦ Find the standard matrix of $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x + 2y, 3z - x)$.

3. ◦ Find the standard matrices of the reflection of $\R^2$ in the line $y = -x$ and of the orthogonal projection of $\R^2$ onto the line $y = x$. Check each on the vectors $(1, 1)$ and $(1, -1)$.

4. ◦ Let $A = \begin{pmatrix} 1 & -1 & 2 \\ 2 & -2 & 4 \end{pmatrix}$. Find a basis of the [kernel](/0S23E6YE83/) and of the [image](/0WSFKKT6FF/) of $x \mapsto Ax$, and check the [rank-nullity theorem](/0W4FSW1TVB/).

5. ◦ Answer from rank-nullity alone. (a) A linear map $\R^7 \to \R^4$ is surjective; what is its nullity? (b) A linear map $\R^5 \to \R^8$ is injective; what is its rank? (c) Can a linear map $\R^3 \to \R^5$ be surjective? (d) Can a linear map $\R^5 \to \R^3$ be injective?

6. ◦ A linear map $T \colon \R^2 \to \R^2$ has $T(1, 1) = (3, 1)$ and $T(1, -1) = (1, -1)$. Find $T(x, y)$ and the standard matrix of $T$.

7. ◦ Is there a linear map $T \colon \R^2 \to \R^2$ with $T(1, 0) = (1, 1)$, $T(0, 1) = (2, 0)$ and $T(1, 1) = (3, 2)$? Explain with the theorem that [linear maps are determined by a basis](/0R8X9XA83A/).

8. ◦ Give the dimensions of $\operatorname{Hom}(\R^3, \R^2)$, of $\operatorname{Hom}(P_2(\R), P_3(\R))$, where $P_n(\R)$ is the space of real polynomials of degree at most $n$, and of $\operatorname{End}(M_{2 \times 2}(\R))$.

9. ◦ Let $S(x, y) = (x + y, y)$ and $T(x, y) = (2x, x - y)$ on $\R^2$. Compute $T \circ S$ and $S \circ T$, and their standard matrices. Do the two maps commute?

10. • Let $T \colon P_3(\R) \to \R^2$ be $T(p) = (p(0), p(1))$. Show that $T$ is linear and surjective, find a basis of $\ker T$, and check rank-nullity.

11. • Show that the trace $M_{n \times n}(F) \to F$ is linear and surjective, and use rank-nullity to find the dimension of the space of $n \times n$ matrices of trace $0$.

12. • Let $T \colon M_{2 \times 2}(\R) \to M_{2 \times 2}(\R)$ be $T(X) = X - X^{\mathsf{T}}$. Find $\ker T$ and $\operatorname{im} T$ with their dimensions.

13. • Let $T \colon V \to W$ be linear, with $V$ and $W$ finite-dimensional. Show that if $T$ is injective then $\dim V \le \dim W$, and if $T$ is surjective then $\dim V \ge \dim W$.

14. • Give an explicit [linear isomorphism](/0B8T10CE7N/) between $P_3(\R)$ and $M_{2 \times 2}(\R)$. Explain why neither space is isomorphic to $\R^3$.

15. • Find a linear map $T \colon \R^3 \to \R^3$ whose kernel is the line spanned by $(1, 1, 1)$ and whose image is the plane $x + y + z = 0$.

16. • Let $T$ be an endomorphism of a space $V$ of dimension $n$ with $T \circ T = 0$. Show that $\operatorname{im} T \subseteq \ker T$, and deduce that $\operatorname{rank} T \le n/2$. Give an example with equality for $n = 2$.

17. • Let $D$ be differentiation. Decide whether $D \colon P_n(\R) \to P_n(\R)$ is injective or surjective, and find its rank. Then do the same for $D \colon \R[x] \to \R[x]$. Why does this not contradict the theorem on [injective, surjective and bijective endomorphisms](/0912EEEVCT/)?

18. • Let $T \colon U \to V$ and $S \colon V \to W$ be linear. Show that if $S \circ T$ is injective then $T$ is injective, and if $S \circ T$ is surjective then $S$ is surjective. Find $T \colon \R \to \R^2$ and $S \colon \R^2 \to \R$ with $S \circ T = \mathrm{id}_{\R}$ but $T \circ S \ne \mathrm{id}_{\R^2}$.

19. • Let $\varphi_a \colon P_2(\R) \to \R$ be evaluation at $a$, $\varphi_a(p) = p(a)$. Show that $\varphi_0, \varphi_1, \varphi_2$ form a basis of $\operatorname{Hom}(P_2(\R), \R)$.

20. • Let $U$ be a subspace of $V$. Show that the endomorphisms $T$ of $V$ with $T(U) \subseteq U$ form a subalgebra of $\operatorname{End}(V)$: a subspace that contains the identity and is closed under composition. Find its dimension when $V = \R^3$ and $U$ is a line.

21. • Show that $T(z, w) = (\bar w, \bar z)$ on $\C^2$ is [antilinear](/BNPDDM95KF/) and not linear, and that the composite of two antilinear maps is linear.

22. ★ Let $T \colon U \to V$ and $S \colon V \to W$ be linear, with $V$ finite-dimensional. Prove that $\operatorname{rank}(S \circ T) \le \min(\operatorname{rank} S, \operatorname{rank} T)$ and Sylvester's inequality $\operatorname{rank}(S \circ T) \ge \operatorname{rank} S + \operatorname{rank} T - \dim V$.

23. ★ Let $T \colon V \to W$ be linear of rank $r$, with $V$ and $W$ finite-dimensional. Show that there are bases of $V$ and of $W$ in which the matrix of $T$ is $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.

24. ★ Show that every infinite-dimensional vector space has an endomorphism that is injective but not surjective, and one that is surjective but not injective.

25. ★ Let $V$ have dimension $n$ and let $T \in \operatorname{End}(V)$. Show that there is a nonzero polynomial $p$ of degree at most $n^2$ with $p(T) = 0$.

26. ★ Show that every additive map $f \colon \Q^n \to \Q^m$, that is, every map with $f(u + v) = f(u) + f(v)$, is $\Q$-linear.
