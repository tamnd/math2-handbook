1. $A e_1 = e_1$, so $m_{e_1} = x - 1$. $A (1, 1) = (3, 3)$, so $m_{(1,1)} = x - 3$. For $e_2$, the vectors $e_2$ and $A e_2 = (2, 3)$ are independent and $A^2 e_2 = (8, 9) = 4 A e_2 - 3 e_2$, so $m_{e_2} = x^2 - 4x + 3$. Only $e_2$ is a cyclic vector.

2. $C(p) = \begin{pmatrix} 0 & 0 & -6 \\ 1 & 0 & -1 \\ 0 & 1 & 4 \end{pmatrix}$ and $p = (x + 1)(x - 2)(x - 3)$. Both polynomials equal $p$, $\det C(p) = (-1)^3 \cdot 6 = -6$, and $C(p)$ is diagonalizable over $\Q$ because the three roots are distinct rationals.

3. Group by irreducible factor: $(x - 1)$ and $(x - 1)^2$; $(x + 2)$ and $(x + 2)$; $(x^2 + 1)$. The largest powers multiply to $d_2 = (x - 1)^2 (x + 2)(x^2 + 1)$ and the rest to $d_1 = (x - 1)(x + 2)$. The size is $7$, $\chi = d_1 d_2 = (x - 1)^3 (x + 2)^2 (x^2 + 1)$ and $m = d_2$.

4. The size is $1 + 2 + 4 = 7$. The elementary divisors are $x - 2$, $x - 2$, $(x - 2)^2$, $x + 1$, $(x + 1)^2$, so the Jordan form is $J_1(2) \oplus J_1(2) \oplus J_2(2) \oplus J_1(-1) \oplus J_2(-1)$. The eigenspaces have dimensions $3$ and $2$, the numbers of blocks.

5. $\chi_A = m_A = (x - 1)^2 (x + 1) = x^3 - x^2 - x + 1$, so $A$ is cyclic and its rational canonical form is $\begin{pmatrix} 0 & 0 & -1 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$.

7. With $r_0, \dots, r_4 = 6, 3, 1, 0, 0$, the numbers of blocks of sizes $1, 2, 3$ are $1, 1, 1$. So $N \sim J_3(0) \oplus J_2(0) \oplus J_1(0)$, with $3$ blocks, and $\dim \ker N^2 = 5$.

9. The eigenvalues are $1 \pm i$, so the real form is $R(1, 1) = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. The matrix $P = \begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix}$ works: both $A P$ and $P R(1, 1)$ equal $\begin{pmatrix} 4 & -2 \\ 2 & 0 \end{pmatrix}$.

10. The entry $-4$ gives $D_1 = 1$. The $2 \times 2$ minors include $(x - 3)^2$, $4(x - 3)$ and $(x - 3)(x + 1)$, and all are multiples of $x - 3$, so $D_2 = x - 3$. $D_3 = (x - 3)^2 (x + 1)$. The Smith form is $\operatorname{diag}(1, x - 3, (x - 3)(x + 1))$, and the rational form is $C(x - 3) \oplus C(x^2 - 2x - 3)$. $A$ is diagonalizable, since $m_A = (x - 3)(x + 1)$ has simple roots.

11. (a) Two classes: invariant factors $(x^2 + 1)^2$, or $x^2 + 1, x^2 + 1$. (b) Over $\C$ the blocks for $i$ are $J_2(i)$ or $J_1(i) \oplus J_1(i)$, and the same for $-i$, which gives $4$ classes. A class that contains a rational matrix has rational invariant factors, and only the two choices with the same block sizes for $i$ and $-i$ have them.

12. The number of blocks is right, but $4 = 3 + 1$ as well as $2 + 2$. Compute $\operatorname{rank}(A - 2I)^2 = 1$: then there is one block of size at least $3$, and the form is $J_3(2) \oplus J_1(2)$.

13. The ranks of $(A - I)^j$ are $2, 1, 0$, so the form is $J_3(1)$. The vector $e_3$ is not killed by $(A - I)^2$; the chain is $e_3$, $(A - I) e_3 = (0, 1, 1)$, $(A - I)^2 e_3 = (1, 1, 1)$, and $P$ has the columns $(1, 1, 1)$, $(0, 1, 1)$, $e_3$.

14. (a) $N e_2 = e_1$ and $N e_4 = e_3$; in the order $e_1, e_3, e_2, e_4$ the matrix is $W$. (b) Writing $X$ in $2 \times 2$ blocks, $X W = W X$ forces $X_{21} = 0$ and $X_{22} = X_{11}$, so $X = \begin{pmatrix} Y & Z \\ 0 & Y \end{pmatrix}$ with $Y, Z$ arbitrary: dimension $8$. (c) The invariant factors are $x^2, x^2$, and $4 \cdot 2 = 8$.

15. Scalar: $4$. Two distinct eigenvalues: $\binom{4}{2} = 6$. Not diagonalizable, $J_2(a)$ with $a \ne 0$: $4$. Irreducible: the number of monic irreducible quadratics over $\mathbb{F}_5$, $(25 - 5)/2 = 10$. Total $24$.

18. The kernels of $N, N^2, N^3, N^4$ have dimensions $3, 4, 5, 6$, so the Weyr structure is $(3, 1, 1, 1)$ and the centralizer has dimension $9 + 1 + 1 + 1 = 12$. The invariant factors $x, x, x^4$ give $1 \cdot 8 + 4 = 12$ as well.

19. $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$, with complex roots $-1 \pm i\sqrt3$. The real Jordan form is $J_1(2) \oplus R(-1, \sqrt 3)$.

21. If $A \sim 2A$, the set of eigenvalues is closed under multiplication by $2$; being finite, it is $\set{0}$. Conversely, with $D = \operatorname{diag}(1, 2, \dots, 2^{k-1})$ one has $D^{-1} J_k(0) D = 2 J_k(0)$; apply this to each block of the Jordan form.

22. $J_n(0)^2$ sends $e_i \mapsto e_{i-2}$, so the odd-indexed and even-indexed basis vectors form two chains, of lengths $\lceil n/2 \rceil$ and $\lfloor n/2 \rfloor$.

23. With one invariant factor there are $q^3$ monic cubics. With two, $d_1 = x - a$ and $d_2 = (x - a)(x - b)$, which gives $q^2$ lists. With three, $d_1 = d_2 = d_3 = x - a$, which gives $q$. For $q = 2$ the total is $14$.

24. $V_A \cong F[x] / (\chi_A)$, whose submodules are the ideals $(g) / (\chi_A)$ with $g \mid \chi_A$. The image of $(g)/(\chi_A)$ is $\operatorname{im} g(A) = \ker f(A)$ with $f = \chi_A / g$, of dimension $\deg f$. For $(x - 1)^2 (x - 2)$ there are $3 \cdot 2 = 6$ monic divisors, so $6$ invariant subspaces.

25. (a) Reduce to one block $J_k(\lambda) = \lambda (I + N/\lambda)$ with $\lambda \ne 0$: take $\mu$ with $\mu^2 = \lambda$ and the binomial series of $(1 + t)^{1/2}$, which stops because $N^k = 0$. For $J_2(4)$: $B = \begin{pmatrix} 2 & 1/4 \\ 0 & 2 \end{pmatrix}$. (b) If $B^2 = J_2(0)$, then $B^4 = 0$, so $B$ is a nilpotent $2 \times 2$ matrix and $B^2 = 0$.
