A theorem has a logical form before it has a proof. "If $n^2$ is even, then $n$ is even" is an implication about every integer. "There is no largest prime" is the negation of an existence statement. "The equation $3x \equiv 1 \pmod 7$ has exactly one solution modulo $7$" is an existence claim and a uniqueness claim joined together. The form of the statement suggests the first line of its proof, and often the shape of the whole proof.

Take the first example. A direct attack assumes $n^2 = 2k$ and gets stuck, because there is no good way to get a formula for $n$ from a formula for $n^2$. The [contrapositive](/0BB5TPGQ1N/) turns the claim around: if $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd. The same algebra, started from the other end, is a two-line proof. Choosing the method is often most of the work, and this chapter is about how to choose.

The methods here are the ones every later chapter of the book uses without comment: direct proof, the arbitrary element, contrapositive, contradiction, cases, two directions of an equivalence, existence with or without a witness, uniqueness, counterexample, symmetry and impossibility. Each entry gives the method, the logic that makes it valid, worked examples, and a non-example where the method is misused.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The map and the direct method.** The [map of proof methods](/G9JFJGY4TQ/) sorts them by the form of the goal. A [direct proof](/0NTF6DMVAP/) assumes the hypothesis and reasons forward; [proving a universal statement](/CX38X989TB/) means arguing about an arbitrary element, never about a chosen one.
2. **Indirect proofs.** [Proof by contrapositive](/0BB5TPGQ1N/) proves "not $Q$ implies not $P$". [Proof by contradiction](/0J0XBKG64S/) assumes the negation and derives a contradiction. The first ends at a definite statement, not $P$; the second may end at any contradiction, which makes it more general and its errors harder to find.
3. **Splitting the goal.** A [proof by cases](/0WCP0PVET6/) needs cases that cover every possibility. A [biconditional](/TFQ1845T84/) needs two directions, and a list of equivalent statements needs a cycle of implications.
4. **Existence and uniqueness.** A [constructive proof](/01XM7JEKHY/) names a witness. A [non-constructive proof](/JZQVJ9XT63/) shows that one exists without naming it. A [proof of uniqueness](/GQHHNV79PA/) shows that two objects with the property are equal.
5. **Counterexamples, shortcuts and impossibility.** A [counterexample](/0ED72CTBNP/) refutes a universal claim. [Without loss of generality](/Y7NE0E6PCV/) reduces symmetric cases to one. The [forward-backward method](/V8ZB838JY5/) plans a proof from both ends. A [proof of impossibility](/6F55216R53/) shows that no object or method of a given kind exists.

## A first reading

For a first reading, take these ten entries in order: [proof methods](/G9JFJGY4TQ/), [direct proof](/0NTF6DMVAP/), [proving universal statements](/CX38X989TB/), [proof by contrapositive](/0BB5TPGQ1N/), [proof by contradiction](/0J0XBKG64S/), [proof by cases](/0WCP0PVET6/), [proving biconditionals](/TFQ1845T84/), [constructive proof](/01XM7JEKHY/), [counterexample](/0ED72CTBNP/) and the [forward-backward method](/V8ZB838JY5/). Read the worked examples printed with each one; the non-examples matter as much as the examples, since each shows a mistake that looks like a proof.

On a first pass you can skip the L3 explanations, which connect the methods to natural deduction and intuitionistic logic, and the entries on [non-constructive proof](/JZQVJ9XT63/), [without loss of generality](/Y7NE0E6PCV/) and [impossibility](/6F55216R53/). Come back to them before Chapter 1.7, where impossibility proofs by invariants and colourings are the main subject.

## Before you start

You need the language of statements from [the language of mathematical statements](/WMY13MXY3W/): conditionals, quantifiers, the rules for [negating a statement](/K930V33BSC/), and "exactly one". You need the idea of a [mathematical proof](/0B94TKFQJX/), which the chapter on [proof, theorems and mathematical method](/N4P3E53HM0/) explains. From school you need algebra with inequalities and the integers with even and odd numbers and divisibility. A few examples use sets, functions, limits or groups, and they say so at the start. The formal rules of inference behind the methods are in [propositions, connectives and quantifiers](/PM1AYWABA7/), but you do not need them to read this chapter.
