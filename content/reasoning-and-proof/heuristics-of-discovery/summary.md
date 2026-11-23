## What to remember

- A **[heuristic](/6KCEWEP4WA/)** is a rule of thumb for finding a solution or a proof, such as "try a special case". It leaves choices to the solver, may lead nowhere, and gives a guess or a plan that still needs a proof. An **algorithm**, such as the Euclidean algorithm, fixes every step and always ends with a correct answer.
- **[Pólya's four steps](/DYD57G2Y5Z/)**: understand the problem (unknown, data, condition; or hypothesis and conclusion), devise a plan (a related problem, a special case, a part of the condition), carry out the plan (check each step), look back (check the result by a special case, by units or by a second method).
- **Specialization.** One failing case refutes a universal claim, and no number of agreeing cases proves one. An extreme case gives the answer only when you already know that the answer does not depend on the parameter.
- **Generalization and the [inventor's paradox](/FVRKDXBJF6/).** A wider problem can be easier: a fixed number becomes a parameter that can be varied or differentiated, or a stronger statement gives an induction a stronger hypothesis. Induction proves $1 + \frac{1}{4} + \dots + \frac{1}{n^2} \le 2 - \frac{1}{n}$ for all $n \ge 1$, and so the bound $< 2$, which has no direct induction.
- **Analogy** carries a method along a correspondence, such as integers and polynomials with degree in place of size. Check each step in the new setting: unique factorization fails in $\Z[\sqrt{-5}]$, where $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$, because [Euclid's lemma](/051VYKA1EX/) has no analogue there.
- **[Working backwards](/3QTB9S1THS/)** replaces the goal by a nearer goal until it reaches the data, and then reverses the chain. The reversed chain is the proof, valid only if every step reverses.
- **Auxiliary problems and elements, decomposing, variation.** A bijection turns a problem into an equivalent one; a new line, point or variable connects data and unknown; a split must come with a way to recombine, as the [Chinese remainder theorem](/0FNN9B4W64/) recombines answers modulo coprime factors; dropping a condition gives a family of solutions in which to look for the full answer.
- **[Proofs and refutations](/79P9CTRN0V/).** When a counterexample breaks a proved conjecture, find the step of the proof it breaks and add that step as a hypothesis. [Euler's formula](/09HT3P35YP/) $V - E + F = 2$ holds for a polyhedron whose surface is a topological sphere and whose faces are all discs; Cauchy's sum theorem needs uniform convergence.
- **Intuition and invention.** Wallas's stages (preparation, incubation, illumination, verification) describe what often happened; they are not a method, and an illumination is not a proof.

## What each heuristic changes

| Heuristic | Changes | How it can mislead |
|---|---|---|
| Specialization | the size of the problem | a pattern that holds for a few cases and then fails |
| Generalization | the size of the problem | the general problem may be harder or false |
| Analogy | the setting | a step with no analogue |
| Working backwards | the order of the work | steps that do not reverse |
| Auxiliary problem | the question | the detour loses a condition, as rounding a linear programme does |
| Auxiliary element | the figure or the variables | a substitution that is not valid on the whole domain |
| Decomposing | the problem, cut into parts | parts that interact, so that the best parts do not make the best whole |
| Variation | the data or the condition | a converse that is false |

: Every row gives a guess or a plan; the last column is why its output must be checked or proved.

## Common errors

- **A pattern taken for a proof.** Five cases of $1, 2, 4, 8, 16$ do not make $2^{n-1}$; look in the cases for a reason that does not depend on them.
- **Testing only the cases used to form the guess.** Test a new and general case; a claim checked only on an equilateral triangle has passed the easiest test.
- **A backward chain read forward.** "If $x^2 = 36$ then $x = 6$" reverses "if $x = 6$ then $x^2 = 36$" and loses $x = -6$.
- **An analogy without the check.** Find the lemma on which the old proof rests and test it in the new setting first.
- **The four steps as a recipe.** They say what to ask. A failed plan sends you back to an earlier phase, and nothing guarantees that a plan will come.
- **Monster-barring.** Redefining the objects to exclude a counterexample saves the statement and loses the information; ask instead which step of the proof the counterexample breaks.
