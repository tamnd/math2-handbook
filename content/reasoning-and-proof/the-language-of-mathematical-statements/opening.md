Take the numbers $1, 2, 3, 4, 5, 6$ on the faces of a die and read two sentences about them.

- (A) For every $n$ in $\set{1, \dots, 6}$ there is an $m$ in $\set{1, \dots, 6}$ with $n + m = 7$.
- (B) There is an $m$ in $\set{1, \dots, 6}$ such that for every $n$ in $\set{1, \dots, 6}$, $n + m = 7$.

Both can be settled by hand. For (A), go through the six values of $n$ and write down a partner: $m = 6, 5, 4, 3, 2, 1$. Each $n$ has one, so (A) is true. For (B), a single $m$ has to serve all six values of $n$. The value $n = 1$ forces $m = 6$ and the value $n = 2$ forces $m = 5$, and $m$ cannot be both, so (B) is false. The two sentences use the same words, and only the order of "for every" and "there is" differs. The same swap separates a real definition from an empty one. A sequence $(a_n)$ is [bounded](/0A8JNBGT2Z/) when there is an $M$ with $\abs{a_n} \le M$ for every $n$; with the quantifiers the other way round, the sentence holds for every sequence, since $M = \abs{a_n}$ works for each $n$ separately.

Two more computations show the other tools the chapter needs. The sentence "$6$ is divisible by $4$ only if $6$ is even" is true. "Only if" introduces the conclusion, so the sentence says "if $4$ divides $6$, then $6$ is even", and a conditional whose hypothesis is false is true. Next, to show that (B) is false, a reader needs the negation of (B): for every $m$ there is an $n$ with $n + m \ne 7$. That is exactly what was checked, since for each $m$ one of $n = 1$ and $n = 2$ fails. The negation of a statement tells you what a [counterexample](/0ED72CTBNP/) must contain.

The chapter is about these rules: what counts as a statement, what "and", "or", "not", "if" and "for every" mean in mathematical English, how to negate the result, and what "exactly one" and "the" demand. They are not a formal logic, which the book treats elsewhere, but the logic that sits inside the prose of every definition and theorem. A reader who confuses "$P$ only if $Q$" with "$P$ if $Q$" proves the [converse](/09A3N7ZN5G/) of the theorem asked for, and a reader who negates "for every $\varepsilon > 0$ there is an $N$" wrongly builds a counterexample to the wrong statement.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Statements and the words that join them.** [The language of mathematics](/661V0DH7V3/) describes how words and symbols mix and why the small words have fixed meanings. A [mathematical statement](/S9MHMRAX88/) is true or false and not both; an open sentence becomes one when its variables get values or are quantified. [Connectives](/12QQ51VK01/) build compound statements: "or" is inclusive, "but" means "and", and not every "and" in a sentence is a connective.
2. **Conditionals and quantifiers.** [Conditional statements](/FA6YZGR2SS/) cover "if … then", "only if", "unless", "necessary", "sufficient" and "if and only if", the hidden "for every" in front of most conditionals, and the "if" of a definition. [Quantifiers](/EGTZPA6QH3/) cover "for every" and "there is", the ones that a text leaves unwritten, and why their order matters.
3. **Negation, existence and uniqueness.** [Negating statements](/K930V33BSC/) gives five rules for pushing "not" inward and tests them on continuity and convergence. [Existence and uniqueness](/ACSC75R7R5/) splits "exactly one" into two claims, each with its own proof.
4. **Where ordinary English misleads.** [Ambiguity](/8BZPKYF912/) collects the traps of "any", "a", "the", the scope of "not" and spoken formulas. The [Wason selection task](/7GYZJ2MGY9/) shows how badly people read a single conditional.

## A first reading

Take these entries in order:

- [mathematical statement](/S9MHMRAX88/);
- [connectives in mathematical language](/12QQ51VK01/);
- [conditional statements](/FA6YZGR2SS/);
- [quantifiers in mathematical writing](/EGTZPA6QH3/);
- [negating mathematical statements](/K930V33BSC/);
- [existence and uniqueness statements](/ACSC75R7R5/);
- [ambiguity in mathematical language](/8BZPKYF912/).

Try the [Wason selection task](/7GYZJ2MGY9/) before you read its answer; it takes a minute. The first entry, [the language of mathematics](/661V0DH7V3/), is a survey and can be read last. The examples on continuity and differentiability in the entries on connectives and negation can wait until you have met limits.

## Before you start

No earlier chapter is required, and school algebra with inequalities and the integers is enough for nearly all the examples. A few examples use limits, [continuity](/0KRMJRDRZT/) or [groups](/G5S1M9/); they say so where they start. Chapter 1.1 on [proof](/0B94TKFQJX/) helps but is not needed. The formal laws behind these pages, such as [De Morgan's laws](/09PKJKA6J0/) and the [truth table](/05RSK4Q657/) of the conditional, are in [propositions, connectives and quantifiers](/PM1AYWABA7/). The proof methods that use them, such as [proof by contrapositive](/0BB5TPGQ1N/) and [proof by contradiction](/0J0XBKG64S/), are in [proof methods](/G9JFJGY4TQ/).
