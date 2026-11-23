## What to remember

- A [vector](/0QN3D80AWP/) of $\R^n$ is a list $v = (v_1, \dots, v_n)$ of real numbers. Vectors add and scale component by component, and the arrow from the point $A$ to the point $B$ is $B - A$.
- For $v \in \R^n$ the [length](/0XKBKGTCPC/) is $\norm{v} = \sqrt{v \cdot v}$. It is $0$ only for $v = 0$, and $\norm{cv} = \abs{c}\,\norm{v}$ for every real $c$. For $v \neq 0$ the vector $v / \norm{v}$ is the unit vector in the direction of $v$.
- For $u, v \in \R^n$ the [dot product](/0S52TNNTH9/) is $u \cdot v = u_1 v_1 + \cdots + u_n v_n$. It is symmetric and linear in each factor; $\abs{u \cdot v} \le \norm{u}\,\norm{v}$ by the [Cauchy-Schwarz inequality](/0RFWW56Y22/), with equality exactly when one vector is a multiple of the other.
- For nonzero $u, v \in \R^n$ the [angle](/0ZEHZY85E6/) $\theta \in [0, \pi]$ is given by $\cos\theta = \dfrac{u \cdot v}{\norm{u}\,\norm{v}}$. For all $u, v \in \R^n$, $u$ and $v$ are [perpendicular](/03NK6RSRQ1/) exactly when $u \cdot v = 0$; the zero vector is perpendicular to every vector and is the only vector with this property.
- For $u, v \in \R^n$ with $v \neq 0$ the [projection](/0JW13B48YP/) of $u$ along $v$ is $p = \dfrac{u \cdot v}{v \cdot v}\, v$. It is the only multiple of $v$ with $(u - p) \cdot v = 0$, and $\norm{u}^2 = \norm{p}^2 + \norm{u - p}^2$.
- For $a, b \in \R^3$ the [cross product](/0N5N15HWZ7/) $a \times b$ is perpendicular to $a$ and $b$, has length $\norm{a}\,\norm{b}\sin\theta$ (the area of the parallelogram on $a$ and $b$), and satisfies $b \times a = -\, a \times b$. It is $0$ exactly when $a$ and $b$ are parallel, one being a multiple of the other.
- For $a, b, c \in \R^3$ the [scalar triple product](/34VJYG6GVD/) $a \cdot (b \times c)$ is the determinant with rows $a$, $b$, $c$. Its absolute value is the volume of the parallelepiped on $a$, $b$, $c$, and it is $0$ exactly when the three vectors lie in one plane through $0$. The [vector triple product](/03FTB26QYD/) is $a \times (b \times c) = (a \cdot c)\, b - (a \cdot b)\, c$.
- A [line](/0399QFDFS8/) is $\set{a + td : t \in \R}$ with $d \neq 0$, and a [plane](/07SDJ5DNE4/) in $\R^3$ is $\set{r : n \cdot r = d}$ with $n \neq 0$. The [distance](/C6GAS92QHX/) from $q$ to the plane is $\abs{n \cdot q - d} / \norm{n}$, from $q$ to the line $a + td$ it is $\norm{(q - a) \times d} / \norm{d}$, and between the lines $a + td$ and $b + se$ with $d \times e \neq 0$ it is $\abs{(b - a) \cdot (d \times e)} / \norm{d \times e}$.

The dot product and the cross product are easy to confuse, because both take two vectors.

| | Dot product $u \cdot v$ | Cross product $a \times b$ |
|---|---|---|
| Defined for | $u, v \in \R^n$, any $n$ | $a, b \in \R^3$ only |
| Value | a number | a vector of $\R^3$ |
| Swapping the factors | unchanged | changes sign |
| Zero exactly when | the vectors are perpendicular | the vectors are parallel |
| Size | $\norm{u}\,\norm{v}\cos\theta$ | length $\norm{a}\,\norm{b}\sin\theta$ |

: The two products of vectors compared

## Common errors

- Dividing by a dot product. From $u \cdot v = u \cdot w$ with $u \neq 0$ it follows only that $u \perp (v - w)$, not that $v = w$. The same holds for the cross product: $a \times v = a \times w$ says only that $v - w$ is parallel to $a$.
- Treating the cross product as associative or commutative. In general $a \times (b \times c) \neq (a \times b) \times c$, and $a \times b = -\, b \times a$.
- Using the angle formula with a zero vector. The angle is defined only for nonzero vectors, although the test $u \cdot v = 0$ for perpendicularity holds for all vectors.
- Forgetting to divide by $\norm{n}$ in the distance to a plane. The number $\abs{n \cdot q - d}$ is the distance only when $n$ is a unit vector.
- Confusing the projection $\frac{u \cdot v}{v \cdot v}\, v$, a vector, with the scalar component $\frac{u \cdot v}{\norm{v}}$, a number that can be negative.
- Taking two lines in space that do not meet to be parallel. In $\R^3$ they can be skew: their directions are not parallel and they still have no common point.
