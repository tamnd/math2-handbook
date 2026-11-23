Write down any five integers. Can you always choose three of them whose sum is divisible by $3$? Try a few lists and the answer seems to be yes, but a proof cannot check every list. What works is to sort the integers by their remainder on division by $3$, so that there are three boxes, for the remainders $0$, $1$ and $2$. If every box is occupied, take one integer from each box: the remainders add up to $0 + 1 + 2 = 3$, so the sum is divisible by $3$. If some box is empty, the five integers lie in at most two boxes, so one box holds at least $\ceil{5/2} = 3$ of them, and three integers with the same remainder $r$ have a sum with remainder $3r$, again divisible by $3$. Four integers are not enough: $0, 0, 1, 1$ has no such triple.

The proof computes nothing hard. It chooses the right boxes, counts, and splits into two cases. Most of the arguments in this chapter are like that. They prove that something exists, or cannot exist, or must happen, by looking at the problem from one well-chosen angle: a count made in two ways, a quantity that no move can change, the largest object in sight, or the average of many numbers. The same few ideas settle puzzles about chessboards and sliding tiles, and they also prove that transcendental numbers exist and that no set can be mapped onto its power set.

## What the chapter covers

1. **The pigeonhole principle.** The [pigeonhole principle](/0HGVCWQGY3/) forces a box with two objects, the [generalized form](/0BY7GN3449/) gives the sharp count $\ceil{N/k}$, and the [infinite form](/0FS3RHF6KE/) gives a box with infinitely many. The [applications](/5EAFG80VX6/) show how to choose the boxes, from rational approximation to monotone subsequences.
2. **Counting one set in two ways.** [Double counting](/0F8YBHF2W3/) sums a table by rows and by columns, the [bijection principle](/0GV2573FP4/) compares two sets by matching them, and [combinatorial and bijective proof](/SS07J9ZAQ7/) proves identities by naming the set that both sides count.
3. **Quantities that do not change or move one way.** An [invariant](/8NQ190278Y/) shows that a position cannot be reached, as in the 15 puzzle, and a [monovariant](/TP3GC5J08D/) shows that a process stops.
4. **Parity and colouring.** [Parity arguments](/H9JT1XNDKQ/) rule out configurations by counting modulo $2$, and [coloring proofs](/90Q4PK1CST/) rule out tilings by comparing colour counts.
5. **Looking at the extreme and at the average.** The [extremal principle](/MD3MRG90W4/) studies a best object, and the [averaging argument](/HXP9VMXV8S/) uses that some value is at least the mean.
6. **Existence without construction.** [Counting arguments for existence](/1KVSS0KRZA/) show that the bad objects are too few, [probabilistic proofs](/6YY8W7HG5M/) bring in a random object to prove a theorem with no chance in it, and [diagonalization](/V2H30SA654/) builds an object that is missing from any given list.

## A first reading

1. [Pigeonhole principle](/0HGVCWQGY3/) and the [generalized pigeonhole principle](/0BY7GN3449/).
2. [Applications of the pigeonhole principle](/5EAFG80VX6/).
3. [Double counting](/0F8YBHF2W3/).
4. [Combinatorial and bijective proof](/SS07J9ZAQ7/).
5. [Invariants](/8NQ190278Y/) and [monovariants](/TP3GC5J08D/).
6. [Coloring proofs](/90Q4PK1CST/).
7. [Extremal principle](/MD3MRG90W4/).
8. [Averaging argument](/HXP9VMXV8S/).

On a first pass you can skip the [infinite pigeonhole principle](/0FS3RHF6KE/), which matters for analysis and Ramsey theory, and the [bijection principle](/0GV2573FP4/), whose content most readers already use. [Probabilistic proofs](/6YY8W7HG5M/) need some probability and analysis, and [diagonalization](/V2H30SA654/) is most useful just before a course on set theory or computability.

## Before you start

The chapter relies on [basic proof methods](/958EF46EYJ/), above all proof by contradiction, and on [induction and the well-ordering principle](/EEH2F76CYQ/), which justify monovariants and the extremal principle. Double counting and the counting arguments use the rule of sum, the rule of product and binomial coefficients from [counting principles](/SQX86RBN8M/). Some examples use vertices, edges and degrees from [graph theory](/BCQTYD70W4/), but each entry defines what it uses. For the last entry, [Cantor's diagonal argument](/0XCH8QVDCQ/) is the model case.
