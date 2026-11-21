A number $a \ne 0$ has a reciprocal, and the equation $ax = b$ is solved by $x = a^{-1}b$. A square matrix $A$ sometimes has an inverse in the same sense: a matrix $A^{-1}$ with $AA^{-1} = A^{-1}A = I_n$. When it does, the system $Ax = b$ has exactly one solution for every right-hand side, namely $x = A^{-1}b$, and the linear map $x \mapsto Ax$ can be undone. When it does not, some nonzero vector is sent to $0$, and information is lost. The matrix $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has the inverse $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$; the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has none, because it sends $(2, -1)$ to $0$.

The tool of the chapter is Gaussian elimination, seen as matrix algebra. Each row operation is multiplication on the left by an elementary matrix, so a whole elimination is one matrix product. Read this way, elimination decides whether $A$ is invertible, computes $A^{-1}$, and factors $A$ into simpler pieces. The factorization $A = LU$ into a lower and an upper triangular matrix is how computers solve linear systems: the work of elimination is done once, and each new right-hand side then costs only two triangular solves.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Inverses and their first rules.** The [invertible matrix](/0EB9N0S33C/), the [inverse of a $2 \times 2$ matrix](/8XWC7RKNN1/), the [inverse of a product](/0S4WTRE9GG/), and the theorem that a [one-sided inverse of a square matrix is two-sided](/0753Y2X5K6/).
2. **Elementary matrices and row reduction.** [Elementary matrices](/01REXW3WWE/) perform row operations. A square matrix is invertible exactly when its [reduced row echelon form is the identity](/1ZK55FS2BF/), and reducing $[A \mid I_n]$ [computes the inverse](/0Z83DHFMYM/).
3. **The invertible matrix theorem.** The [invertible matrix theorem](/ACDFDABVQK/) collects the many equivalent tests, and [triangular matrices](/7X1B65CTG4/) are invertible exactly when their diagonal entries are nonzero.
4. **Groups of matrices and transvections.** The [general linear group](/0FCHE902D7/) and the [special linear group](/0V9PMN0RBH/), with the [transvections](/0DTCBCKEJP/) that [generate](/YSS4XNY9RC/) $\mathrm{SL}_n(F)$.
5. **Factorizations from elimination.** The [LU decomposition](/0RKG5YW66Y/), the [Schur complement](/6HWFBXYPZP/) of a block, and the [Sherman-Morrison-Woodbury formula](/MDZDEFE53C/) for the inverse after a low-rank change.
6. **Equivalence of matrices.** Under row and column operations together, [equivalent matrices](/0CMHSGTWXB/) are classified by rank alone.

## A first reading

For a first reading, take these entries in order: [invertible matrix](/0EB9N0S33C/), [inverse of a $2 \times 2$ matrix](/8XWC7RKNN1/), [inverse of a product](/0S4WTRE9GG/), [elementary matrix](/01REXW3WWE/), [invertibility and the reduced row echelon form](/1ZK55FS2BF/), [computing the inverse by row reduction](/0Z83DHFMYM/), [one-sided inverse of a square matrix is two-sided](/0753Y2X5K6/), [invertible matrix theorem](/ACDFDABVQK/) and [LU decomposition](/0RKG5YW66Y/). Work at least one example by hand in each: the attached examples invert a $3 \times 3$ matrix, catch a singular one, and factor a matrix as $LU$ and as $PA = LU$.

The groups $\mathrm{GL}_n$ and $\mathrm{SL}_n$, transvections, the Schur complement, the Sherman-Morrison-Woodbury formula and equivalent matrices can wait for a second pass. The group-theoretic entries matter later for geometry and algebra, and the block formulas for numerical work and statistics.

## Before you start

You need [elementary row operations](/04XWH28452/), the [reduced row echelon form](/0WF5AQYTW6/), [Gaussian elimination](/0JVJ2WCXZH/) and [Gauss-Jordan elimination](/098D6FQN3N/) from the chapter on systems of linear equations, and the [homogeneous system](/04KGXJG1A2/) $Ax = 0$. From the chapter on matrices you need [matrix multiplication](/032Q9FB8MT/) and its [associativity](/073E4XC016/), the [identity matrix](/6NHZRCKJNW/), the [transpose](/09DXWYRD43/), [upper triangular matrices](/0N4XY7Z3NN/), [block matrices](/0ASDFEQS6P/) and the [matrix units](/4H93XF4RVH/) $E_{ij}$. Some conditions of the invertible matrix theorem use [linear independence](/0CRMGPAH83/), [span](/0DTY8B9HMS/) and [rank](/0ZC9YTXZRY/), which the next chapters treat in full; the [determinant](/00KDZRW4C0/) appears in a few remarks and is the subject of its own chapter. For the group entries, the definition of a [group](/G5S1M9/) is enough.
