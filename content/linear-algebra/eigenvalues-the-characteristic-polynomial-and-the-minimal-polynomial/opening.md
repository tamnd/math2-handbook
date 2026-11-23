Let $A = \begin{pmatrix} 5 & -6 \\ 3 & -4 \end{pmatrix}$ and compute $A^{10} \begin{pmatrix} 3 \\ 2 \end{pmatrix}$. Multiplying ten times is slow, but two vectors make it easy. One checks that $A (2, 1)^{\mathsf{T}} = (4, 2)^{\mathsf{T}} = 2 \, (2, 1)^{\mathsf{T}}$ and $A (1, 1)^{\mathsf{T}} = (-1, -1)^{\mathsf{T}} = -(1, 1)^{\mathsf{T}}$. On these two lines $A$ only stretches, by $2$ and by $-1$. Since $(3, 2) = (2, 1) + (1, 1)$, ten applications of $A$ give
$$A^{10} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = 2^{10} \begin{pmatrix} 2 \\ 1 \end{pmatrix} + (-1)^{10} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2049 \\ 1025 \end{pmatrix}.$$
The vectors $(2, 1)$ and $(1, 1)$ are eigenvectors, and $2$ and $-1$ are the eigenvalues. To find them without guessing, note that $Av = \lambda v$ with $v \ne 0$ says that $A - \lambda I$ is singular, that is $\det(A - \lambda I) = 0$. Here this is $\lambda^2 - \lambda - 2 = (\lambda - 2)(\lambda + 1) = 0$. The search for special vectors has become the search for the roots of a polynomial of degree $2$.

There is a second polynomial in the picture. Since $(A - 2I)(A + I)$ kills both eigenvectors, and they form a basis, $A^2 - A - 2I = 0$. So $A^2 = A + 2I$, and every power of $A$ is a combination of $A$ and $I$. This chapter makes both observations general. The [characteristic polynomial](/0VSSPAFM2C/) $\det(tI - A)$ has the eigenvalues as its roots. The [minimal polynomial](/03NDVCSHSB/) is the monic polynomial of least degree that kills $A$. The [Cayley–Hamilton theorem](/0F765KFC2J/) says that $A$ always satisfies its characteristic polynomial, even when there are not enough eigenvectors to make a basis.

## What the chapter covers

The chapter is in seven groups, read in order. The first four build the eigenvalues and the characteristic polynomial, the fifth deals with existence, and the last two with polynomials in a map.

1. **Eigenvalues, eigenvectors and eigenspaces.** [Eigenvalues](/0BQAA2BK3Q/), [eigenvectors](/0N6960W0BV/), [eigenspaces](/0G0RFPG8HR/) and the [spectrum](/0XPX5NC67E/) of a matrix.
2. **The characteristic polynomial.** The [characteristic polynomial](/0VSSPAFM2C/) of a matrix and that of an [endomorphism](/C98TZ6ZAXC/), the theorem that [eigenvalues are its roots](/053QVHF6N7/), and the [method by hand](/7JJE96MZQY/).
3. **Coefficients, trace and determinant.** The [coefficients](/0FRYPZ6D0X/) as sums of principal minors, the [trace as the sum](/0NMXDCNNKR/) and the [determinant as the product](/0C2F40MEBC/) of the eigenvalues.
4. **Independence and multiplicities.** [Eigenvectors for distinct eigenvalues are independent](/0HNMFG8F8K/); [algebraic](/0FY42N02DV/) and [geometric](/099TWVJ909/) multiplicity.
5. **Existence of eigenvalues, and two products.** [Existence over an algebraically closed field](/08CJB2NQ92/), [invariant lines and planes of real maps](/KAV44BRV77/), the [eigenvalues of $AB$ and $BA$](/MCXV71BY74/), and [left eigenvectors](/32M8VY9A1M/).
6. **Polynomials in a map and the minimal polynomial.** The [polynomial of an endomorphism](/0E3MV6E6MG/), [annihilating polynomials](/0PBN8VEKY8/), the [minimal polynomial](/03NDVCSHSB/), the fact that it [divides every annihilating polynomial](/0VTAD25A3G/), and that its [roots are the eigenvalues](/0QF4ZEFG52/).
7. **The Cayley–Hamilton theorem.** The [theorem](/0F765KFC2J/), the consequence that the [minimal polynomial divides the characteristic polynomial](/093X6MN6Y6/), and [inverses and powers](/R4CPYXFJEQ/) computed from it.

## A first reading

A first course needs these entries, in this order.

- [Eigenvalue](/0BQAA2BK3Q/), [eigenvector](/0N6960W0BV/) and [eigenspace](/0G0RFPG8HR/).
- The [characteristic polynomial](/0VSSPAFM2C/) and the theorem that [eigenvalues are its roots](/053QVHF6N7/).
- [Computing eigenvalues and eigenvectors by hand](/7JJE96MZQY/).
- [Trace](/0NMXDCNNKR/) and [determinant](/0C2F40MEBC/) in terms of the eigenvalues.
- [Eigenvectors with distinct eigenvalues are independent](/0HNMFG8F8K/).
- [Algebraic](/0FY42N02DV/) and [geometric](/099TWVJ909/) multiplicity.
- The [minimal polynomial](/03NDVCSHSB/).
- The [Cayley–Hamilton theorem](/0F765KFC2J/).

The characteristic polynomial of an endomorphism, the general formula for the coefficients, and the results on real maps, on $AB$ and $BA$, and on left eigenvectors can wait until a second reading. The entry on [existence over an algebraically closed field](/08CJB2NQ92/) is worth reading early: it gives two proofs, and the second uses no determinants at all.

## Before you start

The chapter uses the following.

- [Vector spaces, span, independence, bases and dimension](/MVH97H8B2J/) and [linear maps](/9080WQTZ3M/), with kernels and the rank–nullity theorem.
- [Matrices and the operations on them](/Y1ESNQ2V52/), and [matrices of linear maps and change of basis](/S6559D61BP/), for similarity.
- [Determinants](/DTBK11SR77/), in particular the product rule, the invertibility test and the adjugate identity, which is the heart of the proof of Cayley–Hamilton.
- The [polynomial ring](/0Q9EZS90GY/) over a field: division with remainder, roots and factors, and ideals of $F[x]$.

The next chapter, [diagonalization, triangularization and invariant subspaces](/Z6S6PWMJPH/), uses all of this to decide when a matrix has a basis of eigenvectors.
