Which parabola $y = a + bx + cx^2$ passes through the points $(1, 2)$, $(2, 3)$ and $(3, 6)$? Each point gives one condition on the unknown coefficients, and each condition is a [linear equation](/0Q3ZT8J05R/) in $a$, $b$, $c$:

$$\begin{aligned} a + b + c &= 2, \\ a + 2b + 4c &= 3, \\ a + 3b + 9c &= 6. \end{aligned}$$

Subtract the first equation from the other two to remove $a$. This leaves $b + 3c = 1$ and $2b + 8c = 4$. Subtract twice the first of these from the second to remove $b$, which leaves $2c = 2$. Now solve from the bottom up: $c = 1$, then $b = 1 - 3c = -2$, then $a = 2 - b - c = 3$. The parabola is $y = 3 - 2x + x^2$, and indeed it gives $2$, $3$ and $6$ at $x = 1, 2, 3$.

The same work can be done on the array of numbers alone. The [augmented matrix](/0YCDZ7N8VD/) of the system goes, by the same two rounds of subtraction, to a staircase shape:

$$\left(\begin{array}{rrr|r} 1 & 1 & 1 & 2 \\ 1 & 2 & 4 & 3 \\ 1 & 3 & 9 & 6 \end{array}\right) \longrightarrow \left(\begin{array}{rrr|r} 1 & 1 & 1 & 2 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 2 & 2 \end{array}\right).$$

Small changes to the question show what else can happen. With only the first two points, the third row is missing, $c$ can be chosen freely, and there are infinitely many parabolas. With a fourth point $(4, 10)$ added, the new equation $a + 4b + 16c = 10$ fails for $(3, -2, 1)$, which gives $11$ there, so no parabola passes through all four points. One system, three possible answers: exactly one solution, infinitely many, or none. This chapter shows that these are the only possibilities over the real numbers, and it gives a procedure, row reduction, that decides which one occurs and finds all the solutions.

## What the chapter covers

1. **Equations and systems.** [Linear equations](/0Q3ZT8J05R/), [systems](/0GT4WWGWH2/) of them, [consistent and inconsistent](/0X6V9B1V10/) systems, and [homogeneous](/04KGXJG1A2/) systems.
2. **Matrices and row operations.** The [coefficient matrix](/0P7A2MJD24/), the [augmented matrix](/0YCDZ7N8VD/), the three [elementary row operations](/04XWH28452/), and [row equivalence](/006BHFWMAP/).
3. **Echelon forms and pivots.** [Row echelon form](/0VYCDGMJJJ/), [reduced row echelon form](/0WF5AQYTW6/), the [uniqueness of the reduced form](/BF9SMZMJZE/), and [pivots, basic and free variables](/0J0BBCMJ5W/).
4. **The elimination algorithms.** [Gaussian elimination](/0JVJ2WCXZH/), [back substitution](/0ATFVE08MW/) and [Gauss-Jordan elimination](/098D6FQN3N/).
5. **The solution set.** [Vector equations](/E7SAHXQEVC/), the [existence and uniqueness theorem](/BKA191KD1S/), the [parametric form](/KQT68YPHD1/), the [structure theorem](/PDH3HKXWAZ/) and the [Rouché-Capelli theorem](/0HV1SKWPMS/).
6. **Shapes of systems and other fields.** [Overdetermined and underdetermined systems](/QJ0P26J9BV/) and [systems over finite fields](/J6A58MEM8R/).

## A first reading

Start with [systems](/0GT4WWGWH2/) and the [augmented matrix](/0YCDZ7N8VD/), then learn the [elementary row operations](/04XWH28452/) and [row echelon form](/0VYCDGMJJJ/). Work through [Gaussian elimination](/0JVJ2WCXZH/) and [back substitution](/0ATFVE08MW/) with pencil and paper, then [reduced row echelon form](/0WF5AQYTW6/) and [pivots](/0J0BBCMJ5W/). Finish with the [existence and uniqueness theorem](/BKA191KD1S/), the [parametric form](/KQT68YPHD1/) and the [structure theorem](/PDH3HKXWAZ/).

On a first pass you can skip the proof of the uniqueness of the reduced form; use the result and come back to the proof later. The Rouché-Capelli theorem restates the existence test in the language of rank, which the chapter on rank develops, and the systems over finite fields can wait until you meet fields other than the real numbers.

## Before you start

You need the vectors of the [previous chapter](/VKVAJ94SKZ/): lists of numbers, their sums and multiples, and lines and planes given by equations. From [elementary algebra and functions](/DPW5ETDQ27/) you need the solution of one linear equation and of two equations in two unknowns by substitution or elimination. Fields other than the real numbers appear in a few entries; there it is enough to know that a field is a set with the four operations of arithmetic, division by zero excluded.
