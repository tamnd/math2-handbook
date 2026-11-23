## What to remember

- [Pigeonhole](/0HGVCWQGY3/): if $N$ objects go into $k \ge 1$ boxes, some box holds at least $\ceil{N/k}$ objects ([generalized form](/0BY7GN3449/)), so at least two when $N > k$. If infinitely many objects go into finitely many boxes, some box holds infinitely many ([infinite form](/0FS3RHF6KE/)). It proves "two of these objects share a property"; the work is to choose boxes such that two objects in one box give what you want.
- [Double counting](/0F8YBHF2W3/): for finite sets $A, B$ and a relation $R \subseteq A \times B$, $\sum_{a \in A} \abs{\set{b : (a, b) \in R}} = \abs{R} = \sum_{b \in B} \abs{\set{a : (a, b) \in R}}$. Use it when one count is easy by rows and the other by columns. For infinite sums the two orders can differ.
- [Bijection principle](/0GV2573FP4/): finite sets $A$ and $B$ have $\abs{A} = \abs{B}$ if and only if there is a bijection $A \to B$. A [combinatorial proof](/SS07J9ZAQ7/) of $L = R$ names a set, shows that $L$ counts it one way and $R$ another way, or gives a bijection between a set of size $L$ and a set of size $R$. Check both injectivity and surjectivity.
- [Invariant](/8NQ190278Y/): a function $I$ of positions with $I(x) = I(y)$ whenever a move takes $x$ to $y$. If $I(\text{start}) \ne I(\text{target})$, the target is unreachable. Equal values prove nothing about reachability.
- [Monovariant](/TP3GC5J08D/): a function $M$ with $M(y) < M(x)$ for every move from $x$ to $y$, with values in $\N$ or in another well-ordered set. Then every run of the process stops, after at most $M(\text{start}) - \min M$ moves when $M$ drops by at least $1$ each time. A real-valued $M$ needs a fixed minimum drop and a lower bound.
- [Parity](/H9JT1XNDKQ/) and [colouring](/90Q4PK1CST/) are invariants modulo $2$ or modulo $k$. For a tiling: colour so that every tile covers a known number of cells of each colour, whatever its position, and compare with the region. A matching count does not prove that a tiling exists.
- [Extremal principle](/MD3MRG90W4/): take an object that is largest or smallest in some measure, and show it has the property, or that a failure gives a more extreme object. The extreme must exist: a finite nonempty set or a nonempty subset of $\N$ is safe, an infinite set of reals is not.
- [Averaging](/HXP9VMXV8S/): if $x_1, \ldots, x_n$ have mean $\mu$, then some $x_i \ge \mu$ and some $x_j \le \mu$. Choose it when a total is easy to compute; the probabilistic form says that a random variable takes a value at least its expectation with positive probability.
- Existence without an example: a [count](/1KVSS0KRZA/) with $\abs{B} < \abs{S}$ (or $B$ countable, $S$ uncountable) gives a good element of $S \setminus B$; a [probabilistic proof](/6YY8W7HG5M/) gives an object from positive probability; [diagonalization](/V2H30SA654/) builds $d$ with $d(x) \ne f_x(x)$ for every $x$, and the step that checks $d$ lies in the class must be done.

## Invariant, monovariant, extremal

| Method | What it proves | Key hypothesis | Typical slip |
|---|---|---|---|
| Invariant | a position cannot be reached | every move keeps $I$ fixed | taking equal values as proof that a position can be reached |
| Monovariant | every process stops | $M$ strictly decreases in a well-ordered set | a decreasing real quantity with no minimum drop |
| Extremal principle | a best object has the property | an extreme object exists | choosing a maximum in an infinite set |
| Averaging | some object is at least the mean | the total is known | claiming more than the mean, or that all are near it |

: Four methods that look alike and what each one needs

## Common errors

- **Too many boxes.** With $n$ objects and $n$ boxes, pigeonhole gives nothing.
- **A non-strict count.** $\abs{B} \le \abs{S}$ allows $B = S$; existence needs $\abs{B} < \abs{S}$.
- **Mixing up the directions.** An invariant proves impossibility; it never shows that a position is reachable.
- **Colour counts as proof of a tiling.** Equal counts of black and white cells are necessary, not sufficient.
- **A bijection that is only a map.** A combinatorial proof needs a two-sided inverse or both injectivity and surjectivity.
- **Diagonal objects outside the class.** The diagonal of a list of finitely supported sequences is not finitely supported, so it proves nothing.
