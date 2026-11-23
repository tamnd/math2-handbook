Draw $n$ straight lines in the plane so that no two are parallel and no three pass through one point, and count the regions they cut the plane into. By hand you find $2$ regions for one line, $4$ for two, $7$ for three and $11$ for four. The differences are $2, 3, 4$, which suggests the formula
$$R(n) = 1 + \frac{n(n + 1)}{2}.$$
A pattern in four cases is not a proof. Put $n$ points on a circle in general position and join every pair by a chord: the numbers of regions inside the circle are $1, 2, 4, 8, 16$ for $n = 1, \dots, 5$, and then $31$, not $32$, for $n = 6$.

What settles the question for the lines is an argument that links each case to the one before. Add the $(n + 1)$st line to a picture with $n$ lines. It crosses each of the $n$ old lines exactly once, at $n$ different points, so it is cut into $n + 1$ pieces, and each piece splits one old region in two. So $R(n + 1) = R(n) + n + 1$, and with $R(0) = 1$ this gives the formula for every $n$. That is a proof by [mathematical induction](/0ASJVEFA9J/): a base case and a step that carries the truth from each case to the next.

The same proof can be read backwards. If the formula failed for some $n$, there would be a least such $n$, and it cannot be $0$, so the formula holds for $n - 1$ and the step gives it for $n$. This is the [well-ordering principle](/01BX15HSRR/) at work. The chapter shows that these two views are one fact about the natural numbers, and it builds a set of tools on that fact: a smallest failure, a statement made stronger so that the step goes through, an induction in two variables or along a structure, and an honest list of the ways an induction proof goes wrong.

## What the chapter covers

1. **Induction and strong induction.** [Mathematical induction](/0ASJVEFA9J/) proves $P(n)$ for all $n \ge n_0$ from a base case and a step from $n$ to $n + 1$. [Strong induction](/0KMVFSHFGZ/) lets the step use every earlier case, which is what a proof about prime factors needs.
2. **Least elements and the equivalence of the principles.** The [well-ordering principle](/01BX15HSRR/) gives a least element of every nonempty set of natural numbers. The [equivalence of induction and well-ordering](/J2P9FWBP3Q/) states exactly which properties of $\N$ make the three principles interchangeable.
3. **Arguing from a smallest case.** A [minimal counterexample](/JGRCNPKNGG/) is refuted by a smaller one. [Infinite descent](/0EFYCFHYFG/) shows that a Diophantine equation has no solution because each solution would give a smaller one.
4. **Choosing what to prove and in what order.** [Strengthening the induction hypothesis](/F94KJC2RXP/) rescues a stuck step. [Double induction](/AABX4YPKRR/) handles two variables, and [forward-backward induction](/QC9FKGZH1V/) climbs through the powers of $2$ and comes back down.
5. **Induction on structures and on size.** [Structural induction](/12MQ2NJ29A/) follows the rules that build lists, trees and formulas, and [inductive and recursive definitions](/AM4GQQMZ3C/) explain why such rules define anything. [Induction on size](/B2D8PTFNN1/) chooses the number to induct on for graphs, sets and polynomials.
6. **A false proof, a true one, and the errors.** The proof that [all horses are the same color](/AJ2FDJJGTH/) fails at one step. [Tiling a $2^n \times 2^n$ board with one square removed](/EXRJ0JF2Q3/) is a correct induction with a picture. [Errors in induction proofs](/V52HDTMPV5/) collects the common mistakes.

## A first reading

1. [Mathematical induction](/0ASJVEFA9J/), with the examples on the sum of odd numbers and on $2^n > n^2$.
2. [Strong induction](/0KMVFSHFGZ/), with the postage example.
3. [Well-ordering principle](/01BX15HSRR/).
4. [Minimal counterexample](/JGRCNPKNGG/).
5. [Strengthening the induction hypothesis](/F94KJC2RXP/).
6. [Structural induction](/12MQ2NJ29A/).
7. [Induction on size](/B2D8PTFNN1/).
8. [All horses are the same color](/AJ2FDJJGTH/) and [errors in induction proofs](/V52HDTMPV5/).

On a first pass you can skip the [equivalence theorem](/J2P9FWBP3Q/), which matters for the foundations of arithmetic, and [forward-backward induction](/QC9FKGZH1V/), which is a special tool. [Infinite descent](/0EFYCFHYFG/) and [double induction](/AABX4YPKRR/) can wait until a problem needs them.

## Before you start

You need [basic proof methods](/958EF46EYJ/), in particular proof by contradiction, and the wider survey of [proof methods](/G9JFJGY4TQ/). You should be able to read quantifiers and implications, as in the [language of statements](/WMY13MXY3W/), and know what counts as a [mathematical proof](/0B94TKFQJX/). The [natural numbers](/0MWKJ44V5A/) with their order are the setting throughout. The [Peano axioms](/0QFT7Z76N5/) are needed only for the equivalence theorem.
