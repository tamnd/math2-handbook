1. ◦ Which of these matrices are [orthogonal](/0W02QESPJQ/)? For each one that is, give its determinant. (a) $\frac{1}{5} \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix}$. (b) $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. (c) $\frac{1}{\sqrt 2} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. (d) $\frac{1}{7} \begin{pmatrix} 2 & 3 & 6 \\ 3 & -6 & 2 \\ 6 & 2 & -3 \end{pmatrix}$.

2. ◦ Let $T$ be a linear isometry, and let $u$, $v$ be vectors of a real inner product space with $\norm{u} = 1$, $\norm{v} = 2$ and $\norm{u + v} = \sqrt 7$. Find $\langle Tu, Tv \rangle$ and the angle between $Tu$ and $Tv$.

3. ◦ Let $Q = \frac{1}{9} \begin{pmatrix} 1 & -4 & 8 \\ 8 & 4 & 1 \\ -4 & 7 & 4 \end{pmatrix}$. Check that $Q \in SO(3)$, and use the [classification of $O(3)$](/2ZVG43GSKA/) to find its axis and its angle.

4. ◦ Find the Householder matrix $H = I - 2 \frac{u u^{\mathsf{T}}}{u^{\mathsf{T}} u}$ of a [reflection](/06BRDF3F0E/) that sends $x = (3, 4, 0)$ to $(5, 0, 0)$.

5. ◦ Which of these are [unitary](/0AR68JTMDT/)? Give the determinant of each unitary one. (a) $\frac{1}{\sqrt 2} \begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$. (b) $\frac{1}{2} \begin{pmatrix} 1 + i & 1 - i \\ 1 - i & 1 + i \end{pmatrix}$. (c) $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$.

6. ◦ With $R(\theta)$ and $S(\alpha)$ as in the [classification of $O(2)$](/C97Z06HHB2/), write $R(\pi/2) S(\pi/6)$ and $S(\pi/6) R(\pi/2)$ in the form $S(\beta)$, and give the mirror lines.

7. ◦ Let $P$ be the $4 \times 4$ permutation matrix with $P e_1 = e_2$, $P e_2 = e_3$, $P e_3 = e_4$, $P e_4 = e_1$. Find its eigenvalues, its determinant and its [normal form](/QTY3VMFGY1/).

8. ◦ Compute the [Cayley transform](/HKQ5YY027B/) $(I - A)(I + A)^{-1}$ of $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and identify it as a rotation $R(\theta)$.

9. • Show that a linear isometry is injective. Deduce that a linear isometry of a finite-dimensional space to itself is invertible and that its inverse is an isometry. Give a linear isometry $\R^2 \to \R^3$ that is not surjective.

10. • Show that a real upper triangular orthogonal matrix is diagonal with diagonal entries $\pm 1$.

11. • Let $Q = \frac{1}{3} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & -2 \\ 2 & -2 & 1 \end{pmatrix}$. Show that $Q \in O(3)$ and $\det Q = -1$, and that $Q$ is a reflection. Find the mirror plane.

12. • Show that every $U \in U(n)$ can be written as $U = \lambda V$ with $\lambda \in U(1)$ and $V \in SU(n)$. How many such pairs $(\lambda, V)$ are there for a given $U$?

13. • Show that the centre of $O(2)$ is $\set{I, -I}$, and that $SO(2)$ is commutative.

14. • Let $w = \frac{1}{3}(1, 2, 2)$, let $[w]_\times$ be the matrix of $x \mapsto w \times x$, and let $A = -[w]_\times$. Compute the Cayley transform $C(A)$, and compare it with exercise 3.

15. • Prove Euler's theorem in matrix form: if $R \in SO(3)$, then $\det(R - I) = 0$. (Use $R - I = R (I - R^{\mathsf{T}})$.)

16. • Let $R \in SO(3)$ with $\operatorname{tr} R = -1$. Show that $R$ is a half-turn, that $R^2 = I$ and that $R$ is symmetric. Conversely, show that a symmetric matrix in $SO(3)$ is $I$ or a half-turn.

17. • Let $R_x(\theta)$ and $R_y(\theta)$ be the [basic rotations](/HNY4CPEEJA/) about the $x$- and $y$-axes. Find the axis and the angle of $R_x(\pi/2) R_y(\pi/2)$ and of $R_y(\pi/2) R_x(\pi/2)$.

18. • Write the cyclic permutation matrix $C$ with $C e_1 = e_2$, $C e_2 = e_3$, $C e_3 = e_1$ as a product of two reflections $s_u s_v$, as the [Cartan-Dieudonné theorem](/0VMWGYY35Q/) allows. Explain why no single reflection equals $C$.

19. • Use the normal form to show: if $n$ is odd and $Q \in SO(n)$, then $Q$ has the eigenvalue $1$; if $n$ is even and $Q \in O(n)$ has $\det Q = -1$, then $Q$ has both eigenvalues $1$ and $-1$.

20. ★ Let $T \colon \R^n \to \R^n$ be linear, and suppose that $\langle Tu, Tv \rangle = 0$ whenever $\langle u, v \rangle = 0$. Show that $T = c Q$ for a real number $c \ge 0$ and an orthogonal matrix $Q$.

21. ★ Let $n \ge 2$. Show that any two reflections in $O(n)$ are conjugate by an element of $SO(n)$. Then show that two rotations of $\R^3$ by the same angle $\theta$ are conjugate in $SO(3)$.

22. ★ Let $A$ be real skew-symmetric. Show that $I + A$ is invertible, that $C(A) = (I - A)(I + A)^{-1}$ is orthogonal with determinant $1$, and that $-1$ is not an eigenvalue of $C(A)$.

23. ★ Show that every element of $SO(3)$ is a product of two half-turns. (Start from two reflections in planes through the axis.)

24. ★ Let $\mathcal{H}$ be the real vector space of traceless Hermitian $2 \times 2$ matrices $X = \begin{pmatrix} z & x - iy \\ x + iy & -z \end{pmatrix}$, identified with $\R^3$, so that $\det X = -(x^2 + y^2 + z^2)$. Show that for $U \in SU(2)$ the map $X \mapsto U X U^*$ is a linear isometry of $\mathcal{H}$, and that $U \mapsto (X \mapsto U X U^*)$ is a homomorphism $SU(2) \to O(3)$ with kernel $\set{I, -I}$.
