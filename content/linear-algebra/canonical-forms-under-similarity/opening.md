Here are three real $3 \times 3$ matrices:
$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 3 & 0 \end{pmatrix}, \qquad C = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}.$$
Which of them describe the same linear map in different bases? All three have the characteristic polynomial $x^3 - 3x + 2 = (x - 1)^2 (x + 2)$, so they have the same eigenvalues with the same multiplicities, the same trace and the same determinant. That is not enough. The eigenvalue $1$ has a plane of eigenvectors for $C$, since $C - I$ has rank $1$, but only a line for $A$ and for $B$, since $A - I$ and $B - I$ both have rank $2$. So $C$ is not similar to the other two. And $A$ and $B$ are similar: each has one block for the eigenvalue $1$, of size $2$, and one for $-2$.

This argument used ranks that happen to settle the question in size $3$. In larger sizes one needs the ranks of all the powers $(A - \lambda I)^j$, and over $\Q$ or $\R$ the eigenvalues may not even exist: the matrix of the same shape as $B$ with last row $(2, 0, 0)$ has characteristic polynomial $x^3 - 2$, with one real root and no rational root. The chapter gives two answers that always work. Over any field, a short list of polynomials, the invariant factors, decides similarity, and they can be computed by row and column operations on $x I - A$ with no roots at all. When the characteristic polynomial splits, the list can be refined into the sizes of Jordan blocks, and the Jordan normal form is a matrix as close to diagonal as similarity allows.

The idea behind both answers is already in $B$. Its transpose $B^{\mathsf T}$ sends $e_1$ to $e_2$, $e_2$ to $e_3$, and $e_3$ to $-2 e_1 + 3 e_2$. So $B^{\mathsf T}$ runs through the whole basis starting from the single vector $e_1$, and its matrix is fixed by one polynomial, $x^3 - 3x + 2$, whose coefficients sit in the last column. A vector that generates the space in this way is a cyclic vector, the matrix is a companion matrix, and the whole theory splits a space into pieces of this kind.

The chapter is in 6 groups, read in order.

## What the chapter covers

1. **Cyclic subspaces, companion matrices and modules.** The [cyclic subspace and cyclic vector](/42MMQBTP0M/), the [companion matrix](/0ZCWPNZTQ3/), whose characteristic and minimal polynomials are read off its last column, and [an endomorphism as an $F[x]$-module](/KGVTFBZX59/), in which similar matrices become isomorphic modules.
2. **Invariant factors and the rational canonical form.** The [cyclic decomposition theorem](/R3Z20J19BR/), [invariant factors and elementary divisors](/F7GJPMVBXA/), the [rational canonical form](/042JWAR3Q0/), and [similarity via the characteristic matrix](/92VZF0QRM8/), which computes the invariant factors by the Smith normal form.
3. **Two consequences.** [Similarity does not depend on the field](/5PVFX89NM7/), and [a matrix is similar to its transpose](/C708QKZPE6/).
4. **The Jordan normal form.** The [Jordan block](/07PH4RX0X5/), the [normal form of nilpotent endomorphisms](/Z2RTKWZZAZ/), the [Jordan normal form](/085HQ5G5TE/), and [computing the Jordan form](/7M1W0ZA49Q/) from ranks and chains.
5. **Other normal forms.** The [real Jordan form](/MPFT45RFGV/) for real matrices with complex eigenvalues, and the [Weyr canonical form](/9XEA4VR8WP/).
6. **Commuting matrices and classification.** [Matrices that commute with a given matrix](/GXZGWZSJ2J/), the [classification of matrices up to similarity](/H3E52HTEZ2/), and [conjugacy classes of $GL_n$ over a finite field](/4FV9TDGWWH/).

## A first reading

Take these entries in order: [cyclic subspace and cyclic vector](/42MMQBTP0M/), [companion matrix](/0ZCWPNZTQ3/), [invariant factors and elementary divisors](/F7GJPMVBXA/), [rational canonical form](/042JWAR3Q0/), [Jordan block](/07PH4RX0X5/), [normal form of nilpotent endomorphisms](/Z2RTKWZZAZ/), [Jordan normal form](/085HQ5G5TE/), [computing the Jordan form](/7M1W0ZA49Q/) and [classification of matrices up to similarity](/H3E52HTEZ2/). This path gives both normal forms and the practical method for finding them. On a first pass skip the module viewpoint, the Smith normal form, the Weyr form and the count for finite fields; read them when you need to compute without eigenvalues or to see why the theory works over any principal ideal domain.

## Before you start

You need [eigenvalues, the characteristic polynomial and the minimal polynomial](/6R1D6QPY3S/), with the Cayley-Hamilton theorem. From [diagonalization, triangularization and invariant subspaces](/Z6S6PWMJPH/) you need invariant subspaces, generalized eigenspaces and the reasons a matrix can fail to be diagonalizable. The [modules over a principal ideal domain](/WKJXXX0DYG/) chapter is needed only for the module proofs; the elementary proofs use polynomial division and greatest common divisors.
