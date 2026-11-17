## What to remember

- **Pigeonhole.** If $m$ objects are placed in $n$ boxes and $m > n$, some box contains at least two objects; in general some box contains at least $\ceil{m/n}$ of them. If infinitely many objects are placed in finitely many boxes, some box contains infinitely many.
- **Double counting.** If $R \subseteq A \times B$ is finite, then $\sum_{a \in A} \abs{\set{b : (a, b) \in R}} = \abs{R} = \sum_{b \in B} \abs{\set{a : (a, b) \in R}}$. The handshaking lemma $\sum_v \deg v = 2\abs{E}$ is the case of vertex-edge incidences.
- **Bijections.** Two finite sets have the same number of elements exactly when there is a bijection between them. A combinatorial proof shows that two expressions count the same set, or two sets related by a bijection.
- **Invariants.** If a quantity $I$ is unchanged by every move and $I(s) \ne I(t)$, then the state $t$ cannot be reached from $s$. Parities and colourings give invariants for tilings, walks and puzzles.
- **Monovariants.** If every move strictly decreases a quantity with values in $\N$, or in any well-ordered set, then every sequence of moves is finite. A strictly decreasing real quantity is not enough.
- **Extremal principle.** In a finite nonempty set, or in a set of natural numbers, a largest or smallest element exists; take it and show that a failure of the claim gives a larger or smaller one. Without such existence the argument is invalid, as Perron's paradox shows.
- **Averaging and counting.** Among finitely many real numbers, some number is at least the mean and some is at most the mean. If fewer than all objects are bad, a good object exists; for infinite sets, a countable set of bad objects inside an uncountable set leaves good ones.
- **Diagonalization.** For any list $s_1, s_2, \ldots$ of binary sequences, the sequence with $n$-th term $1 - s_n(n)$ is not in the list. So the binary sequences are uncountable, and no map from a set onto its power set exists.

| Method | It proves | Key step | Typical use |
|---|---|---|---|
| Pigeonhole | two objects share a box | choose the boxes | approximation, monotone subsequences |
| Double counting | an equation between two counts | count one set of pairs by rows and by columns | handshaking lemma, identities |
| Bijective proof | two sets have the same size | build a map and its inverse | partition identities, Cayley's formula |
| Invariant | a state cannot be reached | find a quantity that no move changes | puzzles, tilings |
| Monovariant | a process stops | find a quantity that moves one way in a well-ordered set | algorithms, chip-firing |
| Extremal principle | a structure exists or a claim holds | take a largest or smallest object | paths and cycles in graphs, geometry |
| Averaging | an element at least the mean exists | compute the mean | large bipartite subgraphs, sum-free sets |
| Counting and probability | a good object exists | show the bad objects are fewer | Ramsey lower bounds, circuit lower bounds |
| Diagonalization | an object is missing from every list | change the $n$-th object at place $n$ | uncountability, undecidability |

: The methods of the chapter, what each one proves and where it is used.

## Choosing a method

Read the form of the claim first. "Some two of these must agree" suggests the pigeonhole principle, and the work is in choosing the boxes: the number of boxes must be less than the number of objects, and sharing a box must give what the claim asks. "This configuration cannot be reached" or "this region cannot be tiled" suggests an invariant: compute a few candidate quantities, such as a sum, a parity or a count of colours, on the start and the target, and keep the one that differs and that each move keeps. "This process always stops" suggests a monovariant with values in $\N$.

"Some object has this property" has several routes. If the objects can be ordered by size, take the largest or smallest and show that it works. If there is a natural average, show that the average is large enough. If you can count, show that the bad objects are fewer than all objects. Each route proves existence without naming the object.

Check the non-examples of the entries before you trust an argument. A quantity can be invariant and still fail to separate the start from the target, as the total number of chameleons does. A count can be true and decide nothing, and a largest element may not exist.
