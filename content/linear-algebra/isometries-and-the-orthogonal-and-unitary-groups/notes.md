## History

Rotations were studied long before matrices. In the 1770s Euler showed, by an argument in spherical geometry, that every motion of a rigid body that keeps one point fixed is a rotation about some axis through that point. That is the statement that every element of $SO(3)$ has the eigenvalue $1$, and the proof by determinants that the chapter gives is much later. Olinde Rodrigues gave formulas in 1840 for the composite of two rotations in terms of their axes and angles. In 1843 Hamilton found the quaternions, and soon afterwards it was seen that unit quaternions describe rotations of space, each rotation coming from two quaternions $\pm q$. This is the map $SU(2) \to SO(3)$ in another form.

Cayley published his parametrization of orthogonal matrices by skew-symmetric ones in 1846. It gives every orthogonal matrix without the eigenvalue $-1$ by rational formulas, and it was one of the first results about matrices as objects in their own right. Later in the century the theory of quadratic forms and of the transformations that keep them invariant, developed by Hermite, Frobenius and others, gave the unitary and orthogonal groups their present setting. Weyl's book on the classical groups (1939) made these groups a standard subject, together with their invariants and representations.

The theorem that every orthogonal map of $\R^n$ is a product of at most $n$ reflections is due to Élie Cartan, who used it in his lectures on spinors in the 1930s. Jean Dieudonné extended it to quadratic forms over general fields. A different kind of result is the Mazur–Ulam theorem of 1932: a distance-preserving surjection of one real normed space onto another is affine. So on spaces with a norm, keeping distances already forces linearity up to a translation.

In numerical work, reflections came back in 1958, when Householder proposed using them to reduce a matrix to triangular form. Householder reflections are now the standard way to compute a QR factorization. They are stable because orthogonal matrices do not enlarge rounding errors.

## Further reading

- Michael Artin, *Algebra*, 2nd edition (2011). The chapters on symmetry and on linear groups treat $O(n)$, $SO(3)$ and $SU(2)$ with many pictures and examples.
- John Stillwell, *Naive Lie Theory* (2008). Rotations, quaternions and the classical groups are treated with matrices only, and $SU(2) \to SO(3)$ is worked out in full.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition (2015). The first chapters study matrix groups such as $O(n)$, $U(n)$ and $SU(n)$ as groups and as spaces.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (1939). The classic account, harder going but still worth reading.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (2013). It covers Householder reflections, Givens rotations and their use in QR.
