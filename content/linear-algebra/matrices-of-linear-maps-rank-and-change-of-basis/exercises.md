1. ◦ Let $P_2$ be the real polynomials of degree at most $2$, with basis $1, x, x^2$. Find the [matrix](/0YQSGNYE3K/) of $T(p) = p + p'$ in this basis.

2. ◦ Let $A = \begin{pmatrix} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & 1 & 0 & 1 \\ 1 & 1 & 3 & 1 & 1 \end{pmatrix}$. Find the rank of $A$ and the dimensions of its [four fundamental subspaces](/73DVECPAT6/), and give a nonzero vector of its left null space.

3. ◦ Find the error: "The reduced row echelon form of $A = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$ is $R = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, whose pivot column is $(1, 0)$. So $(1, 0)$ is a basis of the column space of $A$." What is a correct basis?

4. ◦ Let $B'$ be the basis $(1, 2)$, $(1, 3)$ of $\R^2$. Write down the [change of basis matrix](/0MKRHZB3WS/) $P$ from the standard basis to $B'$, and find $[v]_{B'}$ for $v = (4, 9)$.

5. ◦ Which pairs are [similar](/0E89HQATM8/) over $\R$? (a) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$. (b) $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}$. (c) $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and the zero matrix.

6. ◦ Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$. Find the [trace](/0KZDNGA561/) of the linear map $X \mapsto AX$ on $M_2(\R)$.

7. ◦ Let $A$ be a $3 \times 5$ matrix of rank $3$ and $B$ a $5 \times 4$ matrix of rank $4$. What do the inequalities for the [rank of a product](/02FDWY55AS/) say about $\operatorname{rank}(AB)$?

8. ◦ Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}$. Use the [Fredholm alternative](/4HH8C9V8JQ/) to find the condition on $b$ for $Ax = b$ to be solvable. Is $Ax = (1, 2, 3)$ solvable? Is $Ax = (1, 1, 2)$?

9. • Let $T \colon P_2 \to \R^3$ be $T(p) = (p(-1), p(0), p(1))$. Find the matrix of $T$ in the basis $1, x, x^2$ and the standard basis, and show that $T$ is an isomorphism.

10. • Let $S(x, y) = (x + y, y)$ and $T(x, y) = (2x, x - y)$ on $\R^2$. Find the matrices of $T \circ S$ and $S \circ T$, once by composing the maps and once by multiplying matrices, and check that they agree.

11. • Let $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \\ 1 & 2 & 2 \end{pmatrix}$. Find a basis of each of the four fundamental subspaces, check that the null space is orthogonal to the row space and the left null space to the column space, and write $A = CR$ as in the [rank factorization](/5JGAG62VN8/).

12. • Show that $\operatorname{rank}(A^\top A) = \operatorname{rank} A$ for every real matrix $A$. Then show that this fails over $\C$ with the plain transpose, using $A = \begin{pmatrix} 1 \\ i \end{pmatrix}$.

13. • Let $T(x, y) = (4x - 2y, x + y)$. Use the [change of basis formula](/0MQXVZEBMT/) to find the matrix of $T$ in the basis $(1, 1)$, $(2, 1)$.

14. • Find an invertible $P$ with $P^{-1} A P = A^\top$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

15. • Let $A, B \in M_n(F)$. Find the traces of the linear maps $X \mapsto AXB$ and $X \mapsto AX - XA$ on $M_n(F)$.

16. • Find the rank of $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ over $\Q$ and over $\F_2$.

17. • Can a $5 \times 3$ matrix have a null space of dimension $1$ and a left null space of dimension $2$? Use [rank–nullity for matrices](/TR48YQGCCA/).

18. • Show that $\operatorname{rank}(A + B) \le \operatorname{rank} A + \operatorname{rank} B$. Give $2 \times 2$ examples where equality holds and where it fails.

19. • Let $T(p) = x p'$ on $P_2$. Its matrix in the basis $1, x, x^2$ is $\operatorname{diag}(0, 1, 2)$. Find its matrix in the basis $1, 1 + x, 1 + x + x^2$.

20. • Let $A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 4 & 7 \end{pmatrix}$. Find a basis of $\operatorname{Null}(A^\top)$ and the condition on $b$ for $Ax = b$ to be solvable.

21. ★ Show that two complex $2 \times 2$ matrices are similar if and only if they have the same trace and the same determinant and either both or neither of them are multiples of $I$.

22. ★ Let $f$ be a linear form on $M_n(F)$ with $f(AB) = f(BA)$ for all $A, B$. Show that $f = c \operatorname{tr}$ for some $c \in F$.

23. ★ Prove the Frobenius inequality $\operatorname{rank}(AB) + \operatorname{rank}(BC) \le \operatorname{rank} B + \operatorname{rank}(ABC)$ for matrices of compatible sizes.

24. ★ Let $A$ be an $n \times n$ matrix with $A^2 = 0$. Show that $\operatorname{rank} A \le n/2$, and give a $4 \times 4$ example with rank $2$.

25. ★ Let $T \colon M_n(F) \to M_n(F)$ be the transpose, $T(X) = X^\top$. Show that $\operatorname{tr} T = n$ and $\det T = (-1)^{n(n-1)/2}$.
