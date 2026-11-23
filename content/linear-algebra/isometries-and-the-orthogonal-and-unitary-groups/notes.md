## History

Rotations were studied long before matrices. In the 1770s Leonhard Euler proved, by an argument in spherical geometry, that every motion of a rigid body with one point fixed is a rotation about an axis through that point; in the language of this chapter, every element of $SO(3)$ has the eigenvalue $1$. Olinde Rodrigues gave formulas in 1840 for composing two rotations in terms of their axes and angles. In 1843 William Rowan Hamilton found the quaternions, and it was soon seen that unit quaternions describe the rotations of space, each rotation coming from two quaternions $\pm q$. This is the map from $SU(2)$ onto $SO(3)$ in another form.

Arthur Cayley published his parametrization of orthogonal matrices by skew-symmetric ones in 1846. It produces every orthogonal matrix without the eigenvalue $-1$ by rational formulas, and so it gives rotations with rational entries in abundance. Hermann Weyl's book *The Classical Groups: Their Invariants and Representations* (1939) made the orthogonal, unitary and symplectic groups a standard subject.

The theorem that every orthogonal map of $\R^n$ is a product of at most $n$ reflections is named after Élie Cartan, who used it in his lectures on spinors in the 1930s, and Jean Dieudonné, who proved it for quadratic forms over general fields. A result of a different kind is the Mazur–Ulam theorem of 1932: a distance-preserving map of a real normed space onto another is affine. For inner product spaces this chapter proves the linear case directly, without the hypothesis that the map is onto.

Reflections returned in numerical analysis in 1958, when Alston Householder proposed them for reducing a matrix to triangular form. Householder reflections are now the standard way to compute a QR factorization, and they are numerically stable because orthogonal matrices do not enlarge rounding errors.

## Further reading

- Michael Artin, *Algebra*, second edition (2011). The chapters on symmetry and on linear groups treat $O(n)$, $SO(3)$ and $SU(2)$ with many pictures and examples.
- John Stillwell, *Naive Lie Theory* (2008). Rotations, quaternions and the classical groups using matrices only, with the map from $SU(2)$ to $SO(3)$ worked out in full.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, second edition (2015). The first chapters study matrix groups such as $O(n)$, $U(n)$ and $SU(n)$ both as groups and as spaces, with the exponential map.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (1939). The classic account of these groups and their invariant theory, harder going but still rewarding.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, fourth edition (2013). Householder reflections, Givens rotations and their use in the QR factorization and in eigenvalue algorithms.
