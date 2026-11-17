A proof method such as contradiction or induction says how an argument is organized. A proof pattern says what an argument must check for a goal of a given shape. To prove that two sets $A$ and $B$ are equal, you show $A \subseteq B$ and $B \subseteq A$: take an arbitrary element of one and show it lies in the other. To prove that $f(x) = x^3 + x$ is injective on $\R$, you take $f(a) = f(b)$ and derive $a = b$. To prove that $x^2 \to 4$ as $x \to 2$, you are given $\varepsilon > 0$ and must produce a $\delta > 0$ that works, and the work is a chain of inequalities that bounds $\abs{x^2 - 4}$ by a multiple of $\abs{x - 2}$.

Once the shape of the goal is recognized, the first lines of the proof write themselves, and the remaining effort goes into the one step that needs an idea. The patterns of this chapter range from the routine (double inclusion, the three checks for an equivalence relation) to those that carry whole fields (the $\varepsilon/3$ argument and the density argument in analysis, the open-closed argument in topology and complex analysis, bootstrapping in differential equations).

## What the chapter covers

The chapter is in five groups, read in order.

1. **Equalities and properties of maps and relations.** [Set equality by double inclusion](/MKHVRNW68H/), [injectivity and surjectivity](/DD2P85Y8E9/), [equivalence relations](/RGNF33GVHX/), [equality by two inequalities](/S3QADD13E9/) and [proving identities](/XP5SDYKJX0/). Each goal has a standard form, and each entry shows a case where one of the required checks fails.
2. **Estimates in analysis.** The [epsilon-delta pattern](/RXG5JTZ2PZ/) for limits and continuity, the [$\varepsilon/3$ argument](/VXV7M0QDH6/) for passing properties through uniform limits, and the [density argument](/J2J35J3055/) for extending a statement from a dense set.
3. **Reducing the work.** [Symmetry](/H840D9TM2X/) and [reduction to a special case](/DX2H7AD66G/), two ways to make a problem smaller before solving it.
4. **From local to global.** The [open-closed argument](/1JJCDJB7FM/) on connected spaces and [bootstrapping](/YKA0ADKYFR/), which upgrades a weak bound to a strong one by continuity.
5. **Existence by procedure.** [Proof by algorithm](/X5HG1RNWQX/): a procedure that terminates and preserves an invariant proves that its output exists.

## A first reading

On a first pass, read [set equality by double inclusion](/MKHVRNW68H/), [injectivity and surjectivity](/DD2P85Y8E9/), [equivalence relations](/RGNF33GVHX/), [equality by two inequalities](/S3QADD13E9/), [proving identities](/XP5SDYKJX0/), the [epsilon-delta pattern](/RXG5JTZ2PZ/), [symmetry](/H840D9TM2X/) and [proof by algorithm](/X5HG1RNWQX/). These cover the goals that come up in a first course on proofs and in first-year analysis.

The $\varepsilon/3$ argument, the density argument, the open-closed argument and bootstrapping need more background: uniform convergence, $L^p$ spaces, connectedness, differential equations. They can wait until a course in real analysis or topology, and their examples can be skipped on a first reading. Reduction to a special case can be read at any point.

## Before you start

The chapter assumes the [basic proof methods](/958EF46EYJ/) of the volume: [direct proof](/0NTF6DMVAP/), [proof by contrapositive](/0BB5TPGQ1N/), [proof by contradiction](/0J0XBKG64S/) and [proof by cases](/0WCP0PVET6/). It also assumes the [language of mathematical statements](/WMY13MXY3W/), in particular [quantifiers](/EGTZPA6QH3/) and how to [negate a statement](/K930V33BSC/), since a limit statement is a nest of three quantifiers. The general ideas of [mathematical proof](/0B94TKFQJX/) and of [proof methods](/G9JFJGY4TQ/) are the background for all of it.

For the examples you need sets, functions and relations at the level of a first proofs course, and limits and continuity at the level of a first calculus course. The analysis group also uses [uniform convergence](/08VZ57PT26/), and the local-to-global group uses connectedness; each entry recalls the definitions it needs.
