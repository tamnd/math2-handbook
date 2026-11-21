1. $A = \begin{pmatrix} 0 & 1 \\ -2 & 3 \end{pmatrix}$, since $A_{ij} = B(e_i, e_j)$. Then $B((1, 1), (1, -1)) = (1, 1) A (1, -1)^T = -1 - 2 - 3 = -6$.

2. (b) and (d) are bilinear; (d) is alternating. (a) fails because $B(0, 0) = 1 \ne 0$, and (c) is not linear in $x$.

4. The rank is $1$. The radical is the line spanned by $(2, -1)$: both rows of the matrix are multiples of $(1, 2)$.

5. $u = e_2$, $v = e_1$: $B(e_2, e_1) = A_{21} = 0$ but $B(e_1, e_2) = A_{12} = 1$. The form is neither symmetric nor alternating, so it is not reflexive, by the theorem on [reflexive forms](/M0G958M917/).

7. $M_1$, because $M_1^* = M_1$. Then $h(v, v) = v^T M_1 \bar v = 7$, a real number, as it must be.

9. Over $\R$, $I_2$ is positive definite while $H$ takes the value $-2$ at $(1, -1)$, and congruent matrices define the same set of values. Over $\mathbb F_2$, $H$ is alternating and $I_2$ is not, and $P^T H P$ is alternating for every $P$. Over $\C$ the columns $(1, i)/\sqrt 2$ and $(1, -i)/\sqrt 2$ of $P$ work.

10. $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ gives $P^T P = 2 I_2$. If $I_2$ and $3 I_2$ were congruent, $x^2 + y^2$ would take the value $3$ at a rational point. Clear denominators to get $m^2 + n^2 = 3 k^2$, and use that squares are $0$ or $1$ modulo $3$ for a descent.

12. The radical is spanned by $w = (3, -2, 1)$. The basis $e_1, e_2, w$ works, since $B(e_1, e_2) = 1$ and $w$ is orthogonal to everything.

13. Take $u_1 = e_1$, $v_1 = e_2$. Replace $e_3$ by $e_3 + B(e_2, e_3) e_1 - B(e_1, e_3) e_2 = (1, -2, 1, 0)$ and check that $e_4$ is already orthogonal to $u_1$ and $v_1$. Then $u_2 = (1, -2, 1, 0)$ and $v_2 = e_4$ satisfy $B(u_2, v_2) = 1$.

14. Apply Gram-Schmidt for $h$: $f_1 = e_1$ and $f_2 = e_2 - \frac{h(e_2, e_1)}{h(e_1, e_1)} e_1 = (i/2, 1)$. Then $h(f_1, f_1) = 2$ and $h(f_2, f_2) = 5/2$, both positive.

16. Take $H_1 = \operatorname{span}(e_1, e_3)$ and $H_2 = \operatorname{span}(e_2, e_4)$, with hyperbolic pairs $e_1 + e_3$, $\frac12 (e_1 - e_3)$ and $e_2 + e_4$, $\frac12 (e_2 - e_4)$, and the anisotropic line $\operatorname{span}(e_5)$. The Witt index is $2$.

17. Split $\R^n = V_+ \perp V_-$ with the form positive definite on $V_+$ ($\dim p$) and negative definite on $V_-$ ($\dim q$). A totally isotropic $W$ meets $V_+$ and $V_-$ only in $0$, so $\dim W \le \min(p, q)$. Pairs $e_i + f_i$ with $e_i \in V_+$, $f_i \in V_-$ of opposite squares give a totally isotropic subspace of dimension $\min(p, q)$.

18. On a line $\operatorname{span}(v)$, $\omega(v, v) = 0$, and in dimension $2$ the complement of a line is a line. For $\mathbb F_2^4$ the answer is $15$: a Lagrangian is a plane $\operatorname{span}(a, b)$ with $\omega(a, b) = 0$; count the pairs and divide by the $6$ ordered bases of each plane.

19. $u = (1, i)$ and $v = \frac12 (1, -i)$ are isotropic with $B(u, v) = 1$. Pair the coordinates two at a time; for odd $n$ one line $\operatorname{span}(e_n)$ is left, and it is anisotropic.

20. Let $e_1, \dots, e_m$ be a basis of $L$. Since $\omega$ is nondegenerate and $L^\perp = L$, there are $f_j$ with $\omega(e_i, f_j) = \delta_{ij}$. Replace $f_j$ by $f_j' = f_j - \sum_{k > j} \omega(f_j, f_k) e_k$ to make the $f_j'$ pairwise orthogonal; then $L' = \operatorname{span}(f_1', \dots, f_m')$ works in every characteristic.
