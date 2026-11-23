Find the last digit of $3^{25}$ by hand. The last digit of a product depends only on the last digits of the factors, so you may keep only last digits as you go: the powers of $3$ end in $3, 9, 7, 1$, and then the cycle repeats. Since $25 = 4 \cdot 6 + 1$, the number $3^{25}$ ends in $3$. The step "keep only the last digit" is a rule on residues modulo $10$, and it is safe because multiplication of residues is [well defined](/HNGZEBKVY2/): replacing a factor by another number with the same last digit never changes the last digit of the product.

A tempting second shortcut is to reduce the exponent modulo $10$ as well. For $3^{25}$ it happens to give the right answer, since $3^5 = 243$ also ends in $3$. For $2^{12}$ it gives $2^2 = 4$, but $2^{12} = 4096$ ends in $6$. The rule "replace the exponent by its last digit" is not well defined: the exponents $2$ and $12$ have the same last digit but lead to different answers. Telling these two rules apart is a question about definitions, not about arithmetic, and so are many questions that look like arithmetic. Whether $0$ is even, whether $0$ divides $0$, and why $1$ is not prime are settled only by the exact wording of a definition, and the wording was chosen for reasons.

This chapter is about what a definition says, what it quietly claims, and how a good one is chosen.

## What the chapter covers

1. **What a definition is and the forms it takes.** A [mathematical definition](/8ZCZ3HW91Z/) is a stipulation that a new term means exactly some condition in old terms. It is read as "if and only if", and it is unfolded inside proofs. The [kinds of definitions](/B60DBNF77S/) (explicit, recursive, inductive, by abstraction, axiomatic, implicit, by a universal property, by construction) differ in what has to be proved before the definition may be used.
2. **The claims a definition carries.** A rule on equivalence classes must be [well defined](/HNGZEBKVY2/), that is, independent of the representative. Two definitions of one notion are [equivalent](/NZ42PS2P1A/) only by a theorem, and often only in one setting. A [definite description](/5P955TVSS2/), "the $x$ such that ...", needs existence and uniqueness. When strict uniqueness fails, the honest claim is uniqueness [up to](/CBC72TX3NQ/) a named equivalence relation.
3. **Where definitions start and how they are chosen.** A theory begins with [primitive notions](/QMQEJKFEYZ/) that are fixed only by axioms, and small models show what the axioms do and do not prove. The chapter closes with [choosing good definitions](/S1R1VD31BS/): why $1$ is not prime, why $0! = 1$, and how counterexamples reshaped the definition of a polyhedron.

## A first reading

Read these in order:

- [mathematical definition](/8ZCZ3HW91Z/), with its examples on even integers and divisibility;
- [kinds of definitions](/B60DBNF77S/), with the factorial and the rationals by abstraction;
- [well-defined](/HNGZEBKVY2/), the most important entry of the chapter for later work, with the examples on residue addition and the map from $\Z/6\Z$ to $\Z/3\Z$;
- [definite descriptions in definitions](/5P955TVSS2/);
- [up to](/CBC72TX3NQ/);
- [choosing good definitions](/S1R1VD31BS/).

On a first pass you can skip the example on continuity in [equivalent definitions](/NZ42PS2P1A/) and the example on the ring $\Z[\sqrt{-5}]$, which use more analysis and algebra than the rest. The example on sets and membership in [primitive notion](/QMQEJKFEYZ/) can also wait until you meet set theory.

## Before you start

You should be able to read quantified statements and know what "if and only if" asserts, as in [the language of mathematical statements](/WMY13MXY3W/), and you should know what a [proof](/0B94TKFQJX/) is and the basic [proof methods](/G9JFJGY4TQ/). The chapter uses [equivalence relations](/0G8VEZ3WTK/), [equivalence classes](/0W95W33CMP/) and the [quotient set](/0011MTQMR6/) throughout, and arithmetic modulo $n$ in many examples. Proofs by induction appear in the entries on recursion.

Some examples use first-year material: limits and continuity, the [mean value theorem](/0BARQY52N5/), and the definition of a [group](/G5S1M9/). Each of these examples is self-contained, and you can skip the ones whose background you have not met without losing the thread.
