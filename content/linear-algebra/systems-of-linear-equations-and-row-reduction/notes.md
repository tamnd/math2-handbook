## History

Elimination is far older than matrices. The Chinese collection *The Nine Chapters on the Mathematical Art* has a chapter called *Fangcheng*, "rectangular arrays". In it, systems of linear equations are set out as arrays of counting rods, one column per equation, and solved by subtracting multiples of one column from another. That is Gaussian elimination in all but name, with negative numbers handled by explicit rules. Liu Hui wrote a commentary on the book in the third century.

In Europe, Newton's *Arithmetica Universalis* (1707) gave rules for eliminating unknowns from a set of equations. Leibniz, in a letter of 1693, wrote the coefficients of a system with double indices and found the condition for three equations in two unknowns to be consistent. Gabriel Cramer published his rule for solving $n$ equations in $n$ unknowns in 1750, in his *Introduction à l'analyse des lignes courbes algébriques*.

Large systems came from astronomy and surveying. Legendre published the method of least squares in 1805. In 1810, in his work on the orbit of the asteroid Pallas, Gauss described a systematic elimination for the normal equations of least squares, with a bracket notation that surveyors and geodesists took up. The variant that goes on to the reduced form is named after Wilhelm Jordan, a German geodesist, who described it in the 1888 edition of his handbook of surveying; B.-I. Clasen published the same method that year. It is not named after the mathematician Camille Jordan. The name "Gaussian elimination" itself became standard only in the twentieth century, with the arrival of electronic computers.

The rank criterion for consistency has many names. Eugène Rouché and Alfredo Capelli both stated it in the nineteenth century, and it is called the Rouché-Capelli theorem in Italy and in English, the Kronecker-Capelli theorem in Russia, the Rouché-Fontené theorem in France and the Rouché-Frobenius theorem in Spain. The short proof that the reduced row echelon form is unique, by induction on the number of columns, is due to Thomas Yuster, "The reduced row echelon form of a matrix is unique: a simple proof", *Mathematics Magazine* 57 (1984).

Linear systems over $\F_2$ have a popular face in the game Lights Out, sold by Tiger Electronics from 1995 on a $5 \times 5$ board. Which patterns can be solved is a question about the rank of a $25 \times 25$ matrix over $\F_2$, which is $23$.

## Further reading

- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*. Its first chapter covers this chapter's material, from row reduction to vector equations and the structure of solution sets, with many drill exercises.
- Gilbert Strang, *Introduction to Linear Algebra*. Treats elimination as the factorization $A = LU$ from the start, a good bridge to the chapter on matrix factorizations.
- Jim Hefferon, *Linear Algebra*. A freely available text whose first chapter proves the theory of Gauss's method with care, including the uniqueness of the reduced form.
- Lloyd N. Trefethen and David Bau, *Numerical Linear Algebra*. Explains what happens to elimination in floating-point arithmetic: pivoting, stability and operation counts.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*. The standard reference for the algorithms behind linear systems on a computer.
- Joseph F. Grcar, "Mathematicians of Gaussian elimination", *Notices of the American Mathematical Society* 58 (2011). A short, well-sourced history of the method from the *Nine Chapters* to the computer age.
