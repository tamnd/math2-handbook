Take the three points $A = (1, 0, 0)$, $B = (0, 1, 0)$ and $C = (0, 0, 1)$ in space, and the point $P = (2, 3, 4)$. How far is $P$ from the plane through $A$, $B$ and $C$, and which point of that plane is nearest to $P$?

Coordinates alone do not give a quick answer. The nearest point is the foot of the perpendicular from $P$, so we need a direction at right angles to the plane. Vectors give one in two steps. The arrows along two sides of the triangle are $B - A = (-1, 1, 0)$ and $C - A = (-1, 0, 1)$, and their [cross product](/0N5N15HWZ7/) is perpendicular to both:

$$n = (B - A) \times (C - A) = (1 \cdot 1 - 0 \cdot 0,\; 0 \cdot (-1) - (-1) \cdot 1,\; (-1) \cdot 0 - 1 \cdot (-1)) = (1, 1, 1).$$

So the plane is $x + y + z = 1$. The distance from $P$ to the plane is the length of the part of $P - A = (1, 3, 4)$ that points along $n$. The [dot product](/0S52TNNTH9/) measures that part:

$$\frac{(P - A) \cdot n}{\norm{n}} = \frac{1 + 3 + 4}{\sqrt{3}} = \frac{8}{\sqrt{3}} \approx 4.62.$$

The foot is $P - \tfrac{8}{3} n = \left(-\tfrac23, \tfrac13, \tfrac43\right)$, and its coordinates do add up to $1$. As a by-product, the [length](/0XKBKGTCPC/) $\norm{n} = \sqrt{3}$ is twice the area of the triangle $ABC$.

Each step used one idea of this chapter: the arrow $B - A$ between two points, the cross product for a normal vector, the dot product for a component, and the length for a distance. With these few tools a geometric question becomes a short calculation, and the same calculations work in every dimension where they make sense.

## What the chapter covers

1. **The subject and how it is taught.** The [overview](/Y7PBW8VD4Q/) describes linear algebra as a whole, the [essay on teaching](/9AXCDDT1Z1/) compares ways of building a course, the [essay on eigenvalues without determinants](/4C6EBHFF3R/) shows a second road through the theory, and the [list of common errors](/79YPKR857M/) names the traps that recur in later chapters.
2. **Vectors and their length.** [Vectors](/0QN3D80AWP/) as arrows and as lists of numbers, and their [length](/0XKBKGTCPC/).
3. **The dot product, angles and projection.** The [dot product](/0S52TNNTH9/), the [angle](/0ZEHZY85E6/) between two vectors, the [perpendicularity test](/03NK6RSRQ1/) $u \cdot v = 0$, and [projection](/0JW13B48YP/) along a vector.
4. **Products in space.** The [cross product](/0N5N15HWZ7/), the [scalar triple product](/34VJYG6GVD/) and volume, and the [vector triple product](/03FTB26QYD/).
5. **Lines, planes, distances and plane geometry.** [Lines](/0399QFDFS8/), [planes](/07SDJ5DNE4/), [distances](/C6GAS92QHX/) between them, and [vector proofs in plane geometry](/ZVEKWJTSV7/).

## A first reading

Read the [overview](/Y7PBW8VD4Q/) for orientation, then [vectors](/0QN3D80AWP/) and their length, the [dot product](/0S52TNNTH9/), the [angle](/0ZEHZY85E6/) and [projection](/0JW13B48YP/). In space, read the [cross product](/0N5N15HWZ7/) and the [scalar triple product](/34VJYG6GVD/), then [lines](/0399QFDFS8/), [planes](/07SDJ5DNE4/) and [distances](/C6GAS92QHX/). The [Cauchy-Schwarz inequality](/0RFWW56Y22/) is worth reading early, because the definition of the angle in $\R^n$ depends on it.

On a first pass you can skip the essays on teaching and on eigenvalues without determinants; they make more sense after the chapters on linear maps and eigenvalues. The vector triple product is needed only for identities such as the Jacobi identity and can wait. Come back to the list of common errors after the chapters on matrices and row reduction, when each error has a context.

## Before you start

You need the algebra of [elementary algebra and functions](/DPW5ETDQ27/): expanding products, solving one linear equation and taking square roots. From [Euclidean geometry](/D1SR8GDYJX/) you need the Pythagorean theorem, similar triangles and the parallelogram. The cosine of an angle and the law of cosines come from [angles and right-triangle trigonometry](/N4X05D0TPR/), and coordinates, slopes and the equation of a line in the plane from [analytic geometry of lines and circles](/6NVHQ3XAD6/).
