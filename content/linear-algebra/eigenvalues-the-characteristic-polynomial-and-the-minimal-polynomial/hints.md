1. $p_A(t) = t^2 - 5t + 6 = (t - 2)(t - 3)$. The vector $(1, 1)$ is an eigenvector for $2$, and $(2, 1)$ is one for $3$.

2. $A(1, 2, 1) = (3, 2, 3)$, which is not a multiple of $(1, 2, 1)$. $A(1, 1, 1) = 2(1, 1, 1)$, with eigenvalue $2$, and $A(1, 0, -1) = (1, 0, -1)$, with eigenvalue $1$. Since $\operatorname{tr} A = 2$, the third eigenvalue is $2 - 2 - 1 = -1$.

3. $\operatorname{tr} A = 9$. The principal minors are $5$, $8$ and $11$, with sum $24$, and $\det A = 18$. So $p_A(t) = t^3 - 9t^2 + 24t - 18$.

5. $p_A(t) = (t - 5)^2 (t - 2)$, so $a(5) = 2$ and $a(2) = 1$. The matrix $A - 5I$ has rank $2$, so $g(5) = 1$, and $g(2) = 1$. There is no basis of eigenvectors, since $1 + 1 < 3$.

6. $p_A(t) = t^2 - 2t + 2$, with discriminant $-4$. The spectrum is empty over $\R$, $\set{1 + i, 1 - i}$ over $\C$, $\set{3, 4}$ over $\F_5$, and empty over $\F_3$, where $p_A$ takes the values $2, 1, 2$ at $0, 1, 2$.

7. For $\operatorname{diag}(2, 2, 5)$, $(A - 2I)(A - 5I) = 0$, so $m = (x - 2)(x - 5)$, while $p = (x - 2)^2 (x - 5)$. For the second matrix $(A - 2I)(A - 5I) \ne 0$, so $m = p = (x - 2)^2 (x - 5)$.

8. $p_A(t) = t^2 - 4t + 1$, so $A^2 = 4A - I$. Then $A(4I - A) = I$ gives $A^{-1} = 4I - A = \begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix}$, and $A^3 = 4A^2 - A = 15A - 4I = \begin{pmatrix} 41 & 15 \\ 30 & 11 \end{pmatrix}$.

10. $p_A(t) = (t - 1)(t - 3)^2$. $E_1$ is spanned by $(1, -1, 0)$ and $E_3$ by $(1, 1, 0)$, so $g(3) = 1 < 2 = a(3)$ and there is no basis of eigenvectors. The product $(A - I)(A - 3I)$ is not $0$, so $m_A = (x - 1)(x - 3)^2$.

12. Solve $\pi(P - I) = 0$: this gives $\pi_2 = 2\pi_1$, so $\pi = (1/3, 2/3)$. The trace is $5/4$, so the other eigenvalue is $1/4$, with right eigenvector $v = (2, -1)$. Then $\pi v = 2/3 - 2/3 = 0$.

16. The minimal polynomial divides $(x - 1)(x - 2)$ and has degree $2$, because $A$ is not a multiple of $I$; so $m_A = (x - 1)(x - 2)$. The characteristic polynomial has degree $3$, its roots are $1$ and $2$, and both occur: $(x - 1)^2 (x - 2)$ or $(x - 1)(x - 2)^2$.

17. The minimal polynomial is $(x - 2)(x + 1)$, for example for $\operatorname{diag}(2, 2, -1)$, or $(x - 2)^2 (x + 1)$, for example for $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & -1 \end{pmatrix}$.

20. Take the trace: $\operatorname{tr}(AB - BA) = 0$, but $\operatorname{tr} I = n \ne 0$ in characteristic $0$. Over $\F_2$, $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ give $AB - BA = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = I$.

22. If $A$ is invertible, $BA = A^{-1}(AB)A$ is similar to $AB$. For general $A$, the matrix $A - sI$ is invertible for all but at most $n$ values of $s$. Both $\det(tI - (A - sI)B)$ and $\det(tI - B(A - sI))$ are polynomials in $s$ and $t$, so they agree for all $s$, in particular for $s = 0$.

23. With $g = \dim E_\lambda$, the matrix of $T$ in the extended basis is $\begin{pmatrix} \lambda I_g & C \\ 0 & D \end{pmatrix}$. So $p_T(t) = (t - \lambda)^g p_D(t)$, and $(t - \lambda)^g$ divides $p_T$.

24. If $Av = \lambda v$, then $A(Bv) = BAv = \lambda Bv$, so $Bv \in E_\lambda$, which has dimension $1$; hence $Bv = \mu v$. In a basis of eigenvectors of $A$, both matrices are diagonal. Choose $f$ by Lagrange interpolation with $f(\lambda_i) = \mu_i$ for each $i$.

25. Let $\mu_1, \ldots, \mu_r$ be the distinct nonzero eigenvalues, with algebraic multiplicities $m_1, \ldots, m_r$, and suppose $r \ge 1$. Then $\sum_j m_j \mu_j^k = \operatorname{tr}(A^k) = 0$ for $k = 1, \ldots, r$. The matrix $(\mu_j^k)$ is a Vandermonde matrix times $\operatorname{diag}(\mu_j)$, so it is invertible, and every $m_j = 0$. So all eigenvalues are $0$, $p_A = t^n$, and Cayley-Hamilton gives $A^n = 0$.

26. $T$ maps $T^{k-1} v$ to $T^k v \in W$, so $W$ is invariant. $q(T) T^j v = T^j q(T) v = 0$, so $q(T|_W) = 0$, and no nonzero polynomial of degree less than $k$ kills $v$, by the choice of $k$. Since $m_T(T|_W) = 0$, the polynomial $q$ divides $m_T$, and the roots of $m_T$ in $F$ are eigenvalues.
