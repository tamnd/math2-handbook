## What to remember

- A **bilinear form** on $V$ over $F$ is linear in each slot. In a basis $(e_i)$ its matrix is $A_{ij} = B(e_i, e_j)$, and $B(u, v) = x^T A y$ for the coordinate vectors $x$, $y$.
- **Change of basis.** If the columns of $P$ are the new basis vectors in old coordinates, the new matrix is $P^T A P$. So rank is an invariant, and $\det A$ is an invariant up to a nonzero square factor. Matrices related in this way are **congruent**.
- **Symmetric and alternating.** $B$ is symmetric when $A^T = A$, and alternating when $B(v, v) = 0$ for all $v$, that is, $A^T = -A$ with zero diagonal. Alternating forms are skew-symmetric; the converse holds when $\operatorname{char} F \ne 2$. A form is **reflexive** ($B(u, v) = 0 \Rightarrow B(v, u) = 0$) exactly when it is symmetric or alternating.
- **Nondegenerate** means that the radical is $\{0\}$, or that $A$ is invertible, or that $u \mapsto B(u, \cdot)$ is an isomorphism $V \to V^*$. For a nondegenerate form, $\dim W + \dim W^\perp = \dim V$ for every subspace $W$, but $W \cap W^\perp$ may be nonzero.
- A vector $v \ne 0$ is **isotropic** when $B(v, v) = 0$. A **hyperbolic plane** has a basis $(u, v)$ with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$; outside characteristic $2$, every nondegenerate plane containing an isotropic vector is hyperbolic.
- A **sesquilinear form** is linear in the first slot and conjugate-linear in the second: $h(x, y) = x^T M \bar y$, and a change of basis gives $P^T M \bar P$. It is **Hermitian** when $h(v, u) = \overline{h(u, v)}$, equivalently $M^* = M$, equivalently $h(v, v) \in \R$ for all $v$.
- **Alternating forms** have a symplectic basis: the matrix becomes $J \oplus \cdots \oplus J \oplus 0$ with $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. The rank is even and is a complete invariant. A symplectic space has even dimension $2m$, and its Lagrangian subspaces ($L^\perp = L$) have dimension $m$.
- **Witt.** Outside characteristic $2$, a nondegenerate symmetric space is $H_1 \perp \cdots \perp H_m \perp V_{\mathrm{an}}$ with hyperbolic planes $H_i$ and anisotropic $V_{\mathrm{an}}$; the number $m$, the Witt index, is the dimension of every maximal totally isotropic subspace. By Witt's theorem every isometry between subspaces extends to an isometry of $V$.

## Kinds of forms compared

| Kind | Matrix condition | Change of basis | Complete invariant |
|---|---|---|---|
| [Bilinear](/0SQZMXB6GP/) | none | $P^T A P$ | none simple in general |
| [Symmetric](/0AXZNE5XNH/) | $A^T = A$ | $P^T A P$ | depends on $F$; over $\C$ the rank, over $\R$ the signature |
| [Alternating](/0DGDS5XY84/) | $A^T = -A$, zero diagonal | $P^T A P$ | the rank, which is even |
| [Sesquilinear](/054YEQ0Y8M/) | none | $P^T M \bar P$ | none simple in general |
| [Hermitian](/48P4A1CX85/) | $M^* = M$ | $P^T M \bar P$ | the numbers of positive, negative and zero squares |

: The main kinds of forms of the chapter. The invariants of symmetric forms over $\R$ and $\C$ are proved in the next chapter by the method used here for alternating forms, splitting off one piece at a time; the same argument gives the Hermitian case.

## Common errors

- **Using similarity instead of congruence.** A form changes by $P^T A P$, a linear map by $P^{-1} A P$. The two agree only for orthogonal $P$, and the eigenvalues of $A$ are not invariants of the form.
- **Forgetting characteristic $2$.** Over $\mathbb F_2$, the identity matrix is skew-symmetric but not alternating, and some quadratic forms do not come from any symmetric bilinear form. State the characteristic whenever you use $\frac12$.
- **Treating $W^\perp$ as a complement.** For a form that is not definite, $W$ and $W^\perp$ can intersect, and $V = W \oplus W^\perp$ holds exactly when the form restricted to $W$ is nondegenerate.
- **Confusing the radicals.** For a form that is not reflexive, the left and right radicals can differ; they have the same dimension, $\dim V - \operatorname{rank} A$.
- **Mixing conventions for sesquilinear forms.** Some books make the first slot conjugate-linear, and then $h(x, y) = x^* M y$. Check the convention before you copy a formula.
