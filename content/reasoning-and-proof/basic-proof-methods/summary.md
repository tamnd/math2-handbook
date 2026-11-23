## What to remember

- **Direct proof** proves $P \Rightarrow Q$: assume $P$, unfold the definitions, compute, and fold the result into $Q$. Choose it first whenever $P$ gives something concrete, such as $n = 2k + 1$. A **universal statement** $\forall x \in D \; P(x)$ is proved by "let $x \in D$ be arbitrary" and a proof of $P(x)$ that uses nothing else about $x$.
- **Contrapositive**: $P \Rightarrow Q$ is equivalent to $\neg Q \Rightarrow \neg P$, so assume $\neg Q$ and derive $\neg P$. Choose it when $\neg Q$ is easier to compute with than $P$, as with "$n$ is not divisible by $3$". The converse $Q \Rightarrow P$ and the inverse $\neg P \Rightarrow \neg Q$ are different statements.
- **Contradiction**: assume the negation of the goal and derive some $R$ together with $\neg R$. For a negative goal $\neg P$ (irrational, no largest, no solution) this is a refutation of $P$. For a positive goal it also uses $\neg\neg P \Rightarrow P$. If the assumption is never used, the proof is a direct proof and should be written as one.
- **Cases**: from $A_1 \lor \dots \lor A_k$ and $A_i \Rightarrow R$ for each $i$, conclude $R$. Choose a split that follows the definitions (signs for $\abs x$, remainders for divisibility) and say why it is exhaustive.
- **Biconditional**: prove $P \Rightarrow Q$ and $Q \Rightarrow P$. For a list of conditions, a cycle of implications suffices; a chain of $\iff$ steps is valid only if every step reverses.
- **Existence**: name a witness and check it (constructive), or show that a witness must exist (non-constructive, by cases, contradiction, the intermediate value theorem or pigeonhole). **Uniqueness**: take two objects with the property and prove them equal, or take one known object and prove that every object with the property equals it. Existence and uniqueness are separate proofs.
- **Counterexample**: to refute $\forall x \, (H(x) \Rightarrow C(x))$, exhibit one $x$ with $H(x)$ true and $C(x)$ false. **Wlog**: if a symmetry turns each case into a case already proved, prove one case and name the symmetry.
- **Forward-backward**: work forward from the hypothesis and backward from the goal; a backward step must replace the goal by a condition that implies it. **Impossibility**: assume an object exists and reach a contradiction, usually with a remainder, an invariant, or a structure that contains everything reachable but not the target.

## Choosing a method

| Form of the goal | First line of the proof | What the proof must reach |
|---|---|---|
| $P \Rightarrow Q$ | Assume $P$. | $Q$ |
| $P \Rightarrow Q$, by contrapositive | Assume $\neg Q$. | $\neg P$ |
| $\neg P$ | Suppose $P$. | a contradiction |
| $\forall x \in D \; P(x)$ | Let $x \in D$ be arbitrary. | $P(x)$ |
| $\exists x \; P(x)$ | Let $x = \dots$ (a named witness). | a check of $P(x)$ |
| $\exists! x \; P(x)$ | Existence, then: suppose $P(x)$ and $P(y)$. | $x = y$ |
| $P \iff Q$ | $(\Rightarrow)$ Assume $P$. $(\Leftarrow)$ Assume $Q$. | $Q$, then $P$ |
| $\neg \forall x \; P(x)$ | Let $x = \dots$ (a counterexample). | a check that $P(x)$ fails |

: The outermost symbol of the goal decides the first line. Hypotheses of the form "A or B" add a case split, and hypotheses of the form "there is an x" add a named object.

## Common errors

- **Proving the converse.** Starting from the conclusion and reaching the hypothesis, as in the opening of the chapter, proves $Q \Rightarrow P$.
- **Proof by example.** Checking $P(1), \dots, P(100)$ proves those cases only; a universal statement needs an arbitrary element.
- **A wrong negation.** The negation of "for every $x > 0$, $x + 1/x \ge 2$" is "there is an $x > 0$ with $x + 1/x < 2$", not "for every $x > 0$, $x + 1/x < 2$".
- **A missing case.** The cases must cover every possibility, including boundary values such as $0$.
- **One direction twice.** Proving $P \Rightarrow Q$ and then $\neg Q \Rightarrow \neg P$ gives the same implication twice and leaves $Q \Rightarrow P$ unproved.
- **Uniqueness without existence.** "Any two solutions are equal" is true of an equation with no solution.
- **A non-counterexample.** An object that fails the hypothesis says nothing about the claim.
- **Wlog without symmetry.** Assuming $a \le b$ is valid only if exchanging $a$ and $b$ leaves the statement unchanged, or turns it into a statement already proved.
- **A failed search as a proof of impossibility.** Finding no solution below $10^6$ shows nothing about larger candidates.
