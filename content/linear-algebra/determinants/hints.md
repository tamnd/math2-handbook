2. Sarrus gives $(1 + 0 + 24) - (4 - 4 + 0) = 25$. Along the first row: $1 \cdot (1 + 4) - 0 + 2 \cdot (12 - 2) = 25$.

4. A swap gives the factor $-1$, the scaling the factor $-4$, and the row addition the factor $1$. So $\det B = 5 \cdot (-1) \cdot (-4) = 20$.

8. (a) $\det = 1$, a unit of $\Z$; the inverse is $\begin{pmatrix} 7 & -5 \\ -4 & 3 \end{pmatrix}$. (b) $\det = 2$ is not a unit of $\Z$, so there is no integer inverse. (c) $\det = 3$ and $\gcd(3, 6) = 3$, so the matrix is not invertible over $\Z/6$. (d) $\det = -5 \equiv 1$, and the inverse is the adjugate $\begin{pmatrix} 1 & -2 \\ -3 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 4 \\ 3 & 1 \end{pmatrix}$.

9. (a) The matrix with columns $e_2, e_3, e_1$ is a cyclic permutation matrix of determinant $1$, so the orientation is the same. The matrix with columns $e_3, e_2, e_1$ comes from $I$ by one swap and has determinant $-1$, so the orientation is opposite. (b) The determinant of the matrix with rows $(1, 0, 2)$, $(2, 1, 0)$, $(0, 3, 1)$ is $13$, so the volume is $13/6$.

10. $\det A = \det A^{\mathsf{T}} = \det(-A) = (-1)^n \det A$, so $2 \det A = 0$ for odd $n$. Over $\F_2$, $-1 = 1$, so $A = (1)$ satisfies $A^{\mathsf{T}} = -A$, with determinant $1$.

12. Multiply rows by $-1$ until the first column is $(1, 1, 1)^{\mathsf{T}}$; this changes only the sign. Subtract row $1$ from rows $2$ and $3$: their entries become $0$ or $\pm 2$, so a factor $2$ comes out of each of them. The matrix with rows $(1, 1, 1)$, $(1, -1, 1)$, $(1, 1, -1)$ has determinant $4$.

15. The upper left block is $2I$ and $B = C = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, so $CA^{-1}B = \tfrac12 CB = I$. The Schur complement is $3I - I = 2I$, and $\det = \det(2I) \det(2I) = 16$.

18. $\det = -(s - 1)^2 (s + 2)$, so the matrix is invertible exactly for $s \ne 1, -2$. For $s = 1$ every entry is $1$ and the rank is $1$. For $s = -2$ the minor $\det \begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix} = -3$ is nonzero, so the rank is $2$.

19. (a) In the basis $1, x, x^2$, the images are $1$, $1 - x$, $1 - 2x + x^2$. The matrix is upper triangular with diagonal $1, -1, 1$, so $\det T = -1$. (b) In the basis $E_{11}, E_{21}, E_{12}, E_{22}$, the map $L$ acts on each column of $X$ separately, so its matrix is block diagonal with two blocks equal to $A$.

22. Expand along the first row. The second term needs one more expansion along the first column of the minor, and gives $-D_{n-2}$. With $D_1 = 3 = F_4$ and $D_2 = 8 = F_6$, the identity $F_{k+2} = 3F_k - F_{k-2}$ finishes the induction.

23. Since $AB = BA$, $(A + iB)(A - iB) = A^2 + B^2$. The matrix $A - iB$ is the complex conjugate of $A + iB$, so its determinant is the conjugate, and $\det(A^2 + B^2) = \abs{\det(A + iB)}^2$. For the given $A$ and $B$, $A^2 + B^2 = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}$ has determinant $-1$.

24. $A \operatorname{adj} A = (\det A) I = 0$, so every column of $\operatorname{adj} A$ lies in $\ker A$, which has dimension $1$. So $\operatorname{rank} \operatorname{adj} A \le 1$. By rank by minors, some minor of size $n - 1$ is nonzero, so $\operatorname{adj} A \ne 0$.

25. For odd $n$, $\det A = (-1)^n \det A$ over $\Q$, so $\det A = 0 = 0^2$. For even $n$, $\det A = \operatorname{pf}(A)^2$, and $\operatorname{pf}(A)$ is a polynomial with integer coefficients in the entries, so it is an integer.

26. Use $\operatorname{adj} A = (\det A) A^{-1}$ twice, together with $\det(\operatorname{adj} A) = (\det A)^{n-1}$, which follows from taking determinants in $A \operatorname{adj} A = (\det A) I$. For $n = 2$, $\operatorname{adj} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, and applying this twice returns $A$.
