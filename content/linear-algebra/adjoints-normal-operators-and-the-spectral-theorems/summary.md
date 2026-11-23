## What to remember

- **[Adjoint](/0R9NMSM1ZP/):** for a linear map $T \colon V \to W$ between finite-dimensional inner product spaces over $\R$ or $\C$, there is exactly one linear map $T^* \colon W \to V$ with $\ip{Tv}{w} = \ip{v}{T^*w}$ for all $v \in V$ and $w \in W$. It satisfies $(ST)^* = T^*S^*$ and $(T^*)^* = T$.
- **[Matrix of the adjoint](/0DBTE6HVBD/):** if $B$ and $C$ are orthonormal bases, the matrix of $T^*$ is the conjugate transpose of the matrix of $T$, and over $\R$ the transpose. In a basis that is not orthonormal, $[T^*]_B = H^{-1}[T]_B^* H$ with $H_{ij} = \ip{b_j}{b_i}$.
- **[Kernel and image](/YPP8XT6B7Y/):** for $T \colon V \to W$ with $V$ and $W$ finite-dimensional, $\ker T^* = (\im T)^\perp$ and $\im T^* = (\ker T)^\perp$, so $\rank T^* = \rank T$, and $T$ is injective exactly when $T^*$ is surjective.
- **[Self-adjoint operators](/0NEGN5CRSC/):** if $T^* = T$ on a finite-dimensional inner product space, then [every eigenvalue is real](/0C4NT4GT3X/) and, if $V \ne 0$, an eigenvalue exists, even over $\R$. If $T$ is normal, in particular self-adjoint, then [eigenvectors for distinct eigenvalues are orthogonal](/0JHGAV9H25/).
- **[Schur decomposition](/V1JG4C7R7B/):** every complex $n \times n$ matrix is $QUQ^*$ with $Q$ unitary and $U$ upper triangular, the eigenvalues on the diagonal of $U$. A real matrix is $QMQ^{\mathsf{T}}$ with $Q$ real orthogonal and $M$ block upper triangular, with blocks of size $1$ and $2$.
- **[Spectral theorems](/04CW1P44VD/):** on a finite-dimensional complex inner product space, $T$ has an orthonormal basis of eigenvectors if and only if $T$ is [normal](/0C8BR8XRTR/), $TT^* = T^*T$. On a finite-dimensional real inner product space, $T$ has one if and only if $T$ is self-adjoint, so a real matrix is $QDQ^{\mathsf{T}}$ with $Q$ orthogonal and $D$ diagonal exactly when it is [symmetric](/06J4PXRG22/). A [Hermitian matrix](/0DGZBQWZWN/) is $UDU^*$ with $U$ unitary and $D$ real.
- **[Spectral decomposition](/D5KVBA1K9R/):** if $V$ has an orthonormal eigenbasis of $T$, with distinct eigenvalues $\lambda_1, \dots, \lambda_m$ and orthogonal projections $P_i$ onto the eigenspaces, then $T = \sum_i \lambda_i P_i$, $\sum_i P_i = I$, $P_iP_j = 0$ for $i \ne j$, $p(T) = \sum_i p(\lambda_i)P_i$ for every polynomial $p$, and $P_i = \prod_{j \ne i} (T - \lambda_j I)/(\lambda_i - \lambda_j)$.
- **[Real normal operators](/G6T1FNE3JC/) and [commuting families](/BFQQDA489F/):** a real normal matrix $A$ has $Q^{\mathsf{T}}AQ$ block diagonal for some orthogonal $Q$, with $1 \times 1$ blocks and blocks $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $b > 0$. A set of normal operators on a finite-dimensional complex space, or of self-adjoint operators on a real one, has a common orthonormal eigenbasis if and only if its members commute pairwise.
- **[Rayleigh quotient](/06WHP8SE98/):** for $T$ self-adjoint on a finite-dimensional space and $v \ne 0$, $R(v) = \ip{Tv}{v}/\ip{v}{v}$ is a weighted average of the eigenvalues, so $\lambda_{\min} \le R(v) \le \lambda_{\max}$, with equality exactly at eigenvectors of the extreme eigenvalues.

| Class | Condition | Eigenvalues | Orthonormal eigenbasis over $\R$ |
|---|---|---|---|
| [Self-adjoint](/0NEGN5CRSC/) | $T^* = T$ | real | yes |
| Skew-adjoint | $T^* = -T$ | purely imaginary | only if $T = 0$ |
| Unitary or orthogonal | $T^*T = I$ | of absolute value $1$ | only if every eigenvalue is $\pm 1$ |
| [Normal](/0C8BR8XRTR/) | $TT^* = T^*T$ | any complex numbers | only if all eigenvalues are real |

: The classes of normal operators; over $\C$ each has an orthonormal eigenbasis.

## Common errors

- **Transposing in a basis that is not orthonormal.** The matrix of $T^*$ is the conjugate transpose of the matrix of $T$ only in orthonormal bases.
- **Forgetting the conjugate.** Over $\C$ the adjoint matrix is $\bar A^{\mathsf{T}}$, not $A^{\mathsf{T}}$. A complex symmetric matrix such as $\begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix}$ need not be normal, or even diagonalizable.
- **Real eigenvalues are not enough.** A real matrix with real eigenvalues and an eigenbasis, such as $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, need not have an orthogonal one. The spectral theorem needs symmetry, or normality over $\C$.
- **Using the complex spectral theorem over $\R$.** A real normal matrix such as a rotation by a right angle has no real eigenvectors. Over $\R$ only the block form of the normal form theorem survives.
- **Choosing an arbitrary basis in a repeated eigenspace.** Within an eigenspace of dimension $2$ or more, the eigenvectors must be orthonormalized by Gram–Schmidt. For a commuting family, an arbitrary eigenbasis of one member need not diagonalize the others.
- **Reading the Rayleigh bounds for a matrix that is not symmetric.** For a real matrix that is not symmetric, $x^{\mathsf{T}}Ax/x^{\mathsf{T}}x$ sees only the symmetric part, so it need not lie between the eigenvalues.
