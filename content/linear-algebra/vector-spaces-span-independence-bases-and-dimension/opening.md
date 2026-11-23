Solve the homogeneous system
$$
\begin{aligned}
x + 2y - z + w &= 0, \\
y + z - w &= 0
\end{aligned}
$$
in $\R^4$. If you take $z$ and $w$ as the free variables, the second equation gives $y = w - z$ and the first then gives $x = 3z - 3w$, so every solution is
$$
z \, (3, -1, 1, 0) + w \, (-3, 1, 0, 1).
$$
A classmate takes $y$ and $w$ as free variables and writes every solution as $y \, (-3, 1, -1, 0) + w \, (0, 0, 1, 1)$. Both answers are right. The second pair is made of solutions, and $(0, 0, 1, 1)$ is the sum of the first two vectors while $(-3, 1, -1, 0)$ is the negative of the first, so each pair is built from the other. Row reduction alone leaves three things open: whether some other description uses a single vector, or three vectors none of which is redundant; whether the number $2$ belongs to the solution set or only to the way it was computed; and what the same question means for the solutions of $f'' + f = 0$, which are functions and not lists of numbers.

This chapter settles these points once and for all. The solution set is a [subspace](/00YC1D652K/) of $\R^4$: it contains $0$ and is closed under sums and scalar multiples. Each pair above [spans](/0DTY8B9HMS/) it and is [linearly independent](/0CRMGPAH83/), so each pair is a [basis](/0KCQ9Y3QKA/). The [Steinitz exchange lemma](/08ZDRN6H41/) shows that an independent list is never longer than a spanning list, and from this all bases of a space have the same size, its [dimension](/03GSZ8RTZJ/). So the solution set has dimension $2$, and no correct description uses one vector or three independent ones. To cover functions, sequences, polynomials and matrices as well as lists, the chapter starts from the [axioms of a vector space](/000AYPA9AJ/) over an arbitrary field, so that one proof serves all of them at once, including spaces over finite fields.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Vector spaces and their examples.** The [eight axioms](/000AYPA9AJ/), and the spaces [$F^n$](/713F6AM1X1/), [matrices](/0RE6X3BGPN/), [polynomials](/0JGZCDT5DN/) and [functions and sequences](/0GZB2SN0PH/).
2. **Subspaces and sums.** The [subspace test](/00YC1D652K/), [intersections and unions](/0V33SPH7RR/) of subspaces, and the [sum](/0JMTY8MF54/) $U + W$.
3. **Span and linear independence.** [Linear combinations](/0V8F3E48E6/), [span](/0DTY8B9HMS/), [spanning sets](/088RYKAWK9/), [independence](/0CRMGPAH83/), and the [column test](/76GG9B25A1/) by row reduction.
4. **Bases and coordinates.** [Bases](/0KCQ9Y3QKA/), the [standard bases](/C5QA672NPH/), and [coordinate vectors](/04CYQHN6MC/), which turn a space with a basis of $n$ vectors into $F^n$.
5. **Dimension.** The [exchange lemma](/08ZDRN6H41/), the [dimension theorem](/0WK0Y8RH1M/), [dimension](/03GSZ8RTZJ/) and [finite-dimensional spaces](/0ZHWKQMVX5/).
6. **Building bases.** [Thinning a spanning set](/06MRNP4BNT/), [extending an independent set](/0M4SXE5WW3/), the [existence of bases](/00MS9VMQ9Z/) by Zorn's lemma, and a [Hamel basis](/ZCBD0GRGVA/) of $\R$ over $\Q$.
7. **Counting with dimension.** The [dimension of a subspace](/0QW084460E/), the [right-size criterion](/096V7H13H9/) for a basis, and [Grassmann's formula](/06HTJNCMPA/) for $\dim(U + W)$.
8. **Changing the field.** [Spaces over finite fields](/J9VE1X14PV/), and [complexification and realification](/CT2F31EDH8/) between $\R$ and $\C$.

## A first reading

A first pass through the chapter can take these entries in order.

- [Vector space](/000AYPA9AJ/), for the axioms and the first examples.
- [Linear subspace](/00YC1D652K/), for the three-condition test.
- [Linear span](/0DTY8B9HMS/).
- [Linear independence](/0CRMGPAH83/), with the dependence lemma.
- [Linear dependence of the columns of a matrix](/76GG9B25A1/), the test used in every computation.
- [Basis](/0KCQ9Y3QKA/) and [coordinate vector](/04CYQHN6MC/).
- [Steinitz exchange lemma](/08ZDRN6H41/) and the [dimension theorem](/0WK0Y8RH1M/).
- [Every spanning set contains a basis](/06MRNP4BNT/) and [extension of an independent set to a basis](/0M4SXE5WW3/).
- [Right-size criterion for a basis](/096V7H13H9/) and the [dimension formula for sums](/06HTJNCMPA/).

The entries on [bases in general](/00MS9VMQ9Z/) and the [Hamel basis](/ZCBD0GRGVA/) use Zorn's lemma and can wait. [Complexification](/CT2F31EDH8/) returns later, with real matrices that have complex eigenvalues.

## Before you start

The chapter assumes the following.

- [Fields](/04C5ZBG1WT/): the scalars, among them $\Q$, $\R$, $\C$ and the finite fields $\F_q$.
- [Vectors in the plane and in space](/VKVAJ94SKZ/), the picture behind the axioms.
- [Systems of linear equations](/DXSXFVDMXQ/): row reduction, echelon form and pivots, which the column tests use.
- For the results in infinite dimension only: [cardinal numbers](/0EBACQFAZW/) and [Zorn's lemma](/04RXTQA5ZA/).
