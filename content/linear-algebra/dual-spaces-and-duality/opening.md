Take the basis $b_1 = (1, 1, 0)$, $b_2 = (0, 1, 1)$, $b_3 = (1, 0, 1)$ of $\R^3$.
Every vector is $v = c_1 b_1 + c_2 b_2 + c_3 b_3$, and each coefficient $c_i$ depends linearly on $v$.
Solving for them gives three [linear forms](/07YQ1C78G0/):
$$c_1 = \tfrac12(x + y - z), \qquad c_2 = \tfrac12(-x + y + z), \qquad c_3 = \tfrac12(x - y + z).$$
You can check that $c_i(b_j)$ is $1$ for $i = j$ and $0$ otherwise.
These three forms are the [dual basis](/0ZD2CF6ZS0/) of $b_1, b_2, b_3$.

Now keep $b_1$ and $b_2$ but replace $b_3$ by $(0, 0, 1)$.
The first coordinate form changes from $\tfrac12(x + y - z)$ to $x$, although $b_1$ itself did not change.
So the form that belongs to $b_1$ is not fixed by $b_1$ alone; it depends on the whole basis.
This is why the isomorphism $V \cong V^*$ that sends each $b_i$ to its coordinate form changes with the basis, and why identifying $V$ with $V^*$ always needs a choice, such as a basis or an inner product.

The forms on a space $V$ over $F$ make up a vector space of their own, the [dual space](/07JBSZE0V4/) $V^*$.
They appear everywhere once you look for them.
A row vector acts on columns by matrix product.
The value $p \mapsto p(2)$ and the integral $p \mapsto \int_0^1 p(t)\,dt$ are forms on polynomials.
The trace is a form on square matrices, and every form on $M_n(F)$ is $X \mapsto \operatorname{tr}(AX)$ for exactly one matrix $A$.
A plane through $0$ in $\R^3$ is the kernel of a nonzero form, and the [theorem on hyperplanes](/XR0EQN0H8T/) says the same in every space: the kernels of nonzero forms are exactly the hyperplanes, and a hyperplane fixes its form up to a scalar.

Three things go better with duality than without.
First, the dual of the dual comes back to $V$ without any choice: a vector $v$ gives the form "evaluate at $v$" on $V^*$, and in finite dimension this is an [isomorphism](/0ZJM9D7NPS/) $V \to V^{**}$.
Second, a subspace $U$ is described from the outside by the forms that vanish on it, its [annihilator](/0ASHNYF7AG/) $U^0$; a subspace of dimension $k$ in $F^n$ is cut out by $n - k$ independent equations.
Third, a linear map $f \colon V \to W$ pulls forms back, $f^*(\varphi) = \varphi \circ f$, and this [dual map](/0AZ5ARP287/) is the meaning of the transpose: in dual bases the matrix of $f^*$ is $A^{\mathsf{T}}$.

In infinite dimension the picture changes.
The coordinate forms of a basis no longer span the dual, the dual is strictly larger than the space, and the evaluation map into the double dual is injective but not onto.

## What the chapter covers

1. Linear forms and hyperplanes. [Linear forms](/07YQ1C78G0/) and their kernels, and the [theorem on hyperplanes](/XR0EQN0H8T/): the kernels of nonzero forms are the hyperplanes, and a form is fixed by its kernel up to a scalar.
2. The dual space and its size. The [dual space](/07JBSZE0V4/), the [dual basis](/0ZD2CF6ZS0/), the equality [$\dim V^* = \dim V$](/00889YD15K/) in finite dimension, and the [Erdős-Kaplansky theorem](/S5ET1HG2ZX/) for the dimension of the dual in infinite dimension.
3. The double dual and annihilators. The [canonical map into the double dual](/0ZJM9D7NPS/), the [annihilator](/0ASHNYF7AG/) of a subspace, and the [dimension formula](/06Q1EFVH0Q/) $\dim U + \dim U^0 = \dim V$ with the duals of subspaces and quotients.
4. The dual map. The [dual map](/0AZ5ARP287/), the theorem that its [matrix is the transpose](/0ZPB3180AY/), and the [kernel and image of the dual map](/7FA499AW3T/), which give a proof that row rank equals column rank.

## A first reading

For a first pass, read these entries in order:

1. [Linear form](/07YQ1C78G0/)
2. [Hyperplanes and linear forms](/XR0EQN0H8T/)
3. [Dual space](/07JBSZE0V4/)
4. [Dual basis](/0ZD2CF6ZS0/)
5. [Dimension of the dual space](/00889YD15K/)
6. [Annihilator of a subspace](/0ASHNYF7AG/)
7. [Dimension of the annihilator](/06Q1EFVH0Q/)
8. [Dual map](/0AZ5ARP287/)
9. [Matrix of the dual map is the transpose](/0ZPB3180AY/)

The Erdős-Kaplansky theorem and the infinite-dimensional half of the double dual theorem can wait; they need cardinal arithmetic and the existence of bases in every vector space.
In finite dimension, the theorem on the double dual is short and worth reading early.

## Before you start

You need bases, dimension and the extension of independent sets from [vector spaces, span, independence, bases and dimension](/MVH97H8B2J/), the matrix product and the transpose from [matrices and the operations on them](/Y1ESNQ2V52/), and kernel, image and rank-nullity from [linear maps](/9080WQTZ3M/).
Quotient spaces from [direct sums, complements and quotient spaces](/QHKTJ89V6S/) appear in the duals of quotients.
The matrix of a linear map and the change of basis matrix come from [matrices of linear maps, rank and change of basis](/S6559D61BP/).
