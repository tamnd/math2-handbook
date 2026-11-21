## History

Least squares began in astronomy and geodesy, where more observations were made than there were unknowns, and the observations did not agree. Adrien-Marie Legendre published the method in 1805, in an appendix to *Nouvelles méthodes pour la détermination des orbites des comètes*, and gave it its name. Carl Friedrich Gauss published it in 1809 in *Theoria motus corporum coelestium* and claimed to have used it since 1795. He linked it to a normal distribution of errors, and the dispute over priority lasted for years. Gauss solved the normal equations by the elimination that now carries his name.

The geometry came later. Jørgen Pedersen Gram studied expansions in series by least squares in 1883, and Erhard Schmidt gave the orthogonalization process in its modern form in 1907, in his work on integral equations. In the early twentieth century the theory of Hilbert spaces made orthogonal complements and projections central: the projection theorem says that every closed subspace of a Hilbert space has a complement with $H = U \oplus U^\perp$. Legendre's polynomials, from his work on the attraction of spheroids in the 1780s, and Joseph Fourier's series, from *Théorie analytique de la chaleur* of 1822, became examples of orthogonal expansions in spaces of functions.

The four fundamental subspaces and their orthogonality are old as facts, but the picture of them as two pairs of orthogonal complements became a teaching standard through Gilbert Strang's textbooks. The generalized inverse that gives the shortest least-squares solution was described by E. H. Moore in 1920 and independently by Roger Penrose in 1955, in "A generalized inverse for matrices".

Numerical practice moved away from the normal equations once computers made the loss of accuracy visible. Alston Householder showed in 1958 how to triangularize a matrix by reflections, and Gene Golub used Householder's method in 1965 to solve least-squares problems through a QR decomposition, without forming $A^{\mathsf{T}} A$. Principal angles go back to Camille Jordan, who discussed angles between subspaces of any dimension in 1875. Harold Hotelling's canonical correlations of 1936 are the same idea in statistics, and Åke Björck and Gene Golub gave a stable algorithm for computing the angles in 1973.

## Further reading

- Gilbert Strang, *Introduction to Linear Algebra*, sixth edition (2023). The four fundamental subspaces, projections and least squares, with many fitted lines and parabolas.
- David C. Lay, Steven R. Lay and Judi J. McDonald, *Linear Algebra and Its Applications*, fifth edition (2016). The chapter on orthogonality covers orthogonal complements, projections, Gram-Schmidt, QR and least squares at the level of this chapter, with applications to linear models.
- Sheldon Axler, *Linear Algebra Done Right*, fourth edition (2024). Orthogonal complements and minimization problems in abstract inner product spaces, including approximation of functions by polynomials.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997). Short lectures on projectors, QR by Gram-Schmidt and Householder reflections, and the conditioning and stability of least squares.
- Åke Björck, *Numerical Methods for Least Squares Problems* (1996). The standard reference on the algorithms, from normal equations to QR and the SVD, with their error analysis.
