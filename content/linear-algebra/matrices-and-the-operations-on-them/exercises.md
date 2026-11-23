1. ◦ Let $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$. Compute $AB$ and $BA$, and name one entry in which they differ.

2. ◦ Let $A$ be $2 \times 3$, $B$ be $3 \times 4$ and $C$ be $4 \times 2$. For each of $AB$, $BA$, $ABC$, $CAB$, $BCA$ and $A + C^{\mathsf{T}}$, say whether it is defined and, if so, give its size.

3. ◦ Write $\begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$ as a combination of the columns of the matrix, and evaluate it.

4. ◦ Let $A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 3 \end{pmatrix}$. Compute $AB$ and $BA$. They have different sizes; compare their [traces](/0XC1RDBY7A/).

5. ◦ A student writes $(A + B)(A - B) = A^2 - B^2$ for square matrices. Test the claim with the [matrix units](/A4HTT7JFD1/) $A = E_{11}$ and $B = E_{12}$ of size $2 \times 2$, and name the law the student used that fails for matrices.

6. ◦ Classify each real matrix as [symmetric](/0VR671PHE5/), [skew-symmetric](/0PBY4E9GQF/), both or neither: $\begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}$, $\begin{pmatrix} 2 & 5 \\ 5 & -1 \end{pmatrix}$, the $2 \times 2$ zero matrix, $\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$.

7. ◦ Which of these complex matrices are [Hermitian](/0P17NGQQMQ/)? $\begin{pmatrix} 2 & 3 - i \\ 3 + i & -1 \end{pmatrix}$, $\begin{pmatrix} 1 & i \\ i & 2 \end{pmatrix}$, $\begin{pmatrix} i & 0 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 0 & -2i \\ 2i & 5 \end{pmatrix}$. For each one that is not, name an entry that breaks the condition.

8. ◦ Compute the squares of $P = \begin{pmatrix} 2 & -2 \\ 1 & -1 \end{pmatrix}$, $N = \begin{pmatrix} 3 & 9 \\ -1 & -3 \end{pmatrix}$ and $S = \begin{pmatrix} 5 & -12 \\ 2 & -5 \end{pmatrix}$. Which is [idempotent](/0KCE8CG86P/), which is [nilpotent](/07BSPZPSMF/) and which is [involutory](/NH2QE3671N/)?

9. ◦ Use $E_{ij} E_{kl} = \delta_{jk} E_{il}$ for the $3 \times 3$ matrix units to evaluate $E_{13} E_{32} E_{21}$, $E_{21} E_{13} E_{32}$ and $E_{13} E_{13}$ without writing out any matrix.

10. • Find all real $2 \times 2$ matrices $X$ with $XJ = JX$, where $J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Write the answer in the form $aI + bN$ for a fixed matrix $N$.

11. • Show that for square matrices $A$ and $B$ over a field, $(A + B)^2 = A^2 + 2AB + B^2$ holds if and only if $AB = BA$.

12. • Write $A = \begin{pmatrix} 1 & 4 & 0 \\ 2 & 3 & -1 \\ 6 & 5 & 2 \end{pmatrix}$ as the sum of a symmetric and a skew-symmetric matrix, and check that both parts have the right shape.

13. • Let $U = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{pmatrix}$. Write $U = I + N$ with $N$ strictly upper triangular, compute $N^2$ and $N^3$, and use the result to find $U^{-1}$ as a polynomial in $N$. Check your answer by multiplying.

14. • Let $X$ be an $n \times n$ matrix over a field with $\operatorname{tr}(XA) = 0$ for every $n \times n$ matrix $A$. Prove that $X = 0$. (Compute $\operatorname{tr}(X E_{ji})$.)

15. • For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ over a commutative ring, verify by direct computation that $A^2 - (a + d) A + (ad - bc) I = 0$. Deduce that a $2 \times 2$ matrix with trace $1$ and $ad - bc = 0$ is idempotent, and give one such matrix with no zero entry.

16. • List all idempotent $2 \times 2$ matrices over the field $\F_2$ with two elements, and check that there are eight.

17. • A student argues: "If $A$ and $B$ are symmetric, then $(AB)^{\mathsf{T}} = A^{\mathsf{T}} B^{\mathsf{T}} = AB$, so $AB$ is symmetric." Find the error, and give real symmetric $A$ and $B$ with $AB$ not symmetric.

18. • Let $X$ be any $2 \times 2$ matrix. Show with [block multiplication](/0ASDFEQS6P/) that $\begin{pmatrix} I_2 & X \\ 0 & -I_2 \end{pmatrix}$ is an involutory $4 \times 4$ matrix. Conclude that there are infinitely many real involutory $4 \times 4$ matrices.

19. • Let $M$ and $N$ be square matrices over a commutative ring with $MN = NM$, $M^p = 0$ and $N^q = 0$. Prove that $(M + N)^{p + q - 1} = 0$. Then show that the hypothesis $MN = NM$ cannot be dropped, using $E_{12}$ and $E_{21}$.

20. • Find Hermitian $H$ and $K$ with $A = H + iK$ for $A = \begin{pmatrix} 1 & 2 + 2i \\ 0 & 3i \end{pmatrix}$.

21. • Prove that a real matrix $A$ with $A^{\mathsf{T}} A = 0$ is zero. Then show that $A = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ has $A^{\mathsf{T}} A = 0$, and compute $A^* A$ for the same matrix.

22. ★ Let $N$ be the $3 \times 3$ matrix with $1$ in positions $(1,2)$ and $(2,3)$ and $0$ elsewhere. Find all $3 \times 3$ matrices over a field that commute with $N$, and show that they are exactly the polynomials $aI + bN + cN^2$.

23. ★ Prove that a matrix $C \in M_n(F)$ over a field that commutes with every $E_{ij}$ is a scalar matrix. Deduce the [centre of the matrix ring](/DVZ1V4A884/).

24. ★ Prove that there are no $n \times n$ matrices $A$ and $B$ over $\Q$ with $AB - BA = I$. Then show that over $\F_2$ the matrices $E_{12}$ and $E_{21}$ of size $2 \times 2$ satisfy $AB - BA = I$, and say which step of your proof fails there.

25. ★ Let $f$ be a linear map from $M_n(F)$ to $F$ with $f(AB) = f(BA)$ for all $A$ and $B$. Prove that $f = c \operatorname{tr}$ for some $c \in F$. (Look at $f(E_{ij})$ for $i \ne j$, and at $f(E_{ii}) - f(E_{jj})$.)

26. ★ Prove that a real symmetric nilpotent matrix is zero. Give a complex symmetric $2 \times 2$ matrix that is nilpotent and not zero.
