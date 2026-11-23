1. ◦ Which of these maps are [linear](/0NRYHJPQG2/)? Give a reason for each. (a) $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x - z, 2y)$. (b) $T \colon \R^2 \to \R^3$, $T(x, y) = (x, y, 1)$. (c) $T \colon \R^2 \to \R^2$, $T(x, y) = (\abs{x}, y)$. (d) $T \colon P_2 \to \R$, $T(p) = p(1) + p'(0)$. (e) $T \colon M_2(\R) \to M_2(\R)$, $T(A) = A + A^T$. (f) $T \colon M_2(\R) \to \R$, $T(A) = \det A$.

2. ◦ Find the [standard matrix](/W6KB0J3SZZ/) of (a) $T \colon \R^3 \to \R^2$, $T(x, y, z) = (2x - y + z, x + 3z)$, and (b) the reflection of $\R^2$ in the line $y = -x$.

3. ◦ Let $S(x, y) = (x + y, 2y)$ and $T(x, y) = (y, x - y)$ on $\R^2$. Find the matrices of $S \circ T$ and $T \circ S$, and check that they differ.

4. ◦ Let $T \colon \R^3 \to \R^3$ be $x \mapsto Ax$ with $A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ -1 & 0 & 1 \end{pmatrix}$. Find the [kernel](/0S23E6YE83/) and the [image](/0WSFKKT6FF/) of $T$, each described by a basis or by equations.

5. ◦ Which of these linear maps are injective? (a) $T \colon \R^2 \to \R^3$, $T(x, y) = (x - y, x + y, 2x)$. (b) $T \colon P_2 \to P_2$, $T(p) = p + p'$. (c) $T \colon P_2 \to \R^2$, $T(p) = (p(0), p(1))$. (d) $T \colon \R^3 \to \R^3$, $x \mapsto Ax$ with $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$.

6. ◦ Give the [rank](/0ZZXSBTR4J/) and the [nullity](/0APCFW7639/) of each map. (a) The second derivative $p \mapsto p''$ on $P_4$. (b) $A \mapsto A - A^T$ on $M_2(\R)$. (c) $T \colon \R^4 \to \R^2$, $T(x_1, x_2, x_3, x_4) = (x_1 + x_2, x_3 + x_4)$. (d) $x \mapsto Ax$ with $A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 1 \\ 3 & 6 & 1 & 2 \end{pmatrix}$.

7. ◦ There is exactly one linear map $T \colon \R^2 \to \R^2$ with $T(1, 1) = (3, 1)$ and $T(1, 2) = (5, 0)$. Find $T(x, y)$ and the matrix of $T$.

8. ◦ (a) A linear map $T \colon \R^7 \to \R^4$ is surjective. What is its nullity? (b) Can a linear map $\R^3 \to \R^5$ be surjective? (c) Can a linear map $\R^5 \to \R^3$ be injective? Answer (b) and (c) with the [rank-nullity theorem](/0W4FSW1TVB/).

9. ◦ Give the dimensions of (a) $\operatorname{Hom}(P_2, M_{2 \times 3}(\R))$, (b) $\operatorname{End}(\R^4)$, (c) the real vector space of $\R$-linear maps $\C^2 \to \C^3$.

10. • Let $T \colon \R^4 \to \R^3$ be $x \mapsto Ax$ with $A = \begin{pmatrix} 1 & 1 & 0 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 2 & 1 & 3 \end{pmatrix}$. Find a basis of $\ker T$, a basis of $\operatorname{im} T$, and an equation for $\operatorname{im} T$, and check the rank-nullity theorem.

