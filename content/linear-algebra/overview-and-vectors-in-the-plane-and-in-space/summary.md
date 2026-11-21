## What to remember

- A [vector](/0QN3D80AWP/) in $\R^n$ is a list $v = (v_1, \ldots, v_n)$. Vectors add componentwise and are multiplied by numbers componentwise. Its [length](/0XKBKGTCPC/) is $\norm{v} = \sqrt{v_1^2 + \cdots + v_n^2}$, and the distance between points $p$ and $q$ is $\norm{p - q}$.
- The [dot product](/0S52TNNTH9/) is $u \cdot v = u_1 v_1 + \cdots + u_n v_n = \norm{u}\,\norm{v} \cos\theta$, where $\theta \in [0, \pi]$ is the [angle](/0ZEHZY85E6/) between $u$ and $v$. In particular $v \cdot v = \norm{v}^2$.
- Two vectors are [perpendicular](/03NK6RSRQ1/) if and only if $u \cdot v = 0$. The angle is acute when $u \cdot v > 0$ and obtuse when $u \cdot v < 0$.
- For $v \neq 0$ the [projection](/0JW13B48YP/) of $u$ along $v$ is $\operatorname{proj}_v u = \dfrac{u \cdot v}{v \cdot v}\, v$. It is the only multiple $p$ of $v$ with $u - p \perp v$.
- The [cross product](/0N5N15HWZ7/) $a \times b$ of two vectors in $\R^3$ is perpendicular to $a$ and to $b$. Its length $\norm{a}\,\norm{b} \sin\theta$ is the area of the parallelogram on $a$ and $b$. It is anticommutative, $b \times a = -a \times b$, and it is not associative.
- The [scalar triple product](/34VJYG6GVD/) $a \cdot (b \times c)$ is the determinant with rows $a$, $b$, $c$. Its absolute value is the volume of the parallelepiped on the three vectors, and it is $0$ exactly when they lie in one plane through $0$. The [vector triple product](/03FTB26QYD/) expands as $a \times (b \times c) = (a \cdot c)\, b - (a \cdot b)\, c$.
- A [line](/0399QFDFS8/) is $\set{a + t d : t \in \R}$ with $d \neq 0$. A [plane](/07SDJ5DNE4/) with normal $n \neq 0$ through $a$ is $n \cdot (r - a) = 0$, or $n_1 x + n_2 y + n_3 z = d$ with $d = n \cdot a$.
- The [distances](/C6GAS92QHX/) are lengths of projections and cross products. The table gives the formulas.

| Distance | Formula | Condition |
|---|---|---|
| point $q$ to plane $n \cdot r = d$ | $\dfrac{\abs{n \cdot q - d}}{\norm{n}}$ | $n \neq 0$ |
| point $q$ to line $a + t d$ | $\dfrac{\norm{(q - a) \times d}}{\norm{d}}$ | $d \neq 0$ |
| line $a + t d$ to line $b + s e$ | $\dfrac{\abs{(b - a) \cdot (d \times e)}}{\norm{d \times e}}$ | $d \times e \neq 0$ |
| parallel lines $a + t d$ and $b + s d$ | $\dfrac{\norm{(b - a) \times d}}{\norm{d}}$ | $d \neq 0$ |
| parallel planes $n \cdot r = d_1$ and $n \cdot r = d_2$ | $\dfrac{\abs{d_1 - d_2}}{\norm{n}}$ | the same normal $n$ |

: Distance formulas in $\R^3$. The closest points are where the connecting vector is perpendicular to the given sets.

## Common errors

- **Forgetting to divide.** The number $\abs{n \cdot q - d}$ alone is not a distance: it doubles when the equation of the plane is multiplied by $2$. Divide by $\norm{n}$, $\norm{d}$ or $\norm{d \times e}$ as the formula says.
- **Projecting along a vector that is not a unit vector.** $(u \cdot v)\, v$ is the projection only when $\norm{v} = 1$. In general, divide by $v \cdot v$.
- **Treating the cross product like a product of numbers.** $b \times a = -\,a \times b$, and $a \times (b \times c)$ is in general not $(a \times b) \times c$. Also $a \times b = 0$ does not force $a = 0$ or $b = 0$: it means that $a$ and $b$ are parallel.
- **Distance between base points.** The distance between two lines is not the distance between the points $a$ and $b$ used to write them down. For skew lines it is the length of the part of $b - a$ along the common perpendicular $d \times e$.
- **Two lines in space that do not meet need not be parallel.** In $\R^3$ two lines can be parallel, meet in one point, or be skew. Check $d \times e$ first, then whether a common point exists.
- **Reading the angle from the cross product.** $\norm{a \times b} = \norm{a}\,\norm{b}\sin\theta$ cannot tell $\theta$ from $\pi - \theta$. Use $\cos\theta = \dfrac{u \cdot v}{\norm{u}\,\norm{v}}$, which fixes $\theta \in [0, \pi]$.
