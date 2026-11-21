1. ◦ Use the [formula for the inverse of a $2 \times 2$ matrix](/8XWC7RKNN1/) to invert $A = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$. Then use $A^{-1}$ to solve $3x + 5y = 4$, $x + 2y = 1$.

2. ◦ For which real numbers $t$ is $\begin{pmatrix} t & 2 \\ 8 & t \end{pmatrix}$ invertible?

3. ◦ Write the $3 \times 3$ [elementary matrices](/01REXW3WWE/) of the row operations $R_3 \to R_3 - 4R_1$, $R_2 \to 5R_2$ and $R_2 \leftrightarrow R_3$, and the inverse of each. Which of the three are [transvections](/0DTCBCKEJP/)?

4. ◦ Let $T_{12}(3) = I + 3E_{12}$ be the $2 \times 2$ transvection matrix. Compute $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} T_{12}(3)$, and say which column operation the product performs.

5. ◦ Decide, without row reduction, which of these are invertible: $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 0 & 3 \\ 0 & 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 4 & 7 \\ 0 & 2 & 5 \\ 0 & 0 & -1 \end{pmatrix}$. For the invertible one, give the diagonal of its inverse before computing the inverse, and then compute it.

6. ◦ For each matrix, say whether it lies in $\mathrm{GL}_2(\R)$, $\mathrm{SL}_2(\R)$, $\mathrm{GL}_2(\Z)$ and $\mathrm{SL}_2(\Z)$: $\begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix}$, $\begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$, $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 4 & 2 \\ 1 & 1 \end{pmatrix}$.

7. ◦ Find the [LU decomposition](/0RKG5YW66Y/) of $\begin{pmatrix} 2 & 3 \\ 4 & 7 \end{pmatrix}$. Then show that $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ is invertible but has no LU decomposition.

8. ◦ Sort these $2 \times 3$ real matrices into classes of [equivalent matrices](/0CMHSGTWXB/): $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$, $\begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \end{pmatrix}$. How many equivalence classes of $2 \times 3$ real matrices are there in all?

9. • Row reduce $[A \mid I_3]$ to [compute the inverse](/0Z83DHFMYM/) of $A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$. Then show that $B = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ is singular by finding a nonzero $x$ with $Bx = 0$.

10. • Let $A$ be invertible. Show that $AB = AC$ implies $B = C$. Give $2 \times 2$ matrices $A \ne 0$, $B \ne C$ with $AB = AC$.

11. • A square matrix $A$ satisfies $A^2 = A + I$. Show that $A$ is invertible and express $A^{-1}$ as a polynomial in $A$.

12. • Let $A$ and $B$ be $n \times n$ matrices over a field with $AB$ invertible. Show that $A$ and $B$ are both invertible. Where does the proof use that the matrices are square?

13. • Show that the inverse of an invertible symmetric matrix is symmetric, and that the inverse of an invertible skew-symmetric matrix is skew-symmetric.

14. • Find the inverse of $\begin{pmatrix} 1 & 0 & 0 \\ a & 1 & 0 \\ b & c & 1 \end{pmatrix}$ for arbitrary $a, b, c$.

15. • Write $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ as a product of elementary matrices.

16. • Write $\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$, which lies in $\mathrm{SL}_2(\Z)$, as a product of three transvection matrices with integer entries.

17. • Verify for $3 \times 3$ transvection matrices that $T_{12}(a)\,T_{23}(b)\,T_{12}(-a)\,T_{23}(-b) = T_{13}(ab)$, and that $T_{12}(a)$ and $T_{13}(b)$ commute.

18. • Find the LU decomposition of $A = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 5 & 3 \\ 2 & 3 & 6 \end{pmatrix}$. Check the pivots against the leading principal minors, and write $A = LDL^{\mathsf{T}}$.

19. • Let $M = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 7 & 2 \\ 1 & 1 & 4 \end{pmatrix}$, with $A = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$ the upper left block. Compute the [Schur complement](/6HWFBXYPZP/) $M/A$, and use it to find $\det M$ and the $(3,3)$ entry of $M^{-1}$.

20. • Let $u = (1, 2, 3)^{\mathsf{T}}$ and $v = (1, 1, 1)^{\mathsf{T}}$. Use the [Sherman-Morrison formula](/MDZDEFE53C/) to invert $I_3 + uv^{\mathsf{T}}$. For which real $c$ is $I_3 + c\,uv^{\mathsf{T}}$ singular?

21. • Show that two $m \times n$ matrices are equivalent if and only if one can be turned into the other by a finite sequence of row operations and column operations.

22. ★ Show that the centre of $\mathrm{GL}_n(F)$, the set of matrices that commute with every invertible matrix, consists of the nonzero scalar matrices $cI_n$.

23. ★ Prove that an invertible matrix has at most one LU decomposition, using only that products and inverses of unit lower triangular matrices are unit lower triangular, and similarly for invertible upper triangular matrices.

24. ★ Derive the Sherman-Morrison formula from the [block inverse formula](/5QTK7JWXF3/), applied to $M = \begin{pmatrix} A & u \\ v^{\mathsf{T}} & -1 \end{pmatrix}$ and its two Schur complements.

25. ★ Let $F$ be a field with $q$ elements. Count the invertible $2 \times 2$ matrices over $F$ by choosing the columns one at a time, and deduce the orders of $\mathrm{GL}_2(F)$ and $\mathrm{SL}_2(F)$. Give both numbers for $q = 3$.

26. ★ Show that a matrix of rank $r$ is a sum of $r$ matrices of rank $1$, and not of fewer.
