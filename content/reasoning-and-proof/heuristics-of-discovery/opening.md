Find a formula for

$$A_n = 1 - 4 + 9 - 16 + \dots + (-1)^{n+1} n^2.$$

No rule from a textbook applies at once, so compute small cases: $A_1 = 1$, $A_2 = -3$, $A_3 = 6$, $A_4 = -10$, $A_5 = 15$. The absolute values $1, 3, 6, 10, 15$ are the sums $1 + 2 + \dots + n$, and the signs alternate, so we guess

$$A_n = (-1)^{n+1} \frac{n(n+1)}{2}.$$

The guess is not yet a result, and the case $n = 4$ shows why it holds. Group the terms in pairs: $(1 - 4) + (9 - 16) = -3 - 7$, and $3 = 1 + 2$, $7 = 3 + 4$. In general $(2k)^2 - (2k - 1)^2 = (2k - 1) + 2k$, so for even $n = 2m$ the pairs give

$$A_{2m} = -(1 + 2 + \dots + 2m) = -m(2m + 1).$$

For odd $n = 2m + 1$, add the last term: $A_{2m+1} = -m(2m + 1) + (2m + 1)^2 = (2m + 1)(m + 1)$. Both cases agree with the guess, and this is a proof. A last check on a case not used so far: $A_6 = 15 - 36 = -21 = -\frac{6 \cdot 7}{2}$.

Several moves found this solution: compute special cases, look for a known sequence in the data, look in one case for the reason, split the sum into pairs and the problem into two cases by parity, and check the result on a new case. None of them is a method of proof, and none is sure to work. The same first move on the regions cut out of a disc by the chords between $n$ points gives $1, 2, 4, 8, 16$, which suggests $2^{n-1}$, and the sixth value is $31$. Such moves are [heuristics](/6KCEWEP4WA/): advice on where to look for an idea, which a proof must then confirm. The chapter takes the common heuristics one at a time, and each entry shows a problem the move solves and a case where it misleads.

## What the chapter covers

1. **What a heuristic is.** [Heuristics in mathematics](/6KCEWEP4WA/) separates a heuristic from an algorithm and from a proof, and [Pólya's four steps](/DYD57G2Y5Z/) give the plan in which the other moves sit.
2. **Related, smaller and larger problems.** [Analogy](/7KDT0R1HF2/), [specialization](/FTBJX4G51S/), [generalization](/8NJ0VN9Z97/) and the [inventor's paradox](/FVRKDXBJF6/), which says that a stronger statement can be easier to prove.
3. **Starting from the goal.** [Working backwards](/3QTB9S1THS/), the analysis and synthesis of the Greek geometers, and the [auxiliary problem](/DYSJB93V11/), a detour through a problem that is easier to solve.
4. **Adding, splitting and changing.** [Auxiliary elements](/8TKKRAXKFN/), [decomposing and recombining](/KEZPDNM2NH/), [variation of the problem](/KT5SASGTQ5/), and how to [draw a figure and introduce notation](/6CVYB413ER/).
5. **Discovery beyond single rules.** Lakatos's [proofs and refutations](/79P9CTRN0V/), [mathematical intuition](/4BT08RE4CR/), the [psychology of mathematical invention](/XMGGTNSTYC/) and [problem posing](/Y896GWYF8A/).

## A first reading

1. [Heuristics in mathematics](/6KCEWEP4WA/)
2. [Pólya's four steps](/DYD57G2Y5Z/)
3. [Specialization](/FTBJX4G51S/)
4. [Analogy](/7KDT0R1HF2/)
5. [Generalization](/8NJ0VN9Z97/)
6. [Inventor's paradox](/FVRKDXBJF6/)
7. [Working backwards](/3QTB9S1THS/)
8. [Auxiliary problem](/DYSJB93V11/)
9. [Decomposing and recombining](/KEZPDNM2NH/)
10. [Proofs and refutations](/79P9CTRN0V/)

The entries on intuition, on the psychology of invention and on problem posing describe how mathematicians work rather than a move to practise, and they can wait. Some examples use calculus (an integral with a parameter, Euler's sum of the reciprocal squares) or algebra beyond school (the ring $\Z[\sqrt{-5}]$); each entry also has examples with whole numbers, counting or plane geometry, and those are enough at first.

## Before you start

The chapter assumes what a proof is, from [proof, theorems and mathematical method](/N4P3E53HM0/), and the methods of [basic proof methods](/958EF46EYJ/), in particular the [forward-backward method](/V8ZB838JY5/) and [mathematical induction](/0ASJVEFA9J/), which turn many guesses of this chapter into theorems. The warning that examples do not prove a universal statement is treated in detail under [proof by example](/ZX6ERT3SW7/). [Plausible reasoning and experimental mathematics](/DME0TPC348/) continues with the weighing of evidence for a conjecture, and [problem solving and competitions](/2HNEG88WT8/) trains these heuristics on contest problems.
