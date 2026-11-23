## What to remember

- **[Vector space](/000AYPA9AJ/):** a set $V$ with an addition and a multiplication by the scalars of a field $F$, satisfying eight axioms: addition is associative and commutative, there is a zero vector and each vector has a negative, $a(bv) = (ab)v$, $1v = v$, and both distributive laws hold. Examples: [$F^n$](/713F6AM1X1/), [$M_{m \times n}(F)$](/0RE6X3BGPN/), [$F[x]$ and $P_n$](/0JGZCDT5DN/), [$F^S$](/0GZB2SN0PH/).
- **[Subspaces](/00YC1D652K/):** a subset $U \subseteq V$ is a subspace exactly when $0 \in U$ and $U$ is closed under addition and under scalar multiplication. [Intersections](/0V33SPH7RR/) of subspaces are subspaces; $U \cup W$ is one only when $U \subseteq W$ or $W \subseteq U$. The [sum](/0JMTY8MF54/) $U + W = \set{u + w : u \in U, \ w \in W}$ is the smallest subspace containing $U$ and $W$.
- **[Span](/0DTY8B9HMS/) and [independence](/0CRMGPAH83/):** the span of $S$ is the set of all finite linear combinations of elements of $S$, the smallest subspace containing $S$. A family is independent when $a_1 v_1 + \cdots + a_k v_k = 0$ forces $a_1 = \cdots = a_k = 0$. Independence depends on the field: a family can be independent over $\R$ and dependent over $\F_2$.
- **[Basis](/0KCQ9Y3QKA/) and [coordinates](/04CYQHN6MC/):** a basis is an independent spanning family. With a basis $(b_1, \ldots, b_n)$ every $v \in V$ is $a_1 b_1 + \cdots + a_n b_n$ for exactly one $(a_1, \ldots, a_n) \in F^n$, and $v \mapsto (a_1, \ldots, a_n)$ is a bijection $V \to F^n$ that respects sums and scalar multiples.
- **[Dimension](/03GSZ8RTZJ/):** by the [Steinitz exchange lemma](/08ZDRN6H41/), if $V$ is spanned by $n$ vectors then every independent family in $V$ has at most $n$ vectors. Hence all bases of $V$ have the same size ([dimension theorem](/0WK0Y8RH1M/)), in infinite dimension as cardinals. $V$ is [finite-dimensional](/0ZHWKQMVX5/) when it has a finite spanning set. It depends on $F$: $\dim_\R \C^n = 2n$.
- **Building bases:** in a finite-dimensional space, every spanning set [contains a basis](/06MRNP4BNT/) and every independent set [extends to a basis](/0M4SXE5WW3/). With Zorn's lemma, [every vector space has a basis](/00MS9VMQ9Z/); over ZF this statement implies the axiom of choice. A [Hamel basis](/ZCBD0GRGVA/) of $\R$ over $\Q$ exists, and its existence rests on the axiom of choice.
- **Counting, for $\dim V = n$ finite:** a subspace $U$ has [$\dim U \le n$](/0QW084460E/), and $\dim U = n$ forces $U = V$. A family of exactly $n$ vectors is a basis as soon as it is independent, and as soon as it spans ([right-size criterion](/096V7H13H9/)). For finite-dimensional subspaces $U$, $W$: [$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$](/06HTJNCMPA/).
- **Other fields:** a space of dimension $n$ over [$\F_q$](/J9VE1X14PV/) has $q^n$ vectors and $(q^n - 1)(q^n - q) \cdots (q^n - q^{n-1})$ ordered bases. For a real space $V$ and a complex space $W$, [$\dim_\C V_\C = \dim_\R V$ and $\dim_\R W_\R = 2 \dim_\C W$](/CT2F31EDH8/).

## Three tests for columns

| Property of $v_1, \ldots, v_k \in F^m$ | Test on an echelon form of $A = (v_1 \cdots v_k)$ | Forces |
|---|---|---|
| [spanning $F^m$](/088RYKAWK9/) | a pivot in every row | $k \ge m$ |
| [independent](/76GG9B25A1/) | a pivot in every column | $k \le m$ |
| [basis of $F^m$](/0KCQ9Y3QKA/) | a pivot in every row and every column | $k = m$ |

: Spanning and independence are tested on different lines of the same echelon form. The inequalities are necessary only: $k = m$ vectors can fail both tests.

## Common errors

- **Forgetting the zero vector.** The plane $x + y + z = 1$ does not contain $0$, so it is not a subspace.
- **Union for sum.** The union of the two axes of $\R^2$ is not a subspace; their sum is $\R^2$.
- **Pairwise for global.** Three vectors that are pairwise independent can be dependent, as $(1, 0)$, $(0, 1)$, $(1, 1)$ are. Independence is a property of the whole family.
- **Dividing by a coefficient that may be zero.** From a dependence relation $a_1 v_1 + \cdots + a_k v_k = 0$ one can only solve for a $v_i$ with $a_i \ne 0$.
- **Reading the basis off the reduced matrix.** The pivot columns tell which of the original columns to keep; the columns of the echelon form usually do not lie in the column space.
- **Dropping finite dimension.** A subspace of the same dimension equals the whole space only in finite dimension: the polynomials with zero constant term form a proper subspace of $F[x]$ of the same, countable, dimension.
- **Forgetting the field.** $\C$ has dimension $1$ over $\C$ and $2$ over $\R$. State the field with every dimension.
- **Inclusion–exclusion for three subspaces.** Grassmann's formula is for two subspaces. For three lines through $0$ in $\R^2$ the three-term analogue fails.
