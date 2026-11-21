Two square matrices are similar when they describe the same linear map in two bases. So a question about a map that does not depend on a basis, such as whether $T^k = 0$ for some $k$ or how fast the powers $T^k$ grow, is a question about the similarity class of its matrix. This chapter answers the question that sits behind all of these: when are two matrices similar, and what is the simplest matrix in each class?

The characteristic polynomial does not answer it. The matrices $J_2(0) \oplus J_2(0)$ and $J_2(0) \oplus J_1(0) \oplus J_1(0)$ have the same characteristic polynomial $x^4$ and the same minimal polynomial $x^2$, yet they are not similar, since the first has rank $2$ and the second rank $1$. The full answer is a list of polynomials $d_1 \mid d_2 \mid \cdots \mid d_r$, the invariant factors, which every matrix over every field has and which can be computed by gcds of polynomials. Each class then holds exactly one *rational canonical form*, a block diagonal matrix of companion matrices. When the characteristic polynomial splits, as it always does over $\C$, the same data give the *Jordan normal form*, a block diagonal matrix of Jordan blocks $\lambda I + N$. With the Jordan form the powers and the exponential of a matrix become explicit, and the solutions of $x' = Ax$ can be written down.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Cyclic subspaces and companion matrices.** The [cyclic subspace](/42MMQBTP0M/) spanned by $v, Tv, T^2 v, \dots$ and the [companion matrix](/0ZCWPNZTQ3/) of a monic polynomial, which is the matrix of $T$ on such a subspace.
2. **Invariant factors and the rational canonical form.** The [cyclic decomposition theorem](/R3Z20J19BR/) splits $V$ into cyclic subspaces with annihilators $d_1 \mid \cdots \mid d_r$. These [invariant factors](/F7GJPMVBXA/) decide similarity and give the [rational canonical form](/042JWAR3Q0/), and [the Smith normal form of $xI - A$](/92VZF0QRM8/) computes them.
3. **Two consequences over every field.** [Similarity does not depend on the field](/5PVFX89NM7/), and [every matrix is similar to its transpose](/C708QKZPE6/).
4. **The Jordan normal form.** The [Jordan block](/07PH4RX0X5/), the [normal form of nilpotent endomorphisms](/Z2RTKWZZAZ/) by chains and partitions, the [Jordan normal form](/085HQ5G5TE/) itself, and [how to compute it](/7M1W0ZA49Q/) from the numbers $\dim \ker (A - \lambda I)^k$.
5. **Other forms for special purposes.** The [real Jordan form](/MPFT45RFGV/) for real matrices with nonreal eigenvalues, and the [Weyr form](/9XEA4VR8WP/), which suits problems about commuting matrices.
6. **Centralizers and the shape of the classification.** The dimension of the space of [matrices that commute with a given matrix](/GXZGWZSJ2J/), an [overview of the classification](/H3E52HTEZ2/) and its limits, and the [conjugacy classes of $GL_n$ over a finite field](/4FV9TDGWWH/).

## A first reading

For a first reading, take these entries in order: [cyclic subspace and cyclic vector](/42MMQBTP0M/), [companion matrix](/0ZCWPNZTQ3/), [cyclic decomposition theorem](/R3Z20J19BR/), [invariant factors and elementary divisors](/F7GJPMVBXA/), [rational canonical form](/042JWAR3Q0/), [Jordan block](/07PH4RX0X5/), [normal form of nilpotent endomorphisms](/Z2RTKWZZAZ/), [Jordan normal form](/085HQ5G5TE/) and [computing the Jordan form](/7M1W0ZA49Q/). Work the attached examples of the last two by hand: the block counts from kernel dimensions are the method used most often in practice.

The Smith normal form, the two consequences over every field, the Weyr form, centralizers and the finite groups can wait for a second pass. A reader who needs only the Jordan form over $\C$ can go from the Jordan block straight to the end of group 4, taking the cyclic decomposition on trust.

## Before you start

You need [eigenvalues, the characteristic polynomial and the minimal polynomial](/6R1D6QPY3S/), in particular the [minimal polynomial](/03NDVCSHSB/) and the [Cayley-Hamilton theorem](/0F765KFC2J/). From the [previous chapter](/Z6S6PWMJPH/) you need [invariant subspaces](/0ACX5QT8TE/), [generalized eigenspaces](/0AJ035ZTZE/) and the [decomposition into generalized eigenspaces](/0Z3GDY89T5/), which reduces the Jordan form to the case of a [nilpotent endomorphism](/063D5Z2C70/). You also need [similar matrices](/027KDW2K72/) and division with remainder and gcds in $F[x]$. The module proofs use [modules over a principal ideal domain](/WKJXXX0DYG/) and the view of [an endomorphism as an $F[x]$-module](/KGVTFBZX59/); the elementary proofs do not.
