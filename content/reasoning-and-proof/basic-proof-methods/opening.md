Here is a claim and an attempted proof of it.

*Claim.* For every integer $n$, if $3 \mid n^2$, then $3 \mid n$.

*Attempt.* Let $n = 3k$. Then $n^2 = 9k^2 = 3 \cdot 3k^2$, so $3 \mid n^2$.

Every line of the attempt is correct, and it proves nothing about the claim. It starts from $3 \mid n$ and ends at $3 \mid n^2$, so it proves the converse. A direct attempt in the right direction does not get far either: from $n^2 = 3m$ there is no step that produces a factor $3$ in $n$, since the integers do not allow taking square roots.

The proof that works changes the form of the goal. The claim is equivalent to its contrapositive: if $3 \nmid n$, then $3 \nmid n^2$. Now the hypothesis gives something to compute with. An integer not divisible by $3$ has the form $3k + 1$ or $3k + 2$, and in the two cases

$$(3k + 1)^2 = 3(3k^2 + 2k) + 1, \qquad (3k + 2)^2 = 3(3k^2 + 4k + 1) + 1,$$

so $n^2$ leaves remainder $1$ on division by $3$. The proof uses two methods, a contrapositive and a proof by cases, and each was chosen by looking at the form of the statement. The claim is the key step in the proof that $\sqrt 3$ is irrational, which is a third method again: assume $\sqrt 3 = a/b$ in lowest terms and derive a contradiction.

This chapter collects the basic methods and says, for each one, which form of statement it proves, what the skeleton of the proof looks like, and how it goes wrong. The aim is that, faced with a new statement, you can write the first and last lines of its proof before you know the middle.

## What the chapter covers

1. **Reading the goal, and the direct proof.** The topic page on [proof methods](/G9JFJGY4TQ/) matches the forms of statements to methods. Then [direct proof](/0NTF6DMVAP/) of an implication and [proving universal statements](/CX38X989TB/) by an arbitrary element.
2. **Indirect proofs.** [Proof by contrapositive](/0BB5TPGQ1N/), and [proof by contradiction](/0J0XBKG64S/) in its two forms: the refutation of a statement and the proof of a positive statement from the impossibility of its negation.
3. **Splitting the work.** [Proof by cases](/0WCP0PVET6/), with exhaustive splits, and [proving biconditionals and equivalences](/TFQ1845T84/), with two directions or a cycle of implications.
4. **Existence and uniqueness.** [Constructive proof](/01XM7JEKHY/) by a named witness, [non-constructive existence](/JZQVJ9XT63/) without one, and [proof of uniqueness](/GQHHNV79PA/).
5. **Refuting a claim, and using symmetry.** What a [counterexample](/0ED72CTBNP/) must satisfy, and when [without loss of generality](/Y7NE0E6PCV/) is a valid step.
6. **Finding a proof, and proving that none exists.** The [forward-backward method](/V8ZB838JY5/) for planning a proof, and [proof of impossibility](/6F55216R53/) by remainders and invariants.

## A first reading

Read these first, in order:

1. [Proof methods](/G9JFJGY4TQ/)
2. [Direct proof](/0NTF6DMVAP/)
3. [Proving universal statements](/CX38X989TB/)
4. [Proof by contrapositive](/0BB5TPGQ1N/)
5. [Proof by contradiction](/0J0XBKG64S/)
6. [Proof by cases](/0WCP0PVET6/)
7. [Proving biconditionals and equivalences](/TFQ1845T84/)
8. [Constructive proof](/01XM7JEKHY/)
9. [Counterexample](/0ED72CTBNP/)

Non-constructive existence, uniqueness, wlog, the forward-backward method and impossibility proofs can wait for a second pass. On a first pass, skip the remarks on intuitionistic logic in the entries on contradiction and non-constructive proof; they explain why some mathematicians reject certain proofs, and the methods can be used without them.

## Before you start

You need the connectives and quantifiers of [the language of mathematical statements](/WMY13MXY3W/), and in particular how to negate a statement with quantifiers, which is treated in [propositions, connectives and quantifiers](/PM1AYWABA7/). What a proof is, and what it may use, is the subject of [mathematical proof](/0B94TKFQJX/) and of [proof, theorems and mathematical method](/N4P3E53HM0/). The examples use divisibility, remainders, inequalities between real numbers and a little calculus. Induction, the method for statements about all natural numbers, has its own chapter, [induction and well-ordering as proof methods](/EEH2F76CYQ/).
