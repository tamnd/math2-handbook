## History

Eigenvalue problems came from mechanics and astronomy before there were matrices. In the eighteenth century Euler found the principal axes of a rotating rigid body, and Lagrange and Laplace, studying the slow perturbations of the planets, met a polynomial equation whose roots govern the motion. It was called the secular equation, and the name survived in physics long after. In 1829 Cauchy proved that the roots of this equation are real when the system is symmetric, which in modern terms says that a real symmetric matrix has real eigenvalues. The word "characteristic" for the polynomial and its roots goes back to Cauchy.

The Cayley-Hamilton theorem is named after two people who did not prove it in general. Hamilton found a version for linear maps of the quaternions. Cayley, in "A memoir on the theory of matrices" of 1858, the paper that set up the algebra of matrices, stated that every matrix satisfies its own characteristic equation. He checked the case of size $2$, said that he had verified size $3$, and saw no need for a general proof. Frobenius gave the first proof for every size in 1878, in the same work in which he introduced the minimal polynomial, the monic polynomial of least degree that the matrix satisfies.

In 1870 Jordan published the normal form now named after him, in his *Traité des substitutions et des équations algébriques*, for matrices over finite fields. The theory of a single linear map through its eigenvalues and its invariant polynomials then took the shape it has in this chapter and the next ones. The prefix "eigen", German for "own" or "proper", came into use through Hilbert's work on integral equations of 1904, and English took over "eigenvalue" and "eigenvector" from it.

Computation followed a different path from the theory. Finding the roots of the characteristic polynomial is a poor method for large matrices, because the roots are very sensitive to small errors in the coefficients. The power method, which multiplies a vector by $A$ again and again, was described by von Mises and Pollaczek-Geiringer in 1929. The QR algorithm, found independently by John Francis and Vera Kublanovskaya around 1961, became the standard method and remains so. On the side of teaching, Sheldon Axler's article "Down with Determinants!" in the *American Mathematical Monthly* of 1995 showed how to prove the existence of eigenvalues over $\C$ without the characteristic polynomial, the proof given in this chapter.

## Further reading

- Sheldon Axler, *Linear Algebra Done Right*: eigenvalues, invariant subspaces and the minimal polynomial developed before determinants, as in the existence proof of this chapter.
- Sheldon Axler, "Down with Determinants!", *American Mathematical Monthly*, 1995: a short article that explains the approach and the proof without determinants.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra*: characteristic and minimal polynomials, annihilating polynomials and the Cayley-Hamilton theorem, with full proofs over a field.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*: many results on eigenvalues of matrices, including those of $AB$ and $BA$ and of commuting matrices.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*: how eigenvalues are computed in practice, from the power method to the QR algorithm.
