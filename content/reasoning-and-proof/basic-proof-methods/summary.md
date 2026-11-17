## What to remember

- A **direct proof** of "if $P$, then $Q$" assumes $P$ and derives $Q$ by a finite chain of steps, each an axiom, a definition, an earlier result or a valid inference. It never assumes $Q$. A chain that starts from $Q$ and ends at a true statement proves nothing about $Q$.
- To prove $\forall x \in X \; P(x)$, let $x$ be an **arbitrary** element of $X$: a new letter about which the proof uses nothing except $x \in X$. One counterexample refutes a universal statement; no number of checked cases proves one.
- $P \Rightarrow Q$ is equivalent to its **contrapositive** $\neg Q \Rightarrow \neg P$, and not to its converse $Q \Rightarrow P$ or its inverse $\neg P \Rightarrow \neg Q$.
- A **proof by contradiction** of $P$ assumes $\neg P$ and derives some $R$ and $\neg R$. In the strict form it uses $\neg\neg P \Rightarrow P$, which intuitionistic logic rejects. Proving a negation $\neg P$ by assuming $P$ and reaching a contradiction needs no such law.
- A **proof by cases** needs cases $C_1, \ldots, C_k$ with $C_1 \lor \cdots \lor C_k$ true. The cases need not be disjoint, but they must leave nothing out.
- $P \iff Q$ needs both $P \Rightarrow Q$ and $Q \Rightarrow P$. Statements $P_1, \ldots, P_n$ are equivalent once each can reach each other along proved implications, for example by the cycle $P_1 \Rightarrow P_2 \Rightarrow \cdots \Rightarrow P_n \Rightarrow P_1$.
- A **constructive proof** of $\exists x \, P(x)$ gives a witness $a$ and a proof of $P(a)$. A **non-constructive proof** shows existence without a witness, by contradiction, by cases that cannot be decided, or by a theorem such as the intermediate value theorem.
- $\exists! x \, P(x)$ means $\exists x \, P(x)$ and $\forall x \, \forall y \, \big(P(x) \land P(y) \Rightarrow x = y\big)$. Existence and uniqueness are independent and need separate proofs.
- A **proof of impossibility** proves $\neg \exists x \, P(x)$, that is, $\forall x \, \neg P(x)$. It usually finds an obstruction, such as a parity, a remainder or a degree, that every candidate has and the required object would not have.

## Methods and the goals they fit

| Goal | Method | Assume | Show |
|---|---|---|---|
| $P \Rightarrow Q$ | [direct proof](/0NTF6DMVAP/) | $P$ | $Q$ |
| $P \Rightarrow Q$ | [contrapositive](/0BB5TPGQ1N/) | $\neg Q$ | $\neg P$ |
| $P \Rightarrow Q$ | [contradiction](/0J0XBKG64S/) | $P$ and $\neg Q$ | a contradiction |
| $\forall x \in X \; P(x)$ | [arbitrary element](/CX38X989TB/) | $x \in X$, nothing more | $P(x)$ |
| any goal, hypothesis $A \lor B$ | [cases](/0WCP0PVET6/) | $A$, then separately $B$ | the goal, in each case |
| $P \iff Q$ | [two directions](/TFQ1845T84/) | $P$, then separately $Q$ | $Q$, then $P$ |
| $\exists x \, P(x)$ | [construction](/01XM7JEKHY/) | nothing | $P(a)$ for a named $a$ |
| $\exists x \, P(x)$ | [non-constructive](/JZQVJ9XT63/) | $\forall x \, \neg P(x)$, or a split into cases | a contradiction, or a witness in each case |
| $\exists! x \, P(x)$ | [uniqueness](/GQHHNV79PA/), plus existence | $P(x)$ and $P(y)$ | $x = y$ |
| $\neg \forall x \, P(x)$ | [counterexample](/0ED72CTBNP/) | nothing | $\neg P(a)$ for a named $a$ |
| $\neg \exists x \, P(x)$ | [impossibility](/6F55216R53/) | an object with $P$ | a contradiction, often from an obstruction |

: The basic methods by the logical form of the goal. A long proof combines several of them, one for each layer of the statement. [Without loss of generality](/Y7NE0E6PCV/) shortens a proof by cases, and the [forward-backward method](/V8ZB838JY5/) helps to find a direct proof; neither changes the goal.

## Common errors

- **Starting from the conclusion.** Scratch work may run backward from the goal, but the written proof runs forward, and each backward step must be a sufficient condition, not only a necessary one.
- **Negating wrongly.** The negation of "$A$ or $B$" is "not $A$ and not $B$"; the negation of "every $x$ has $P$" is "some $x$ fails $P$", not "no $x$ has $P$". A contrapositive or a contradiction built on a wrong negation proves nothing.
- **A missing case.** Look for $x = 0$ between positive and negative, for equality between $<$ and $>$, and for the third remainder modulo $3$.
- **A wlog step without a symmetry.** The swap or sign change must keep both the hypotheses and the conclusion.
- **A contradiction that never uses its assumption.** Then the proof is a direct proof with extra words; rewrite it as one.
