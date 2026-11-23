1. $AB = \begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$. They differ in both diagonal entries.

2. $AB$ is $2 \times 4$; $BA$ is not defined; $ABC$ is $2 \times 2$; $CAB$ is $4 \times 4$; $BCA$ is $3 \times 3$; $A + C^{\mathsf{T}}$ is not defined, because $C^{\mathsf{T}}$ is $2 \times 4$.

5. The left side is $E_{11} - E_{12}$ and the right side is $E_{11}$. Expanding gives $A^2 - AB + BA - B^2$, and the student cancelled $-AB + BA$, which needs $AB = BA$. Here $AB = E_{12}$ and $BA = 0$.

8. $P^2 = P$, $N^2 = 0$ and $S^2 = I$. So $P$ is idempotent, $N$ is nilpotent and $S$ is involutory.

10. Write $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$; $XJ = JX$ reduces to $c = 0$ and $a = d$. So $X = aI + bN$ with $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

12. $S = \tfrac12 (A + A^{\mathsf{T}}) = \begin{pmatrix} 1 & 3 & 3 \\ 3 & 3 & 2 \\ 3 & 2 & 2 \end{pmatrix}$ and $K = \tfrac12 (A - A^{\mathsf{T}}) = \begin{pmatrix} 0 & 1 & -3 \\ -1 & 0 & -3 \\ 3 & 3 & 0 \end{pmatrix}$.

13. $N^2$ has $8$ in position $(1,3)$ and zeros elsewhere, and $N^3 = 0$. So $U^{-1} = I - N + N^2 = \begin{pmatrix} 1 & -2 & 5 \\ 0 & 1 & -4 \\ 0 & 0 & 1 \end{pmatrix}$.

16. Write $t$ for the trace and $d = ad - bc$. Subtracting the identity of exercise 15 from $P^2 = P$ gives $(1 - t)P = -dI$, so an idempotent other than $0$ and $I$ has $t = 1$ and $d = 0$. The six of these are $E_{11}$, $E_{22}$, $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$.

19. The [binomial theorem for commuting matrices](/DS9TS6AFMW/) writes $(M + N)^{p+q-1}$ as a sum of multiples of $M^k N^{p+q-1-k}$; in each term $k \ge p$ or $p + q - 1 - k \ge q$. Both $E_{12}$ and $E_{21}$ square to $0$, but $(E_{12} + E_{21})^2 = I$, so no power of the sum is $0$.

20. Take $H = \tfrac12 (A + A^*)$ and $K = \tfrac{1}{2i} (A - A^*)$. This gives $H = \begin{pmatrix} 1 & 1 + i \\ 1 - i & 0 \end{pmatrix}$ and $K = \begin{pmatrix} 0 & 1 - i \\ 1 + i & 3 \end{pmatrix}$.

22. Write the commuting matrix as $X = (x_{ij})$. The product $XN$ shifts the columns of $X$ one place to the right, and $NX$ shifts its rows one place up. Equating them forces $X$ to be upper triangular with constant diagonals, which is $aI + bN + cN^2$.

23. $C E_{ij}$ has column $j$ equal to column $i$ of $C$, and zeros elsewhere; $E_{ij} C$ has row $i$ equal to row $j$ of $C$, and zeros elsewhere. Comparing the two gives $c_{ki} = 0$ for $k \ne i$ and $c_{ii} = c_{jj}$.

24. Over $\Q$ the trace of $AB - BA$ is $0$, while $\operatorname{tr} I = n \ne 0$. Over $\F_2$, $E_{12} E_{21} - E_{21} E_{12} = E_{11} - E_{22} = E_{11} + E_{22} = I$. The step that fails is $n \ne 0$, since $2 = 0$ in $\F_2$.

25. For $i \ne j$, $E_{ij} = E_{ii} E_{ij}$ while $E_{ij} E_{ii} = 0$, so $f(E_{ij}) = 0$. Also $E_{ij} E_{ji} = E_{ii}$ and $E_{ji} E_{ij} = E_{jj}$, so all $f(E_{ii})$ are equal to one value $c$. Linearity gives $f(A) = c \sum_i a_{ii}$.

26. For real symmetric $A$, $\operatorname{tr}(A^2) = \operatorname{tr}(A^{\mathsf{T}} A) = \sum_{i,j} a_{ij}^2$. If $A$ is nilpotent, so is $A^2$, and a nilpotent matrix has trace $0$. The matrix of exercise 21 is complex symmetric, nonzero and squares to $0$.
