## What to remember

- A **definition** has a definiendum, the new term, and a definiens, a condition in known terms. It is a stipulation, so it is neither true nor false. In a definition, "if" means "if and only if": "$n$ is even if $n = 2k$ for some integer $k$" also says that every even $n$ has this form.
- A definition can **hide claims**: that the object it names exists, that it is unique, or that it does not depend on a choice. Each hidden claim needs a proof before the term is used.
- A rule $f([x]) := g(x)$ on a quotient set $X/{\sim}$ is **well defined** exactly when $x \sim x'$ implies $g(x) = g(x')$. The mediant $\frac{a}{b} \oplus \frac{c}{d} = \frac{a + c}{b + d}$ fails this test; the map $\Z/6 \to \Z/3$, $[a]_6 \mapsto [a]_3$, passes it, and $[a]_3 \mapsto [a]_6$ fails it.
- Two definitions are **equivalent** when they single out the same objects, and this is a theorem with two directions. To show that $n$ conditions are equivalent, a cycle of $n$ implications $C_1 \Rightarrow C_2 \Rightarrow \cdots \Rightarrow C_n \Rightarrow C_1$ is enough.
- A **definite description** "the $x$ such that $P(x)$" names an object only when exactly one $x$ satisfies $P$. "The square root of $-1$" in $\C$ fails uniqueness, since $i$ and $-i$ both qualify.
- "$x$ is **unique up to** $\sim$" means that some $x$ has the property and any two such objects are related by $\sim$; the property picks out one equivalence class. Prime factorization in $\Z$ is unique up to order and sign; an antiderivative is unique up to an additive constant on an interval.
- A **primitive notion**, such as point or line in [Hilbert's axioms](/KM1FB8XZ2R/), is not defined. The axioms fix how it may be used, and any objects that satisfy the axioms will do.
- Definitions are **chosen** for the theorems they make true. Excluding $1$ from the [primes](/01826KMG2H/) keeps the factorization in the [fundamental theorem of arithmetic](/084HH1NDCB/) unique, and a field requires $0 \neq 1$ to exclude the one-element ring.

## Kinds of definitions

| Kind | Example | What must be proved |
|---|---|---|
| Explicit | $n$ is even if $n = 2k$ for some integer $k$ | nothing, if the definiens uses only known terms |
| Recursive | $0! = 1$, $(n + 1)! = (n + 1) \cdot n!$ | exactly one function satisfies the recursion ([recursion theorem](/BQ1D7T0EGD/)) |
| Inductive | the even natural numbers: $0$, and $n + 2$ for each member $n$ | a smallest closed set exists |
| By abstraction | $\Q$ as classes of pairs $(a, b)$ with $b \neq 0$ | the relation is an equivalence relation, and each operation is well defined |
| Axiomatic | group, vector space, metric space | nothing for the definition; examples show that the axioms are not empty |
| [Implicit](/20CV0X83V2/) | $\sqrt 2$ is the positive real $x$ with $x^2 = 2$ | a solution exists and it is unique |
| [Universal property](/EN4DD2FAJH/) | product, quotient, free group | an object with the property exists; uniqueness up to unique isomorphism follows |
| By construction | real numbers as [Dedekind cuts](/0G3RRM41X9/) | the constructed object has the expected properties |

: The kinds of definition and their proof obligations, as in the entry on kinds of definitions. The smallest closed set of an inductive definition exists as the intersection of all closed sets.

## Common errors

- **Using a rule on classes before checking it.** Test every operation on residues, cosets or fractions with two representatives of one class before you call it a function.
- **Reading "if" in a definition as one-way.** A definition can be used in both directions; a theorem stated with "if" cannot.
- **Writing "the" too early.** Before you write "the identity" or "the limit", prove uniqueness, or say "an" until you have.
- **Dropping "up to".** "The factorization of $12$ is unique" is false as stated, since $2 \cdot 2 \cdot 3 = 3 \cdot 2 \cdot 2$; "unique up to order" is the theorem.
- **Proving one direction of an equivalence.** Two definitions agree only when each implies the other, or when the implications close a cycle.
- **Defining upwards.** A rule such as $f(n) = f(n + 1) + 1$ computes each value from a later one. No function from $\N$ to $\N$ satisfies it, and infinitely many functions from $\N$ to $\Z$ do, so it defines nothing; a legal recursion moves from earlier values to later ones.
