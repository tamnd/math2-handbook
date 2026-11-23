1. ◦ Decide which of these maps are [linear forms](/07YQ1C78G0/): $f(x, y, z) = x - 2y + 3z$ on $\R^3$; $g(x, y) = xy$ on $\R^2$; $h(p) = p'(0) + p(1)$ on $P_2$; $k(p) = p(0)^2$ on $P_2$. For each linear form on $P_2$, give its row in the basis $(1, x, x^2)$.

2. ◦ Find a nonzero linear form on $\R^3$ whose kernel is the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$. How many such forms are there?

3. ◦ Find the [dual basis](/0ZD2CF6ZS0/) of the basis $(1, 0, 0)$, $(1, 1, 0)$, $(1, 1, 1)$ of $\R^3$, and use it to find the coordinates of $(2, 5, 3)$ in this basis.

4. ◦ Let $U = \operatorname{span}\set{(1, 0, 2, 0), (0, 1, 0, -1)}$ in $\R^4$. Find a basis of the [annihilator](/0ASHNYF7AG/) $U^0$.

5. ◦ Let $f \colon \R^2 \to \R^3$, $f(x, y) = (x + 2y, 3x, x - y)$, and let $\varphi(y_1, y_2, y_3) = 2y_1 - y_2 + y_3$. Compute $f^*(\varphi)$. Between which spaces does $f^*$ go, and what is the size of its matrix?

6. ◦ Find the error: "Let $V = F^{(\N)}$ be the space of sequences with finitely many nonzero terms, and $e_n^*$ the coordinate forms. Every linear form on $V$ is a finite combination of the $e_n^*$." Give a form that is not.

7. ◦ In $\R^2$ let $\varphi_1 = x + 2y$ and $\varphi_2 = x - y$, a basis of $(\R^2)^*$. Let $\Phi \in (\R^2)^{**}$ with $\Phi(\varphi_1) = 4$ and $\Phi(\varphi_2) = 1$. Find the vector $v$ with $\Phi = \operatorname{ev}(v)$.

8. ◦ Use the [Erdős-Kaplansky theorem](/S5ET1HG2ZX/) to find the dimension of the dual of $\Q^{(\N)}$ and of the dual of $\mathbb{F}_2^{(\N)}$. Is either dual isomorphic to a space with a countable basis?

9. • On $P_2$ let $f_0(p) = p(0)$, $f_1(p) = p'(0)$ and $f_2(p) = p''(0)$. Find the basis of $P_2$ whose dual basis is $f_0, f_1, f_2$, and write the form $p \mapsto p(1)$ in terms of $f_0, f_1, f_2$.

10. • Show that the forms $p \mapsto p(0)$, $p \mapsto p(1)$ and $p \mapsto \int_0^1 p(t)\,dt$ are a basis of $P_2^*$, and find the basis of $P_2$ of which they are the dual basis.

11. • Let $f = x + y + z$ and $g = 2x - y$ on $\R^3$. Find $\ker f \cap \ker g$. Show that $h = x + 4y + 3z$ vanishes on it and write $h$ as a combination of $f$ and $g$.

12. • Let $U$ and $W$ be subspaces of $V$. Show that $(U + W)^0 = U^0 \cap W^0$. If $V$ is finite-dimensional, show that $(U \cap W)^0 = U^0 + W^0$.

13. • In $P_3$ let $\varphi_i$ be the form that takes the coefficient of $x^i$, and let $U = \operatorname{span}\set{1, x^2}$. Find a basis of $U^0$ in terms of the $\varphi_i$, and show that $p \mapsto p'(0)$ and $p \mapsto p(1) - p(-1)$ are another basis of $U^0$.

14. • Let $T \colon P_2 \to P_2$, $T(p)(x) = p(x + 1)$. Find the matrix of $T$ in the basis $(1, x, x^2)$ and compute $T^*(\varphi_0)$, $T^*(\varphi_1)$, $T^*(\varphi_2)$ for the coefficient forms $\varphi_i$. Check that the [matrix of the dual map is the transpose](/0ZPB3180AY/). What is $T^*$ of the form $p \mapsto p(0)$?

15. • Let $f \colon \R^3 \to \R^2$, $f(x, y, z) = (x + y - z, 2x + 2y - 2z)$, and write $u, v$ for the coordinate forms of $\R^2$. Find $\ker f^*$ and $\operatorname{im} f^*$, and check that $\ker f^* = (\operatorname{im} f)^0$ and $\operatorname{im} f^* = (\ker f)^0$.

16. • Let $P$ be the matrix whose columns are a basis $B'$ of $F^n$. Show that the dual basis of $B'$, written as rows, is the list of rows of $P^{-1}$. Use this to find the dual basis of $(1, 0), (2, 1)$ in $\R^2$.

17. • Find the matrix $A$ with $\operatorname{tr}(AX) = x_{11} + 2x_{12} - x_{21}$ for all $X = (x_{ij})$ in $M_2(\R)$.

18. • Let $V$ have dimension $n$ and let $\varphi_1, \dots, \varphi_n \in V^*$. Show that $\varphi_1, \dots, \varphi_n$ is a basis of $V^*$ if and only if the only $v$ with $\varphi_i(v) = 0$ for all $i$ is $v = 0$.

19. ★ Let $f, g$ be linear forms on $V$ with $f(v)g(v) = 0$ for every $v \in V$. Show that $f = 0$ or $g = 0$. (A vector space is never the union of two proper subspaces.) Show that $\mathbb{F}_2^2$ is the union of three proper subspaces.

20. ★ Let $V$ be a space of dimension $n$ over $F$. Show that $U \mapsto U^0$ is a bijection from the subspaces of dimension $k$ of $V$ to the subspaces of dimension $n - k$ of $V^*$ that reverses inclusion. Deduce that $\mathbb{F}_q^n$ has as many hyperplanes as lines, namely $(q^n - 1)/(q - 1)$.

21. ★ Let $f \colon V \to W$ be a linear map between finite-dimensional spaces. Using $\operatorname{im} f^* = (\ker f)^0$ and the [dimension of the annihilator](/06Q1EFVH0Q/), show that $\operatorname{rank} f^* = \operatorname{rank} f$, and explain why this proves that the row rank of a matrix equals its column rank.

22. ★ Let $\varphi_1, \dots, \varphi_k \in V^*$. Show that they are linearly independent if and only if the map $V \to F^k$, $v \mapsto (\varphi_1(v), \dots, \varphi_k(v))$, is onto.

23. ★ Let $V$ be a vector space over $\mathbb{F}_2$ with a countable infinite basis. Show without the Erdős-Kaplansky theorem that $V$ is countable, that $V^*$ is uncountable, and deduce that $\dim V^*$ is uncountable.
