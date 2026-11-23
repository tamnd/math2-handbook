1. $f$ and $h$ are linear forms; $g$ and $k$ are not, since $g(2v) = 4g(v)$ and $k(2p) = 4k(p)$. On $P_2$, $h(a + bx + cx^2) = b + (a + b + c)$, so its row is $(1, 2, 1)$.

3. The dual basis is $x - y$, $y - z$, $z$, the rows of $P^{-1}$ for the matrix $P$ with the basis vectors as columns. The coordinates of $(2, 5, 3)$ are $(-3, 2, 3)$.

5. $f^*(\varphi) = \varphi \circ f = 2(x + 2y) - 3x + (x - y) = 3y$. The dual map goes from $(\R^3)^*$ to $(\R^2)^*$, and its matrix is $2 \times 3$, the transpose of the $3 \times 2$ matrix of $f$.

6. The form $s(a) = \sum_n a_n$ is defined on $V$, because each sequence has only finitely many nonzero terms. It takes the value $1$ on every $e_n$, while a finite combination of the $e_n^*$ vanishes on all but finitely many $e_n$.

8. Both duals have dimension $2^{\aleph_0}$, the cardinal of the continuum, since $\abs{\Q}^{\aleph_0} = \abs{\mathbb{F}_2}^{\aleph_0} = 2^{\aleph_0}$. Neither is isomorphic to a space with a countable basis.

10. The matrix of the three forms on $1, x, x^2$ has determinant $-1/6$, so they are independent. The dual basis is $1 - 4x + 3x^2$, $-2x + 3x^2$, $6x - 6x^2$; check each against the three forms.

12. The first equality is immediate from the definitions. For the second, $U^0 + W^0 \subseteq (U \cap W)^0$ is clear. By the first equality, $\dim(U^0 \cap W^0) = n - \dim(U + W)$; the formula for the dimension of a sum, used once in $V^*$ and once in $V$, then gives $\dim(U^0 + W^0) = n - \dim(U \cap W)$.

14. The matrix is $\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$. Then $T^*(\varphi_0) = \varphi_0 + \varphi_1 + \varphi_2$, $T^*(\varphi_1) = \varphi_1 + 2\varphi_2$ and $T^*(\varphi_2) = \varphi_2$. The form $p \mapsto p(0)$ goes to $p \mapsto p(1)$.

16. $P^{-1}P = I$ says that row $i$ of $P^{-1}$ takes the value $1$ on column $i$ of $P$ and $0$ on the other columns. Here $P^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$, so the dual basis is $x - 2y$, $y$.

19. $V = \ker f \cup \ker g$. If neither kernel is $V$, take $u \notin \ker f$ and $w \notin \ker g$; if $u \in \ker g$ and $w \in \ker f$, then $u + w$ lies in neither kernel. In $\mathbb{F}_2^2$ the three lines spanned by $(1, 0)$, $(0, 1)$ and $(1, 1)$ cover the four vectors.

20. The dimension formula sends dimension $k$ to $n - k$. Under the canonical isomorphism $V \cong V^{**}$, the annihilator of $U^0$ is $U$, so the map is a bijection with inverse $W \mapsto W^0$. With $k = 1$, lines correspond to hyperplanes, and $\mathbb{F}_q^n$ has $(q^n - 1)/(q - 1)$ lines, since each line has $q - 1$ nonzero vectors.

21. $\operatorname{rank} f^* = \dim (\ker f)^0 = \dim V - \dim \ker f = \operatorname{rank} f$. For a matrix $A$, the matrix of the dual map is $A^{\mathsf{T}}$, and the rank of $A^{\mathsf{T}}$ is the column rank of $A^{\mathsf{T}}$, which is the row rank of $A$.

22. If the map is not onto, its image lies in a hyperplane of $F^k$, which is the kernel of a nonzero form $(a_1, \dots, a_k)$; then $\sum a_i \varphi_i = 0$. Conversely, a relation $\sum a_i \varphi_i = 0$ with some $a_i \ne 0$ puts the image in the kernel of the form $\sum a_i y_i$.

23. $V$ is the union over $n$ of the finite sets of combinations of the first $n$ basis vectors, so it is countable. A form is fixed by any choice of values in $\mathbb{F}_2$ on the basis vectors, so $V^* \cong \mathbb{F}_2^{\N}$, which is uncountable by Cantor's diagonal argument. A space with a countable basis over $\mathbb{F}_2$ is countable, so $V^*$ has no countable basis.
