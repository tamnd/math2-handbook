Three towns are joined by one-way bus routes: from town 1 to towns 2 and 3, from town 2 to town 3, and from town 3 back to town 1. Record the routes in a table with a $1$ in row $i$, column $j$ when a bus runs from town $i$ to town $j$:
$$A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}.$$
How many trips with exactly one change lead from town $i$ to town $j$? A trip $i \to k \to j$ needs $a_{ik} = 1$ and $a_{kj} = 1$, so the count is $\sum_k a_{ik} a_{kj}$, which is entry $(i, j)$ of the matrix product $A^2$:
$$A^2 = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}.$$
The entry $(1, 3)$ is $1$, for the trip $1 \to 2 \to 3$, and the entry $(1, 2)$ is $0$, since no trip with one change reaches town 2 from town 1. The same rule of "row times column" composes linear maps, combines systems of equations and chains Markov steps, and this chapter builds the arithmetic of matrices around it.

The product has one feature that numbers lack: the order of the factors matters. For the quarter turn $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and the reflection $S = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ of the plane, $RS = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $SR = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$. Reflecting and then turning is not the same motion as turning and then reflecting. Much of the chapter is about which laws of numbers survive in this setting and which special matrices bring the lost ones back.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Matrices, sums and products.** The [matrix](/0VD9ZSWWJG/) and the [square matrix](/0JXZKX526R/), the [zero matrix](/0ZTKJJDGR7/) and the [identity matrix](/06DW9BAWB1/), [matrix addition and scalar multiplication](/0Y7H3SAVA1/), the [matrix-vector product](/0PDVQEP0ZC/) as a combination of columns, and [matrix multiplication](/032Q9FB8MT/).
2. **The laws of the product and the matrix ring.** The [associative law](/073E4XC016/), which holds over every ring, the failure of commutativity in [noncommutativity of matrix multiplication](/0P506SPZP2/), the [matrix ring](/AB2MD5CD13/) $M_n(R)$, and the [scalar matrices](/067NKSBEWT/), which form its centre.
3. **Diagonal and triangular matrices.** [Diagonal](/044JNC7ZAA/) and [triangular](/0N4XY7Z3NN/) matrices, the shapes that are closed under products and easy to compute with.
4. **The transpose and the conjugate transpose.** The [transpose](/09DXWYRD43/), the rule for the [transpose of a product](/09GK5PS824/), [symmetric](/0VR671PHE5/) and [skew-symmetric](/0PBY4E9GQF/) matrices, and over $\mathbb{C}$ the [conjugate transpose](/0DXKE10PHF/) and [Hermitian matrices](/0P17NGQQMQ/).
5. **Block matrices.** [Block matrices](/0ASDFEQS6P/), multiplied with blocks in place of entries, and [block diagonal matrices](/001T5FJDC1/), which split into independent pieces.
6. **The trace.** The [trace](/0XC1RDBY7A/) and its [cyclic property](/0Y4NF1DRKD/).
7. **Powers, commuting matrices and matrix units.** [Nilpotent](/07BSPZPSMF/), [idempotent](/0KCE8CG86P/) and [involutory](/NH2QE3671N/) matrices, [commuting matrices](/8G3X8MPG7E/) and the binomial theorem, and the [matrix units](/A4HTT7JFD1/) $E_{ij}$, the standard basis of the space of matrices.

## A first reading

For a first pass, read these entries in order:

1. [Matrix](/0VD9ZSWWJG/)
2. [Identity matrix](/06DW9BAWB1/)
3. [Matrix-vector product](/0PDVQEP0ZC/)
4. [Matrix multiplication](/032Q9FB8MT/)
5. [Associativity of matrix multiplication](/073E4XC016/)
6. [Noncommutativity of matrix multiplication](/0P506SPZP2/)
7. [Diagonal matrix](/044JNC7ZAA/)
8. [Upper and lower triangular matrices](/0N4XY7Z3NN/)
9. [Transpose](/09DXWYRD43/)
10. [Transpose of a product](/09GK5PS824/)
11. [Symmetric matrix](/0VR671PHE5/)
12. [Trace of a matrix](/0XC1RDBY7A/)

The matrix ring, the conjugate transpose and Hermitian matrices, block matrices and the matrix units can wait for a second reading. They matter later, for the [determinant](/00KDZRW4C0/), for inner product spaces over $\mathbb{C}$ and for the structure of $M_n(R)$ as a ring, but nothing in the next chapter depends on them. The entries on nilpotent, idempotent and involutory matrices are short and make good practice once the product is familiar.

## Before you start

You need [vectors](/VKVAJ94SKZ/) in $\mathbb{R}^n$ with their sums and scalar multiples, and the [dot product](/0S52TNNTH9/), which is the "row times column" step of the product. Matrices first appear as the coefficient tables of [systems of linear equations and row reduction](/DXSXFVDMXQ/), and that chapter is the natural one to read first. Several entries work over an arbitrary [ring](/0B1261B5ED/), and the statements say each time whether the ring must be commutative; if rings are new, read every statement with $R = \mathbb{R}$ first. The chapter leads on to [invertible matrices and matrix factorizations](/P8J6QR66TJ/), to [determinants](/DTBK11SR77/) and to [matrices of linear maps](/S6559D61BP/).
