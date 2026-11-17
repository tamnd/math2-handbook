## What to remember

- A **proof** of a statement is a finite chain of steps that ends with the statement. Each step is a hypothesis, an axiom, a definition, a result already proved, or a consequence of earlier steps by a valid rule such as [modus ponens](/0Y0MQYST0M/). A proof covers every case its hypotheses allow; a list of checked cases covers only those cases.
- **Only deduction proves.** In a deduction the conclusion must be true whenever all the premises are. Inductive reasoning, from many cases to a general claim, and abductive reasoning, from a fact to a hypothesis that would explain it, only suggest. Mathematical induction is a deduction.
- **Theorem, proposition, lemma, corollary and claim** all name proved statements. They differ only in the role the author gives them: a main result, a smaller result, a step towards another result, a quick consequence, a step inside a proof.
- A theorem has the form "if $H_1, \ldots, H_k$, then $C$". It says nothing about cases where a hypothesis fails. To see why a hypothesis is there, drop it and look for a counterexample: $\abs{x}$ on $[-1, 1]$ satisfies every hypothesis of [Rolle's theorem](/0194DY35BG/) except differentiability at $0$, and its derivative is never $0$.
- The **axiomatic method** fixes primitive terms and axioms, then defines and proves everything else. A model in which all the axioms hold shows that they are consistent relative to the model; a model in which one axiom fails and the others hold shows that the axiom is independent of them.
- A **conjecture** is a statement that is believed but not proved. Its status changes by a proof, as for [Fermat's Last Theorem](/0Y5X3SDBCZ/) in 1994, or by a counterexample, as for [Euler's sum of powers conjecture](/E486QA4JS4/) in 1966.
- A proof serves five **functions**: verification, explanation, communication, discovery and systematization. Two proofs of one theorem can serve them differently.
- A **classification** lists the objects of a kind up to an equivalence. An **invariant** takes equal values on equivalent objects, so different values prove that two objects are not equivalent; a complete set of invariants also proves the converse.

## Kinds of statements

| Kind | Status | How it is justified | Example from the entries |
|---|---|---|---|
| Axiom | assumed | not proved; chosen to fix a theory | the [parallel postulate](/2PC3XY0PYZ/) |
| Definition | stipulated | not proved; it introduces a word | "$n$ is even if $n = 2k$ for some integer $k$" |
| Theorem | proved | a proof; a main result | the [fundamental theorem of arithmetic](/084HH1NDCB/) |
| Lemma | proved | a proof; used to prove another result | [Euclid's lemma](/051VYKA1EX/) |
| Corollary | proved | a short proof from a result just proved | the [irrationality of the square root of 2](/0DZGSDHD92/) |
| Conjecture | open | evidence only; no proof and no counterexample | [Goldbach's conjecture](/063JNBSMJ0/) |

: The status of a mathematical statement. The labels of proved statements are conventions of writing, so the same result can be a lemma in one book and a theorem in another.

## Common errors

- **Taking cases for a proof.** The [Mertens conjecture](/4Y4HWKA2MP/) agrees with every value computed so far, and it is false: Odlyzko and te Riele disproved it in 1985 without exhibiting a counterexample.
- **Affirming the consequent.** From "if $P$ then $Q$" and $Q$, nothing follows about $P$. "Every multiple of $4$ is even, and $6$ is even" does not make $6$ a multiple of $4$.
- **Using a theorem outside its hypotheses.** Before you apply a result, check each hypothesis on your object, including the hidden ones, such as a closed interval or a nonzero denominator.
- **Reading the label as a measure of depth.** Zorn's lemma and the Yoneda lemma are major results, and Fermat's "last theorem" was a conjecture for over three centuries.
- **Trusting a special figure.** A drawing with a right angle or equal sides can make a false general claim look true. Test a geometric claim on a generic figure, not only on a symmetric one.
