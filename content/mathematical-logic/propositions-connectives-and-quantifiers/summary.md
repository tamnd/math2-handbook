## What to remember

- A **[proposition](/0ZGC7ZESYN/)** has exactly one of the two truth values. A formula in $n$ variables has a [truth table](/05RSK4Q657/) with $2^n$ rows, and there are $2^{2^n}$ truth functions of $n$ variables: $16$ binary connectives.
- The **[material implication](/0NMG7W7Q11/)** $p \to q$ is false only when $p$ is true and $q$ is false, so $p \to q \equiv \neg p \lor q$. It is equivalent to its [contrapositive](/04T1CT7212/) $\neg q \to \neg p$, and not to its [converse](/09A3N7ZN5G/) $q \to p$ or its inverse $\neg p \to \neg q$.
- $\varphi \equiv \psi$ holds exactly when $\varphi \leftrightarrow \psi$ is a [tautology](/05006AJ7DZ/). Replacing a subformula by an equivalent one gives an equivalent formula, and substituting formulas for variables in a tautology gives a tautology.
- **Completeness of connectives.** Every truth function is expressed with $\neg$, $\land$, $\lor$. The [Sheffer stroke](/1NNYWRN6B8/) $\uparrow$ and the Peirce arrow $\downarrow$ are the only binary connectives that are complete on their own. The set $\set{\land, \lor, \to, \leftrightarrow}$ is not complete, because each formula over it is true when all its variables are true.
- **[De Morgan's laws](/09PKJKA6J0/)** $\neg(p \lor q) \equiv \neg p \land \neg q$ and $\neg(p \land q) \equiv \neg p \lor \neg q$ extend to quantifiers: $\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$ and $\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$.
- **Valid forms and fallacies.** Modus ponens, modus tollens, hypothetical syllogism and disjunctive syllogism are valid. Affirming the consequent and denying the antecedent are not: the row $p = \mathrm{F}$, $q = \mathrm{T}$ makes their premises true and their conclusions false.
- **Restricted quantifiers.** $\forall x \in A\; P(x)$ means $\forall x\, (x \in A \to P(x))$, and $\exists x \in A\; P(x)$ means $\exists x\, (x \in A \land P(x))$. For $A = \varnothing$ the first is [vacuously true](/0V4QXPGJQK/) and the second is false.
- **[Order of quantifiers](/0FYQMKFE77/).** $\exists y\, \forall x\, P(x, y)$ implies $\forall x\, \exists y\, P(x, y)$, and the converse fails. Quantifiers of the same kind commute.
- **[Uniqueness](/0QAJHFGZZJ/).** $\exists! x\, P(x)$ abbreviates $\exists x\, \bigl(P(x) \land \forall y\, (P(y) \to y = x)\bigr)$, which is existence and uniqueness together.

| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \oplus q$ | $p \to q$ | $p \leftrightarrow q$ | $p \uparrow q$ |
|---|---|---|---|---|---|---|---|---|
| T | T | F | T | T | F | T | T | F |
| T | F | F | F | T | T | F | F | T |
| F | T | T | F | T | T | T | F | T |
| F | F | T | F | F | F | T | T | T |

: The truth tables of the connectives of the chapter, with the rows in the standard order.

| Law | Classical logic | Intuitionistic logic |
|---|---|---|
| excluded middle $p \lor \neg p$ | valid | not valid |
| noncontradiction $\neg(p \land \neg p)$ | valid | valid |
| $p \to \neg\neg p$ | valid | valid |
| $\neg\neg p \to p$ | valid | not valid |
| $\neg(p \lor q) \leftrightarrow (\neg p \land \neg q)$ | valid | valid |
| $\neg(p \land q) \to (\neg p \lor \neg q)$ | valid | not valid |
| $(p \to q) \to (\neg q \to \neg p)$ | valid | valid |
| $(\neg q \to \neg p) \to (p \to q)$ | valid | not valid |
| $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ | valid | not valid |
| $\neg \exists x\, P(x) \leftrightarrow \forall x\, \neg P(x)$ | valid | valid |

: Which laws survive without excluded middle. The entry on each law gives the reason.

## Common errors

- Proving the converse instead of the statement, or proving the inverse and calling it the contrapositive. Write down the four forms of $p \to q$ first.
- Pairing $\forall$ with $\land$ or $\exists$ with $\to$. "Every $A$ is $B$" is $\forall x\, (A(x) \to B(x))$; "some $A$ is $B$" is $\exists x\, (A(x) \land B(x))$.
- Reading "$p$ only if $q$" as $q \to p$. It is $p \to q$: the phrase "only if" introduces the consequent.
- Reading "or" as exclusive. In mathematics $p \lor q$ is true when both parts are true, so "$p \lor q$ and $p$" does not give $\neg q$.
- Negating a statement with several quantifiers by changing the order of the variables. The negation of $\forall x\, \exists y\, P$ is $\exists x\, \forall y\, \neg P$, with $x$ still first.
- Concluding from "every element of $S$ has $P$" that some element has $P$, without checking that $S$ is nonempty.
