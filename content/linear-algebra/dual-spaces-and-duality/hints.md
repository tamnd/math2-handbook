1. (a), (d) and (e) are linear forms. (b) does not send $0$ to $0$, and (c) is not additive: $(1, 0)$ and $(0, 1)$ map to $0$, but their sum maps to $1$.

2. The basis vectors are the columns of an upper triangular $P$, and the dual basis is the rows of $P^{-1}$: $x - y$, $y - z$, $z$.

4. A form $ax + by + cz$ vanishes on $U$ when $a + c = 0$ and $b + c = 0$, so $U^0 = \R(x + y - z)$, of dimension $1$.

5. (a) $6$. (b) $3$. (c) $2^{\aleph_0}$, the cardinality of $\Q^{\N}$.

8. Hyperplanes correspond to nonzero forms up to a nonzero scalar: $(3^3 - 1)/(3 - 1) = 13$.

9. The dual basis is the Lagrange basis $\tfrac12 x(x - 1)$, $1 - x^2$, $\tfrac12 x(x + 1)$. The derivatives of these at $0$ are $-\tfrac12$, $0$, $\tfrac12$, so $p'(0) = \tfrac12 (p(1) - p(-1))$.

11. $U^0$ has basis $x_1 - x_2 + x_3$, $x_4$; $W^0$ has basis $x_1$, $x_2$, $x_3 - x_4$; and $(U + W)^0 = \R(x_1 - x_2 + x_3 - x_4)$.

13. $f$ is surjective, so $\ker f^* = 0$. Its kernel is $\R(1, -1, 1)$, so $\operatorname{im} f^*$ is the plane of forms $ax + by + cz$ with $a - b + c = 0$, spanned by $f^*(e_1^*) = x + y$ and $f^*(e_2^*) = y + z$.

16. The common kernel is $\R(1, 1, -2)$. Since $g(1, 1, -2) = -1$, $g$ is not in the span. Since $h(1, 1, -2) = 0$, it is: $h = 2f_1 + f_2$.

19. Apply rank–nullity to $v \mapsto (f_1(v), \ldots, f_k(v))$. Its kernel is the intersection, and its rank is the rank of the $k \times n$ matrix whose rows are the coordinates of the $f_i$, which is $\dim \operatorname{span}\set{f_i}$.

20. The map is injective, since $\operatorname{tr}(A E_{ji}) = a_{ij}$, so $A \ne 0$ gives a nonzero form; both spaces have dimension $n^2$. The form $X \mapsto x_{ij}$ is $X \mapsto \operatorname{tr}(E_{ji} X)$.

21. If $T(U) \subseteq U$ and $\varphi \in U^0$, then $(T^* \varphi)(u) = \varphi(Tu) = 0$. For the converse, apply the same argument to $T^*$ and $U^0$, and use $U^{00} = \operatorname{ev}(U)$ and $T^{**} \circ \operatorname{ev} = \operatorname{ev} \circ T$.

22. $V$ is countable, and a form is any choice of values on the basis $e_n$, so $V^* \cong \Q^{\N}$, which is uncountable. A $\Q$-space with a countable basis is a countable set.
