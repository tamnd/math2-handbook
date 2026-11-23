Solve the system $4x + 3y = 10$, $2x + 5y = 12$ by elimination. Multiply the first equation by $5$ and the second by $3$ and subtract: $(4 \cdot 5 - 3 \cdot 2) x = 10 \cdot 5 - 3 \cdot 12$, that is $14 x = 14$, so $x = 1$. In the same way $14 y = 4 \cdot 12 - 2 \cdot 10 = 28$, so $y = 2$. The number $14 = 4 \cdot 5 - 3 \cdot 2$ appeared twice, and it does not depend on the right-hand side. If it had been $0$, elimination would have produced $0 = $ something, and the system would have had no solution or infinitely many. The same number has a picture: the vectors $(4, 2)$ and $(3, 5)$ span a parallelogram of area $14$, and the area is $0$ exactly when the two vectors lie on one line.

For three equations in three unknowns, elimination gives the same kind of number, now a sum of six products of three entries with signs. For four unknowns there are $24$ products, and for $n$ unknowns there are $n!$. Writing them out stops being useful long before $n = 10$. What is needed is a definition that explains the signs, rules that compute the number quickly, and theorems that say what it measures. That is the content of this chapter. The [determinant](/00KDZRW4C0/) of a square matrix is defined by three properties: it is linear in each column, it vanishes when two columns are equal, and it is $1$ at the identity. From these follow the formula with $n!$ terms, a computation by row reduction in about $n^3$ steps, the product rule $\det(AB) = \det A \det B$, and the test for invertibility.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Small determinants.** The [$2 \times 2$ formula](/0ZN2J42SK7/) and the [rule of Sarrus](/7H2P40X0MV/) for $3 \times 3$ matrices.
2. **The definition.** [Alternating multilinear maps](/0K6CH0MT0F/), the [determinant](/00KDZRW4C0/) as the unique one that is $1$ at the identity, and the [Leibniz formula](/016PE4VZ8Q/).
3. **Rules for computing.** [Multilinearity in rows](/0PPG793642/), [equal or zero rows](/0K4VQB7HWR/), the [effect of row operations](/09YB3WQG38/), [triangular matrices](/0K1KKMFHYH/) and the [transpose](/0ZZQ2E1MTE/).
4. **Products and invertibility.** The [product rule](/04CPJ6AF00/), the [determinant of the inverse](/0783S9D0ZH/), the [invertibility test over a field](/FBSAPTP1PR/) and its form [over a commutative ring](/03Q7RE2HXR/).
5. **Minors, cofactors and the adjugate.** [Minors](/0BT9BYWVRY/), [cofactors](/0XPKR18APA/), the [Laplace expansion](/0C08BQ3M05/), the [adjugate](/07W9H8QF38/) and the identity [$A \operatorname{adj} A = \det A \cdot I$](/0528HKWZ1Z/), with its two uses: the [inverse via the adjugate](/0ENVM493VK/) and [Cramer's rule](/0977KZ6PQB/).
6. **Block matrices and classical identities.** [Block triangular matrices](/0J9TVTNB4K/), the [Schur complement](/0KA7A4ENVJ/), the [Vandermonde determinant](/0P84B554AS/), the [Cauchy–Binet formula](/08WE2W7DYS/), the [Weinstein–Aronszajn identity](/0G24VQ1088/), the [matrix determinant lemma](/0BC3Q6K92H/), [Sylvester's identity](/7SSKBQYFW1/), [Dodgson condensation](/RQ44FKS5QM/) and [rank by minors](/HVHQ50TJB1/).
7. **Linear maps, volume and orientation.** The [determinant of a linear map](/0X0HQYSZ0K/), the [determinant of a family of vectors](/05CJSSXPR3/) in a basis, the determinant as a [volume scaling factor](/RC5BTSG8T2/), and the [orientation](/0QJJAQ6ZYZ/) of a real vector space.
8. **The derivative and the Pfaffian.** [Jacobi's formula](/357FEAZ0Q4/) for the derivative of $\det A(t)$, and the [Pfaffian](/NH5HWBPWS9/) of a skew-symmetric matrix.

## A first reading

A first course needs these entries, in this order.

- The [$2 \times 2$ formula](/0ZN2J42SK7/) and the [rule of Sarrus](/7H2P40X0MV/).
- The [determinant](/00KDZRW4C0/) and the [Leibniz formula](/016PE4VZ8Q/).
- The [effect of row operations](/09YB3WQG38/) and [triangular matrices](/0K1KKMFHYH/), which together give the fast method.
- The [determinant of the transpose](/0ZZQ2E1MTE/).
- The [product rule](/04CPJ6AF00/) and the [invertibility test](/FBSAPTP1PR/).
- The [Laplace expansion](/0C08BQ3M05/) and the [inverse via the adjugate](/0ENVM493VK/).
- [Cramer's rule](/0977KZ6PQB/).
- The [determinant of a linear map](/0X0HQYSZ0K/) and the [volume scaling factor](/RC5BTSG8T2/).

[Alternating multilinear maps](/0K6CH0MT0F/) can be read quickly at first, with the field $\R$ in mind; the point about characteristic $2$ matters later. The ring version of the invertibility test is needed for matrices over $\Z$ and for the characteristic polynomial in the next chapter. Most of the sixth group can wait: the [block triangular rule](/0J9TVTNB4K/) and the [Vandermonde determinant](/0P84B554AS/) are used often, while Sylvester's identity, Dodgson condensation and the Pfaffian are needed only for special purposes.

## Before you start

The chapter uses the following.

- [Sign of a permutation](/02DKV69ZH0/): the Leibniz formula is a sum over the symmetric group, and every sign in it is the sign of a permutation.
- [Invertible matrices and matrix factorizations](/P8J6QR66TJ/), with [Gaussian elimination](/0JVJ2WCXZH/) and elementary matrices.
- [Matrices of linear maps, rank and change of basis](/S6559D61BP/), for the determinant of a linear map and for rank by minors.
- A [commutative ring](/0310REJJY8/), for the parts that work over $\Z$ or over a ring of polynomials.
