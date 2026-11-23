Take the matrix
$$
A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix}
$$
and ask for which $b \in \R^3$ the system $Ax = b$ has a solution, and how many solutions it then has. Row reduction answers both questions. The third row of $A$ is the sum of the first two, so a solution can exist only when $b_3 = b_1 + b_2$; for $b = (2, 3, 5)$ one solution is $x = (1, 1, 0)$, and for $b = (1, 0, 0)$ there is none. The homogeneous system $Ax = 0$ has the solutions $t(1, 1, -1)$, and adding them to one solution of $Ax = (2, 3, 5)$ gives all of them: $(1 + t, 1 + t, -t)$ for $t \in \R$.

The same computation, read as a statement about the map $x \mapsto Ax$ from $\R^3$ to $\R^3$, says more. The vectors $b$ that are reached form a plane, the [image](/0WSFKKT6FF/) of the map. The vectors sent to $0$ form a line, the [kernel](/0S23E6YE83/). The map is not injective because its kernel is not $\set{0}$, and it is not surjective because its image is a plane. The numbers fit: the plane has dimension $2$, the line has dimension $1$, and $2 + 1 = 3$ is the dimension of the domain. The [rank-nullity theorem](/0W4FSW1TVB/) says this always happens, so after finding the line of solutions of $Ax = 0$ one knows without further work that the image is a plane and not all of $\R^3$.

None of this depends on $A$ being a matrix. Differentiation of polynomials, the shift of a sequence, the trace of a square matrix and a rotation of the plane all send sums to sums and multiples to multiples, so each is a [linear map](/0NRYHJPQG2/) with a kernel, an image and a rank. In finite dimension a choice of bases turns any linear map into a matrix, but the theorems are cleaner without the choice, and in infinite dimension there is no matrix to fall back on. The chapter therefore studies linear maps as maps, and uses matrices to compute.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Linear maps and matrices.** The [definition](/0NRYHJPQG2/) and [examples](/0SS770NS8B/), the theorem that every linear map $F^n \to F^m$ is a [matrix transformation](/W6KB0J3SZZ/), [maps of the plane](/5BXHREC8C8/), and [composition](/00BKRZKMSS/) as matrix multiplication.
2. **Kernel and image.** The [kernel](/0S23E6YE83/), the [image](/0WSFKKT6FF/), the [kernel test for injectivity](/0BJBYCGMWE/), and the fact that a linear map is [determined by its values on a basis](/0R8X9XA83A/), which can be chosen freely.
3. **Rank and nullity.** The [rank](/0ZZXSBTR4J/), the [nullity](/0APCFW7639/) and the [rank-nullity theorem](/0W4FSW1TVB/).
4. **Isomorphisms.** [Linear isomorphisms](/0B8T10CE7N/), the [classification of spaces by dimension](/0VJBSK15SN/), and [endomorphisms](/0912EEEVCT/) for which injective, surjective and bijective agree.
5. **Spaces of maps and the algebra of endomorphisms.** The [space $\operatorname{Hom}(V, W)$](/0X9MBPP2Z3/), its [dimension](/0Z9N1ER0W0/), [endomorphisms](/0J7H0YBFDJ/) and their powers, and the [algebra $\operatorname{End}(V)$](/5JA4CYT1TB/).
6. **Semilinear maps.** [Semilinear and antilinear maps](/BNPDDM95KF/), which twist the scalars by an automorphism of the field.

## A first reading

A first pass through the chapter can take these entries in order.

- [Linear map](/0NRYHJPQG2/), with the non-examples.
- [Matrix transformations of $F^n$](/W6KB0J3SZZ/).
- [Composition of linear maps](/00BKRZKMSS/).
- [Kernel](/0S23E6YE83/) and [image](/0WSFKKT6FF/) of a linear map.
- [Injectivity and the kernel](/0BJBYCGMWE/).
- [Linear maps are determined by a basis](/0R8X9XA83A/).
- [Rank-nullity theorem](/0W4FSW1TVB/).
- [Linear isomorphism](/0B8T10CE7N/) and the [classification by dimension](/0VJBSK15SN/).
- [Injective, surjective and bijective endomorphisms](/0912EEEVCT/).

The [space of linear maps](/0X9MBPP2Z3/) and the [algebra of endomorphisms](/5JA4CYT1TB/) are needed for dual spaces and eigenvalues. [Semilinear maps](/BNPDDM95KF/) are needed for Hermitian forms and projective geometry and can wait until then.

## Before you start

The chapter assumes the following.

- [Vector spaces, span, independence, bases and dimension](/MVH97H8B2J/): subspaces, bases, coordinates and dimension.
- [Matrices and the operations on them](/Y1ESNQ2V52/): the matrix product, the matrix units and the ring $M_n(F)$.
- [Systems of linear equations](/DXSXFVDMXQ/): row reduction, used to compute kernels and images.
