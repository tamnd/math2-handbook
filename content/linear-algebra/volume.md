Linear algebra studies [vector spaces](/000AYPA9AJ/), the [linear maps](/0NRYHJPQG2/) between them, and the [matrices](/0VD9ZSWWJG/) that represent these maps once bases are chosen. A vector space over a field is a set whose elements can be added and multiplied by scalars under the usual rules, and a linear map keeps both operations: $T(u + v) = T(u) + T(v)$ and $T(cv) = c\,T(v)$. Arrows, polynomials, the solutions of $y'' + y = 0$ and matrices are all vectors in this sense.

The subject is used across mathematics, science and computing, because many problems are linear, at least approximately. A circuit, a chemical equation and a discretized differential equation lead to a system $Ax = b$; the long-run state of a Markov chain is an eigenvector for the eigenvalue $1$; a line fitted to data is an orthogonal projection; a compressed image is a truncated singular value decomposition. Elimination already appears in the Chinese *Nine Chapters on the Mathematical Art*; Cayley wrote the first memoir on matrix algebra in 1858, and Peano gave the axioms of a vector space in 1888.

This volume treats linear algebra over a field, mostly in finite dimension; its 398 entries are arranged in twenty-one chapters, from vectors in the plane to the spectral theorems, the singular value decomposition, quadratic forms and a chapter of applications. [Matrix theory and multilinear algebra](/WMBK7M313V/), [numerical analysis](/FJEK0GMJ2J/), [rings and modules](/G7N6BDTEZ2/) and [functional analysis](/AFJZYWP3WQ/) continue where it stops.

## What the volume teaches

