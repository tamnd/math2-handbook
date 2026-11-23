1. ◦ Decide which of the following matrices are [orthogonal](/0W02QESPJQ/), and give the determinant of each one that is:
$$A = \frac{1}{7}\begin{pmatrix} 2 & 3 & 6 \\ 3 & -6 & 2 \\ 6 & 2 & -3 \end{pmatrix}, \qquad B = \frac{1}{3}\begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix}, \qquad C = \begin{pmatrix} 0 & 0 & -1 \\ 1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix}.$$
For the one that is not, find the factor by which it multiplies lengths.

2. ◦ Let $T \colon \R^2 \to \R^3$ have the matrix with columns $\frac{1}{3}(1, 2, 2)$ and $\frac{1}{3}(2, 1, -2)$. Show that $T$ is a [linear isometry](/07SJXTWVQW/) by computing $T^{\mathsf{T}}T$. Compute $TT^{\mathsf{T}}$, show that it is not $I_3$, and identify it as the orthogonal projection onto a plane, giving a normal vector of that plane.

3. ◦ Let $U = \frac{1}{2}\begin{pmatrix} 1 + i & 1 - i \\ 1 - i & 1 + i \end{pmatrix}$. Show that $U$ is [unitary](/0AR68JTMDT/), compute $\det U$, and decide whether $U \in SU(2)$. Find the eigenvalues of $U$ with eigenvectors, and compute $U^2$.

4. ◦ Show that $R = \frac{1}{9}\begin{pmatrix} 1 & -4 & 8 \\ 8 & 4 & 1 \\ -4 & 7 & 4 \end{pmatrix}$ lies in $SO(3)$, and find the axis and the angle of the rotation, using [Euler's rotation theorem](/2ZVG43GSKA/).

5. ◦ Find the unit vector $u$ and the Householder matrix $H = I - 2uu^{\mathsf{T}}$ of a [reflection](/06BRDF3F0E/) of $\R^3$ that sends $x = (1, 4, 8)$ to $(9, 0, 0)$. Check that $Hx = (9, 0, 0)$.

6. ◦ Using the [classification of $O(2)$](/C97Z06HHB2/), identify the two matrices
$$\frac{1}{13}\begin{pmatrix} 5 & 12 \\ 12 & -5 \end{pmatrix}, \qquad \frac{1}{25}\begin{pmatrix} -7 & 24 \\ -24 & -7 \end{pmatrix}.$$
For the reflection, give a nonzero vector on its mirror line; for the rotation, give $\cos\theta$ and $\sin\theta$.

7. ◦ Find the matrix $U \in SU(2)$ whose first column is $(\frac{3i}{5}, \frac{4}{5})$. Show that $U^2 = -I$, and find the eigenvalues of $U$.

8. ◦ Compute the [Cayley transform](/HKQ5YY027B/) $C(A) = (I - A)(I + A)^{-1}$ of $A = \begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}$. Check that it lies in $SO(2)$, and recover $A$ from $Q = C(A)$ by the same formula. Which element of $SO(2)$ is not $C(A)$ for any skew-symmetric $A$?

9. • Prove that a real $n \times n$ matrix that is orthogonal and upper triangular is diagonal with diagonal entries $\pm 1$. How many such matrices are there?

10. • Let $Q \in O(n)$. Prove that if $\det Q = -1$, then $-1$ is an eigenvalue of $Q$, and that if $n$ is odd and $\det Q = 1$, then $1$ is an eigenvalue of $Q$, using $\det(Q \pm I)$ and $Q^{\mathsf{T}}Q = I$. Give an element of $SO(2)$ without the eigenvalue $1$.

11. • The matrix $A$ of Exercise 1 is symmetric and lies in $SO(3)$. Explain why it must be a half turn. Show that the formula $R - R^{\mathsf{T}} = 2\sin\theta\,[u]_\times$ gives no information about its axis, find the axis from $A + I$, and check that $A = 2uu^{\mathsf{T}} - I$ for the unit vector $u$ on the axis.

12. • Let $R_x$ and $R_y$ be the [basic rotations](/HNY4CPEEJA/) about the $x$- and $y$-axes. Compute $M = R_y(\pi/2)\,R_x(\pi/2)$, and find the axis and the angle of the rotation $M$.

13. • Let $\varphi \colon SU(2) \times U(1) \to U(2)$ be given by $\varphi(V, z) = zV$, where $U(1)$ is the group of complex numbers of absolute value $1$. Prove that $\varphi$ is a surjective group homomorphism, and find its kernel.

14. • Let $R$ be the rotation of Exercise 4, and let $a = (2, -2, 1)$. Find a vector $b$ with $R = s_b s_a$, where $s_u$ denotes the reflection in $u^\perp$, as the [Cartan–Dieudonné theorem](/0VMWGYY35Q/) promises. Find the angle between $a$ and $b$, and compare it with the angle of $R$.

15. • Prove that a normal operator on a finite-dimensional complex inner product space all of whose eigenvalues have absolute value $1$ is unitary. Show by the matrix $\begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix}$ that the hypothesis of normality cannot be dropped.

16. • Let $f \colon \R^2 \to \R^2$ satisfy $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x$ and $y$, and suppose $f(1, 0) = \frac{1}{13}(5, 12)$. Find all possible values of $f(2, 3)$, and say for each one whether $f$ is a rotation or a reflection.

17. • Let $P$ be the permutation matrix of $\R^4$ with $Pe_1 = e_2$, $Pe_2 = e_3$, $Pe_3 = e_4$ and $Pe_4 = e_1$. Find its characteristic polynomial, its eigenvalues and its [normal form](/QTY3VMFGY1/) $\operatorname{diag}(R(\theta_1), \dots, -I_q, I_p)$, and check that $\det P = (-1)^q$.

18. • Compute the Cayley transform of the skew-symmetric matrix
$$A = \frac{1}{3}\begin{pmatrix} 0 & 2 & -2 \\ -2 & 0 & 1 \\ 2 & -1 & 0 \end{pmatrix},$$
and compare it with the matrix $R$ of Exercise 4. Write $A = -[w]_\times$ and check the relation between $\norm{w}$ and the angle of $C(A)$.

19. ★ For a unit vector $a \in \R^3$, let $H_a = 2aa^{\mathsf{T}} - I$ be the half turn about $\R a$. Prove that every element of $SO(3)$ is a product $H_b H_a$ of two half turns. Then find unit vectors $a$ and $b$ with $H_b H_a = R_z(\pi/2)$.

20. ★ Let $n \ge 2$ and let $s_u$ and $s_v$ be reflections of $\R^n$, with $u$ and $v$ unit vectors. Prove that there is $R \in SO(n)$ with $R s_u R^{-1} = s_v$. In $O(2)$, find all $\theta$ with $R(\theta)S(0)R(\theta)^{-1} = S(\pi/4)$.

21. ★ Prove that every $U \in U(n)$ can be written $U = \exp(iH)$ with $H$ Hermitian, where $\exp(iH) = \sum_{k \ge 0} (iH)^k/k!$. Find such an $H$ for $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

22. ★ Let $Q \in O(n)$, and let $F = \ker(Q - I)$ be its space of fixed vectors. Prove that the least number of reflections whose product is $Q$ equals $n - \dim F$. Apply this to the matrix $P$ of Exercise 17, and write $P$ as a product of that many reflections explicitly.
