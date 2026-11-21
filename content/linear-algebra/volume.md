Linear algebra studies [vector spaces](/000AYPA9AJ/), the [linear maps](/0NRYHJPQG2/) between them, and the [matrices](/0VD9ZSWWJG/) that represent these maps. A vector space over a field is a set whose elements can be added and multiplied by scalars, with the usual rules of arithmetic. A linear map keeps both operations: $T(u + v) = T(u) + T(v)$ and $T(cv) = c\,T(v)$. Arrows in space, polynomials, the solutions of $y'' + y = 0$ and matrices are all vectors in this sense, and one theory covers them.

The subject is used in almost every part of mathematics and in physics, statistics, engineering and computing, because many problems become linear in a first approximation. A circuit, a chemical equation and a discretized differential equation all lead to a system $Ax = b$. The long-run state of a Markov chain is an eigenvector for the eigenvalue $1$, a line fitted to data is an orthogonal projection, and a compressed image is a truncated singular value decomposition. The Chinese *Nine Chapters on the Mathematical Art* already solved linear systems by elimination, and Peano gave the axioms of a vector space in 1888.

This volume treats linear algebra over a field, mostly in finite dimension, from vectors in the plane to the spectral theorems, the singular value decomposition and quadratic forms. [Matrix theory and multilinear algebra](/WMBK7M313V/), [numerical analysis](/FJEK0GMJ2J/), [rings and modules](/G7N6BDTEZ2/) and [functional analysis](/AFJZYWP3WQ/) have their own areas.

## What the volume teaches

