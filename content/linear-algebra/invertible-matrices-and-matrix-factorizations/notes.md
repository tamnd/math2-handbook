## History

Elimination is much older than matrices. The Chinese text *The Nine Chapters on the Mathematical Art* solves systems of linear equations by operations on the rows of a table of coefficients, which are the row operations of this chapter. Gauss used elimination in his work on least squares in the early nineteenth century, and the method carries his name. In 1888 Wilhelm Jordan, a German geodesist, described the full reduction that also clears the entries above each pivot, and the name Gauss-Jordan elimination comes from his work.

The inverse of a matrix needs the matrix product, and both appear in Arthur Cayley's "A memoir on the theory of matrices" of 1858. Cayley treated matrices as quantities that can be added and multiplied, and gave the inverse of a square matrix as its adjugate divided by its determinant. That a one-sided inverse of a square matrix is two-sided was standard in the matrix algebra of the nineteenth century. The long list of equivalent conditions now called the invertible matrix theorem is a feature of modern textbooks; Lay's is a well-known example.

Leonard Eugene Dickson's book *Linear Groups, with an Exposition of the Galois Field Theory* of 1901 is a classic account of the groups of invertible matrices over finite fields. Jean Dieudonné later used transvections throughout his work on the classical groups, and Robert Steinberg used the commutator relations between elementary matrices, now called the Steinberg relations, to give presentations of groups such as $\mathrm{SL}_n$.

The factorization $A = LU$ was introduced by Tadeusz Banachiewicz in 1938, and Prescott Crout published a variant in 1941. Alan Turing analysed elimination as a factorization in his 1948 paper "Rounding-off errors in matrix processes", one of the first studies of the accuracy of matrix computations. Issai Schur used the determinant formula for a block matrix in a paper of 1917 on power series bounded in the unit disc; Emilie Haynsworth named the Schur complement and introduced the notation $M/A$ in 1968, and in 1969 she and Douglas Crabtree proved the quotient formula. Jack Sherman and Winifred Morrison published the formula for a rank-one change of an inverse in 1949 and 1950, and Max Woodbury gave the rank-$k$ form in a report of 1950.

Equivalence of matrices has its own history. Henry John Stephen Smith found a normal form for integer matrices under row and column operations in 1861, now called the Smith normal form. Over a field the classification is simpler: Frobenius introduced the rank of a matrix, and the rank is the only invariant of equivalence.

## Further reading

- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*, fifth edition (2016). Chapter 2 treats inverses, elementary matrices, the invertible matrix theorem and the LU factorization at the level of this chapter, with many numerical examples.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra*, second edition (1971). Chapter 1 develops row reduction, elementary matrices and invertibility with full proofs.
- Jim Hefferon, *Linear Algebra*, a free textbook. Its section on inverses works through Gauss-Jordan inversion slowly, with exercises and answers.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, second edition (2013). Chapter 0 collects block matrices, Schur complements and the Sherman-Morrison-Woodbury formula; Section 3.5 covers the existence and uniqueness of LU factorizations.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, fourth edition (2013). The standard reference on how LU factorization with pivoting is carried out and analysed on a computer.
