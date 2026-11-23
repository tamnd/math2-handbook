## What to remember

- **A written proof** states what it proves, introduces every letter before using it and says what kind of object it is, gives a reason for every step, and ends with the claim. It is written for a stated reader.
- **Scratch work and the final proof** run in opposite directions. Scratch work starts from the goal and asks what would imply it; the final proof starts from the hypotheses and moves forward. A step that is not reversible, such as squaring or dividing by a quantity that may be $0$, must be checked before it is turned around.
- **The logical form of the goal** gives the first move, and the logical form of a hypothesis tells how to use it (see the table). [Unpacking definitions](/41JZ39GE3F/) replaces each defined term by its definition and its quantifiers, until the goal speaks about objects you can handle.
- **Proof words** have exact jobs. "Let" introduces an arbitrary object, "suppose" an assumption whose scope ends with its part of the proof, "for some" a witness that is not ours to choose, "hence" a consequence, and "we claim" a statement proved next.
- **Layouts.** A two-column proof is a flat list of statements, each with a reason citing earlier rows; it has no scope for assumptions. A structured proof is a tree: each step has its own proof, an ASSUME or CASE holds only inside its step, and the Q.E.D. step of each list cites the steps it uses.
- **Detail.** An omitted step is acceptable when it is true, when the intended reader can supply it from known results, and when it needs no new idea. Otherwise it is a gap, and a false step marked "routine" or "similarly" is an error.
- **Style.** Every formula sits inside a sentence, no sentence starts with a symbol, words separate formulas, and every symbol keeps one meaning. The equals sign is not a word for "the next step is", and $\Rightarrow$ connects statements, not actions.
- **Reading** means writing the reason for each line, testing the lines on an example, and marking where each hypothesis is used. A hypothesis that no line uses means that the theorem holds without it or that the proof has an error.
- **Checking** ends in a verdict with reasons. An argument that would apply word for word to a case where the conclusion fails cannot be correct, so running the argument on such a case finds the faulty line.

## Goals and givens

| Form | To prove it (goal) | To use it (given) |
|---|---|---|
| $P \Rightarrow Q$ | assume $P$, prove $Q$ | once $P$ is known, conclude $Q$ |
| $\forall x \in A, \ P(x)$ | let $x \in A$ be arbitrary, prove $P(x)$ | apply it to any element of $A$ |
| $\exists x \in A, \ P(x)$ | name an $x \in A$, check $P(x)$ | introduce a new letter $x_0$ with $P(x_0)$ |
| $P \wedge Q$ | prove $P$, then prove $Q$ | use $P$ and $Q$ separately |
| $P \vee Q$ | assume $\neg P$, prove $Q$ | split into the cases $P$ and $Q$ |
| $\neg P$ | assume $P$, reach a contradiction | push the negation inside first |
| $P \Leftrightarrow Q$ | prove $P \Rightarrow Q$ and $Q \Rightarrow P$ | use either implication |

: The same statement is handled one way as a goal and another way as a given. A witness from a given existential gets a new letter, never a letter already in use.

## Common errors

- **A column of formulas.** Equations without words do not say which lines are assumptions and which are claims.
- **Handing in the scratch work.** A chain that starts from the goal and ends with a true statement proves nothing unless every step reverses.
- **Choosing a witness that is not ours.** After "$n = 2k$ for some integer $k$", the letter $k$ is fixed by $n$; it cannot then be set to $5$, and two different witnesses need two different letters.
- **An assumption that outlives its scope.** A case assumption used in the next case, or "suppose $x > 0$" still in force after its part of the proof has ended.
- **"Similarly" without checking.** A change of sign or of the direction of an inequality often breaks the similarity.
- **Checking examples instead of the argument.** Examples can refute a statement, but they say nothing about whether the argument is valid.
- **Accepting a familiar-looking step.** A step that looks standard can still use a hypothesis that does not hold, such as multiplying an inequality by a number that may be negative.
