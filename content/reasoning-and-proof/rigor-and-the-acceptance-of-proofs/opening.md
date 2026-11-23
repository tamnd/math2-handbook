Draw the diagonal of a unit square, from $(0,0)$ to $(1,1)$, and next to it a staircase of $n$ steps that goes
right $1/n$, up $1/n$, right $1/n$, and so on. Every staircase has length $2$, since its horizontal pieces add up to
$1$ and its vertical pieces add up to $1$. As $n$ grows, the staircases come as close to the diagonal as you like:
every point of the staircase lies within $1/n$ of it. So the diagonal has length $2$, and $\sqrt 2 = 2$.

Every step sounds reasonable, and the conclusion is false. The step that fails is the unstated one: that the length
of a limit curve is the limit of the lengths. Arc length does not behave that way, and nothing in the picture
warned about it. Finding such a step, and refusing to accept it without a reason, is what rigour means.

The chapter is about that standard and the people who apply it. A proof is rigorous when every step has a reason
that a competent reader can check. But "competent reader" changes: a step that a research paper leaves out must be
spelled out for a student, and every step must be spelled out for a computer. The standard has also changed over
time, usually after a failure, as when Cauchy's claim of 1821 that a convergent series of continuous functions has
a continuous sum led to the notion of uniform convergence. Today some proofs, such as that of the
[four colour theorem](/0M406JC8J1/), rest on computations that no person can check by hand, and some, such as the
classification of finite simple groups, are too long for one reader. The last part of the chapter asks what
mathematicians want from a proof besides correctness.

## What the chapter covers

1. **What rigour asks for.** [Mathematical rigor](/E1PE9R8DBB/) gives the standard and shows that it depends on
   the reader, the period and the axioms. [Formal and informal proofs](/8VZ77R4R8S/) shows how a short textbook
   proof expands into a derivation that a program can check, and the
   [history of proof and rigor](/20F7K9RVT6/) follows the standard from Euclid to proof assistants.
2. **Pictures and computers.** A [proof without words](/V6ESFEFKJC/) can carry a real argument, if the reader
   supplies the general case. A [computer-assisted proof](/MC18C7BMFT/) joins a written reduction to a
   computation, and its trust rests on independent programs, certificates and formal checks.
3. **Proofs no single reader checks.** [Long proofs and surveyability](/RM0S65BHWH/) discusses proofs of
   thousands of pages and Tymoczko's question about the four colour theorem; [acceptance of proofs](/MJ3EHQJJHX/)
   describes how a claim becomes a theorem, and how this can fail or stall.
4. **What a proof gives beyond correctness.** [Many proofs of one theorem](/KNQDDN6PT2/) explains why known
   theorems are proved again, the [debate of Jaffe and Quinn with Thurston](/K3M3TEX7SJ/) weighs speculation
   against proof, and [proofs from the Book](/A4RJYP79A7/) describes the proofs that mathematicians judge best.

## A first reading

Read [mathematical rigor](/E1PE9R8DBB/), [formal and informal proofs](/8VZ77R4R8S/),
[proof without words](/V6ESFEFKJC/), [computer-assisted proof](/MC18C7BMFT/),
[acceptance of proofs](/MJ3EHQJJHX/) and [proofs from the Book](/A4RJYP79A7/), in this order. Together they give
the standard, its two hardest test cases and the social side of checking. The history, the entry on surveyability
and the Jaffe–Quinn debate are best read after you have seen a few proofs that needed repair; the examples
attached to them (Kempe's proof, the four colour and Kepler proofs) can be read on their own.

## Before you start

You need to know what a [mathematical proof](/0B94TKFQJX/) is, from "Proof, theorems and mathematical method",
and to have written proofs by the methods of "Basic proof methods", such as [direct proof](/0NTF6DMVAP/),
[proof by contradiction](/0J0XBKG64S/) and [mathematical induction](/0ASJVEFA9J/). Several examples use first-year
analysis: continuity, the [intermediate value theorem](/00KAFBR32E/) and
[uniform convergence](/08VZ57PT26/). Some use simple facts about primes and graphs. Formal systems appear only in
outline, through the [Hilbert system](/1MGMQX43B8/) and [natural deduction](/6KT3BJZ7D1/).
