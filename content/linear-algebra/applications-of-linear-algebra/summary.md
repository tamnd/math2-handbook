## What to remember

- **Interpolation.** For distinct $t_0, \dots, t_n$ in a field $F$ and any $y_0, \dots, y_n \in F$, exactly one polynomial $p$ of degree at most $n$ has $p(t_i) = y_i$ for all $i$, because the Vandermonde determinant $\prod_{i < j} (t_j - t_i)$ is nonzero.
- **Least squares.** For a real $m \times n$ matrix $A$ and $y \in \R^m$, the normal equations $A^{\mathsf T} A c = A^{\mathsf T} y$ always have a solution, unique when the columns of $A$ are independent, and $Ac$ is the orthogonal projection of $y$ onto the column space. If the model contains the constant column, $R^2 = \norm{Ac - \bar y \mathbf 1}^2 / \norm{y - \bar y \mathbf 1}^2 \in [0, 1]$.
- **Recurrences.** Over a field $K$, the solutions of $u_{n+k} = c_0 u_n + \dots + c_{k-1} u_{n+k-1}$ form a $k$-dimensional space. If $x^k - c_{k-1} x^{k-1} - \dots - c_0$ has $k$ distinct roots $r_j$ in $K$, every solution is $u_n = \sum_j a_j r_j^n$.
- **Discrete time.** If $A$ is diagonalizable with eigenpairs $(\lambda_i, v_i)$ and $x_0 = \sum c_i v_i$, then $A^k x_0 = \sum c_i \lambda_i^k v_i$. If $\abs{\lambda_1} > \abs{\lambda_i}$ for all $i \ge 2$ and $c_1 \ne 0$, then $A^k x_0 / \lambda_1^k \to c_1 v_1$.
- **Markov chains.** A column-stochastic matrix has the eigenvalue $1$. If it is regular (some power has only positive entries), it has exactly one steady-state vector $q$, and $P^k x_0 \to q$ for every probability vector $x_0$. The Google matrix $\alpha S + \frac{1 - \alpha}{n} J$ with $0 \le \alpha < 1$ is positive, so PageRank is well defined.
- **Continuous time.** If the real $n \times n$ matrix $A$ has a basis of eigenvectors $v_i$ of $\C^n$, every solution of $x' = Ax$ is $\sum c_i e^{\lambda_i t} v_i$; a non-real eigenpair $(\lambda, v)$ gives the two real solutions $\operatorname{Re}(e^{\lambda t} v)$ and $\operatorname{Im}(e^{\lambda t} v)$.
- **Pictures and signals.** In homogeneous coordinates the matrix of "first $M_1$, then $M_2$" is $M_2 M_1$. In an orthonormal basis, dropping coordinates costs exactly the sum of their squared absolute values. The truncated SVD $A_k = \sum_{i \le k} \sigma_i u_i v_i^{*}$ is a nearest matrix of rank at most $k$, with $\norm{A - A_k}_F^2 = \sigma_{k+1}^2 + \dots + \sigma_r^2$ and $\norm{A - A_k}_2 = \sigma_{k+1}$.
- **Lights Out and graphs.** A Lights Out pattern $b$ can be switched off exactly when $Ax = b$ is solvable over $\mathbb F_2$; as $A$ is symmetric, this means $b \cdot y = 0$ for every quiet pattern $y$. For a graph, $(A^k)_{ij}$ counts walks of length $k$ from $i$ to $j$, and the Laplacian is $L = B B^{\mathsf T} = D - A$.

## Stability in discrete and continuous time

| | $x_{k+1} = A x_k$ | $x' = Ax$ |
|---|---|---|
| Solution along an eigenvector | $\lambda^k v$ | $e^{\lambda t} v$ |
| Decays to $0$ when | $\abs{\lambda} < 1$ | $\operatorname{Re} \lambda < 0$ |
| Grows when | $\abs{\lambda} > 1$ | $\operatorname{Re} \lambda > 0$ |
| Constant solutions | eigenvectors for $\lambda = 1$ | eigenvectors for $\lambda = 0$ |

: The two kinds of evolution read different features of the same eigenvalue, the unit circle in one case and the imaginary axis in the other.

## Common errors

- Fitting a line by solving two of the equations exactly. The least-squares line usually passes through none of the data points; with a constant term it passes through $(\bar x, \bar y)$.
- Using $R^2 = 1 - \norm{r}^2 / \norm{y - \bar y \mathbf 1}^2$ for a model without the constant column, where it can be negative.
- Mixing conventions. If the columns of $P$ sum to $1$, distributions are columns and evolve by $x \mapsto Px$; if the rows sum to $1$, they are rows and evolve by $\pi \mapsto \pi P$.
- Concluding convergence from a unique steady state. The cyclic chain on three states has one, but its distributions go round for ever.
- Composing transformations in the wrong order, or rotating about a point without conjugating by translations.
- Solving Lights Out over $\R$. Pressing a cell twice does nothing, so the arithmetic is modulo $2$, and the rank over $\mathbb F_2$ can be smaller than over $\R$.
