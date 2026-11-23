## What to remember

- **Pólya's fundamental inductive pattern**: from "$A$ implies $B$" and "$B$ is true" infer "$A$ is more credible".
  A surprising consequence counts for more than an expected one, and an analogy can raise credibility in the same
  way. The **demonstrative pattern** "$A$ implies $B$, $B$ is false, so $A$ is false" is deduction and is certain.
- An **integer relation** for real numbers $x_1, \ldots, x_n$ is a list of integers $a_1, \ldots, a_n$, not all
  zero, with $a_1 x_1 + \cdots + a_n x_n = 0$. The **experimental method** computes the numbers to high precision,
  finds a relation with small coefficients (PSLQ or LLL), tests it at higher precision and on new consequences,
  and then proves it. A report of a found relation states the precision, the range and the method.
- **Numerical evidence** is weighed against the scale on which a failure can occur. When the controlling quantity
  grows like $\ln \ln x$, a check up to $10^{18}$ reaches only $\ln \ln x \approx 3.7$. The Pólya conjecture
  first fails at $906150257$, the Mertens conjecture is false although no counterexample is known, and
  $\pi(x) < \operatorname{li}(x)$ holds for every computed $x$ but fails for some $x$.
- **Guy's strong law of small numbers**: there are not enough small numbers to meet the many demands made of them,
  so different rules agree on their first values by coincidence. His **second law**: two numbers that look equal
  need not be equal, as $e^{\pi\sqrt{163}}$ and the Borwein integrals show.
- A **heuristic argument** predicts a fact from a model that is not fully justified: random models (the Cramér
  model, where $n \ge 3$ is prime with probability $1/\ln n$), dimension counts and scaling. Its conclusion is a
  conjecture. A **probabilistic proof**, such as Erdős's lower bound for Ramsey numbers, studies an object that
  really is random and is a proof.
- **Forming a conjecture**: tabulate, take differences (a polynomial of degree $d$ has constant $d$-th
  differences), look at special cases, then state the claim with all quantifiers and hypotheses and test it on
  cases that were not used to find it.
- A program's output (a conjecture from Graffiti, a cap set from FunSearch, a multiplication scheme from
  AlphaEvolve) is a **candidate**. A construction is accepted after an independent check; a conjecture after a
  proof.
- A **physical argument** suggests a result and often the plan of its proof. Its hidden assumption is usually that
  an equilibrium or a minimum exists, which is what Weierstrass questioned in [Dirichlet's principle](/RKK3XHG4MR/).

| Kind of support | What it gives | What it lacks |
|---|---|---|
| Checked cases | the statement holds in a finite range | any reason for cases beyond the range |
| Heuristic argument | a model in which the statement is expected, often with a predicted constant | a justification of the model |
| Experimental relation | a formula correct to the precision used | a guarantee that the agreement is not a coincidence |
| Physical argument | a mechanism, and often the plan of a proof | proofs that equilibria and minima exist |
| Machine output | a candidate conjecture or construction | an independent check or proof |
| Proof | certainty, given the axioms | nothing |

: Kinds of support for a mathematical statement, and what each lacks.

## Common errors

- Reading "more credible" as "true". Forty prime values of $n^2 + n + 41$ do not make the next one prime.
- Fitting a formula to $k$ values and treating the fit as evidence. A polynomial of degree $k - 1$ fits any $k$
  values, so the fit itself shows nothing; only cases not used in the fit test it.
- Quoting a verification range without the scale of the problem. Going from $10^6$ to $4 \cdot 10^{18}$ moves
  $\ln \ln x$ only from $2.63$ to $3.76$.
- Trusting agreement to a few digits. The integral $I_7$ of the Borwein sequence differs from $\pi/2$ by about
  $2.31 \cdot 10^{-11}$, so ten correct digits report a false equality.
- Calling a heuristic a proof, or a probabilistic proof a heuristic. The test is whether the randomness is in the
  model of a fixed object or in the object itself.
- Stating a conjecture without its exact hypotheses. "An odd prime $p$ is a sum of two squares if and only if
  $p \equiv 1 \pmod 4$" is a theorem, but without the word "prime" it is false: $21 \equiv 1 \pmod 4$ is not a
  sum of two squares.
