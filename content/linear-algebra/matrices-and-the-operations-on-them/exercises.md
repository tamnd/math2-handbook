1. ◦ Let $A = \begin{pmatrix} 1 & -2 & 0 & 4 \\ 3 & 5 & -1 & 2 \end{pmatrix}$ and let $B$ be a $4 \times 3$ [matrix](/0VD9ZSWWJG/). Give the size of $A$ and the entries $a_{23}$ and $a_{14}$. Which of the products $AB$ and $BA$ is defined, and what is its size?

2. ◦ Compute $AB$ and $BA$ for $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$.

3. ◦ Compute the [matrix–vector product](/0PDVQEP0ZC/) $\begin{pmatrix} 2 & -1 & 0 \\ 1 & 3 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$ once by rows and once as a combination of the columns.

4. ◦ A student writes $(AB)^{\mathsf T} = A^{\mathsf T} B^{\mathsf T}$. Let $A$ be $2 \times 3$ and $B$ be $3 \times 4$. Show that the right side is not even defined, and state the correct rule for the [transpose of a product](/09GK5PS824/).

5. ◦ Let $A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix}$. Compute $AB$, $BA$ and their [traces](/0XC1RDBY7A/).

6. ◦ Say for each matrix whether it is [symmetric](/0VR671PHE5/), [skew-symmetric](/0PBY4E9GQF/), both or neither:
$$\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}, \quad \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}, \quad \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$

7. ◦ Let $N$ be the $4 \times 4$ matrix with $1$ in the positions $(1, 2)$, $(2, 3)$, $(3, 4)$ and $0$ elsewhere. Compute $N^2$, $N^3$ and $N^4$. Is $N$ [nilpotent](/07BSPZPSMF/), and what is the least $k$ with $N^k = 0$?

8. ◦ Compute the [conjugate transpose](/0DXKE10PHF/) of $\begin{pmatrix} 1 & i \\ 2 & 3 - i \end{pmatrix}$. Which of $\begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix}$ and $\begin{pmatrix} i & 1 \\ 1 & i \end{pmatrix}$ is [Hermitian](/0P17NGQQMQ/)?

9. • Let $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$. Show that $(A - 2I)(A - 3I) = 0$, although neither factor is $0$. What does this say about cancellation in the [matrix ring](/AB2MD5CD13/)?

10. • Find all real $2 \times 2$ matrices that [commute](/8G3X8MPG7E/) with $J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

11. • Prove that for square matrices $A$ and $B$ of the same size, $(A + B)^2 = A^2 + 2AB + B^2$ if and only if $AB = BA$.

12. • Write $A = \begin{pmatrix} 1 & 4 & 0 \\ 2 & 3 & -1 \\ 6 & 5 & 2 \end{pmatrix}$ as the sum of a symmetric and a skew-symmetric matrix.

13. • Let $P = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a + d = 1$ and $ad - bc = 0$. Prove that $P$ is [idempotent](/0KCE8CG86P/), and check it for $P = \begin{pmatrix} 2 & -2 \\ 1 & -1 \end{pmatrix}$. Show that $I - P$ is then idempotent too.

14. • Let $A$ be a real square matrix. Prove that $A$ is [involutory](/NH2QE3671N/), $A^2 = I$, if and only if $P = \tfrac12 (I + A)$ is idempotent.

15. • Let $X$ be an $n \times n$ matrix and $M = \begin{pmatrix} I & X \\ 0 & I \end{pmatrix}$, a [block matrix](/0ASDFEQS6P/) of size $2n \times 2n$. Prove that $M^k = \begin{pmatrix} I & kX \\ 0 & I \end{pmatrix}$ for every $k \ge 1$, and find $M^{-1}$.

16. • Let $E_{11}$ be the $n \times n$ [matrix unit](/4H93XF4RVH/) with a single $1$ in position $(1, 1)$. Find all $n \times n$ matrices $A$ with $AE_{11} = E_{11}A$.

17. • Prove that for every real $m \times n$ matrix $A$, $\operatorname{tr}(A^{\mathsf T} A)$ is the sum of the squares of the entries of $A$. Deduce that $A^{\mathsf T} A = 0$ only if $A = 0$.

18. • Let $U = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{pmatrix}$ and $N = U - I$. Show that $N^3 = 0$, prove that $(I + N)(I - N + N^2) = I$, and use this to compute $U^{-1}$.

19. • Let $A$ and $B$ be symmetric $n \times n$ matrices. Prove that $AB$ is symmetric if and only if $AB = BA$. Prove also that $C^{\mathsf T} C$ is symmetric for every $m \times n$ matrix $C$.

20. ★ Prove that an $n \times n$ matrix over a field that commutes with every $n \times n$ matrix is a [scalar matrix](/067NKSBEWT/) $cI$. (Use the matrix units $E_{ij}$.)

21. ★ Let $A$ be a $2 \times 2$ matrix over a field. Check by computation that $A^2 = (\operatorname{tr} A)\, A - (\det A)\, I$, where $\det A = a_{11}a_{22} - a_{12}a_{21}$. Deduce that $A^2 = 0$ if and only if $\operatorname{tr} A = 0$ and $\det A = 0$.

22. ★ Find all idempotent $2 \times 2$ matrices over $\F_2$, and say how many there are.

23. ★ Let $A$ be a real symmetric matrix with $A^k = 0$ for some $k \ge 1$. Prove that $A = 0$. Give a real $2 \times 2$ matrix that shows the hypothesis "symmetric" is needed.

24. ★ Let $X$ be an $n \times n$ matrix over a field with $\operatorname{tr}(XA) = 0$ for every $n \times n$ matrix $A$. Prove that $X = 0$. (Compute $\operatorname{tr}(X E_{ij})$.)
