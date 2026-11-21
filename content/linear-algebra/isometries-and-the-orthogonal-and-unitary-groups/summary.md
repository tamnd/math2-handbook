## What to remember

- A linear map $T$ is an **isometry** when $\norm{Tv} = \norm{v}$ for all $v$. By polarization it then keeps inner products, $\langle Tu, Tv \rangle = \langle u, v \rangle$. A map of real inner product spaces that keeps distances and fixes $0$ is linear.
- A real square matrix is **orthogonal** when $Q^{\mathsf{T}} Q = I$: its columns, and also its rows, are orthonormal, and $Q^{-1} = Q^{\mathsf{T}}$. Then $\det Q = \pm 1$, and every eigenvalue, real or complex, has absolute value $1$.
- $O(n)$ is the group of linear isometries of $\R^n$. $SO(n) = \set{Q \in O(n) : \det Q = 1}$ is a normal subgroup of index $2$, and $SO(2) \cong U(1)$, the circle group.
- A complex matrix is **unitary** when $U^* U = I$; then $\abs{\det U} = 1$. $SU(n)$ is the kernel of $\det \colon U(n) \to U(1)$. $SU(2)$ consists of the matrices $\begin{pmatrix} \alpha & \beta \\ -\overline{\beta} & \overline{\alpha} \end{pmatrix}$ with $\abs{\alpha}^2 + \abs{\beta}^2 = 1$, the unit quaternions.
- The **reflection** in $u^\perp$ is $s_u(x) = x - 2 \frac{\langle x, u \rangle}{\langle u, u \rangle} u$; for a unit vector its matrix is the Householder matrix $I - 2 u u^{\mathsf{T}}$, symmetric, orthogonal and with determinant $-1$.
- **$O(2)$:** every element is $R(\theta)$ or $S(\alpha)$, the reflection in the line at angle $\alpha$, and $S(\alpha) S(\beta) = R(2(\alpha - \beta))$.
- **$O(3)$ and Euler:** every $R \in SO(3)$ is a rotation by some $\theta \in [0, \pi]$ about an axis $\R u$ with $Ru = u$. Then $\operatorname{tr} R = 1 + 2 \cos \theta$ and $R - R^{\mathsf{T}} = 2 \sin \theta \, [u]_\times$. If $\det Q = -1$, then $-Q \in SO(3)$.
- **Normal form:** every $Q \in O(n)$ is orthogonally similar to $\operatorname{diag}(R(\theta_1), \dots, R(\theta_k), -I_q, I_p)$, and $\det Q = (-1)^q$. **Cartan-Dieudonné:** every element of $O(n)$ is a product of at most $n$ reflections, and $-I_n$ needs exactly $n$.
- **Cayley transform:** for skew-symmetric $A$, $C(A) = (I - A)(I + A)^{-1}$ lies in $SO(n)$, and $C$ is a bijection onto the rotations without the eigenvalue $-1$, with inverse given by the same formula.

## The groups of the chapter

| Group | Definition | Determinant | Small cases |
|---|---|---|---|
| [$O(n)$](/WWK2E8BRGF/) | real, $Q^{\mathsf{T}} Q = I$ | $\pm 1$ | $O(1) = \set{\pm 1}$; $O(2)$ = rotations and reflections |
| [$SO(n)$](/6WBVP2PB1Y/) | $Q \in O(n)$, $\det Q = 1$ | $1$ | $SO(2) \cong U(1)$; $SO(3)$ = rotations about an axis |
| [$U(n)$](/VW5H9XFNJB/) | complex, $U^* U = I$ | on the unit circle | $U(1)$ = the circle group |
| [$SU(n)$](/ZRYYPHWESP/) | $U \in U(n)$, $\det U = 1$ | $1$ | $SU(2)$ = the unit quaternions |

: The four groups of isometries. Each is a subgroup of the general linear group; $O(n)$ is the set of real matrices in $U(n)$, and the special groups are kernels of the determinant.

## Common errors

- **Calling a matrix with orthogonal columns orthogonal.** The columns must be orthonormal. $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ has orthogonal columns of length $\sqrt 2$, and it is $\sqrt 2$ times an orthogonal matrix.
- **Taking $\det Q = 1$ to mean that $Q$ is a rotation without checking $Q^{\mathsf{T}} Q = I$.** A shear has determinant $1$ and is not orthogonal.
- **Reading the angle of a rotation of space from the trace alone.** $\operatorname{tr} R = 1 + 2\cos \theta$ gives $\theta \in [0, \pi]$ but not the sense of turning; the sign comes from $R - R^{\mathsf{T}}$ and the chosen direction of the axis.
- **Forgetting that complex orthogonal is not unitary.** A complex matrix with $Q^{\mathsf{T}} Q = I$ need not keep the norm of $\C^n$; unitary means $U^* U = I$.
- **Expecting reflections or rotations of space to commute.** Plane rotations commute; reflections, and rotations of $\R^3$ about different axes, usually do not.
- **Applying the Cayley transform to every rotation.** $C(A)$ never has the eigenvalue $-1$, so a half-turn such as $\operatorname{diag}(-1, -1, 1)$ is not a Cayley transform.
