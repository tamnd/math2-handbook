1. ◦ Use the [formula for a $2 \times 2$ inverse](/8XWC7RKNN1/) to invert $\begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$, and use the inverse to solve $3x + 5y = 4$, $x + 2y = 1$.

2. ◦ For which real numbers $t$ is $\begin{pmatrix} t & 2 \\ 8 & t \end{pmatrix}$ invertible?

3. ◦ Write down the $3 \times 3$ [elementary matrices](/01REXW3WWE/) for the operations "exchange rows 2 and 3", "subtract $5$ times row 1 from row 3" and "multiply row 1 by $2$", and the inverse of each.

4. ◦ You are told that $A^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $B^{-1} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$. Find $(AB)^{-1}$ without computing $A$ or $B$.

5. ◦ Invert the upper triangular matrix $\begin{pmatrix} 2 & 4 & 0 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}$, and check that the diagonal of the inverse is as the [triangular case](/7X1B65CTG4/) predicts.

6. ◦ A student factors $A = \begin{pmatrix} 2 & 1 \\ 6 & 5 \end{pmatrix}$ as $LU$ with $L = \begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$. Multiply out $LU$, find the error, and give the correct $L$.

7. ◦ For each matrix, say whether it lies in $\mathrm{SL}_2(\Z)$, in $\mathrm{GL}_2(\Z)$, in $\mathrm{GL}_2(\Q)$, or in none of them: $\begin{pmatrix} 3 & 2 \\ 4 & 3 \end{pmatrix}$, $\begin{pmatrix} 2 & 3 \\ 1 & 1 \end{pmatrix}$, $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, $\begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$.

8. ◦ Decide which pairs are [equivalent](/0CMHSGTWXB/): $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ and $\begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$; $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $I_2$; $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$.

9. • [Compute the inverse by row reduction](/0Z83DHFMYM/) of $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}$, and check the answer by multiplying.

10. • Find the [LU decomposition](/0RKG5YW66Y/) of $A = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 5 & 7 \\ -1 & 2 & 4 \end{pmatrix}$. Check that the products $u_{11}$, $u_{11} u_{22}$ and $u_{11} u_{22} u_{33}$ are the leading principal minors of $A$, and use the factors to solve $Ax = (3, 9, 3)^{\mathsf{T}}$.

11. • Let $M = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 7 & 2 \\ 1 & 1 & 4 \end{pmatrix}$, with $A$ the upper left $2 \times 2$ block. Compute $A^{-1}$ and the [Schur complement](/6HWFBXYPZP/) $M/A$, deduce $\det M$, and find the last row of $M^{-1}$ from the block inverse formula.

12. • Use the [Sherman-Morrison formula](/MDZDEFE53C/) to invert $I_3 + uv^{\mathsf{T}}$ for $u = (1, 2, 3)^{\mathsf{T}}$ and $v = (1, 1, 1)^{\mathsf{T}}$.

13. • A square matrix $A$ satisfies $A^2 = A + I$. Show that $A$ is invertible and express $A^{-1}$ as a polynomial in $A$.

14. • Write $\begin{pmatrix} 3 & 2 \\ 4 & 3 \end{pmatrix}$ as a product of three [transvections](/0DTCBCKEJP/), by reducing it to $I_2$ with row replacements only.

15. • Count the elements of $\mathrm{GL}_2(\F_3)$ by counting the possible first and second columns, and deduce the order of $\mathrm{SL}_2(\F_3)$.

16. • A student claims that every invertible matrix has an LU decomposition. Show that $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix}$ is invertible but has no factorization $A = LU$, and find a permutation matrix $P$ and factors with $PA = LU$.

17. • Find invertible $P$ and $Q$ with $PAQ = \begin{pmatrix} I_2 & 0 \\ 0 & 0 \end{pmatrix}$ for $A = \begin{pmatrix} 1 & -1 & 2 \\ -2 & 2 & -4 \\ 0 & 1 & 1 \end{pmatrix}$.

18. • Prove that a square matrix whose rows each sum to $0$ is not invertible. Use the [invertible matrix theorem](/ACDFDABVQK/) and a suitable vector in the null space.

19. • Let $A$ and $D$ be invertible square matrices over a field, not necessarily of the same size, and let $C$ have the right size. Show that $\begin{pmatrix} A & 0 \\ C & D \end{pmatrix}$ is invertible and find its inverse in block form.

20. ★ Prove that an invertible matrix over a field has at most one factorization $A = LU$ with $L$ unit lower triangular and $U$ upper triangular.

21. ★ Let $A$ be an invertible $n \times n$ matrix and $u$, $v$ column vectors. Compute both Schur complements of $M = \begin{pmatrix} A & u \\ -v^{\mathsf{T}} & 1 \end{pmatrix}$, and compare the two block inverse formulas to derive the Sherman-Morrison formula.

22. ★ Prove that the centre of $\mathrm{GL}_n(F)$, for a field $F$, consists of the nonzero scalar matrices. (A matrix that commutes with $I_n + E_{ij}$ commutes with $E_{ij}$.)

23. ★ Let $p$ be a prime. Show that the unit upper triangular $3 \times 3$ matrices over $\F_p$ form a subgroup of $\mathrm{SL}_3(\F_p)$ of order $p^3$, and that this subgroup is not abelian.

24. ★ Use the rank normal form to prove that every $m \times n$ matrix of rank $r$ over a field is a sum of $r$ matrices of rank $1$, and that it cannot be written as a sum of fewer than $r$ matrices of rank $1$.
