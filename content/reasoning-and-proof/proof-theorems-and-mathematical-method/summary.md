## What to remember

- A **proof** of a statement is a finite sequence of steps ending with the statement, where each step is a hypothesis, an axiom, a definition, a result proved earlier, or a consequence of earlier steps by a valid rule of inference such as modus ponens. An informal proof leaves routine steps to the reader; a formal proof gives every step, so that a computer can check it.
- **Deduction** is the only kind of reasoning that proves: its conclusion is true whenever all its premises are true. Checking many cases (enumerative induction) and proposing an explanation (abduction) produce conjectures, not theorems. Proof by [mathematical induction](/0ASJVEFA9J/) is a deduction, despite its name.
- **Theorem, proposition, lemma, corollary** and **claim** all mean "proved". A lemma is proved mainly to help prove another result, and a corollary follows quickly from a result just proved. The labels are conventions of writing; a lemma is exactly as true as a theorem.
- A result "if $H_1, \dots, H_k$, then $C$" asserts $C$ in every case where all the $H_i$ hold, and **nothing** in the other cases. A hypothesis is needed when the statement becomes false without it, which one counterexample shows; it is sharp when no weaker condition of the same kind suffices.
- An **axiom system** consists of primitive terms, axioms, definitions and the theorems proved from them. A theorem holds in every model of the axioms. The system is **consistent** if it has a model, and an axiom is **independent** of the others if some model satisfies the others but not it.
- A **conjecture** is an exact statement that is believed and is neither proved nor disproved. It ends in a proof (it becomes a theorem), a disproof (often a counterexample), or a proof that the accepted axioms cannot settle it.
- Proofs have several **functions**: verification, explanation, communication, discovery and systematization (in the list of Michael de Villiers). Two correct proofs of one theorem can serve different functions.
- An **example** of a notion satisfies every condition of its definition; a useful **non-example** fails exactly one condition; a **counterexample** makes a universal statement false, and one counterexample is enough.
- Let $\sim$ be an equivalence relation on a class $X$. An **invariant** is a function $f$ on $X$ with $x \sim y \Rightarrow f(x) = f(y)$, so different values prove $x \not\sim y$. It is **complete** if also $f(x) = f(y) \Rightarrow x \sim y$. For finite-dimensional vector spaces over a fixed field, dimension is a complete invariant for isomorphism; for finite groups, the order is an invariant but not a complete one.

## Three kinds of reasoning

| Kind | Passes from | To | Is the conclusion certain? |
|---|---|---|---|
| Deduction | premises | a conclusion true whenever all premises are true | yes, given the premises |
| Enumerative induction | many checked cases | a general claim | no: $n^2 + n + 41$ is prime for $40$ cases and then fails |
| Abduction | an observed fact | a hypothesis that would explain it | no: it proposes a reason that must then be proved |

: Only the first row produces theorems. The other two produce conjectures, which a deduction must then confirm or refute.

## Common errors

- **Proof by examples.** Checking $n = 1, \dots, 100$ proves nothing about all $n$.
- **Affirming the consequent.** From "if $P$ then $Q$" and $Q$, nothing follows about $P$. The converse of a theorem is a new statement that needs its own proof, and it is often false.
- **Using a theorem without its hypotheses.** Check every hypothesis in the case at hand; $|x|$ on $[-1, 1]$ satisfies all hypotheses of Rolle's theorem except differentiability at $0$, and its derivative is never $0$.
- **Reading a failed hypothesis as a failed conclusion.** If a hypothesis fails, the theorem is silent; the conclusion may still be true. For $x^2$ on $[-1, 2]$ the endpoint values differ, yet the derivative vanishes at $0$.
- **Using an unstated assumption.** A proof inside an axiom system may use only the axioms, the definitions and earlier theorems. Euclid's first proposition takes a point where two circles meet, and none of his postulates gives one.
- **Using an invariant backwards.** Equal values of an invariant prove nothing unless the invariant is complete: $\Z/4$ and the Klein four-group both have order $4$ and are not isomorphic.
- **Generalizing a rule without its hypothesis.** The identity $(a + b)^2 = a^2 + 2ab + b^2$ uses $ab = ba$, and it fails for most pairs of square matrices.
