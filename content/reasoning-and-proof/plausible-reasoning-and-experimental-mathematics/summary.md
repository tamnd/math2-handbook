## What to remember

- **Plausible reasoning** makes a statement more or less credible without settling it. Pólya's basic pattern: if $A$ implies $B$ and $B$ turns out true, $A$ becomes more credible. If $B$ turns out false, $A$ is refuted, and that step is deductive. Verifying a consequence that was unlikely in advance counts for more than verifying one that was expected anyway.
- **Experimental mathematics** computes to find patterns and exact values. Compute a number to many digits, use an integer relation algorithm such as PSLQ or LLL to guess a closed form, and test the guess at higher precision. The output is a conjecture until it is proved, as the BBP formula for $\pi$ was.
- **Numerical evidence** is weak evidence for statements about all integers. Pólya's conjecture fails first near $9 \cdot 10^8$, and $\pi(x) < \operatorname{li}(x)$ fails somewhere below $1.4 \cdot 10^{316}$. When the error terms grow like $\log \log x$ or $\sqrt{x}/\log x$, no feasible check reaches the range where the behaviour shows.
- Guy's **strong law of small numbers**: there are not enough small numbers to meet the many demands made of them. Early agreement of two sequences is often a coincidence. His second law: when two sequences agree in their first terms, they need not be the same.
- **Heuristic arguments** predict results from models: treat $n$ as prime with probability $1/\ln n$, count parameters against conditions, or compare the orders of size of terms. The Hardy–Littlewood constant for twin primes comes from such a model and agrees with the data. A heuristic gives a prediction, not a proof, and the model can be wrong in ways the data does not reveal at first.
- **Forming a conjecture** means stating it precisely: the range of the variables, the exact claim, and what would refute it. Gather small cases, take differences and ratios, compare with known sequences, then test the statement on cases you did not use to form it.
- **Machine-assisted discovery** uses programs that propose conjectures (Graffiti, the Ramanujan Machine) or search for objects with a property (FunSearch, AlphaEvolve). A constructed object can be checked independently, and then the result is a theorem. A proposed identity is evidence of the same kind as any numerical evidence.
- **Physical arguments** read mathematics off levers, strings, soap films and currents. Archimedes found the volume of the sphere by balancing slices before he proved it by exhaustion. A physical argument usually takes for granted that an extremum or equilibrium exists, and that is often the step a proof has to supply.

## Kinds of evidence compared

| Kind of evidence | What it gives | Where it led to a theorem | Where it misled |
|---|---|---|---|
| [A verified consequence](/8DHD3H1CJ9/) | More credibility | [Euler's Basel sum](/A1NXVMGPG0/) | [A false consequence refutes](/GHWRJ1BQTN/) |
| [High-precision computation](/BPEPTN0TT9/) | A closed form to prove | [The BBP formula](/ZQWC236CQQ/) | [Ramanujan's constant](/7ZM5VCCB7H/) |
| [A finite check](/JFD3QWCX8Z/) | Support up to a bound | [Goldbach partitions grow](/RKFZV5NFXE/) | [$\pi(x) < \operatorname{li}(x)$](/Q61WD2AEBS/) |
| [Small cases](/8AFXPXCE3N/) | A pattern | [Sums of odd numbers](/9WSEMZ8BWN/) | [31, 331, 3331](/1HBCH5V3AN/) |
| [A model or count](/VCQQNJ3SEZ/) | A prediction | [Lines on surfaces](/MSMXVPKRN1/) | [Twin primes, still open](/XHHKMPD8A9/) |
| [A table of data](/R2T42N5XGK/) | A precise conjecture | [Sums of two squares](/GD5KTM6Y6P/) | [A list does not fix its continuation](/G9FEX51ASB/) |
| [A physical system](/THJV0NFPDQ/) | A value or a shape | [Archimedes' sphere](/QHY889QBEC/) | [The Fermat point at a wide angle](/1SXA826AZS/) |

: Seven kinds of evidence in the chapter. For each, an attached example where the evidence pointed to a theorem and one where it misled or left the question open.

## Weighing evidence in practice

Ask three questions of any evidence. What would the data look like if the conjecture were false? Has the check reached the range where the error terms matter? Were the cases used to test the conjecture different from the cases used to find it? Prefer evidence from several independent sources: numerics, a heuristic model, and a proof of a special case. Report what was checked and to what precision. Keep the word "theorem" for statements that have been proved.
