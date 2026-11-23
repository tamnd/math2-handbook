Take three rules that pair two vectors of the plane and give a number:
$$x_1 y_1 + x_2 y_2, \qquad x_1 y_1 - x_2 y_2, \qquad x_1 y_2 - x_2 y_1.$$
Each is linear in $x$ when $y$ is fixed and linear in $y$ when $x$ is fixed, so each is a [bilinear form](/0SQZMXB6GP/). Pair the vector $v = (2, 1)$ with itself. The first rule gives $5$, the second gives $3$, and the third gives $0$. Now try $v = (1, 1)$: the first rule gives $2$, the second $0$, and the third $0$ again. The dot product never pairs a nonzero vector to $0$ with itself. The second rule does so exactly on the two lines $x_2 = \pm x_1$. The third does so for every vector, because it measures signed area and a vector spans no area with itself.

The second rule shows how a change of basis acts. The vectors $(2, 1)$ and $(1, 2)$ give $2 \cdot 1 - 1 \cdot 2 = 0$, so they are orthogonal for it, and they pair with themselves to $3$ and $-3$. In the basis $(2, 1), (1, 2)$ the rule therefore has the matrix $\operatorname{diag}(3, -3)$. In the standard basis its matrix is $\operatorname{diag}(1, -1)$. The two matrices are not similar, since their determinants $-1$ and $-9$ differ, but they are related by $P^{\mathsf{T}} A P$, where the columns of $P$ are the new basis vectors. This rule, [matrix congruence](/WJWNYSQKK8/), is the basic tool of the chapter. It keeps the rank and, over $\R$, the signs $+, -$, but not the numbers $1$ and $-1$.

The three rules are three kinds of form: an inner product, a symmetric form with isotropic vectors, and an alternating form. Over $\C$ there is a fourth kind, $x_1 \bar y_1 + x_2 \bar y_2$, which is conjugate-linear in the second slot. The chapter studies all of them. The same objects come up elsewhere. The Hessian of a function at a critical point is a symmetric form, and its signs decide between a minimum, a maximum and a saddle. Special relativity uses the form $x_1 y_1 + x_2 y_2 + x_3 y_3 - x_4 y_4$, whose isotropic vectors make the light cone. Hamiltonian mechanics uses an alternating form on position and momentum. Quantum mechanics uses Hermitian forms on complex spaces.

## What the chapter covers

1. **Bilinear forms and their matrices.** The [matrix of a bilinear form](/0QK6K857HS/), the [change of basis](/0SPYAGE7T0/) rule $P^{\mathsf{T}} A P$, and congruence of matrices.
2. **Symmetric, alternating and reflexive forms.** [Symmetric](/0AXZNE5XNH/) and [alternating](/0DGDS5XY84/) forms, how characteristic $2$ separates alternating from skew-symmetric, and why the [reflexive forms](/M0G958M917/) are exactly these two kinds.
3. **Nondegeneracy, orthogonality and isotropy.** [Nondegenerate forms](/01NHFZF2SK/), the [orthogonal complement](/01TXN7ETH2/) $W^\perp$ and its dimension, [isotropic vectors and subspaces](/MZHFGPV1YT/), and the [hyperbolic plane](/1X5PZSK44P/).
4. **Sesquilinear and Hermitian forms.** [Sesquilinear forms](/054YEQ0Y8M/) on complex spaces, their change of basis $P^{\mathsf{T}} M \bar P$, and [Hermitian forms](/48P4A1CX85/), the forms with real values on the diagonal.
5. **Alternating forms and symplectic spaces.** The [classification of alternating forms](/V8KKHKXXB3/) by their rank alone, and [symplectic vector spaces](/PQ7JJY0VPH/) with their Lagrangian subspaces.
6. **Witt's theory of symmetric forms.** The [Witt decomposition](/BPMRSPB6GD/) into hyperbolic planes and an anisotropic part, the Witt index, and [Witt's theorem](/CCB8VNQCV0/) on extending isometries.

## A first reading

A first pass through the chapter can follow nine entries:

1. [Bilinear form](/0SQZMXB6GP/)
2. [Matrix of a bilinear form](/0QK6K857HS/)
3. [Change of basis](/0SPYAGE7T0/)
4. [Symmetric bilinear form](/0AXZNE5XNH/)
5. [Alternating bilinear form](/0DGDS5XY84/)
6. [Nondegenerate bilinear form](/01NHFZF2SK/)
7. [Orthogonality](/01TXN7ETH2/)
8. [Hermitian form](/48P4A1CX85/)
9. [Classification of alternating forms](/V8KKHKXXB3/)

Reflexive forms can wait; for a first pass it is enough to know that symmetric and alternating forms are the two cases. The hyperbolic plane and the two entries on Witt's theory matter most when you go on to quadratic forms, and they read best after you have done a few computations with isotropic vectors. If you work only over $\R$ or $\C$, you may skip the remarks on characteristic $2$ at first, but come back to them: they show which hypotheses each theorem really uses.

## Before you start

You should know [linear forms](/07YQ1C78G0/) and the [dual space](/07JBSZE0V4/), because a bilinear form is the same thing as a linear map $V \to V^*$. The chapter on [dual spaces and duality](/9K7FFF26QR/) covers this, including [annihilators](/0ASHNYF7AG/), which are the model for orthogonal complements. You need [rank](/0ZC9YTXZRY/) and the [change of basis matrix](/0MKRHZB3WS/) from the chapter on [matrices of linear maps](/S6559D61BP/). The chapter on [inner product spaces](/1D4JTZ9VS3/) gives the main example, the [inner product](/0NB0AWGJBW/), which is a positive definite symmetric or Hermitian form. Some examples work over [finite fields](/0ZXZ82FTX2/), and several theorems depend on the [characteristic](/1ZB13N78XW/) of the field, so you should know what characteristic $2$ means.
