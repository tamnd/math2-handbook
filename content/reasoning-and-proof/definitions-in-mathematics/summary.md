## What to remember

- A [definition](/8ZCZ3HW91Z/) stipulates that a new term means exactly a condition in older terms. It is a biconditional even when written with "if": "$n$ is even if $n = 2k$ for some $k \in \Z$" also says that an integer of no such form is not even.
- The [principle of recursive definition](/BQ1D7T0EGD/): a value $f(0)$ and a rule giving $f(n+1)$ from $f(0), \dots, f(n)$ determine exactly one function on $\N$. A rule that refers to larger arguments, or one with no base case, is not covered.
- A function on classes is [well defined](/HNGZEBKVY2/) by a rule $f([x]) := g(x)$ exactly when $x \sim x'$ implies $g(x) = g(x')$ for all $x, x'$. The condition runs from "same class" to "same value", the reverse of injectivity.
- Two definitions $C_1$, $C_2$ of a notion of kind $K$ are [equivalent](/NZ42PS2P1A/) when $C_1(x) \iff C_2(x)$ for every $x$ of kind $K$. This is a theorem with two directions, and it can fail outside $K$: in $\Z[\sqrt{-5}]$ the element $2$ is irreducible but not prime.
- "The $x$ such that $P(x)$" is legal only after a proof of $\exists! x\, P(x)$, which means existence, $\exists x\, P(x)$, together with uniqueness, $\forall x\, \forall y\, (P(x) \land P(y) \Rightarrow x = y)$ ([definite descriptions](/5P955TVSS2/)).
- "Unique [up to](/CBC72TX3NQ/) $\sim$" means that some $x$ has $P(x)$ and any two such are related by $\sim$; equivalently, $\{x : P(x)\}$ is nonempty and lies in one class of $\sim$. Only properties preserved by $\sim$ can be stated about "the" object up to $\sim$.
- A [primitive notion](/QMQEJKFEYZ/) is used without definition, and the axioms are all that proofs may assume about it. A statement true in one model of the axioms and false in another is not provable from them.
- [Good definitions](/S1R1VD31BS/) are chosen so that the main theorems hold without exceptions: $1$ is not prime so that factorization into primes is unique, and $0! = 1$ so that $n! = n \cdot (n-1)!$ holds for every $n \ge 1$.

## Kinds of definition and what they require

| Kind | Example | What must be proved before use |
|---|---|---|
| Explicit | $n$ even iff $n = 2k$ for some $k \in \Z$ | Nothing |
| Recursive | $0! = 1$, $(n+1)! = (n+1)\, n!$ | Covered by the recursion principle when each value uses only earlier ones |
| Inductive | smallest $E \subseteq \N$ with $0 \in E$ and $n \in E \Rightarrow n+2 \in E$ | Nothing beyond the intersection argument |
| By abstraction | $\Q$ as classes of pairs $(a, b)$, $b \neq 0$ | $\sim$ is an equivalence relation; every operation is well defined |
| Axiomatic | group, vector space, metric space | Nothing, but examples show that the axioms have models |
| Implicit | $\sqrt 2$ as the real $x > 0$ with $x^2 = 2$ | Existence and uniqueness |
| Universal property | product of sets with two projections | Existence; uniqueness holds up to a unique isomorphism |
| By construction | reals as Dedekind cuts | The expected properties of the result |

: Kinds of definition and the obligation each one carries

## Common errors

- **Reading "if" as one-way.** Concluding that $-4$ is not a square uses the "only if" half, which every definition has.
- **Checking a rule on one pair of representatives.** Take arbitrary $x \sim x'$ and show $g(x) = g(x')$; for a binary operation, change both arguments.
- **Proving the wrong direction.** Showing that equal outputs come from equal classes proves injectivity, not that the rule is well defined.
- **Writing "the" too early.** "Let $c$ be the point given by the mean value theorem" is wrong when several points work. Say "a point" or prove uniqueness first.
- **Dropping the relation in "up to".** "The solution is unique" for $x^2 = 4$ is false; "unique up to sign" is true. Name the relation, and do not use a property of one representative that the relation does not preserve.
- **Proving half an equivalence.** Two definitions are equivalent only after both implications are proved, and a characterization proved in $\Z$ may fail in another ring.
- **Recursing upwards or without a base.** $f(n) = f(n+1) + 1$ has no solution $\N \to \N$, and $(n+1)! = (n+1)\, n!$ alone allows $c \cdot n!$ for every $c$.
- **Using a picture of a primitive notion.** From the incidence axioms you may not conclude that every line has three points, however obvious it looks; the three-point model shows that it does not follow.
