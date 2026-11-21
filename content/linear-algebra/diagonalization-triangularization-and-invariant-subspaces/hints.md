2. $A e_1 = (2, 1, 0)$ and $A e_2 = (1, 2, 0)$ lie in $U$. The restriction has the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with characteristic polynomial $(t - 3)(t - 1)$. The quotient operator sends $e_3 + U$ to $(5, 7, -1) + U = -e_3 + U$, so its matrix is $(-1)$. Hence $p_A = (t - 3)(t - 1)(t + 1)$. The vector $e_3$ is not an eigenvector, since $A e_3 = (5, 7, -1)$; an eigenvector for $-1$ is $(1, 2, -1)$.

4. The algebraic multiplicity is $3$. The matrix $A - 2I$ has rank $1$, so the geometric multiplicity is $2 < 3$. Also $(A - 2I)^2 = 0$ and $A \ne 2I$, so $m_A = (t - 2)^2$, which has a repeated root. Both tests say that $A$ is not diagonalizable.

5. The polynomial $t^3 - 1$ kills $C$ and has the three distinct roots $1, \omega, \omega^2$ in $\C$, where $\omega = e^{2\pi i/3}$. Over $\R$, $p_C = t^3 - 1 = (t - 1)(t^2 + t + 1)$ does not split.

6. The eigenvectors are $(1, 0)$ for $3$ and $(1, -1)$ for $2$. With $P = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}$, which is its own inverse, $A^k = \begin{pmatrix} 3^k & 3^k - 2^k \\ 0 & 2^k \end{pmatrix}$. For $k = 2$ this is $\begin{pmatrix} 9 & 5 \\ 0 & 4 \end{pmatrix}$.

7. $p_A = (t - 1)^2 (t - 2)$. The eigenspace of $1$ is $\operatorname{span}(e_1)$, while $\ker(A - I)^2 = \operatorname{span}(e_1, e_2 - e_3)$ is the generalized eigenspace, of dimension $2$. For $2$, the eigenspace and the generalized eigenspace are both $\operatorname{span}(e_3)$. $A$ is not diagonalizable.

8. (a) Nilpotent of index $2$. (b) Not nilpotent: its square is $I$. (c) Nilpotent of index $3$: the square is $3 E_{13}$, which is not $0$. (d) Not nilpotent: it equals its own square.

9. $\ker T = \operatorname{span}(e_1)$ and $\ker T^2 = \ker T^3 = \operatorname{span}(e_1, e_2)$, so the kernels stop growing at $j = 2$. Also $T^3 = T^2$ has image $\operatorname{span}(2, 1, 1)$, which meets the plane $z = 0$ only in $0$.

11. $T|_U \colon U \to U$ is injective, so it is onto $U$ by dimension. For the shift, $T(U)$ consists of the sequences that vanish for $n < 1$, which is smaller than $U$, and $T^{-1}$ sends $e_0 \in U$ to $e_{-1} \notin U$.

13. Exactly when $a = 0$, for every $b$. The eigenvalue $1$ has algebraic multiplicity $2$, and $A - I$ has rank $1$ when $a = 0$ and rank $2$ when $a \ne 0$.

15. Write $A = u v^{\mathsf T}$ with nonzero column vectors $u$ and $v$. Then $A^2 = (v^{\mathsf T} u) A = (\operatorname{tr} A) A$. If $\operatorname{tr} A \ne 0$, the polynomial $t(t - \operatorname{tr} A)$ has distinct roots and kills $A$. If $\operatorname{tr} A = 0$, then $A$ is nonzero and nilpotent.

16. The eigenvalues are $4$ and $1$, with $E_1 = \tfrac{1}{3}\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ for $4$ and $E_2 = \tfrac{1}{3}\begin{pmatrix} 2 & -1 \\ -2 & 1 \end{pmatrix}$ for $1$. Then $B = 2 E_1 + E_2 = \tfrac{1}{3}\begin{pmatrix} 4 & 1 \\ 2 & 5 \end{pmatrix}$. The line $f(t) = (t + 2)/3$ has $f(4) = 2$ and $f(1) = 1$, so $B = \tfrac{1}{3}(A + 2I)$.

17. Both $J C$ and $C J$ equal $J$. The vectors $(1, \omega^k, \omega^{2k})$ for $k = 0, 1, 2$ are eigenvectors of $C$ for $\omega^k$, and of $J$ for $3, 0, 0$.

19. The summands are the line $\ker(C - I) = \operatorname{span}(1, 1, 1)$ and the plane $\ker(C^2 + C + I) = \set{x + y + z = 0}$. A Bézout identity is $-\tfrac{1}{3}(t + 2)(t - 1) + \tfrac{1}{3}(t^2 + t + 1) = 1$. The projection onto the line is $\tfrac{1}{3}(C^2 + C + I) = \tfrac{1}{3} J$, and the projection onto the plane is $I - \tfrac{1}{3} J$.

20. From $(t - 1)^2 - t(t - 2) = 1$, the projection onto $\ker(A - I)^2$ is $-A(A - 2I)$ and the projection onto $\ker(A - 2I)$ is $(A - I)^2$. So $S = A^2 - 2A + 2I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix}$ and $N = A - S = -(A - I)(A - 2I)$, the matrix with a single $1$ in row $1$, column $2$.

21. Choose $v$ with $N^2 v \ne 0$; then $N^3 = 0$ because $N$ is nilpotent on a space of dimension $3$. Apply $N^2$, then $N$, to a relation $a v + b N v + c N^2 v = 0$. The matrix is the nilpotent Jordan block with ones just above the diagonal.

23. Rank-nullity gives (a) $\Leftrightarrow$ (b). If $x \in \ker T^2$, then $T x \in \ker T \cap \operatorname{im} T$. Conversely, if $y = T x$ lies in $\ker T$, then $x \in \ker T^2$.

24. Write $A = P U P^{-1}$ with $U$ upper triangular. Add to $U$ a small diagonal matrix $D$ chosen so that the diagonal entries of $U + D$ are distinct. Then $P(U + D)P^{-1}$ has $n$ distinct eigenvalues, and it tends to $A$ as $D \to 0$.

25. If $\ker(A - \lambda I) = \ker(A - \lambda I)^2$, show by induction that $\ker(A - \lambda I)^j = \ker(A - \lambda I)$ for every $j \ge 1$, so the generalized eigenspace is the eigenspace. Then use the [decomposition into generalized eigenspaces](/0Z3GDY89T5/). For the converse, a diagonalizable $A - \lambda I$ is diagonal in some basis, where its kernel and the kernel of its square are visibly equal.

26. $S'$ commutes with $N'$, hence with $T = S' + N'$, hence with the polynomials $S$ and $N$ in $T$; so does $N'$. Then $S - S' = N' - N$ is diagonalizable, by simultaneous diagonalization, and nilpotent, by the binomial theorem. A map that is both is $0$.

27. Let $U$ be invariant of dimension $k$. Then $N|_U$ is nilpotent on a $k$-dimensional space, so $N^k$ kills $U$, and $U \subseteq \ker N^k$. Both have dimension $k$.

28. The eigenvalues of $S$ are those of $T$, so $S$ is invertible, and $S^{-1}$ is a polynomial in $S$, so it commutes with $N$; hence $S^{-1} N$ is nilpotent. For uniqueness, write $T = S' + S'(U' - I)$ and check that $S'(U' - I)$ is nilpotent and commutes with $S'$. The additive uniqueness gives $S' = S$, and then $U' = S^{-1} T = U$.
