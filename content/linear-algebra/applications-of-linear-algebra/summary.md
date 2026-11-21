## What to remember

- A conservation law (flow in equals flow out, current in equals current out, atoms before equal atoms after) gives one linear equation for each node or element. The solution set is an affine space, and its free variables are the choices the model leaves open.
- Interpolation through $n + 1$ points with distinct $x$-values by a polynomial of degree at most $n$ is a square Vandermonde system with exactly one solution. The Lagrange basis writes the answer down without solving.
- Fitting more data than parameters is a least-squares problem. The best coefficients solve $A^T A c = A^T y$, the fitted values are the orthogonal projection of $y$ onto the column space, and $R^2$ is the squared cosine of the angle between the centred data and the centred fit.
- For $x_{k+1} = A x_k$ with $A$ diagonalizable, $x_k = \sum c_i \lambda_i^k v_i$. The largest $\abs{\lambda_i}$ sets the growth rate and its eigenvector sets the long-run shape; a linear recurrence is the case of a companion matrix, and Binet's formula comes out this way.
- A column-stochastic matrix has eigenvalue $1$. If some power has all entries positive, the steady-state vector is unique and every starting distribution converges to it, at a rate set by the second largest $\abs{\lambda}$. PageRank is the steady state of a stochastic matrix built from links, with damping to make it positive.
- For $x' = Ax$ the solutions are combinations of $e^{\lambda t} v$. Negative real parts give decay, positive real parts give growth, and a complex pair $a \pm bi$ gives oscillation at frequency $b$ inside the envelope $e^{at}$.
- Homogeneous coordinates make translations and perspective linear, so a whole chain of motions is one $4 \times 4$ matrix. A change to an orthonormal basis such as Fourier or Haar preserves energy, and compression keeps the large coordinates.
- Keeping the first $k$ terms of the SVD gives the best rank-$k$ approximation; its error in the Frobenius norm is the square root of the sum of the squares of the dropped singular values.
- Linear algebra works over any field. Lights Out is a system over $\mathbb F_2$, and the matrices of a graph turn walks, cycles and Kirchhoff's laws into products, null spaces and ranks.

## The tools behind the applications

| Application | Equation | Tool |
|---|---|---|
| Networks, chemistry, input-output | $Ax = b$ or $(I - C)x = d$ | row reduction |
| Interpolation | $Vc = y$, $V$ Vandermonde | invertibility, $\det V \ne 0$ |
| Curve fitting | $A^T A c = A^T y$ | orthogonal projection |
| Recurrences, populations | $x_{k+1} = A x_k$ | diagonalization, dominant eigenvalue |
| Markov chains, PageRank | $Pq = q$ | eigenvalue $1$, Perron-Frobenius |
| Differential equations | $x' = Ax$ | eigenvectors, $e^{tA}$ |
| Graphics | $x \mapsto Mx$ in homogeneous coordinates | composition of matrices |
| Signals and images | $x = \sum c_i b_i$ | orthonormal change of basis |
| Image compression | $A \approx \sum_{i \le k} \sigma_i u_i v_i^T$ | SVD, Eckart-Young-Mirsky |
| Lights Out | $Ax = b$ over $\mathbb F_2$ | rank and null space over $\mathbb F_2$ |
| Graphs and networks | $A^k$, $B$, $L = BB^T$ | matrix powers, rank, Laplacian |

: Each application, the equation it leads to, and the part of the theory that solves it.

## Common errors

- Fitting a line through the data by solving two of the equations exactly. The least-squares line usually passes through none of the data points; it passes through the mean point $(\bar x, \bar y)$.
- Using a row-stochastic matrix with column vectors. If the columns of $P$ sum to $1$, the distribution is a column and evolves by $Pq$; if the rows sum to $1$, it is a row and evolves by $qP$.
- Forgetting that a stochastic matrix need not have a unique steady state or converge to one. A disconnected chain has several steady states, and the swap $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ oscillates forever.
- Reading the long-run behaviour from the largest eigenvalue when the starting vector has no component along its eigenvector. The coefficient $c_1$ must be nonzero.
- Applying the real formula for $x' = Ax$ to a complex pair without taking real and imaginary parts. The real solutions come from $\operatorname{Re}$ and $\operatorname{Im}$ of $e^{\lambda t} v$.
- Composing graphics transformations in the wrong order. The matrix of "first $M_1$, then $M_2$" is $M_2 M_1$.
- Solving Lights Out over $\R$ or over $\Z$. Pressing a cell twice does nothing, so all arithmetic is modulo $2$.
