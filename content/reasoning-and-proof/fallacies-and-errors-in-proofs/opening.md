For a positive integer $x$, the square $x^2$ is the sum of $x$ copies of $x$:

$$x^2 = \underbrace{x + x + \dots + x}_{x \text{ terms}}.$$

Differentiate both sides with respect to $x$. The left side gives $2x$. Each term on the right gives $1$, and there are $x$ terms, so the right side gives $x$. Hence $2x = x$, and since $x$ is positive we may divide by it and get $2 = 1$.

Check the first line by hand at $x = 3$: $9 = 3 + 3 + 3$, and it is true. Each later step quotes a rule you know: the derivative of $x^2$, the derivative of a sum, the cancellation of a nonzero factor. The conclusion is false, so some rule was used where it does not hold. The derivative is defined for a function on an interval, and the identity holds only at the positive integers, where the right side is not a sum with a fixed number of terms: the number of terms is $x$ itself. The rule "the derivative of a sum is the sum of the derivatives" is a theorem about a fixed finite number of functions. Written correctly, the right side is the product $x \cdot x$, and the product rule gives $x + x = 2x$, as it should.

This is the pattern of the chapter. A [mathematical fallacy](/S2BW0FDHV8/) is an argument that looks valid and has an invalid step, and the step is found by testing each line against the exact statement of the rule it uses, hypotheses included. The errors fall into a few kinds: a true rule used outside its range, a fact read off a figure, and a broken logical form, such as reasoning from a converse or exchanging "for every" and "there is". They are worth study because the same errors occur in serious work. Lamé's 1847 proof of Fermat's Last Theorem assumed unique factorization in rings of cyclotomic integers, where it can fail, and Kempe's 1879 proof of the four colour theorem was accepted until Heawood found the gap in 1890.

## What the chapter covers

1. **What a fallacy is.** [Mathematical fallacies](/S2BW0FDHV8/) defines the term, separates a fallacy from a plain slip and from a true but surprising result such as $0.999\ldots = 1$, and names the wrong method with a right answer, the howler.
2. **Rules used outside their range.** [Division by zero](/V7601AG5G3/) hidden in a cancellation, [roots and powers](/75ZEQ21AG2/) taken where the rules for them fail, and [infinite series and integrals](/KDXKVT5K1E/) handled as if they were finite sums.
3. **Figures that mislead.** [Geometric fallacies](/5CJ4KD4D96/) read a point's position off a drawing or trust a cut-and-paste of areas.
4. **Errors of logic.** [Circular reasoning](/JPHE53PABT/), [affirming the consequent and denying the antecedent](/J7KFCFQRBT/), [proof by example](/ZX6ERT3SW7/), the [quantifier shift fallacy](/CRW82NARQV/) and [non-reversible steps](/641ZP4RA5S/) in solving equations.
5. **Errors in the practice of proof.** [Famous incorrect proofs](/1CV4HTA6C8/) by Kempe, Lamé, Legendre and others, and [proof by intimidation](/D8A1K052XV/), where "clearly" stands in for a step.

## A first reading

1. [Mathematical fallacies](/S2BW0FDHV8/)
2. [Division by zero fallacies](/V7601AG5G3/)
3. [Fallacies with roots and powers](/75ZEQ21AG2/)
4. [Affirming the consequent and denying the antecedent](/J7KFCFQRBT/)
5. [Proof by example](/ZX6ERT3SW7/)
6. [Quantifier shift fallacy](/CRW82NARQV/)
7. [Non-reversible steps in solving equations](/641ZP4RA5S/)
8. [Circular reasoning](/JPHE53PABT/)

The entry on series and integrals needs first-year calculus and can wait until you have met improper integrals and conditional convergence. The geometric fallacies and the famous incorrect proofs read well at any time; the second needs some algebra and graph theory for its details, but its lessons are plain.

## Before you start

The chapter assumes the proof methods of [basic proof methods](/958EF46EYJ/) and the logic of [the language of mathematical statements](/WMY13MXY3W/): the [conditional](/FA6YZGR2SS/), its [converse](/09A3N7ZN5G/), and the [order of quantifiers](/0FYQMKFE77/). Errors that are special to induction, such as the "proof" that [all horses are the same colour](/AJ2FDJJGTH/), are treated with [induction and well-ordering](/EEH2F76CYQ/). For the third entry you need [improper integrals](/05KQ3F99BQ/) and [conditional convergence](/02YRQXZDCS/); for the quantifier shift, the definition of [uniform continuity](/0M4JJT780X/) helps.
