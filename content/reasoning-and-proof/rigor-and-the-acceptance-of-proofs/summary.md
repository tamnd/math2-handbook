## What to remember

- A proof is **rigorous** when every step has a reason that a competent reader can check. The standard is relative
  to the reader, to the period and to the starting axioms, and it is not the same as formality: a proof in words
  can be rigorous, and a page of symbols with gaps is not.
- An **informal proof** is written for a reader who fills in routine steps. A **formal proof** is a finite
  sequence of formulas of a formal language, each an axiom, an assumption or the result of a stated rule applied
  to earlier formulas. Checking a formal proof is mechanical; finding one is hard. In practice a proof is
  accepted when experts agree that each gap can be filled by routine work.
- Results that depend on the axioms show why rigour matters: over $\Q$ a continuous function can change sign
  without a zero, so the intermediate value theorem needs the completeness of $\R$. Changes in the standard
  followed failures, such as Cauchy's claim of 1821 about series of continuous functions, which needed
  uniform convergence.
- A **proof without words** shows one case of a statement. It becomes a proof when the reader states the general
  construction, checks that the picture shows what it seems to (areas, lengths, a tiling without overlaps), and
  supplies any limit argument. The staircase shows that the length of a limit curve need not be the limit of
  the lengths.
- A **computer-assisted proof** has two parts: a written reduction of the theorem to finitely many cases, and a
  computation that settles the cases. Trust in the computation comes from independent programs, from
  certificates (such as DRAT proofs) that a small checker verifies, and from formal proofs in a proof assistant.
  A check up to a bound proves only the bounded statement.
- A proof is **surveyable** when a competent mathematician can read it and check each step in a reasonable time.
  Tymoczko named three features of a proof (it convinces, it is surveyable, it can be formalized) and argued that
  the computer proof of the four colour theorem lacks the second. A long proof is not a weaker proof.
- A proof is **accepted** when the experts of its field agree that it is correct and start to use the result.
  Acceptance can be wrong (Kempe's proof of 1879 stood until Heawood's objection of 1890) and can stall (the
  disputed step in Mochizuki's work on the abc conjecture).
- New proofs of known theorems add reasons, methods and generalizations. A **proof from the Book** is short, turns
  on one clear idea, needs little background and shows why the theorem holds; the label is a shared judgment,
  not a definition.

| Kind of proof | Who or what checks it | Typical weak point |
|---|---|---|
| Informal proof | a competent reader | a step that looks routine and is not |
| Formal proof | a program, with a small trusted kernel | the formal statement may not say what was meant |
| Proof without words | a reader who supplies the general case | the picture shows one case, or misleads |
| Computer-assisted proof | readers for the reduction, programs and certificates for the cases | an error in the reduction or the program |
| Very long proof | many experts over years | no single person checks everything |

: Kinds of proof, how each is checked, and where each tends to fail.

## Common errors

- Taking symbols for rigour. A string of formulas with an unjustified step is not a formal proof, and a proof
  assistant file that contains `sorry` proves nothing about the theorem it states.
- Calling a step obvious because a picture suggests it. Euclid's first proposition assumes that two circles meet;
  in the plane $\Q^2$ they need not.
- Reading a picture for one value of $n$ as a proof for all $n$, without the construction that passes from $n$ to
  $n + 1$.
- Treating a computation up to a bound as a proof of the unbounded statement, or a solver's "no solution found"
  as a proof that none exists without a checked certificate.
- Confusing "accepted" with "certain", or "long" with "doubtful". Acceptance is a judgment that can be revised,
  and length makes checking harder without making a correct proof less correct.
- Thinking that a theorem with a Book proof needs no other proof, or that a proof that is not from the Book is
  worse mathematics. The criteria describe form, not worth.
