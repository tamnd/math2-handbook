Try to compute the tenth power of two $2 \times 2$ matrices by hand:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad C = \begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix}.$$
Both have trace $6$, and multiplying ten times is slow for either. For $A$ there is a shortcut. The vector $(1, 1)$ goes to $(3, 3)$ and the vector $(1, -1)$ goes to $(1, -1)$, so in the basis made of these two vectors $A$ only stretches: by $3$ along the first and by $1$ along the second. Write $e_1 = \tfrac12 (1, 1) + \tfrac12 (1, -1)$, apply $A^k$ to each part, and do the same for $e_2$. The result is
$$A^k = \frac12 \begin{pmatrix} 3^k + 1 & 3^k - 1 \\ 3^k - 1 & 3^k + 1 \end{pmatrix},$$
so $A^{10}$ has the entries $29525$ and $29524$ with no multiplication of matrices at all.

The same idea fails for $C$. Its characteristic polynomial is $t^2 - 6t + 9 = (t - 3)^2$, so $3$ is the only eigenvalue, and $C - 3I = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$ has rank $1$. The eigenvectors fill one line, spanned by $(1, 1)$, and there is no basis of eigenvectors. Something survives, though. The matrix $N = C - 3I$ satisfies $N^2 = 0$, and $3I$ commutes with $N$, so the binomial theorem stops after two terms:
$$C^k = (3I + N)^k = 3^k I + k \, 3^{k-1} N.$$
For $k = 10$ this gives the entries $255879$, $-196830$, $196830$ and $-137781$. The factor $k$ in front of $3^{k-1}$ is new: it cannot come from any diagonal matrix, and it is the trace left by the missing eigenvector.

These two computations are the whole chapter in small. A map is easiest to handle in a basis of eigenvectors, and the first question is when such a basis exists. When it does not, the map still splits as a part that only stretches plus a part that dies after a few steps, and the two parts commute. Both statements rest on one notion, the invariant subspace: a subspace that the map sends into itself. A basis of eigenvectors splits the space into invariant lines; a triangular form is a chain of invariant subspaces, one in each dimension; and the generalized eigenspaces are invariant pieces on which the map has a single eigenvalue.

The chapter is in 7 groups, read in order.

## What the chapter covers

1. **Invariant subspaces and the two pieces of a map.** The [invariant subspace](/0ACX5QT8TE/) and the [restriction and quotient operators](/0KN7EPH7Z0/), which cut a map into two smaller maps whose characteristic polynomials multiply to the original one.
2. **When a map is diagonalizable.** The [diagonalizable matrix](/07SQCNV233/), the [characterization by a basis of eigenvectors](/056SW1E0AC/), the sufficient condition of [$n$ distinct eigenvalues](/0Y95Z7MT02/), the [test by multiplicities](/CDB8KCNNG9/), the [minimal polynomial test](/0MPAJRB23T/), and the [defective matrices](/5F2AV5855Y/) that fail.
3. **Using a diagonalization.** The [eigendecomposition](/D0AP2R7272/), [powers of a diagonalizable matrix](/0TNR9BQ871/) and [simultaneous diagonalization](/0FK17N4DKA/) of commuting maps.
4. **Triangular forms.** [Triangularization](/0363JMQ42Y/) when the characteristic polynomial splits, and [simultaneous triangularization](/42PG67Q5YN/) of commuting maps.
5. **Splitting the space with polynomials.** The [kernels lemma](/ACBNK1VFVG/) and the [primary decomposition theorem](/49ZHBMYKVE/).
6. **Generalized eigenvectors.** The [generalized eigenvector](/01H6QKWGDH/), the [generalized eigenspace](/0AJ035ZTZE/) and the [decomposition into generalized eigenspaces](/0Z3GDY89T5/).
7. **Nilpotent and semisimple parts.** [Nilpotent](/063D5Z2C70/) and [semisimple](/08VRX3Q4PB/) endomorphisms, the [Jordan-Chevalley decomposition](/011K11VPJN/) and the [Fitting decomposition](/77SACA9CVQ/).

## A first reading

Take these entries in order: [invariant subspace](/0ACX5QT8TE/), [diagonalizable matrix](/07SQCNV233/), [diagonalizable iff there is a basis of eigenvectors](/056SW1E0AC/), [$n$ distinct eigenvalues imply diagonalizable](/0Y95Z7MT02/), [the test by multiplicities](/CDB8KCNNG9/), [defective matrix](/5F2AV5855Y/), [powers of a diagonalizable matrix](/0TNR9BQ871/), [triangularization](/0363JMQ42Y/), [generalized eigenspace](/0AJ035ZTZE/) and [the decomposition into generalized eigenspaces](/0Z3GDY89T5/). They answer the three practical questions: whether a matrix is diagonalizable, how to diagonalize it, and what to do when it is not. On a first pass you can skip the quotient operator, the simultaneous forms, semisimple maps and the Fitting decomposition. The kernels lemma and the primary decomposition give the general proof of the generalized eigenspace decomposition, and they matter most over fields such as $\Q$ and $\R$, where the characteristic polynomial need not split.

## Before you start

You need [eigenvalues, the characteristic polynomial and the minimal polynomial](/6R1D6QPY3S/), including the Cayley-Hamilton theorem and the algebraic and geometric multiplicities. The [direct sums, complements and quotient spaces](/QHKTJ89V6S/) chapter supplies the language of direct sums, projections and quotient spaces. From [determinants](/DTBK11SR77/) you need the determinant of a triangular and of a block triangular matrix. The chapter on [canonical forms under similarity](/GEBYZKYV3D/) comes next and builds the Jordan normal form on top of this one.
