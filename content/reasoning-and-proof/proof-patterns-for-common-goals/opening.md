Which integers can be written as $3x + 5y$ with $x$ and $y$ integers? A few trials: $3 \cdot 2 + 5 \cdot (-1) = 1$, $3 \cdot 4 + 5 \cdot (-2) = 2$, $3 + 5 = 8$, $3 \cdot (-5) + 5 \cdot 3 = 0$. The guess is that every integer appears, so that the set $S = \set{3x + 5y : x, y \in \Z}$ equals $\Z$. The proof has two halves. Every element of $S$ is an integer, because sums and products of integers are integers, so $S \subseteq \Z$. For the other inclusion, take any integer $n$. Since $1 = 3 \cdot 2 + 5 \cdot (-1)$, multiplying by $n$ gives $n = 3 \cdot 2n + 5 \cdot (-n)$, so $n \in S$. Hence $\Z \subseteq S$, and $S = \Z$.

Change $3$ and $5$ to $4$ and $6$, and the answer changes. Every number $4x + 6y = 2(2x + 3y)$ is even, and every even number $2m$ equals $4 \cdot 2m + 6 \cdot (-m)$, so $\set{4x + 6y : x, y \in \Z}$ is the set of even integers, again by two inclusions. Its least positive element is $2$, which is $\gcd(4, 6)$, and that is no accident: for positive integers $a$ and $b$, the least positive integer of the form $ax + by$ is $\gcd(a, b)$. Every number $ax + by$ is a multiple of $\gcd(a, b)$, and the Euclidean algorithm, run backwards, finds $x$ and $y$ with $ax + by = \gcd(a, b)$.

The steps of these proofs were chosen by the form of each goal, not by its content. A set equality became two inclusions. "Every integer lies in $S$" is a universal claim, so its proof started from an arbitrary $n$. "There are integers $x$ and $y$ with $ax + by = \gcd(a, b)$" is an existence claim, so its proof produces $x$ and $y$, here by an algorithm. Once you see the form of a goal, you know how the proof starts and what its last line must say, and the real work is in the middle.

The chapter collects such patterns for the goals that come up most often in a first course: two sets are equal, a function is injective or surjective, a relation is an equivalence relation, two numbers or two expressions are equal, a limit exists, a property holds on a whole interval, an object with given properties exists. Each entry proves one short goal with its pattern and then shows a case where the pattern seems to apply and fails.

## What the chapter covers

1. **Sets, functions and relations.** [Set equality by double inclusion](/MKHVRNW68H/) proves $A = B$ as $A \subseteq B$ and $B \subseteq A$. [Proving injectivity and surjectivity](/DD2P85Y8E9/) gives a template for each property and shows how a one-sided inverse proves it. [Proving a relation is an equivalence relation](/RGNF33GVHX/) checks the three properties, or gets them all from a function whose fibres are the classes.
2. **Equal numbers and identities.** [Equality by two inequalities](/S3QADD13E9/) proves $a = b$ from $a \le b$ and $b \le a$, as for suprema. [Proving identities](/XP5SDYKJX0/) chains justified equalities from one side to the other.
3. **Estimates in analysis.** [Writing epsilon-delta proofs](/RXG5JTZ2PZ/) finds $\delta$ in scratch work and writes the proof forward. The [epsilon over three argument](/VXV7M0QDH6/) proves that a uniform limit of continuous functions is continuous. The [density argument](/J2J35J3055/) proves a claim on a dense set and extends it by continuity.
4. **Symmetry and reduction.** [Symmetry arguments](/H840D9TM2X/) use a change that leaves a problem the same, and [reduction to a special case](/DX2H7AD66G/) moves every case to one normal form.
5. **From local to global.** The [open-closed argument](/1JJCDJB7FM/) spreads a property over a connected space, and [bootstrapping](/YKA0ADKYFR/) turns a weak bound into a stronger one.
6. **Existence by algorithm.** A [proof by algorithm](/X5HG1RNWQX/) builds the object and proves that the procedure stops with a correct output.

## A first reading

Read these first, in order:

1. [Set equality by double inclusion](/MKHVRNW68H/)
2. [Proving injectivity and surjectivity](/DD2P85Y8E9/)
3. [Proving a relation is an equivalence relation](/RGNF33GVHX/)
4. [Equality by two inequalities](/S3QADD13E9/)
5. [Proving identities](/XP5SDYKJX0/)
6. [Writing epsilon-delta proofs](/RXG5JTZ2PZ/)
7. [Symmetry arguments](/H840D9TM2X/)
8. [Proof by algorithm](/X5HG1RNWQX/)

The epsilon over three argument, the density argument, the open-closed argument and bootstrapping use uniform convergence, dense sets and connected spaces, and they can wait until a first course in analysis. Several of their examples use integrals, $L^p$ spaces or differential equations; skip those on a first reading and keep the opening example of each entry.

## Before you start

The chapter uses the methods of [basic proof methods](/958EF46EYJ/): [direct proof](/0NTF6DMVAP/), [proof by contradiction](/0J0XBKG64S/), the [contrapositive](/0BB5TPGQ1N/) and [proof by cases](/0WCP0PVET6/). It reads statements with [quantifiers](/EGTZPA6QH3/) and forms their [negations](/K930V33BSC/), as in [the language of mathematical statements](/WMY13MXY3W/). The first group needs [sets](/0BSJ7RQ9BW/), [functions](/0EPAT51DXQ/) and [relations](/05AVARPXA2/). The analysis entries need the [limit of a function](/0TXTSEMHR5/), [continuity](/0X3WGX95FE/) and the [supremum](/0R3H5PANRQ/), and the later ones also [uniform convergence](/08VZ57PT26/) and [connected spaces](/0V032VWTHD/). The list of all methods is in [proof methods](/G9JFJGY4TQ/).
