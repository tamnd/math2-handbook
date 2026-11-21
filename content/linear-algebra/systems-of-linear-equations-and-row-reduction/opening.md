A chemist who burns propane needs numbers $x, y, z, w$ with $x\,\mathrm{C_3H_8} + y\,\mathrm{O_2} \to z\,\mathrm{CO_2} + w\,\mathrm{H_2O}$. Each element gives one equation: carbon gives $3x = z$, hydrogen gives $8x = 2w$, and oxygen gives $2y = 2z + w$. This is a homogeneous system of three linear equations in four unknowns. Its solutions are the multiples of $(1, 5, 3, 4)$, and the balanced reaction is $\mathrm{C_3H_8} + 5\,\mathrm{O_2} \to 3\,\mathrm{CO_2} + 4\,\mathrm{H_2O}$. A parabola $y = a + bx + cx^2$ through three given points is found the same way, from three equations in $a$, $b$, $c$, and so are the currents in a circuit, the prices in an economic model and the values of a discretized differential equation.

Every such system is solved by one method. Write the coefficients in a matrix, then use one row to clear the entries below it, then the next row, and so on, until the matrix is a staircase. The method is very old: it appears in the Chinese *Nine Chapters on the Mathematical Art*. What this chapter adds is the theory behind it. Row operations do not change the solutions. The final reduced form does not depend on the choices made on the way. The form tells at once whether a solution exists, whether it is unique, and how many free parameters the solution set has.

The chapter works over any field $F$, so the same steps solve systems over $\R$, over $\Q$, over $\C$ and over finite fields such as $\F_2$.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Linear equations and systems.** The [linear equation](/0Q3ZT8J05R/), the [system of linear equations](/0GT4WWGWH2/), [consistent and inconsistent systems](/0X6V9B1V10/) and the [homogeneous system](/04KGXJG1A2/), which always has the zero solution.
2. **Matrices and row operations.** The [coefficient matrix](/0P7A2MJD24/) and the [augmented matrix](/0YCDZ7N8VD/) of a system, the three [elementary row operations](/04XWH28452/), and [row equivalence](/006BHFWMAP/).
3. **Echelon forms and pivots.** The [row echelon form](/0VYCDGMJJJ/), the [reduced row echelon form](/0WF5AQYTW6/) and its [uniqueness](/BF9SMZMJZE/), and the [pivots, basic variables and free variables](/0J0BBCMJ5W/) that it shows.
4. **The algorithms.** [Gaussian elimination](/0JVJ2WCXZH/) to an echelon form, [back substitution](/0ATFVE08MW/) for a triangular system, and [Gauss–Jordan elimination](/098D6FQN3N/) to the reduced form, with their operation counts.
5. **The solution set.** [Linear systems as vector equations](/E7SAHXQEVC/), the [existence and uniqueness theorem](/BKA191KD1S/), the [parametric form](/KQT68YPHD1/) of the solutions, the [structure of the solution set](/PDH3HKXWAZ/) as $p + N$, and the [Rouché–Capelli theorem](/0HV1SKWPMS/), which states the test with ranks.
6. **Shapes and fields.** [Overdetermined and underdetermined systems](/QJ0P26J9BV/), with a first look at least squares, and [linear systems over finite fields](/J6A58MEM8R/).

## A first reading

For a first pass, read these entries in order:

1. [System of linear equations](/0GT4WWGWH2/).
2. [Augmented matrix](/0YCDZ7N8VD/).
3. [Elementary row operations](/04XWH28452/).
4. [Row echelon form](/0VYCDGMJJJ/).
5. [Reduced row echelon form](/0WF5AQYTW6/).
6. [Pivots, basic variables and free variables](/0J0BBCMJ5W/).
7. [Gaussian elimination](/0JVJ2WCXZH/).
8. [Existence and uniqueness of solutions of a linear system](/BKA191KD1S/).
9. [Parametric form of the solution set](/KQT68YPHD1/).
10. [Structure of the solution set of a linear system](/PDH3HKXWAZ/).

The proof of the uniqueness of the reduced row echelon form can wait until the result has been used a few times. The Rouché–Capelli theorem needs the rank, which later chapters treat in full; read its statement now and its proof later. The entry on finite fields is an application and can be read at any time after Gaussian elimination.

## Before you start

The chapter assumes that you can solve two or three equations in two or three unknowns by substitution, as in [elementary algebra and functions](/DPW5ETDQ27/), and it uses vectors in $\R^2$ and $\R^3$ with their sums and multiples from [overview and vectors in the plane and in space](/VKVAJ94SKZ/). A field is a set with the four operations of arithmetic and the usual rules; the definition is in [field](/04C5ZBG1WT/), but $\R$ and $\Q$ are enough for most of the chapter. The geometric picture of an equation in three unknowns as a [plane](/07SDJ5DNE4/) helps with the examples.