- **Three views of one problem.** The system $x + 2y = 5$, $3x + 4y = 6$ is a pair of equations, a matrix equation $Ax = b$, and a question about a linear map, as the [overview](/Y7PBW8VD4Q/) shows.
- **One algorithm.** [Gaussian elimination](/0JVJ2WCXZH/) solves systems, inverts matrices, and finds ranks, bases and determinants.
- **Bases and dimension.** All bases of a space have the same size, by the [Steinitz exchange lemma](/08ZDRN6H41/), and a finite-dimensional space is [determined by its dimension](/0VJBSK15SN/) up to isomorphism.
- **Kernel and image.** For a linear map $T$ on a finite-dimensional space $V$, the [rank-nullity theorem](/0W4FSW1TVB/) gives $\dim V = \dim \ker T + \dim \operatorname{im} T$.
- **What does not depend on the basis.** A [change of basis](/0MQXVZEBMT/) replaces the matrix of an operator by a [similar](/0E89HQATM8/) one. Rank, trace, [determinant](/00KDZRW4C0/) and [characteristic polynomial](/0VSSPAFM2C/) are unchanged, and the [invariant factors](/F7GJPMVBXA/) decide similarity.
- **Splitting an operator into simple pieces.** [Eigenvalues](/0BQAA2BK3Q/) and invariant subspaces lead to the [diagonalizable](/07SQCNV233/) operators and, when the characteristic polynomial splits, to the [Jordan normal form](/085HQ5G5TE/).
- **Geometry from an inner product.** An [inner product](/0NB0AWGJBW/) gives lengths and right angles, [orthogonal projection](/0B8KZRT28M/) gives [least squares](/0BYTQ4X1HC/), and the [real spectral theorem](/06J4PXRG22/) gives every real symmetric matrix an orthonormal basis of eigenvectors.
- **Every matrix is an isometry, a stretch and an isometry.** The [singular value decomposition](/000NPTMX6J/) $A = U \Sigma V^*$ holds for every real or complex matrix.
- **Forms are not maps.** Under a change of basis the matrix of a [bilinear form](/0SQZMXB6GP/) changes to $P^{\mathsf T} A P$, not $P^{-1} A P$, and the classification of forms depends on the field, as [Sylvester's law of inertia](/0WFED3K3DQ/) shows over $\R$.

## The chapters

**Chapter 3.1, Overview and vectors in the plane and in space**, surveys the subject and treats [Euclidean vectors](/0QN3D80AWP/), the [dot](/0S52TNNTH9/) and [cross](/0N5N15HWZ7/) products, lines, [planes](/07SDJ5DNE4/) and distances.

**Chapter 3.2, Systems of linear equations and row reduction**, solves every [linear system](/0GT4WWGWH2/) by [row operations](/04XWH28452/), proves that the [reduced form is unique](/BF9SMZMJZE/), and describes the [solution set](/PDH3HKXWAZ/).

**Chapter 3.3, Matrices and the operations on them**, builds the algebra of matrices: [multiplication](/032Q9FB8MT/), which is [not commutative](/0P506SPZP2/), the [transpose](/09DXWYRD43/), [blocks](/0ASDFEQS6P/) and the [trace](/0XC1RDBY7A/).

**Chapter 3.4, Invertible matrices and matrix factorizations**, reads elimination as products of [elementary matrices](/01REXW3WWE/), proves the [invertible matrix theorem](/ACDFDABVQK/), and gives the [general linear group](/0FCHE902D7/) and the [LU decomposition](/0RKG5YW66Y/).

**Chapter 3.5, Vector spaces, span, independence, bases and dimension**, gives the axioms, [span](/0DTY8B9HMS/), [linear independence](/0CRMGPAH83/), [bases](/0KCQ9Y3QKA/) and [dimension](/03GSZ8RTZJ/), and, with Zorn's lemma, a [basis of every space](/00MS9VMQ9Z/).

**Chapter 3.6, Linear maps**, treats the [kernel](/0S23E6YE83/) and [image](/0WSFKKT6FF/), the rank-nullity theorem, [isomorphisms](/0B8T10CE7N/) and the [space of linear maps](/0X9MBPP2Z3/).

**Chapter 3.7, Direct sums, complements and quotient spaces**, cuts a space by [direct sums](/0XYYT5KNTX/) and [projections](/033DA1WE8Y/), divides it by [quotients](/0BR3FY5Q8M/), and ends with the [isomorphism theorems](/0MTBGVZ4XJ/) and [exact sequences](/946YAZNYKX/).

**Chapter 3.8, Matrices of linear maps, rank and change of basis**, joins maps and matrices through the [matrix of a linear map](/0YQSGNYE3K/), studies the [rank](/0ZC9YTXZRY/) and proves that [row rank equals column rank](/0TZAG60ZYT/), and ends with similar matrices.

**Chapter 3.9, Dual spaces and duality**, studies [linear forms](/07YQ1C78G0/), the [dual space](/07JBSZE0V4/), [annihilators](/0ASHNYF7AG/), the [double dual](/0ZJM9D7NPS/) and the [dual map](/0AZ5ARP287/).

**Chapter 3.10, Determinants**, characterizes the determinant by three rules, writes it by the [Leibniz formula](/016PE4VZ8Q/), proves the [product rule](/04CPJ6AF00/), and covers [Laplace expansion](/0C08BQ3M05/), [Cramer's rule](/0977KZ6PQB/) and [volume](/RC5BTSG8T2/).

**Chapter 3.11, Eigenvalues, the characteristic polynomial and the minimal polynomial**, finds [eigenvectors](/0N6960W0BV/) as roots of the characteristic polynomial, and proves the [Cayley-Hamilton theorem](/0F765KFC2J/) with the [minimal polynomial](/03NDVCSHSB/).

**Chapter 3.12, Diagonalization, triangularization and invariant subspaces**, decides when an operator is diagonalizable, [triangularizes](/0363JMQ42Y/) it when its characteristic polynomial splits, and splits the space into [generalized eigenspaces](/0Z3GDY89T5/).

**Chapter 3.13, Canonical forms under similarity**, decides similarity by the [rational canonical form](/042JWAR3Q0/), which exists over every field, and by the Jordan normal form.

**Chapter 3.14, Inner product spaces**, treats real and complex inner products, the [Cauchy-Schwarz inequality](/0RFWW56Y22/), [orthonormal bases](/0S9GGTR0EX/), [Parseval's identity](/047RFCNVSK/) and the [Gram-Schmidt process](/0VT6P0GNQR/).

**Chapter 3.15, Orthogonal complements, projections and least squares**, proves the [best approximation theorem](/0MCDDSCB9Z/) and solves least-squares problems by the [normal equations](/4D7MRG4D91/) and the [QR decomposition](/0ERWG4NXQ9/).

**Chapter 3.16, Adjoints, normal operators and the spectral theorems**, defines the [adjoint](/0R9NMSM1ZP/), proves the [Schur decomposition](/V1JG4C7R7B/), and characterizes the operators with an orthonormal eigenbasis: [normal](/0C8BR8XRTR/) ones over $\C$, in the [complex spectral theorem](/04CW1P44VD/), and [self-adjoint](/0NEGN5CRSC/) ones over $\R$.

**Chapter 3.17, Isometries and the orthogonal and unitary groups**, studies [orthogonal](/0W02QESPJQ/) and [unitary](/0AR68JTMDT/) matrices, their groups and [Euler's rotation theorem](/2ZVG43GSKA/).

**Chapter 3.18, Positive definite matrices and the singular value decomposition**, tests [positive definiteness](/0KX66CZMBB/), gives the [Cholesky](/0WKG8CYY6A/) and [polar](/0J2C7BDJQA/) decompositions and the SVD, and proves the [Eckart-Young-Mirsky theorem](/JJT6GC055J/).

**Chapter 3.19, Bilinear and sesquilinear forms**, treats [congruence](/WJWNYSQKK8/), [Hermitian forms](/48P4A1CX85/), the [classification of alternating forms](/V8KKHKXXB3/) and [Witt's theorem](/CCB8VNQCV0/).

**Chapter 3.20, Quadratic forms over fields and the principal axis theorem**, diagonalizes [quadratic forms](/0RBQS1JJCR/), classifies them over $\C$, $\R$ and [finite fields](/2HBR7137AD/), and puts [conics](/1DGT7X9E35/) in normal form by the [principal axis theorem](/0PR5P9Z4KM/).

**Chapter 3.21, Applications of linear algebra**, shows the theory at work in [curve fitting](/C170QFW8QB/), [Markov chains](/Y9FRWY8YX4/), [differential equations](/DH7CQXQYJX/), [computer graphics](/REB4ZHN28T/), [image compression](/9QB82PPEMV/) and the [Lights Out puzzle](/E8DZ9CPEEE/).

## How to read this volume

Start with Chapter 3.1, which surveys the subject and then works with vectors in the plane and in space. From there two routes lead on. If you want computations first, read Chapters 3.2, 3.3 and 3.4 on systems, matrices and invertible matrices, then Chapters 3.5 and 3.6 on spaces and maps. If you prefer structure first, go from vectors straight to Chapters 3.5 and 3.6, and come back to Chapters 3.2 to 3.4 when matrices appear as the coordinates of maps. Both routes meet in Chapter 3.8 at rank and change of basis. From there determinants, eigenvalues, inner products and forms build on each other in the order of the chapters. Chapters 3.7, 3.9, 3.13, 3.19 and 3.20 can wait for a second course, and Chapter 3.21 can be read at any time after its prerequisites.

If this is your first course, read these entries in this order: [linear algebra: overview](/Y7PBW8VD4Q/), [Gaussian elimination](/0JVJ2WCXZH/), [matrix multiplication](/032Q9FB8MT/), [invertible matrix theorem](/ACDFDABVQK/), [vector space](/000AYPA9AJ/), [linear independence](/0CRMGPAH83/), [basis](/0KCQ9Y3QKA/), [dimension](/03GSZ8RTZJ/), [linear map](/0NRYHJPQG2/), [rank-nullity theorem](/0W4FSW1TVB/), [matrix of a linear map](/0YQSGNYE3K/), [change of basis formula](/0MQXVZEBMT/), [determinant](/00KDZRW4C0/), [eigenvalue](/0BQAA2BK3Q/), [diagonalizable matrix](/07SQCNV233/), [Gram-Schmidt process](/0VT6P0GNQR/), [least squares](/0BYTQ4X1HC/), [real spectral theorem](/06J4PXRG22/) and [singular value decomposition](/000NPTMX6J/). With the exercises marked ◦ and • in Chapters 3.2, 3.5, 3.6, 3.11, 3.12 and 3.15, that is a complete first course.

## What you need first

You should be able to follow and write short proofs, including [proof by contradiction](/0J0XBKG64S/) and [mathematical induction](/0ASJVEFA9J/), and to compute with real and complex numbers. Chapter 3.1 needs only school algebra, geometry and trigonometry. From algebra the volume uses the definition of a [field](/04C5ZBG1WT/), the [polynomial ring](/0Q9EZS90GY/) $F[x]$ with division with remainder, the [symmetric group](/0515A6D2Y1/) for determinants, and the definition of a [group](/G5S1M9/) for the matrix groups. The [fundamental theorem of algebra](/0JP0W07Y9A/) supplies eigenvalues over $\C$, and [Zorn's lemma](/04RXTQA5ZA/) appears only for spaces of infinite dimension. Calculus appears only in some examples and applications.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you have read the entries closely, for example by computing a small case; each takes a few minutes. Exercises marked • ask you to use a theorem in a new place, to prove a short claim about a subspace or a rank, or to build a counterexample. Exercises marked ★ are harder, and some ask for a known result in your own words. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
