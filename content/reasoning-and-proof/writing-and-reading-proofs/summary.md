## What to remember

- **A proof is a text for a stated reader.** It states exactly what is proved, introduces each letter with its type, gives a reason for each step and ends with the claim. A reason is a hypothesis, a definition, an earlier result or a rule of logic.
- **Scratch work is not the proof.** The search may run backwards from the goal; the final text runs forwards from the hypotheses, and it keeps only the steps that the reader needs.
- **The logical form fixes the first moves.** The outermost connective or quantifier of the goal, and of each given, says what sentence to write next.
- **Unpack definitions until the goal is a statement about simpler objects,** and stop at the level where a calculation or a known result settles it.
- **Proof words carry logical status.** "Let" and "fix" introduce an object, "suppose" opens an assumption, "hence" draws a consequence, "it suffices to show" replaces the goal by one that implies it.
- **An omitted step is acceptable** for a reader when it is true, the reader can supply it with known results, and it needs no new idea. Otherwise it is a gap.
- **Active reading** asks of each line what justifies it, tests the statement on examples, finds where each hypothesis is used, and states the main idea in a few sentences.
- **Checking a proof** includes running the argument on a case where the conclusion fails. If every step still goes through, the argument has an error, and the first step that should break locates it.

| Form of the goal | What to write |
|---|---|
| $\forall x \, P(x)$ | "Let $x$ be arbitrary." Then prove $P(x)$. |
| $\exists x \, P(x)$ | Name a witness $a$ and prove $P(a)$. |
| $P \Rightarrow Q$ | "Suppose that $P$." Then prove $Q$. |
| $P \iff Q$ | Prove $P \Rightarrow Q$ and $Q \Rightarrow P$. |
| $P \wedge Q$ | Prove $P$, then prove $Q$. |
| $P \vee Q$ | Prove one part, or suppose that $P$ fails and prove $Q$. |
| $\neg P$ | Suppose $P$ and derive a contradiction, or rewrite $\neg P$ in positive form. |

: The first sentence that the form of the goal dictates, from the entry on proof strategies by logical form.

| Format | Shape | Strength | Weakness |
|---|---|---|---|
| Paragraph proof | Sentences in order | Reads like prose and shows the idea | Structure of a long proof is hard to see |
| Two-column proof | Statements and reasons in a table | A reason for every step is visible | Awkward for long proofs, cases and contradiction, since a flat table has no place for an assumption that is later dropped |
| Structured proof | Numbered tree of steps, such as $\langle 2 \rangle 3$ | Shows the logical structure, can be read to any depth | Adds little to a short argument |

: Three formats for a written proof.

## Common errors

- **The bare computation.** A column of formulas with no words: the reader cannot tell what is assumed and what is claimed.
- **Scratch work handed in.** A chain that starts from the conclusion and ends at a true statement proves nothing unless every step reverses.
- **One letter for two objects.** Two existential givens need two new letters; calling both witnesses $k$ silently assumes they are equal.
- **Unpacking too far.** Expanding a definition down to the axioms buries the idea; stop where a known result applies.
- **"From the diagram".** A figure suggests a fact but does not prove it; the reason must be a given, a definition or a theorem.
- **Testing instead of checking.** Confirming that the conclusion holds in examples says nothing about whether the argument is valid.
