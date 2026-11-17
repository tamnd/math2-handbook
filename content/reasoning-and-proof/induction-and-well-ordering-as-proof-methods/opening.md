Many statements in mathematics are about every natural number, or every finite graph, or every list. One finite argument cannot check infinitely many cases one at a time, but it can check that each case follows from earlier ones. That is induction. To prove $1 + 3 + \cdots + (2n - 1) = n^2$ for every $n \ge 1$, check $n = 1$, then show that adding $2n + 1$ to $n^2$ gives $(n + 1)^2$. To prove that every integer $n \ge 2$ is a product of primes, assume it for all smaller integers: if $n$ is not prime, then $n = ab$ with $a$ and $b$ smaller than $n$, and the products for $a$ and $b$ combine.

The same fact about the natural numbers appears in a second form. Every nonempty set of natural numbers has a least element, so if a statement had counterexamples, it would have a smallest one. Many proofs start there: take the smallest counterexample and find a smaller one, or take a solution of an equation and build a smaller solution. Fermat called the second form infinite descent and used it to prove that certain Diophantine equations have no solutions in positive integers.

Writing the base case and the step is routine. The difficulty is choosing what to induct on, what exactly to assume, and what to prove. The chapter collects the forms induction takes in practice and the errors that make a plausible induction prove a false statement.

## What the chapter covers

The chapter is in five groups.

1. **Induction and its equivalents.** [Mathematical induction](/0ASJVEFA9J/), [strong induction](/0KMVFSHFGZ/) and the [well-ordering principle](/01BX15HSRR/) are three forms of one fact, and [their equivalence](/J2P9FWBP3Q/) is proved over a stated base theory.
2. **Arguing from a least case.** The [minimal counterexample](/JGRCNPKNGG/) and [infinite descent](/0EFYCFHYFG/) use the well-ordering principle inside a proof by contradiction.
3. **Making the induction work.** [Strengthening the induction hypothesis](/F94KJC2RXP/) proves more to get a step that works. [Double induction](/AABX4YPKRR/) handles two variables, and [forward-backward induction](/QC9FKGZH1V/) proves the claim for powers of $2$ and then steps down.
4. **Induction beyond the natural numbers.** [Structural induction](/12MQ2NJ29A/) works over sets given by an [inductive definition](/AM4GQQMZ3C/), and [induction on size](/B2D8PTFNN1/) works over graphs, sets and polynomials.
5. **Worked cases, right and wrong.** The false proof that [all horses are the same colour](/AJ2FDJJGTH/), the [tiling of a deficient board by L-trominoes](/EXRJ0JF2Q3/), and a list of [errors in induction proofs](/V52HDTMPV5/).

## A first reading

Read these entries first, in order: [mathematical induction](/0ASJVEFA9J/), [strong induction](/0KMVFSHFGZ/), the [well-ordering principle](/01BX15HSRR/), [minimal counterexample](/JGRCNPKNGG/), [infinite descent](/0EFYCFHYFG/), [strengthening the induction hypothesis](/F94KJC2RXP/), [induction on size](/B2D8PTFNN1/), [all horses are the same colour](/AJ2FDJJGTH/) and [errors in induction proofs](/V52HDTMPV5/). Work through the attached examples of the first entry in full; they show the layout that every later proof follows.

On a first pass you can skip the [equivalence theorem](/J2P9FWBP3Q/), which matters mainly for the foundations, and [forward-backward induction](/QC9FKGZH1V/). Read [structural induction](/12MQ2NJ29A/) and [inductive definitions](/AM4GQQMZ3C/) before any work in logic or computer science, where formulas, terms and programs are defined in that way.

## Before you start

You should know the methods of the chapter on [basic proof methods](/958EF46EYJ/), in particular [proof by contradiction](/0J0XBKG64S/) and the [map of proof methods](/G9JFJGY4TQ/), and you should be able to read quantifiers and implications as in [the language of statements](/WMY13MXY3W/). You need the idea of a [mathematical proof](/0B94TKFQJX/) and the [natural numbers](/0MWKJ44V5A/) with their order; in this book they start at $0$. The [Peano axioms](/0QFT7Z76N5/) are needed only for the equivalence theorem. A few examples use graphs, binary trees and polynomials, and each one defines what it uses.
