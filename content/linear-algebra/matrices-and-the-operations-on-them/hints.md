1. $A$ is $2 \times 4$, $a_{23} = -1$ and $a_{14} = 4$. Only $AB$ is defined, and it is $2 \times 3$; $BA$ would need $3 = 2$.

2. $AB = \begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$, so $AB \neq BA$.

5. $AB = \begin{pmatrix} 1 & 7 \\ 2 & 3 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 1 & 3 \\ 2 & 0 & 4 \\ 0 & 3 & 3 \end{pmatrix}$. The two products have different sizes, but both traces are $4$, as the [cyclic property of the trace](/0Y4NF1DRKD/) says.

7. $N^2$ has $1$ in positions $(1, 3)$ and $(2, 4)$, $N^3$ has a single $1$ in position $(1, 4)$, and $N^4 = 0$. So $N$ is nilpotent, and the least $k$ is $4$.

8. $\begin{pmatrix} 1 & 2 \\ -i & 3 + i \end{pmatrix}$. The first matrix is Hermitian. The second is not: its diagonal entries are not real, and in fact it is symmetric.

10. Write $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and compare $XJ$ with $JX$. The equations give $c = 0$ and $a = d$, so the answer is all matrices $\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$, that is, $aI + b(J - I)$.

16. $AE_{11}$ keeps the first column of $A$ and makes the rest $0$, and $E_{11}A$ keeps the first row. They agree exactly when $a_{1j} = 0$ and $a_{j1} = 0$ for all $j \neq 1$: the first row and the first column are $0$ off the diagonal.

18. $N^2$ has the single nonzero entry $8$ in position $(1, 3)$, and $N^3 = 0$. Expanding, $(I + N)(I - N + N^2) = I + N^3 = I$. So $U^{-1} = I - N + N^2 = \begin{pmatrix} 1 & -2 & 5 \\ 0 & 1 & -4 \\ 0 & 0 & 1 \end{pmatrix}$.

20. Let $A$ commute with all matrices. Then $AE_{ij} = E_{ij}A$. The left side has the $i$-th column of $A$ in column $j$ and zeros elsewhere; the right side has the $j$-th row of $A$ in row $i$ and zeros elsewhere. Comparing the entries gives $a_{ki} = 0$ for $k \neq i$ and $a_{ii} = a_{jj}$.

21. For the converse, suppose $A^2 = 0$, so that $(\operatorname{tr} A)\, A = (\det A)\, I$. If $A$ is not a scalar matrix, both coefficients must be $0$. If $A = cI$, then $A^2 = c^2 I = 0$ gives $c = 0$.

22. Besides $0$ and $I$, an idempotent matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ has trace $1$ and determinant $0$ by the identity of the previous exercise, so $\set{a, d} = \set{0, 1}$ and $bc = 0$. This gives $3 + 3 = 6$ more, so $8$ in all: $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$.

23. Every power of $A$ is symmetric. If $A^{2m} = 0$, then $\operatorname{tr}\big((A^m)^{\mathsf T} A^m\big) = \operatorname{tr}(A^{2m}) = 0$, so $A^m = 0$, since the trace of $C^{\mathsf T} C$ is the sum of the squares of the entries of $C$. Start from a power $2^j \ge k$ and halve the exponent $j$ times. The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has square $0$.

24. The only nonzero column of $XE_{ij}$ is column $j$, which is the $i$-th column of $X$. So its trace is the entry $x_{ji}$. All these are $0$.
