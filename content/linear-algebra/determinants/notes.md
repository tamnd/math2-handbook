## History

Determinants are older than matrices. They arose as the expressions that appear when a system of linear equations is solved by elimination, long before anyone arranged the coefficients in a square array and treated it as an object. In a letter of 1693, Gottfried Wilhelm Leibniz used combinations of the coefficients, indexed by pairs of numbers, to decide when a system of linear equations in several unknowns has a solution. The [Leibniz formula](/016PE4VZ8Q/) carries his name for this reason, though its modern form, a sum over the symmetric group with the sign of each permutation, came much later.

Colin Maclaurin's *Treatise of Algebra*, published in 1748 after his death, solves systems of two and three equations with what is now [Cramer's rule](/0977KZ6PQB/). Gabriel Cramer stated the rule for any number of unknowns in 1750, in his *Introduction à l'analyse des lignes courbes algébriques*, where he needed it to find curves through given points. The rule was a recipe for the solution, and the question of how to compute and manipulate the expressions themselves stayed open.

The word "determinant" comes from Carl Friedrich Gauss, who used it in the *Disquisitiones Arithmeticae* (1801) for the discriminant of a quadratic form, a narrower meaning than the present one. In 1812 Augustin-Louis Cauchy and Jacques Binet both proved the [product rule](/04CPJ6AF00/), and with it the [Cauchy–Binet formula](/08WE2W7DYS/) for the product of a wide and a tall matrix. Cauchy also used the word in its modern sense. The [Laplace expansion](/0C08BQ3M05/), the [Vandermonde determinant](/0P84B554AS/) and [Jacobi's formula](/357FEAZ0Q4/) carry the names of Pierre-Simon Laplace, Alexandre-Théophile Vandermonde and Carl Gustav Jacob Jacobi.

Many identities of the sixth group are special cases of one another. [Sylvester's identity](/7SSKBQYFW1/) contains, as its case $k = 1$, the basis of Chiò's pivotal condensation, and as its case $k = n - 2$, the Desnanot–Jacobi identity. Charles Lutwidge Dodgson, the author known as Lewis Carroll, published his [condensation method](/RQ44FKS5QM/) in 1866; it repeats the Desnanot–Jacobi identity until a single number remains. The [Weinstein–Aronszajn identity](/0G24VQ1088/) $\det(I_m + AB) = \det(I_n + BA)$ is also called Sylvester's determinant theorem.

The modern definition reverses the historical order. Instead of starting from the formula with $n!$ terms, it starts from the three properties of the [determinant](/00KDZRW4C0/): multilinear, alternating, and $1$ at the identity. The formula, the rules for row operations and the product rule then follow, and the same proofs work over any commutative ring. Thomas Muir's *The Theory of Determinants in the Historical Order of Development* collects the older literature in detail.

## Further reading

- Kenneth Hoffman and Ray Kunze, *Linear Algebra*. Defines determinants over a commutative ring as alternating multilinear forms and proves the product rule and the adjugate identity in that setting.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces*. Treats determinants through alternating forms and defines the determinant of a linear map without choosing a basis.
- Gilbert Strang, *Introduction to Linear Algebra*. The computational side: the big formula, cofactors, Cramer's rule and volumes, with many worked examples.
- Sheldon Axler, *Linear Algebra Done Right*. Builds the theory of eigenvalues first and reaches determinants late, which shows how much of linear algebra does not need them.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*. The reference for Schur complements, the Cauchy–Binet formula and determinant inequalities.
