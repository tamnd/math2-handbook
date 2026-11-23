## History

Elimination is much older than matrices. The Chinese text *The Nine Chapters on the Mathematical Art* already solves systems of linear equations by operations on the rows of a table of coefficients. Gauss used elimination to solve the normal equations of his method of least squares. The variant that also clears the entries above each pivot carries the name of the geodesist Wilhelm Jordan, and the method of reducing $[A \mid I_n]$ to $[I_n \mid A^{-1}]$ is now called [Gauss-Jordan elimination](/098D6FQN3N/).

The inverse of a matrix appears in Cayley's memoir on the theory of matrices of 1858. Cayley built it from the adjugate and the determinant, so his formula needs a nonzero determinant. The rank of a matrix, the only invariant of [equivalence](/0CMHSGTWXB/) over a field, was named by Frobenius in 1879. For integer matrices more is left: Smith found in 1861 the normal form that now carries his name.

The groups $\mathrm{GL}_n$ and $\mathrm{SL}_n$ grew out of the study of substitutions. Camille Jordan treated linear groups over the fields of prime order in his *Traité des substitutions* of 1870. Dickson extended the theory to all finite fields in his book *Linear Groups* of 1901. The generation of the [special linear group](/0V9PMN0RBH/) by [transvections](/0DTCBCKEJP/) is a basic step in that theory.

The factorizations of this chapter belong to the twentieth century and to numerical computation. Banachiewicz introduced the [LU decomposition](/0RKG5YW66Y/) in 1938, in his work on the solution of linear systems, and Crout published his variant in 1941. In 1948 Turing analyzed elimination in his paper "Rounding-off errors in matrix processes", where he wrote elimination as a factorization into triangular matrices. The determinant formula $\det M = \det A \det(D - CA^{-1}B)$ goes back to a paper of Schur from 1917. Emilie Haynsworth introduced the name [Schur complement](/6HWFBXYPZP/) and the notation $M/A$ in 1968, and with Crabtree she proved the quotient formula in 1969. Sherman and Morrison published the rank one update formula in 1949 and 1950, and Woodbury gave the rank $k$ form in a report of 1950.

## Further reading

- Gilbert Strang, *Introduction to Linear Algebra*. Builds the subject around elimination and $A = LU$, with many worked examples of inverses and factorizations.
- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*. A first course with a careful treatment of the invertible matrix theorem, partitioned matrices and the LU factorization.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*. The reference for block matrices, Schur complements and inverse formulas, at a graduate level.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*. The standard text on how LU, pivoting and low-rank updates are carried out in practice.
- Lloyd N. Trefethen and David Bau, *Numerical Linear Algebra*. Short lectures that explain why elimination needs pivoting and what it costs.
