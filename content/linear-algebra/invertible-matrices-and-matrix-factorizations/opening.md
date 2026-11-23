Take $A = \begin{pmatrix} 2 & 1 \\ 4 & 5 \end{pmatrix}$. One step of elimination, subtracting twice row 1 from row 2, turns it into $U = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$. That step is multiplication on the left by $\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}$, and undoing it is multiplication by $\begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$. So

$$A = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix},$$

a lower triangular factor that stores the multiplier $2$ times an upper triangular factor that stores the pivots $2$ and $3$. Since neither pivot is zero, $A$ can be undone: $A^{-1} = \tfrac16 \begin{pmatrix} 5 & -1 \\ -4 & 2 \end{pmatrix}$, and every system $Ax = b$ has exactly one solution. The chapter turns this small computation into theory. It says when a square matrix has an inverse, how row reduction finds the inverse, and what the factorizations produced by elimination tell you.

The same ideas run through the rest of linear algebra. A change of basis is an invertible matrix. The invertible matrices of one size form a group, and its subgroups, such as the rotations, are the symmetry groups of geometry. In numerical work, nobody computes $A^{-1}$ to solve $Ax = b$: you factor $A = LU$ once and then solve two triangular systems for each right side.

## What the chapter covers

1. **Inverses.** The [invertible matrix](/0EB9N0S33C/) and its unique inverse, the [inverse of a $2 \times 2$ matrix](/8XWC7RKNN1/), the reversal rule for the [inverse of a product](/0S4WTRE9GG/), and the fact that for square matrices over a field a [one-sided inverse is two-sided](/0753Y2X5K6/).
2. **Elementary matrices and row reduction.** Each row operation is an [elementary matrix](/01REXW3WWE/). A square matrix is invertible exactly when its [reduced row echelon form is the identity](/1ZK55FS2BF/), which gives the method of [computing the inverse by row reduction](/0Z83DHFMYM/) and the formula for [solving a system with an inverse](/3RQX3T70NX/).
3. **The invertible matrix theorem.** The [invertible matrix theorem](/ACDFDABVQK/) puts twenty-two equivalent conditions in one list. The [triangular case](/7X1B65CTG4/) reads invertibility off the diagonal.
4. **The general and special linear groups.** The invertible matrices form the [general linear group](/0FCHE902D7/), and those of determinant $1$ form the [special linear group](/0V9PMN0RBH/). The [transvections](/0DTCBCKEJP/) are the shears $I_n + cE_{ij}$, and over a field [they generate the special linear group](/YSS4XNY9RC/).
5. **LU, the Schur complement and low-rank updates.** The [LU decomposition](/0RKG5YW66Y/) stores elimination as two triangular factors. Elimination with whole blocks leads to the [Schur complement](/6HWFBXYPZP/) and the block inverse formula, and from there to the [Sherman-Morrison-Woodbury formula](/MDZDEFE53C/) for updating an inverse.
6. **Equivalence and rank.** With row and column operations both allowed, [equivalent matrices](/0CMHSGTWXB/) are classified by their rank alone.

## A first reading

On a first pass, read these in order:

1. [Invertible matrix](/0EB9N0S33C/)
2. [Inverse of a $2 \times 2$ matrix](/8XWC7RKNN1/)
3. [Inverse of a product](/0S4WTRE9GG/)
4. [Elementary matrix](/01REXW3WWE/)
5. [Invertibility and the reduced row echelon form](/1ZK55FS2BF/)
6. [Computing the inverse by row reduction](/0Z83DHFMYM/)
7. [Invertible matrix theorem](/ACDFDABVQK/)
8. [LU decomposition](/0RKG5YW66Y/)
9. [Equivalent matrices](/0CMHSGTWXB/)

The invertible matrix theorem quotes rank, bases, determinants and eigenvalues, which come in later chapters. Read the conditions you already know and come back to the others when you meet them. The group-theoretic entries, the generation of the special linear group, the Schur complement and the Sherman-Morrison-Woodbury formula can wait for a second pass. They matter most if you go on to group theory or to numerical linear algebra.

## Before you start

You need [row reduction](/DXSXFVDMXQ/): the three [elementary row operations](/04XWH28452/), the [reduced row echelon form](/0WF5AQYTW6/) and [Gauss-Jordan elimination](/098D6FQN3N/). You also need the matrix product, the transpose and block matrices from [matrices and the operations on them](/Y1ESNQ2V52/). The groups in this chapter use the definition of a [group](/G5S1M9/), and a few results use the [determinant](/00KDZRW4C0/), which has its own [chapter](/DTBK11SR77/). For the triangular factors, the [upper triangular matrices](/0N4XY7Z3NN/) of the previous chapter are enough.
