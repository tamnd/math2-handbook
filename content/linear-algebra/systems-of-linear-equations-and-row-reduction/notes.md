## History

Elimination is far older than matrices. Chapter 8 of the Chinese *Nine Chapters on the Mathematical Art*, called "Fangcheng" (rectangular arrays), sets out the coefficients of a system in columns on a counting board and clears entries by subtracting multiples of one column from another, which is the method of this chapter turned on its side. Liu Hui wrote a commentary on the book in the 3rd century. In Europe, Leibniz in 1693 and Cramer in 1750 gave determinant formulas for square systems, and Newton's lecture notes on algebra, published in 1707 as *Arithmetica Universalis*, describe elimination of unknowns one by one.

Least squares made elimination a daily tool. Legendre published the method of least squares in 1805, and Gauss also used it; fitting many observations with a few parameters gives normal equations that must be solved by hand. In 1810 Gauss gave a notation for symmetric elimination, and generations of hand computers followed it. In 1888 the geodesist Wilhelm Jordan described the reduction to the fully reduced form in a handbook of surveying, and Clasen published the same method in the same year, probably independently. The Jordan of Gauss–Jordan elimination is not Camille Jordan of the Jordan normal form. The name "Gaussian elimination" for the school method is recent; it came into use in the 1950s, out of confusion about the history.

The theory of when a system has solutions was completed in the second half of the 19th century. The test $\operatorname{rank} A = \operatorname{rank}[A \mid b]$ is linked with Rouché, Capelli, Kronecker, Fontené and Frobenius, and its name varies by country: Kronecker–Capelli in Russia and Poland, Rouché–Fontené in France and Rouché–Frobenius in Spain and much of Latin America.

The textbook vocabulary of the chapter, with row echelon forms, pivots, basic and free variables, and the existence and uniqueness theorem, settled in 20th-century textbooks such as those of Hoffman and Kunze and of Lay. A short proof of the uniqueness of the reduced row echelon form, by induction on the number of columns, was published by Yuster in *Mathematics Magazine* in 1984. With electronic computers the question of rounding errors came to the front, and the study of pivoting strategies became part of numerical linear algebra.

## Further reading

- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*, 5th edition. Chapter 1 follows the same path as this chapter, from row reduction to the existence and uniqueness theorem and the parametric vector form.
- Gilbert Strang, *Introduction to Linear Algebra*, 6th edition (2023). Good for the row picture and the column picture of a system and for elimination seen as a factorization $A = LU$.
- Jim Hefferon, *Linear Algebra*, a free textbook. Its first chapter proves the facts about Gaussian elimination and the reduced echelon form with full arguments.
- Lloyd N. Trefethen and David Bau, *Numerical Linear Algebra* (1997). What happens to elimination in floating-point arithmetic, and why pivoting is needed.
- Joseph F. Grcar, "Mathematicians of Gaussian elimination", *Notices of the American Mathematical Society* (2011). A careful history of the method, from the *Nine Chapters* to the computer age.
