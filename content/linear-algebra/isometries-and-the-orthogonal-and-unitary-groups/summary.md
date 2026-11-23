## What to remember

- **[Linear isometries](/07SJXTWVQW/) [keep inner products](/0R7VXTYHYZ/):** if $T \colon V \to W$ is linear between inner product spaces over $\R$ or $\C$ and $\norm{Tv} = \norm{v}$ for all $v$, then $\ip{Tu}{Tv} = \ip{u}{v}$ for all $u$ and $v$. On real inner product spaces, a map $f$ with $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y$ is linear. In finite dimension, $T$ is an isometry exactly when $T^*T = I$.
- **[Orthogonal matrices](/0W02QESPJQ/):** for a real $n \times n$ matrix $Q$, the conditions $Q^{\mathsf{T}}Q = I$, $QQ^{\mathsf{T}} = I$, orthonormal columns, orthonormal rows, and $\norm{Qx} = \norm{x}$ for all $x$ are equivalent. Then $\det Q = \pm 1$, and every complex eigenvalue has absolute value $1$.
- **[The groups](/WWK2E8BRGF/):** $O(n)$ is a group under multiplication, and [$SO(n)$](/6WBVP2PB1Y/), the kernel of $\det \colon O(n) \to \set{\pm 1}$, is a normal subgroup of index $2$. Over $\C$, [$U(n)$](/VW5H9XFNJB/) is the group of matrices with $U^*U = I$, and [$SU(n)$](/ZRYYPHWESP/) is the kernel of $\det \colon U(n) \to U(1)$. $SU(2)$ consists of the matrices $\begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha \end{pmatrix}$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$.
- **[Reflections](/06BRDF3F0E/):** for $u \ne 0$ in a real inner product space, $s_u(x) = x - 2\frac{\ip{x}{u}}{\ip{u}{u}}u$ fixes $u^\perp$, sends $u$ to $-u$, is an isometry with $s_u^2 = \id$, and has $\det s_u = -1$ in finite dimension. In $\R^n$ with $u$ a unit vector, its matrix is $I - 2uu^{\mathsf{T}}$, and if $\norm{x} = \norm{y}$ with $x \ne y$, the reflection with $u = (x - y)/\norm{x - y}$ sends $x$ to $y$.
- **[The plane](/C97Z06HHB2/):** every element of $O(2)$ is a [rotation](/HNY4CPEEJA/) $R(\theta)$, with determinant $1$, or a reflection $S(\alpha)$ in the line through $(\cos\alpha, \sin\alpha)$, with determinant $-1$. Moreover $S(\alpha)S(\beta) = R(2(\alpha - \beta))$, so $SO(2)$ is commutative while $O(2)$ is not.
- **[Space](/2ZVG43GSKA/):** every $R \in SO(3)$ fixes a unit vector $u$ and is the rotation by some $\theta \in [0, \pi]$ about $\R u$, with $\tr R = 1 + 2\cos\theta$ and $R - R^{\mathsf{T}} = 2\sin\theta\,[u]_\times$. A half turn, $\theta = \pi$, is $2uu^{\mathsf{T}} - I$. If $Q \in O(3)$ has $\det Q = -1$, then $-Q \in SO(3)$.
- **[Normal form](/QTY3VMFGY1/):** every real orthogonal $Q$ is $P\operatorname{diag}(R(\theta_1), \dots, R(\theta_k), -I_q, I_p)P^{\mathsf{T}}$ with $P$ orthogonal and $0 < \theta_j < \pi$, the data are determined by $Q$, and $\det Q = (-1)^q$. For odd $n$, a rotation has the eigenvalue $1$.
- **[Cartan–Dieudonné](/0VMWGYY35Q/):** on a real inner product space of finite dimension $n$, every linear isometry is a product of at most $n$ reflections; $-\id$ needs exactly $n$.
- **[Cayley transform](/HKQ5YY027B/):** for real skew-symmetric $A$, the matrix $I + A$ is invertible and $C(A) = (I - A)(I + A)^{-1}$ lies in $SO(n)$. The map $C$ is a bijection onto the rotations without the eigenvalue $-1$, and it is its own inverse.

| Group | Defining condition | Determinant | Eigenvalues |
|---|---|---|---|
| [$O(n)$](/WWK2E8BRGF/) | real, $Q^{\mathsf{T}}Q = I$ | $\pm 1$ | on the unit circle, non-real ones in conjugate pairs |
| [$SO(n)$](/6WBVP2PB1Y/) | real, $Q^{\mathsf{T}}Q = I$, $\det Q = 1$ | $1$ | as for $O(n)$, with $-1$ of even multiplicity |
| [$U(n)$](/VW5H9XFNJB/) | complex, $U^*U = I$ | any $e^{i\varphi}$ | any numbers on the unit circle |
| [$SU(n)$](/ZRYYPHWESP/) | complex, $U^*U = I$, $\det U = 1$ | $1$ | on the unit circle, with product $1$ |

: The four groups of the chapter, with their determinants and eigenvalues.

## Common errors

- **Orthogonal columns are not enough.** An orthogonal matrix needs ortho*normal* columns. The matrix $\begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix}$ has orthogonal columns but stretches every vector by $\sqrt{5}$.
- **Transposing instead of taking the conjugate transpose.** A complex matrix with $U^{\mathsf{T}}U = I$ need not be unitary; the condition is $U^*U = I$.
- **Determinant $\pm 1$ does not mean orthogonal.** $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has determinant $1$ and is a shear.
- **Using the axis formula for a half turn.** When $\theta = \pi$, $R - R^{\mathsf{T}} = 0$ and the formula for $u$ divides by $\sin\theta = 0$. Read the axis from a nonzero column of $R + I$ instead.
- **Confusing reflections in lines and in hyperplanes.** In $\R^3$ the map $2uu^{\mathsf{T}} - I$ is the half turn about $\R u$, with determinant $1$; the reflection in the plane $u^\perp$ is $I - 2uu^{\mathsf{T}}$, with determinant $-1$.
- **Forgetting the order in a product.** In $O(2)$, $S(\alpha)S(\beta) = R(2(\alpha - \beta))$, while $S(\beta)S(\alpha) = R(2(\beta - \alpha))$. In $SO(3)$, rotations about different axes usually do not commute.