- **Three views of one problem.** The system $x + 2y = 5$, $3x + 4y = 6$ is a pair of equations, a matrix equation $Ax = b$, and a question about a linear map, as the [overview](/Y7PBW8VD4Q/) shows. Equations give algorithms, matrices give computation, and maps give the theory.
- **One algorithm.** [Gaussian elimination](/0JVJ2WCXZH/) solves systems, inverts matrices, and finds ranks, bases and determinants.
- **Bases and dimension.** All bases of a space have the same size, by the [Steinitz exchange lemma](/08ZDRN6H41/). A space with a basis of $n$ vectors is a copy of $F^n$, and [dimension is the only invariant](/0VJBSK15SN/) of a finite-dimensional space.
- **Kernel and image.** The [rank-nullity theorem](/0W4FSW1TVB/) says $\dim V = \dim \ker T + \dim \operatorname{im} T$.
- **What does not change with the basis.** A [change of basis](/0MQXVZEBMT/) replaces a matrix by a [similar](/0E89HQATM8/) one. Rank, trace, [determinant](/00KDZRW4C0/) and [characteristic polynomial](/0VSSPAFM2C/) stay the same, and the [invariant factors](/F7GJPMVBXA/) decide similarity completely.
- **Splitting a map into simple pieces.** [Eigenvalues](/0BQAA2BK3Q/) and invariant subspaces lead to the [diagonalizable](/07SQCNV233/) maps and, for the others, to the [Jordan normal form](/085HQ5G5TE/).
- **Geometry from an inner product.** An [inner product](/0NB0AWGJBW/) gives lengths and right angles, orthogonal [projection](/0B8KZRT28M/) gives [least squares](/0BYTQ4X1HC/), and the [spectral theorem](/06J4PXRG22/) gives every real symmetric matrix an orthonormal basis of eigenvectors.
- **Every matrix is an isometry, a stretch and an isometry.** The [singular value decomposition](/000NPTMX6J/) $A = U \Sigma V^*$ holds for every matrix.
- **Forms are not maps.** A [bilinear form](/0SQZMXB6GP/) changes as $P^{\mathsf T} A P$, not $P^{-1} A P$, and its classification depends on the field, as [Sylvester's law of inertia](/0WFED3K3DQ/) shows over $\R$.

## The chapters

**Chapter 3.1, Overview and vectors in the plane and in space**, opens with the [overview](/Y7PBW8VD4Q/) and three essays, then treats [Euclidean vectors](/0QN3D80AWP/), the [dot](/0S52TNNTH9/) and [cross](/0N5N15HWZ7/) products, lines and [planes](/07SDJ5DNE4/).

**Chapter 3.2, Systems of linear equations and row reduction**, solves every [linear system](/0GT4WWGWH2/) by [elementary row operations](/04XWH28452/), proves that the [reduced form is unique](/BF9SMZMJZE/), and describes the [solution set](/PDH3HKXWAZ/) as a particular solution plus the solutions of $Ax = 0$.

**Chapter 3.3, Matrices and the operations on them**, builds the algebra of matrices: [multiplication](/032Q9FB8MT/), which is [not commutative](/0P506SPZP2/), the [transpose](/09DXWYRD43/), [blocks](/0ASDFEQS6P/), the [trace](/0XC1RDBY7A/) and the named kinds of matrices.

**Chapter 3.4, Invertible matrices and matrix factorizations**, reads elimination as products of [elementary matrices](/01REXW3WWE/), proves the [invertible matrix theorem](/ACDFDABVQK/) and gives the [LU decomposition](/0RKG5YW66Y/).

**Chapter 3.5, Vector spaces, span, independence, bases and dimension**, gives the axioms and examples, [span](/0DTY8B9HMS/), [linear independence](/0CRMGPAH83/), [bases](/0KCQ9Y3QKA/) and [dimension](/03GSZ8RTZJ/), and, with Zorn's lemma, a [basis of every space](/00MS9VMQ9Z/).

**Chapter 3.6, Linear maps**, treats [kernel](/0S23E6YE83/) and [image](/0WSFKKT6FF/), the [rank-nullity theorem](/0W4FSW1TVB/), [isomorphisms](/0B8T10CE7N/) and the [space of linear maps](/0X9MBPP2Z3/).

**Chapter 3.7, Direct sums, complements and quotient spaces**, cuts a space into pieces by [direct sums](/0XYYT5KNTX/) and [projections](/033DA1WE8Y/), forms [quotient spaces](/0BR3FY5Q8M/), and proves the [isomorphism theorems](/0MTBGVZ4XJ/).

**Chapter 3.8, Matrices of linear maps, rank and change of basis**, joins maps and matrices through the [matrix of a linear map](/0YQSGNYE3K/), proves that [row rank equals column rank](/0TZAG60ZYT/), and ends with [similar matrices](/0E89HQATM8/).

**Chapter 3.9, Dual spaces and duality**, studies [linear forms](/07YQ1C78G0/), the [dual space](/07JBSZE0V4/), [annihilators](/0ASHNYF7AG/), the [double dual](/0ZJM9D7NPS/) and the [dual map](/0AZ5ARP287/), whose matrix is the transpose.

**Chapter 3.10, Determinants**, defines the [determinant](/00KDZRW4C0/) as the unique normalized alternating multilinear function, writes it by the [Leibniz formula](/016PE4VZ8Q/), proves the [product rule](/04CPJ6AF00/), and covers [Laplace expansion](/0C08BQ3M05/), [Cramer's rule](/0977KZ6PQB/) and [volume](/RC5BTSG8T2/).

**Chapter 3.11, Eigenvalues, the characteristic polynomial and the minimal polynomial**, defines [eigenvalues](/0BQAA2BK3Q/) and [eigenvectors](/0N6960W0BV/), finds them as roots of the [characteristic polynomial](/0VSSPAFM2C/), and proves the [Cayley-Hamilton theorem](/0F765KFC2J/) with the [minimal polynomial](/03NDVCSHSB/).

**Chapter 3.12, Diagonalization, triangularization and invariant subspaces**, decides when a map is [diagonalizable](/07SQCNV233/), [triangularizes](/0363JMQ42Y/) it when its characteristic polynomial splits, and decomposes the space into [generalized eigenspaces](/0Z3GDY89T5/).

**Chapter 3.13, Canonical forms under similarity**, answers when two matrices are similar, by the [rational canonical form](/042JWAR3Q0/) and the [Jordan normal form](/085HQ5G5TE/).

**Chapter 3.14, Inner product spaces**, treats real and complex [inner products](/0NB0AWGJBW/), the [Cauchy-Schwarz inequality](/0RFWW56Y22/), [orthonormal bases](/0S9GGTR0EX/) and the [Gram-Schmidt process](/0VT6P0GNQR/).

**Chapter 3.15, Orthogonal complements, projections and least squares**, splits a space as $U \oplus U^\perp$, proves the [best approximation theorem](/0MCDDSCB9Z/), and solves [least-squares problems](/0BYTQ4X1HC/) by the [normal equations](/4D7MRG4D91/) and the [QR decomposition](/0ERWG4NXQ9/).

**Chapter 3.16, Adjoints, normal operators and the spectral theorems**, defines the [adjoint](/0R9NMSM1ZP/) and proves that [normal operators](/0C8BR8XRTR/) over $\C$ and [self-adjoint operators](/0NEGN5CRSC/) over $\R$ are exactly those with an orthonormal basis of eigenvectors, in the [complex](/04CW1P44VD/) and [real spectral theorems](/06J4PXRG22/).

**Chapter 3.17, Isometries and the orthogonal and unitary groups**, studies the maps that keep the inner product: [orthogonal](/0W02QESPJQ/) and [unitary matrices](/0AR68JTMDT/), their groups, and [Euler's rotation theorem](/2ZVG43GSKA/).

**Chapter 3.18, Positive definite matrices and the singular value decomposition**, tests [positive definite matrices](/0KX66CZMBB/), gives the [Cholesky decomposition](/0WKG8CYY6A/) and the [singular value decomposition](/000NPTMX6J/), and proves the [best low-rank approximation](/JJT6GC055J/).

**Chapter 3.19, Bilinear and sesquilinear forms**, treats [bilinear forms](/0SQZMXB6GP/) and [congruence](/WJWNYSQKK8/), [Hermitian forms](/48P4A1CX85/), the [classification of alternating forms](/V8KKHKXXB3/) and [Witt's theorem](/CCB8VNQCV0/).

**Chapter 3.20, Quadratic forms over fields and the principal axis theorem**, diagonalizes [quadratic forms](/0RBQS1JJCR/), proves [Sylvester's law of inertia](/0WFED3K3DQ/), and uses the [principal axis theorem](/0PR5P9Z4KM/) for [conics](/1DGT7X9E35/) and quadrics.

**Chapter 3.21, Applications of linear algebra**, shows the theory at work in [curve fitting](/C170QFW8QB/), [Markov chains](/Y9FRWY8YX4/), [differential equations](/DH7CQXQYJX/), [computer graphics](/REB4ZHN28T/) and [image compression](/9QB82PPEMV/).

## How to read this volume

If this is your first course, read these entries in this order: [linear algebra: overview](/Y7PBW8VD4Q/), [Gaussian elimination](/0JVJ2WCXZH/), [reduced row echelon form](/0WF5AQYTW6/), [matrix multiplication](/032Q9FB8MT/), [invertible matrix theorem](/ACDFDABVQK/), [vector space](/000AYPA9AJ/), [linear independence](/0CRMGPAH83/), [basis](/0KCQ9Y3QKA/), [dimension](/03GSZ8RTZJ/), [linear map](/0NRYHJPQG2/), [rank-nullity theorem](/0W4FSW1TVB/), [matrix of a linear map](/0YQSGNYE3K/), [change of basis formula](/0MQXVZEBMT/), [determinant](/00KDZRW4C0/), [eigenvalue](/0BQAA2BK3Q/), [characteristic polynomial](/0VSSPAFM2C/), [diagonalizable matrix](/07SQCNV233/), [Gram-Schmidt process](/0VT6P0GNQR/), [least squares](/0BYTQ4X1HC/) and the [real spectral theorem](/06J4PXRG22/). Do the exercises marked ◦ and • in Chapters 3.2, 3.5, 3.6, 3.11, 3.12 and 3.15. That is a complete first course.

Chapters 3.1 to 3.4 compute with matrices, 3.5 to 3.9 build the theory of spaces and maps, 3.10 to 3.13 study one operator, and 3.14 to 3.18 add an inner product. Chapters 3.7, 3.9, 3.13, 3.19 and 3.20 can wait for a second course, and Chapter 3.21 can be read at any time after its prerequisites. The opening page of each chapter names a first reading.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to follow and write short proofs, including [proof by contradiction](/0J0XBKG64S/) and [mathematical induction](/0ASJVEFA9J/) from Volume 1, and to compute with real and complex numbers. Chapter 3.1 needs only school algebra, geometry and trigonometry. From algebra the volume uses the definition of a [field](/04C5ZBG1WT/), the [polynomial ring](/0Q9EZS90GY/) $F[x]$ with division with remainder, the [symmetric group](/0515A6D2Y1/) for determinants, and the definition of a [group](/G5S1M9/) for the matrix groups. The [fundamental theorem of algebra](/0JP0W07Y9A/) supplies eigenvalues over $\C$, and [Zorn's lemma](/04RXTQA5ZA/) appears only for infinite-dimensional spaces. Calculus is needed only in a few examples and entries.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely: compute a small case or decide whether a map is linear; each takes a few minutes. Exercises marked • ask you to use a theorem in a new place, such as proving a small claim about a subspace or a rank, or building a counterexample; each takes some thought. Exercises marked ★ are harder; some ask for a known result in your own words. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
