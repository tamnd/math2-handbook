1. $m_{e_1} = x - 2$ and $m_v = (x - 2)(x - 3)$. The minimal polynomial is $(x - 2)(x - 3)$, of degree $2 < 3$, and every annihilator divides it, so no vector has an annihilator of degree $3$ and $A$ is not cyclic.

3. (a) Yes: the degrees add up to $5$ and each polynomial divides the next. (b) No: $x$ does not divide $x^2 - 1$. (c) No: the degrees add up to $6$. (d) Yes.

4. The size is $1 + 2 + 1 + 3 + 1 = 8$. The invariant factors are $(x - 1)(x - 2)$ and $(x - 1)^2 (x - 2)^3 (x + 1)$, the second is the minimal polynomial, and the blocks have sizes $2$ and $6$.

6. The blocks of size at least $j$ number $7 - 4 = 3$, $4 - 2 = 2$, $2 - 1 = 1$ and $1 - 0 = 1$ for $j = 1, 2, 3, 4$. So the partition is $(4, 2, 1)$, with $3$ blocks and nilpotency index $4$. The Weyr structure is the list of these jumps, $(3, 2, 1, 1)$.

7. Nilpotent classes match the partitions of $6$, and there are $11$. For the second question, choose a partition of $3$ for the eigenvalue $2$ and one of $2$ for $-1$: $3 \cdot 2 = 6$ classes.

10. The invariant factors are $x, x, x^2$, so the sum of $\deg \gcd(d_i, d_j)$ over the nine pairs is $8 \cdot 1 + 2 = 10$. The Weyr structure is $(3, 1)$, and $3^2 + 1^2 = 10$.

11. $v = e_2 + e_3$ works: the matrix with columns $v, Av, A^2 v$ has determinant $-1$. The minimal polynomial is $(x - 2)^2 (x - 3) = x^3 - 7x^2 + 16x - 12$, and the matrix is its companion matrix $\begin{pmatrix} 0 & 0 & 12 \\ 1 & 0 & -16 \\ 0 & 1 & 7 \end{pmatrix}$.

12. The entry $-1$ gives $D_1 = 1$. Every $2 \times 2$ minor is a multiple of $x - 2$, and $(x - 3)(x - 1) + 1 = (x - 2)^2$, so $D_2 = x - 2$ and $D_3 = (x - 2)^3$. The invariant factors are $x - 2$ and $(x - 2)^2$; the rational form is $(2) \oplus \begin{pmatrix} 0 & -4 \\ 1 & 4 \end{pmatrix}$ and the Jordan form is $J_1(2) \oplus J_2(2)$.

13. The degrees of the invariant factors add up to $3$, the last one is $m$ and their product is $\chi$. If $\deg m = 3$ there is one factor; if $\deg m = 2$ the other is $\chi / m$; if $\deg m = 1$ all three equal $m$.

15. $J = J_3(1)$, since $\operatorname{rank}(A - I) = 2$ and $\operatorname{rank}(A - I)^2 = 1$. With $N = A - I$ and the top vector $u = e_1$, which is not in $\ker N^2$, the chain gives $P$ with columns $N^2 u = (1, 1, 1)$, $N u = (2, 2, 1)$ and $u = (1, 0, 0)$.

16. $N^2 = 0$, so the binomial formula stops after two terms: $A^k = 2^k I + k 2^{k-1} N = 2^{k-1} \begin{pmatrix} 2 + k & k \\ -k & 2 - k \end{pmatrix}$.

18. The six forms have invariant factors $(x + 1, x + 1, x + 1)$, $(x + 1, (x + 1)^2)$, $(x + 1)^3$, $(x + 1)(x^2 + x + 1) = x^3 + 1$, $x^3 + x + 1$ and $x^3 + x^2 + 1$. The orders are $1, 2, 4, 3, 7, 7$.

21. $C((x^2 + 1)^2)$ is cyclic with single invariant factor $(x^2 + 1)^2$, so its complex Jordan form is $J_2(i) \oplus J_2(-i)$ and its real Jordan form is $C_2(0, 1)$. The direct sum $C(x^2 + 1) \oplus C(x^2 + 1)$ has the invariant factors $x^2 + 1, x^2 + 1$ and minimal polynomial $x^2 + 1$.

22. The Weyr structure is $(2, 2, 1)$, and the form is $E_{13} + E_{24} + E_{35}$. Both matrices have ranks $3, 1, 0$ for the first three powers. The centralizer has dimension $2^2 + 2^2 + 1^2 = 9$.

24. A module map is fixed by the image $c$ of $1$, which must satisfy $ac \equiv 0 \pmod b$; these $c$ form the multiples of $b / \gcd(a, b)$ modulo $b$, a space of dimension $\deg \gcd(a, b)$. The centralizer is the ring of module endomorphisms of $\bigoplus_i F[x]/(d_i)$. Since $\gcd(d_i, d_j) = d_{\min(i, j)}$, the index $i$ occurs as $\min(j, k)$ for $2(r - i) + 1$ pairs.

25. From $QB = AQ$ you get $XB = AX$ and $YB = AY$. The polynomial $p(t) = \det(X + tY)$ has real coefficients and $p(i) = \det Q \ne 0$, so it is not zero, and $p(t) \ne 0$ for some real $t$. Take $P = X + tY$.

26. $J^{-1} - \lambda^{-1} I = -\lambda^{-1} J^{-1} N$ with $N = J - \lambda I$, and $J^{-1}$ commutes with $N$ and is invertible, so the $j$-th power has rank $k - j$. A nilpotent matrix with these ranks is a single block.

27. Sort the classes by the degrees of the polynomials that carry nonempty partitions. One linear polynomial with a partition of $3$: $3(q - 1)$. Two linear ones with partitions of $2$ and $1$: $2(q - 1)(q - 2)$. Three linear ones: $\binom{q - 1}{3}$. One linear and one quadratic: $(q - 1)(q^2 - q)/2$. One cubic: $(q^3 - q)/3$. The sum is $q^3 - q$.

28. If $\lambda \ne 0$ were an eigenvalue in an algebraic closure, so would be $c\lambda$ for infinitely many $c$, which is impossible. So $\chi_A = x^n$. Conversely $cN$ is nilpotent with the same ranks of powers as $N$. Over $\mathbb{F}_2$ the only $c$ is $1$, so every matrix, such as $I$, has the property.
