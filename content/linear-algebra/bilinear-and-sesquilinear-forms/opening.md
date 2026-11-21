The dot product $x \cdot y = x_1 y_1 + x_2 y_2$ on $\R^2$ is one example of a bilinear form. Two others on the same plane are $x_1 y_1 - x_2 y_2$, which measures time and distance in a two-dimensional version of special relativity, and $x_1 y_2 - x_2 y_1$, the signed area of the parallelogram spanned by $x$ and $y$. All three are linear in each slot, but they behave very differently. For the dot product no nonzero vector is orthogonal to itself. For the second form the vector $(1, 1)$ is. For the third every vector is, and swapping $x$ and $y$ changes the sign. A bilinear form is the general setting for lengths, angles, areas and pairings, over any field, without assuming positivity.

The chapter develops this setting. In a basis, a form is a square matrix $A$ with $B(x, y) = x^T A y$, and a change of basis replaces $A$ by $P^T A P$, not by $P^{-1} A P$. The forms that matter most are symmetric or alternating, and the chapter classifies the alternating ones completely: over every field they are determined by their rank, which is even. For symmetric forms the classification depends on the field, and the chapter gives its first general result, Witt's theory of isotropic vectors and hyperbolic planes. Over $\C$, sesquilinear and Hermitian forms take the place of bilinear forms, so that positive values become possible again.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Bilinear forms and their matrices.** The [bilinear form](/0SQZMXB6GP/), its [matrix](/0QK6K857HS/), the [change of basis](/0SPYAGE7T0/) rule $P^T A P$ and [matrix congruence](/WJWNYSQKK8/).
2. **Symmetric, alternating and reflexive forms.** [Symmetric](/0AXZNE5XNH/) and [alternating](/0DGDS5XY84/) forms, and the theorem that these are the only [reflexive forms](/M0G958M917/).
3. **Nondegeneracy, orthogonality and isotropy.** [Nondegenerate forms](/01NHFZF2SK/) and the radical, [orthogonality](/01TXN7ETH2/) and complements, [isotropic vectors](/MZHFGPV1YT/), and the [hyperbolic plane](/1X5PZSK44P/).
4. **Sesquilinear and Hermitian forms.** [Sesquilinear forms](/054YEQ0Y8M/) and [Hermitian forms](/48P4A1CX85/) over $\C$, with the convention $h(x, y) = x^T M \bar y$.
5. **Alternating forms and symplectic spaces.** The [classification of alternating forms](/V8KKHKXXB3/) by symplectic bases, and [symplectic vector spaces](/PQ7JJY0VPH/) with their Lagrangian subspaces.
6. **Witt's theory of symmetric forms.** The [Witt decomposition and Witt index](/BPMRSPB6GD/), and [Witt's theorem](/CCB8VNQCV0/) on extending isometries.

## A first reading

Read these first, in order: [bilinear form](/0SQZMXB6GP/), [matrix of a bilinear form](/0QK6K857HS/), [change of basis for a bilinear form](/0SPYAGE7T0/), [matrix congruence](/WJWNYSQKK8/), [symmetric bilinear form](/0AXZNE5XNH/), [alternating bilinear form](/0DGDS5XY84/), [nondegenerate bilinear form](/01NHFZF2SK/), [orthogonality](/01TXN7ETH2/), [isotropic vectors](/MZHFGPV1YT/), [Hermitian form](/48P4A1CX85/) and [classification of alternating forms](/V8KKHKXXB3/). Compute with the attached examples over small fields such as $\mathbb F_3$ and $\mathbb F_5$: they show quickly where the field matters.

The reflexive forms theorem can be taken on trust at first. The Witt decomposition and Witt's theorem are needed for the finer classification of quadratic forms and for the orthogonal groups; they can wait until the [next chapter](/6TSCEW8QMK/) has made symmetric forms familiar.

## Before you start

You need [linear forms](/07YQ1C78G0/), the [dual space](/07JBSZE0V4/), [dual bases](/0ZD2CF6ZS0/) and [annihilators](/0ASHNYF7AG/) from [dual spaces and duality](/9K7FFF26QR/). You need the [rank](/0ZC9YTXZRY/) of a matrix and the [change of basis matrix](/0MKRHZB3WS/) from [matrices of linear maps, rank and change of basis](/S6559D61BP/). The [inner products](/0NB0AWGJBW/) of [inner product spaces](/1D4JTZ9VS3/) are the main examples of symmetric and Hermitian forms, and much of the chapter asks which of their properties survive without positivity. Some examples work over [finite fields](/0ZXZ82FTX2/), where the [characteristic](/1ZB13N78XW/) $2$ needs separate care.
