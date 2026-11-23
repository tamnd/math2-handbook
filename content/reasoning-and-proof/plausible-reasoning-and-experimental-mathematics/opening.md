Write each even number from $4$ to $30$ as a sum of two primes, in every possible way. It takes a few minutes by
hand. Every number works, and the number of ways tends to grow: $10 = 3 + 7 = 5 + 5$ has two, and
$30 = 7 + 23 = 11 + 19 = 13 + 17$ has three. The guess that every even number from $4$ on is a sum of two primes is
[Goldbach's conjecture](/063JNBSMJ0/). Computers have checked it up to $4 \cdot 10^{18}$, and the counts of
representations follow a formula of Hardy and Littlewood closely: for $n = 10^5$ the formula predicts about
$810$ representations and the true count is $810$. Nobody doubts the conjecture, and nobody has proved it.

Now take $31, 331, 3331, \ldots$, a run of $3$s followed by a $1$. The first seven numbers of the list are prime,
and the eighth is $333333331 = 17 \cdot 19607843$. Seven confirmed cases here were worth almost nothing.

Both kinds of evidence occur all the time in research. Before a proof exists, mathematicians compute, compare,
draw and guess, and these activities decide which statements are worth the effort of a proof. The chapter studies
this work: the patterns of reasoning that make a statement more credible without proving it, the computations
that find formulas, the reasons evidence misleads, and the steps that turn a guess into a precise conjecture. One
rule runs through all of it. Evidence of any amount gives a conjecture, never a theorem, and one counterexample
ends a conjecture for good.

## What the chapter covers

1. **Plausible reasoning and the experimental method.** Pólya's patterns of
   [plausible reasoning](/8DHD3H1CJ9/) say how a verified consequence or an analogy raises the credibility of a
   statement. [Experimental mathematics](/BPEPTN0TT9/) turns them into a method: compute to many digits, detect a
   relation, test it at higher precision, then prove it. The BBP formula for $\pi$ was found this way.
2. **How evidence misleads.** [Numerical evidence for conjectures](/JFD3QWCX8Z/) explains why a check up to
   $10^{18}$ can be small: some failures are controlled by $\ln \ln x$, and $\ln \ln 10^{18} \approx 3.7$. The
   [strong law of small numbers](/8AFXPXCE3N/) is Guy's warning about the first few cases, and
   [patterns that eventually fail](/A2KSJSQSF6/) gives the classic examples with the reason each breaks.
3. **From evidence to conjecture.** [Heuristic arguments](/VCQQNJ3SEZ/) predict facts from random models,
   dimension counts and scaling; [forming conjectures](/R2T42N5XGK/) shows how a table, its differences and its
   special cases lead to a precise statement.
4. **Discovery by machines and by physics.** [Machine-assisted mathematical discovery](/D1YQW43N3K/) treats programs
   that propose conjectures and constructions, and how their output is checked.
   [Physical arguments](/THJV0NFPDQ/) use levers, strings and soap films to suggest results that then need proof.

## A first reading

Read [plausible reasoning](/8DHD3H1CJ9/), [experimental mathematics](/BPEPTN0TT9/), the
[strong law of small numbers](/8AFXPXCE3N/), [patterns that eventually fail](/A2KSJSQSF6/),
[forming conjectures](/R2T42N5XGK/) and [physical arguments](/THJV0NFPDQ/), in this order. They need only school
algebra, some calculus and elementary number theory. Then read
[numerical evidence for conjectures](/JFD3QWCX8Z/) and [heuristic arguments](/VCQQNJ3SEZ/), which use the
[prime number theorem](/0EHBY5Y84N/) and the logarithmic integral. Machine-assisted discovery can wait until you
have met cap sets and matrix multiplication; its general lesson, that a program's output is a candidate to be
checked, is clear on a first pass.

## Before you start

You should know what a [mathematical proof](/0B94TKFQJX/) and a [conjecture](/WMEMMHZ3BH/) are, and the
difference between [deductive, inductive and abductive reasoning](/5V35SGEN1T/), all from
"Proof, theorems and mathematical method". The role of a single [counterexample](/0ED72CTBNP/) comes up on almost
every page. For the number theory, you need primes, divisibility and congruences; for the later entries, the
statement of the prime number theorem and the logarithmic integral $\operatorname{li}(x)$, which the entries
define. A little linear algebra helps with integer relation algorithms and dimension counts.
