## History

Arrays of coefficients are old: the Chinese *Nine Chapters on the Mathematical Art* laid out linear systems as rectangular arrays on a counting board. For a long time, though, such an array was only a way to store a system, or a source of determinants. Sylvester introduced the word "matrix" in 1850 for an array from which determinants can be formed.

Matrices became objects of an algebra in Cayley's memoir on the theory of matrices of 1858. Cayley defined the sum and the product, the product as the composition of linear substitutions, and so obtained the associative law at once. He noted that matrices can be added and multiplied like numbers, but that the product is not commutative, and he used the transposed matrix. The same memoir treats square matrices as single quantities that can be raised to powers and put into polynomials.

The structure of matrix rings became a subject of its own in the early 20th century. Wedderburn proved in 1908 that every finite-dimensional simple algebra over a field is a matrix ring $M_n(D)$ over a division algebra $D$, so matrix rings are the building blocks of a large class of rings.

Computation brought new questions. The factorization of a matrix into triangular factors goes back to the elimination methods of Gauss, and Turing analysed its rounding errors in 1948. The row-times-column rule needs $n^3$ multiplications for two $n \times n$ matrices. Strassen showed in 1969 that fewer suffice: splitting into $2 \times 2$ blocks and using seven block products instead of eight, applied again and again, needs only about $n^{2.81}$.

## Further reading

- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*, 5th edition. Chapter 2 develops matrix algebra, block matrices and the transpose with many computed examples.
- Gilbert Strang, *Introduction to Linear Algebra*, 6th edition (2023). Good for the four ways to see a matrix product and for products as compositions of maps.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd edition (2013). The standard reference for special classes of matrices, from Hermitian to nilpotent, with the facts this chapter only begins.
- Sheldon Axler, *Linear Algebra Done Right*, 4th edition (2024). Matrices as the records of linear maps, which explains why the product is defined as it is.
