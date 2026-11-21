The system $3x + 2y = 7$, $x + 4y = 9$ has exactly one solution because $3 \cdot 4 - 2 \cdot 1 = 10$ is not $0$. The same number is the area of the parallelogram spanned by the columns $(3, 1)$ and $(2, 4)$, and it is the factor by which the map $v \mapsto Av$ multiplies every area in the plane. The determinant generalizes this one number to square matrices of any size. It is a single scalar built from the entries, and it answers several questions at once: whether $A$ is invertible, how $A$ scales volume, whether $A$ keeps or reverses orientation, and, through quotients of determinants, what the solution of $Ax = b$ is.

The determinant is also the tool that the next chapter needs. A scalar $\lambda$ is an eigenvalue of $A$ exactly when $\det(\lambda I - A) = 0$, so the characteristic polynomial is a determinant. Over a commutative ring such as $\Z$, the determinant decides whether a matrix has an inverse with entries in the same ring: the integer matrix with rows $(2, 1)$ and $(1, 1)$ has determinant $1$ and the integer inverse with rows $(1, -1)$ and $(-1, 2)$, while the matrix with rows $(2, 0)$ and $(0, 1)$ has determinant $2$ and no integer inverse.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Small determinants.** The [determinant of a 2 × 2 matrix](/0ZN2J42SK7/) and the [rule of Sarrus](/7H2P40X0MV/) for size $3$, with an example of why the diagonal picture fails for size $4$.
2. **The definition.** An [alternating multilinear map](/0K6CH0MT0F/) vanishes when two arguments agree. The [determinant](/00KDZRW4C0/) is the unique such function of the columns with value $1$ at $I$, and the [Leibniz formula](/016PE4VZ8Q/) writes it as a sum over permutations.
3. **Rules for computing.** [Multilinearity in rows](/0PPG793642/), the [effect of row operations](/09YB3WQG38/), the [triangular rule](/0K1KKMFHYH/) and the [transpose rule](/0ZZQ2E1MTE/) give the computation by elimination.
4. **Products and invertibility.** The [product rule](/04CPJ6AF00/) $\det(AB) = \det A \det B$, the [invertibility criterion](/FBSAPTP1PR/) over a field, and [determinants over commutative rings](/03Q7RE2HXR/).
5. **Minors, cofactors and the adjugate.** [Minors](/0BT9BYWVRY/), [cofactors](/0XPKR18APA/), [Laplace expansion](/0C08BQ3M05/), the [adjugate](/07W9H8QF38/), the identity [A adj A = det A · I](/0528HKWZ1Z/) and [Cramer's rule](/0977KZ6PQB/).
6. **Block matrices and classical identities.** [Block triangular matrices](/0J9TVTNB4K/), the [Schur complement](/0KA7A4ENVJ/), the [Vandermonde determinant](/0P84B554AS/), the [Cauchy-Binet formula](/08WE2W7DYS/), the [Weinstein-Aronszajn identity](/0G24VQ1088/), the [matrix determinant lemma](/0BC3Q6K92H/), [Sylvester's identity](/7SSKBQYFW1/), [Dodgson condensation](/RQ44FKS5QM/) and [rank by minors](/HVHQ50TJB1/).
7. **Maps, volume and orientation.** The [determinant of a linear map](/0X0HQYSZ0K/), the [determinant of a family of vectors in a basis](/05CJSSXPR3/), [volume scaling](/RC5BTSG8T2/) and [orientation](/0QJJAQ6ZYZ/).
8. **Derivative and Pfaffian.** [Jacobi's formula](/357FEAZ0Q4/) for the derivative of a determinant, and the [Pfaffian](/NH5HWBPWS9/) of a skew-symmetric matrix.

## A first reading

Take these entries in order: [determinant of a 2 × 2 matrix](/0ZN2J42SK7/), [determinant](/00KDZRW4C0/), [Leibniz formula](/016PE4VZ8Q/), [effect of row operations](/09YB3WQG38/), [determinant of a triangular matrix](/0K1KKMFHYH/), [multiplicativity](/04CPJ6AF00/), [invertible iff the determinant is nonzero](/FBSAPTP1PR/), [Laplace expansion](/0C08BQ3M05/), [adjugate matrix](/07W9H8QF38/), [Cramer's rule](/0977KZ6PQB/) and [volume scaling](/RC5BTSG8T2/). With these you can compute any determinant of moderate size, test invertibility, and read the number geometrically.

The alternating maps of the second group can be read quickly at first; their role is to show that the determinant is well defined. Determinants over rings, most of the classical identities of the sixth group, Jacobi's formula and the Pfaffian can wait for a second pass. Of the sixth group, the [block triangular rule](/0J9TVTNB4K/) and the [Vandermonde determinant](/0P84B554AS/) are the ones used most often later.

## Before you start

You need matrices and their products from [matrices and the operations on them](/Y1ESNQ2V52/), and [invertible matrices](/P8J6QR66TJ/) with [Gaussian elimination](/0JVJ2WCXZH/). The Leibniz formula uses the [symmetric group](/0515A6D2Y1/) and the [sign of a permutation](/02DKV69ZH0/). The determinant of a map uses [matrices of linear maps and change of basis](/S6559D61BP/). For the sections over rings, the notion of a [commutative ring](/0310REJJY8/) and its units is enough.