11. • Let $T \colon P_3 \to \R^2$ be $T(p) = (p(1), p'(1))$. Show that $T$ is linear and surjective, find a basis of $\ker T$, and describe $\ker T$ in terms of divisibility.

12. • Let $T \colon V \to W$ be linear and $v_1, \ldots, v_k \in V$. (a) Prove that if $T(v_1), \ldots, T(v_k)$ are independent, then $v_1, \ldots, v_k$ are independent. (b) Show by an example that the converse is false. (c) Prove that the converse holds when $T$ is injective.

13. • Find the error. "Claim: a linear map $T \colon \R^3 \to \R^3$ with $T(e_1)$, $T(e_2)$, $T(e_3)$ all nonzero is injective. Proof: none of $e_1, e_2, e_3$ lies in $\ker T$, so $\ker T = \set{0}$, and $T$ is injective." Name the wrong step and give a $3 \times 3$ matrix for which the claim fails.

14. • Let $T \colon U \to V$ and $S \colon V \to W$ be linear, with $U$, $V$ finite-dimensional. Prove that $\operatorname{rank}(S \circ T) \le \min(\operatorname{rank} S, \operatorname{rank} T)$. Then check that for $S(x, y, z) = (x, y, 0)$ and $T(x, y, z) = (0, y, z)$ on $\R^3$ the inequality is strict.

15. • Let $T \colon \R^n \to \R^n$ be linear with $T \circ T = 0$. Prove that $\operatorname{im} T \subseteq \ker T$ and that $\operatorname{rank} T \le n/2$. Give such a $T$ on $\R^4$ with rank $2$.

16. • Let $T \colon P_2 \to \R^3$ be $T(p) = (p(0), p(1), p(2))$. Prove that $T$ is an [isomorphism](/0B8T10CE7N/), and find the polynomial $p$ with $T(p) = (1, 3, 9)$.

17. • On the space of real sequences, let $T(x_0, x_1, x_2, \ldots) = (x_0, 0, x_1, 0, x_2, 0, \ldots)$ and $S(x_0, x_1, x_2, \ldots) = (x_0, x_2, x_4, \ldots)$. Show that $S \circ T = \mathrm{id}$, that $T$ is injective and not surjective, and that $S$ is surjective and not injective. Explain why this does not contradict the theorem on [endomorphisms of finite-dimensional spaces](/0912EEEVCT/).

18. • Let $T \colon V \to W$ be linear with $V$ finite-dimensional, and let $U$ be a subspace of $V$. Prove that $\dim T(U) = \dim U - \dim(U \cap \ker T)$.

19. • Show that $\set{T \in \operatorname{Hom}(\R^3, \R^2) : T(1, 1, 0) = 0}$ is a subspace of $\operatorname{Hom}(\R^3, \R^2)$ and find its dimension.

20. • Let $T(x, y) = (x + y, -x)$ on $\R^2$. Compute $T^2$ and $T^3$, show that $T^3 = -\mathrm{id}$, and deduce that $T$ is an isomorphism with $T^{-1} = -T^2$.

21. • For each map $\C \to \C$, decide whether it is $\R$-linear, $\C$-linear, [antilinear](/BNPDDM95KF/), or none of these. (a) $z \mapsto 3z$. (b) $z \mapsto i \bar z$. (c) $z \mapsto z + 2 \bar z$. (d) $z \mapsto z^2$.

22. • Let $A \colon \C^n \to \C^n$ be antilinear. Prove that there is exactly one complex $n \times n$ matrix $M$ with $A(z) = M \bar z$ for all $z$, where $\bar z$ is conjugated entrywise. Find $M$ for $A(z, w) = (i \bar z + \bar w, 2 \bar z)$.

23. ★ Let $V$ be a vector space of finite dimension $n$ and $T \in \operatorname{End}(V)$. Prove that there is a nonzero polynomial $p$ of degree at most $n^2$ with $p(T) = 0$.

24. ★ Let $f \colon \Q^n \to \Q^m$ satisfy $f(u + v) = f(u) + f(v)$ for all $u, v$. Prove that $f$ is $\Q$-linear. Explain why the same argument does not show that an additive map $\R \to \R$ is $\R$-linear.

25. ★ Let $\varphi \colon M_n(F) \to F$ be linear with $\varphi(AB) = \varphi(BA)$ for all $A, B \in M_n(F)$. Prove that $\varphi = c \operatorname{tr}$ for some $c \in F$. Use the matrix units $E_{ij}$.

26. ★ Let $V$ have finite dimension $n$ and let $U$ be a subspace of dimension $k$. Prove that $\set{T \in \operatorname{End}(V) : T(U) \subseteq U}$ is a subspace of $\operatorname{End}(V)$ closed under composition, and that its dimension is $n^2 - k(n - k)$.

27. ★ Let $A \in M_n(F)$ have rank $1$. Prove that $A = u w^T$ for some nonzero columns $u, w \in F^n$, and that $A^2 = (\operatorname{tr} A) A$. Check this for $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$.
