## What to remember

- A bilinear form on a space of finite dimension with basis $e_1, \dots, e_n$ is $B(u, v) = x^{\mathsf{T}} A y$ with $A_{ij} = B(e_i, e_j)$. If the columns of an invertible $P$ are a new basis, the new matrix is $P^{\mathsf{T}} A P$. Congruent matrices have the same rank, and their determinants differ by the nonzero square $(\det P)^2$.
- $B$ is symmetric when $A^{\mathsf{T}} = A$ and alternating when $B(v, v) = 0$ for all $v$, that is, when $A^{\mathsf{T}} = -A$ and the diagonal of $A$ is zero. Alternating implies skew-symmetric in every characteristic; skew-symmetric implies alternating if and only if the characteristic is not $2$.
- Over any field, $B$ is reflexive ($B(u, v) = 0 \Rightarrow B(v, u) = 0$) if and only if it is symmetric or alternating.
- On a space $V$ of finite dimension, $B$ is nondegenerate if and only if $\det A \ne 0$, if and only if $u \mapsto B(u, \cdot)$ is an isomorphism $V \to V^*$. Then $\dim W + \dim W^\perp = \dim V$ for every subspace $W$, and $V = W \oplus W^\perp$ if and only if $B$ restricted to $W$ is nondegenerate.
- When the characteristic is not $2$, every symmetric form has an orthogonal basis, and a nondegenerate symmetric plane is a hyperbolic plane if and only if it contains an isotropic vector, if and only if $-\det A$ is a square.
- A sesquilinear form on a complex space is $h(x, y) = x^{\mathsf{T}} M \bar y$, and a change of basis gives $P^{\mathsf{T}} M \bar P$. It is Hermitian if and only if $M^* = M$, if and only if $h(v, v)$ is real for every $v$.
- Every alternating form on a space of finite dimension, over any field, has a basis in which its matrix is $J \oplus \dots \oplus J \oplus 0_k$ with $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Its rank is even and decides its congruence class. A symplectic space has even dimension $2m$, and its Lagrangian subspaces have dimension $m$.
- Let the characteristic not be $2$ and $B$ be nondegenerate symmetric on a space of finite dimension. Then $V = H_1 \perp \dots \perp H_m \perp V_{\mathrm{an}}$ with hyperbolic planes $H_i$ and $V_{\mathrm{an}}$ anisotropic; $m$ is the dimension of every maximal totally isotropic subspace, and $V_{\mathrm{an}}$ is unique up to isometry. Every isometry between two subspaces extends to an isometry of $V$.

## Three kinds of form

| | Symmetric bilinear | Alternating bilinear | Hermitian |
|---|---|---|---|
| Field | any $F$; most results need characteristic not $2$ | any $F$ | $\C$ |
| Matrix condition | $A^{\mathsf{T}} = A$ | $A^{\mathsf{T}} = -A$, zero diagonal | $M^* = M$ |
| Change of basis | $P^{\mathsf{T}} A P$ | $P^{\mathsf{T}} A P$ | $P^{\mathsf{T}} M \bar P$ |
| Value on the diagonal | any element of $F$ | always $0$ | always real |
| Normal form | diagonal (characteristic not $2$) | $J \oplus \dots \oplus J \oplus 0_k$ | real diagonal |
| What decides congruence | depends on the field: rank over $\C$, rank and signature over $\R$ | rank alone | rank and signature |

: Three kinds of form, their change of basis rules and their classification.

## Common errors

- Using $P^{-1} A P$ for a form. That rule is for linear maps. A form changes by $P^{\mathsf{T}} A P$, so its eigenvalues and trace are not invariants; only the rank, the determinant up to squares and, over $\R$, the signs are.
- Treating skew-symmetric and alternating as the same thing in characteristic $2$. Over $\F_2$ the identity matrix is skew-symmetric and nondegenerate in every size, including odd ones.
- Assuming $V = W \oplus W^\perp$ for every subspace. It fails exactly when $W \cap W^\perp \ne \{0\}$; every line of a symplectic plane is its own complement.
- Reading the left radical as the right radical. For a form that is not reflexive they can be different subspaces, although they always have the same dimension.
- Dropping the bar in $P^{\mathsf{T}} M \bar P$. With real $P$ the two rules agree, so the error hides in real examples.
- Expecting the Witt index from an orthogonal basis. The form $\operatorname{diag}(1, 1, -1, -1)$ has Witt index $2$, but no basis vector of that orthogonal basis is isotropic; the hyperbolic planes come from vectors such as $e_1 + e_3$.
- Carrying "rank decides everything" from alternating forms to symmetric ones. Over $\Q$, $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(1, 3)$ both have rank $2$, but their determinants $1$ and $3$ do not differ by a square, so they are not congruent.
