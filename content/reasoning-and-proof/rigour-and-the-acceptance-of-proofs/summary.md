## What to remember

- An argument is **rigorous** when each step follows from the hypotheses, from definitions or from accepted results by accepted rules, and when its intended reader could supply any step that is left out. Rigour is relative to a reader: the same proof can be complete for a specialist and full of gaps for a student.
- A **formal proof** is a finite sequence of formulas in a formal system, each an axiom or obtained from earlier ones by a rule; it can be checked mechanically. An **informal proof** is the usual written argument. It is accepted because readers believe it could be turned into a formal proof, and proof assistants now do this for a growing part of mathematics.
- The standard has a history. Greek geometry made deduction from stated principles the norm. The calculus ran ahead of its foundations until Cauchy, Bolzano, Weierstrass and Dedekind put limits and real numbers on a precise basis. Hilbert repaired Euclid's axioms in 1899, and Frege, Russell and Gödel made proof itself an object of study.
- A **proof without words** is a picture that suggests a general argument. It is a proof only when the reader can say why the picture works for every $n$, or every shape, and not only for the one drawn. Pictures can also mislead, as limits of staircases and zigzags do.
- A **computer-assisted proof** reduces a theorem to finitely many checks done by a program. To accept it, one must trust the reduction, the program and the machine. Independent programs, certificates that a small checker can verify, and formal verification all reduce the trust required.
- A proof is **surveyable** when one competent reader can check it all in a reasonable time. Long proofs, such as the classification of finite simple groups, are checked by many experts working on parts of the proof, and later versions make them shorter.
- **Acceptance** is a social process: refereeing, seminars, independent checks and use of the result in later work. Most errors are found and repaired, as in Wiles's proof; some proofs stand for years before an error appears, as Kempe's did; a few claims stay contested.
- Mathematicians give **many proofs of one theorem** because new proofs bring understanding, generality, new methods, or elementary arguments. A **Book proof**, in Erdős's phrase, is one that also explains why the theorem is true.

## Kinds of proof compared

| Kind of argument | Who or what checks it | Main risk | Example |
|---|---|---|---|
| [Informal proof](/8VZ77R4R8S/) | A competent reader | A gap the reader also misses | [Divisibility is transitive](/RWQ7M25Z5Z/) |
| [Formal derivation](/8VZ77R4R8S/) | A mechanical check | The formal statement says the wrong thing | [Transitivity of implication](/DNRZJKRDZC/) |
| [Proof assistant](/YM6PRDE88V/) | The kernel of the assistant | A step left as `sorry` | [A Lean proof with sorry](/BC3VRFZ7NC/) |
| [Picture](/V6ESFEFKJC/) | A reader who generalizes it | A special case taken for the general one | [The staircase that "proves" √2 = 2](/5WP0CV0866/) |
| [Computer case check](/MC18C7BMFT/) | A program run by the authors | An error in the reduction or the code | [The four colour theorem](/17BMQS5PTG/) |
| [SAT certificate](/MC18C7BMFT/) | A small independent checker | The encoding of the problem | [Boolean Pythagorean triples](/417PHKB4VC/) |
| [Formally verified computation](/RM0S65BHWH/) | A proof assistant | The statement that was formalized | [Kepler and Flyspeck](/40QATE3WJN/) |
| [Book proof](/A4RJYP79A7/) | Any reader, quickly | A short proof can hide a gap | [Euclid's primes](/RB6G2NWW4J/) |

: Eight kinds of argument from the chapter, with what checks each and where each can go wrong. The last column names an attached example.

## Judging a proof in practice

Ask who the proof is for, and check that each step is one that reader can fill in. Treat a picture as a plan for a proof and write the general argument. For a computer proof, ask what the program checks, whether a second program or a certificate confirms it, and whether the reduction to the finite check has been read by people other than the authors. For a long or new proof, wait for independent checks before relying on the result.
