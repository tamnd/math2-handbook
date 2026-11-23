1. $A$ and $C$ are orthogonal, both with determinant $1$; $C$ is a signed permutation matrix. $B$ is not: $B^{\mathsf{T}}B = \frac{5}{9}I$, so its columns are orthogonal but have length $\frac{\sqrt{5}}{3}$, and $B$ multiplies every length by $\frac{\sqrt{5}}{3}$.

3. The columns are orthonormal, since $\abs{1 + i}^2 + \abs{1 - i}^2 = 4$ and $(1 + i)\overline{(1 - i)} + (1 - i)\overline{(1 + i)} = 2i - 2i = 0$. $\det U = \frac{1}{4}\big((1 + i)^2 - (1 - i)^2\big) = i$, so $U \notin SU(2)$. The eigenvalue $1$ has eigenvector $(1, 1)$ and the eigenvalue $i$ has eigenvector $(1, -1)$, and $U^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

4. $\tr R = 1$, so $\cos\theta = 0$ and $\theta = \frac{\pi}{2}$. From $R - R^{\mathsf{T}}$ the vector $(r_{32} - r_{23}, r_{13} - r_{31}, r_{21} - r_{12})$ is $\frac{1}{9}(6, 12, 12)$, so the axis is $\R(1, 2, 2)$, and indeed $R(1, 2, 2) = (1, 2, 2)$.

6. The first has determinant $-1$ and is $S(\alpha)$ with $\cos 2\alpha = \frac{5}{13}$ and $\sin 2\alpha = \frac{12}{13}$; it fixes $(3, 2)$, which spans the mirror line. The second has determinant $1$ and is $R(\theta)$ with $\cos\theta = -\frac{7}{25}$ and $\sin\theta = -\frac{24}{25}$.

8. $C(A) = \frac{1}{5}\begin{pmatrix} -4 & 3 \\ -3 & -4 \end{pmatrix}$, with orthonormal columns and determinant $\frac{16 + 9}{25} = 1$. Applying the formula to $Q = C(A)$ gives back $\begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}$. The rotation $R(\pi) = -I$ is not a Cayley transform, because it has the eigenvalue $-1$.

12. $M = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix}$. Its trace is $0$, so $\cos\theta = -\frac{1}{2}$ and $\theta = \frac{2\pi}{3}$. The vector read off from $M - M^{\mathsf{T}}$ is $(2, 2, -2) = 2\sin\theta \cdot \frac{1}{\sqrt{3}}(1, 1, -1)$, so the axis is spanned by $(1, 1, -1)$, which $M$ fixes.

14. Since $s_a^2 = I$, $s_b = Rs_a$. Computing $I - Rs_a = \frac{1}{9}\begin{pmatrix} 16 & -4 & -4 \\ -4 & 1 & 1 \\ -4 & 1 & 1 \end{pmatrix}$ shows that $b = (4, -1, -1)$ works. Both $a$ and $b$ are perpendicular to the axis $(1, 2, 2)$, and $\cos\angle(a, b) = \frac{9}{3 \cdot 3\sqrt{2}} = \frac{1}{\sqrt{2}}$, so the angle is $\frac{\pi}{4}$, half the angle $\frac{\pi}{2}$ of $R$.

16. By the theorem that [isometries preserve inner products](/0R7VXTYHYZ/), $f$ is linear and orthogonal, so $f(0, 1)$ is a unit vector perpendicular to $\frac{1}{13}(5, 12)$. If $f(0, 1) = \frac{1}{13}(-12, 5)$, $f$ is a rotation and $f(2, 3) = (-2, 3)$. If $f(0, 1) = \frac{1}{13}(12, -5)$, $f$ is a reflection and $f(2, 3) = \frac{1}{13}(46, 9)$.

17. The characteristic polynomial is $t^4 - 1$, with roots $1$, $-1$, $i$ and $-i$. So $k = 1$ with $\theta_1 = \frac{\pi}{2}$, $q = 1$ and $p = 1$: the normal form is $\operatorname{diag}(R(\frac{\pi}{2}), -1, 1)$, and $\det P = -1$, the sign of a $4$-cycle.

19. If $R$ turns by $\theta$ about the unit vector $u$, take unit vectors $a$ and $b$ perpendicular to $u$ with angle $\frac{\theta}{2}$ from $a$ to $b$. In $\R^3$, $H_a = -s_a$, so $H_bH_a = s_bs_a$, the product of the reflections in two planes through the axis $\R u$ at angle $\frac{\theta}{2}$. For $R_z(\pi/2)$ take $a = e_1$ and $b = \frac{1}{\sqrt{2}}(1, 1, 0)$.

20. For any orthogonal $R$, $Rs_uR^{-1} = s_{Ru}$. For $n \ge 2$ some rotation sends $u$ to $v$: turn the plane containing $u$ and $v$, or any plane containing $u$ if $v = \pm u$. In $O(2)$, $R(\theta)S(0)R(-\theta) = S(\theta)$, so $\theta = \frac{\pi}{4} + k\pi$ for an integer $k$.

21. By the spectral theorem, $U = V\operatorname{diag}(e^{i\varphi_1}, \dots, e^{i\varphi_n})V^*$ with $V$ unitary and real $\varphi_j$; take $H = V\operatorname{diag}(\varphi_1, \dots, \varphi_n)V^*$. For the swap, the eigenvalues are $1$ on $(1, 1)$ and $-1 = e^{i\pi}$ on $(1, -1)$, so one choice is $H = \frac{\pi}{2}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$.

22. A product of $k$ reflections fixes the intersection of $k$ hyperplanes, so $\dim F \ge n - k$. Conversely, if $Qv \ne v$, the reflection $s$ in $(Qv - v)^\perp$ fixes $F$ and sends $Qv$ to $v$, so $sQ$ fixes $F + \R v$; induct on $n - \dim F$. For $P$, $F = \R(1, 1, 1, 1)$, so $3$ reflections are needed, and $P = s_{e_1 - e_4}s_{e_1 - e_3}s_{e_1 - e_2}$, a product of three transpositions.
