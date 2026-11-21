Take the matrix $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ and the recurrence $x_{k+1} = A x_k$. Computing $A^{10}$ by multiplication is slow, but two vectors make it easy. $A$ sends $(1, 1)$ to $(5, 5)$ and $(1, -2)$ to $(2, -4)$: it stretches the first by $5$ and the second by $2$. Since $(2, -1) = (1, 1) + (1, -2)$, the recurrence started at $x_0 = (2, -1)$ gives
$$x_k = A^k x_0 = 5^k (1, 1) + 2^k (1, -2)$$
for every $k$, and for large $k$ the vector $x_k$ points almost exactly along $(1, 1)$. The vectors $(1, 1)$ and $(1, -2)$ are eigenvectors of $A$, and $5$ and $2$ are its eigenvalues. They are the roots of the characteristic polynomial $\det(tI - A) = t^2 - 7t + 10$.

The same polynomial carries more information. The Cayley-Hamilton theorem says that $A^2 - 7A + 10I = 0$. Hence $A(7I - A) = 10I$, so $A^{-1} = \frac{1}{10}(7I - A)$, and every power of $A$ is a combination of $A$ and $I$. Eigenvalues come up wherever a linear map is applied over and over or changes in time: in linear recurrences, in Markov chains, whose long-run distribution is a left eigenvector, in the solutions of $x' = Ax$, and in the principal axes of a quadratic form. The chapter builds the tools for all of these. It studies one endomorphism $T$ of a finite-dimensional space through its eigenvalues and through the polynomials $f$ with $f(T) = 0$.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Eigenvalues, eigenvectors and eigenspaces.** The definitions of [eigenvalue](/0BQAA2BK3Q/), [eigenvector](/0N6960W0BV/) and [eigenspace](/0G0RFPG8HR/), and the [spectrum](/0XPX5NC67E/), which depends on the field.
2. **The characteristic polynomial.** The [characteristic polynomial](/0VSSPAFM2C/) $\det(tI - A)$ and its version [for an endomorphism](/C98TZ6ZAXC/). The [eigenvalues are its roots](/053QVHF6N7/), and there is a procedure for [computing eigenvalues and eigenvectors by hand](/7JJE96MZQY/).
3. **Trace, determinant and the coefficients.** The [coefficients](/0FRYPZ6D0X/) are sums of principal minors. The trace is the [sum of the eigenvalues](/0NMXDCNNKR/) and the determinant is [their product](/0C2F40MEBC/).
4. **Independence and multiplicities.** [Eigenvectors for distinct eigenvalues are independent](/0HNMFG8F8K/). The group also defines [algebraic](/0FY42N02DV/) and [geometric multiplicity](/099TWVJ909/).
5. **Existence and related eigenvalue problems.** [Existence over an algebraically closed field](/08CJB2NQ92/), [invariant subspaces of dimension 1 or 2](/KAV44BRV77/) for real operators, the [eigenvalues of AB and BA](/MCXV71BY74/) and [left eigenvectors](/32M8VY9A1M/).
6. **Polynomials in an endomorphism and the minimal polynomial.** [Polynomials of an endomorphism](/0E3MV6E6MG/), [annihilating polynomials](/0PBN8VEKY8/), the [minimal polynomial](/03NDVCSHSB/), the fact that [it divides every annihilating polynomial](/0VTAD25A3G/), and [its roots, which are the eigenvalues](/0QF4ZEFG52/).
7. **The Cayley-Hamilton theorem.** The [theorem](/0F765KFC2J/) $p_A(A) = 0$, the divisibilities [$m_A \mid p_A \mid m_A^n$](/093X6MN6Y6/), and the [inverse and powers](/R4CPYXFJEQ/) as polynomials in $A$.

## A first reading

Take these entries in order: [eigenvalue](/0BQAA2BK3Q/), [eigenvector](/0N6960W0BV/), [eigenspace](/0G0RFPG8HR/), [characteristic polynomial](/0VSSPAFM2C/), [eigenvalues are the roots of the characteristic polynomial](/053QVHF6N7/), [computing eigenvalues and eigenvectors by hand](/7JJE96MZQY/), [trace is the sum of the eigenvalues](/0NMXDCNNKR/), [determinant is the product of the eigenvalues](/0C2F40MEBC/), [eigenvectors with distinct eigenvalues are linearly independent](/0HNMFG8F8K/), [geometric multiplicity](/099TWVJ909/), [minimal polynomial](/03NDVCSHSB/) and [Cayley-Hamilton theorem](/0F765KFC2J/). With these you can find the eigenvalues and eigenspaces of a small matrix, compare the two multiplicities, and compute the minimal polynomial.

The fifth group can wait for a second pass. Axler's existence proof, the real invariant subspaces, $AB$ and $BA$, and left eigenvectors are used later, but not in the rest of this chapter. In the last group, the statement that $p_A$ divides $m_A^n$ can also wait. The next chapters use these tools to decide when a matrix is [diagonalizable](/07SQCNV233/) and to reach the [Jordan normal form](/085HQ5G5TE/).

## Before you start

You need [vector spaces, bases and dimension](/MVH97H8B2J/), [matrices and the operations on them](/Y1ESNQ2V52/), and [linear maps](/9080WQTZ3M/) with their kernels. The characteristic polynomial of an endomorphism uses [matrices of linear maps and change of basis](/S6559D61BP/), in particular similar matrices. From [determinants](/DTBK11SR77/) you need the product rule, the rule for triangular matrices and the adjugate. The minimal polynomial uses division with remainder in the [polynomial ring](/0Q9EZS90GY/) $F[x]$.
