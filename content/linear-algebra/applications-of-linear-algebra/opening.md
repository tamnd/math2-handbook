Each year $5\%$ of the people in a city move to its suburbs and $15\%$ of the people in the suburbs move to the city. If $x_k$ lists the two shares in year $k$, then $x_{k+1} = P x_k$ with $P = \begin{pmatrix} 0.95 & 0.15 \\ 0.05 & 0.85 \end{pmatrix}$. The eigenvalues of $P$ are $1$ and $0.8$. The eigenvector for $1$ with entries summing to $1$ is $(3/4, 1/4)$, so whatever the starting shares, the city ends up with three quarters of the people, and the distance from that state shrinks by the factor $0.8$ every year. Three ideas from the earlier chapters, a matrix model, an eigenvector and a decay rate from the second eigenvalue, settle a question about the future of the city.

The chapter is a collection of such examples. Each entry takes one problem from science, engineering or computing and shows which theorem of linear algebra solves it: row reduction for networks and chemical equations, projections for fitting data, diagonalization for recurrences, population models, Markov chains and differential equations, changes of basis for graphics and signals, the SVD for compression, and linear algebra over $\mathbb F_2$ for a puzzle. The entries are examples, not new theory; they reuse the results of earlier chapters and point back to them.

## What the chapter covers

The chapter is in four groups. They are independent of each other, and each can be read on its own.

1. **Linear systems in models.** The [applications of linear systems](/1QXFM0DNAH/) to traffic, circuits, chemical equations and the input-output model, [polynomial interpolation](/NR58EBS932/) by a Vandermonde system, and [curve fitting by least squares](/C170QFW8QB/).
2. **Powers of matrices and evolution in time.** [Linear recurrences](/K00NJY6C33/) and Binet's formula, [discrete dynamical systems](/2F1B461YN7/) such as predator-prey and Leslie models, [steady states of Markov chains](/Y9FRWY8YX4/), [PageRank](/9ZPQYZ5NDP/) and [linear systems of differential equations](/DH7CQXQYJX/).
3. **Coordinates in graphics and signals.** [Computer graphics](/REB4ZHN28T/) with homogeneous coordinates, [changes of basis in signal and image processing](/6NANBCYMG2/) and [image compression by the SVD](/9QB82PPEMV/).
4. **Discrete structures.** The [Lights Out puzzle](/E8DZ9CPEEE/) over $\mathbb F_2$ and the [matrices of graphs](/JFWP2SBCF0/).

## A first reading

A short course takes one entry from each group: [curve fitting by least squares](/C170QFW8QB/), [steady states of Markov chains](/Y9FRWY8YX4/), [linear systems of differential equations](/DH7CQXQYJX/), [computer graphics](/REB4ZHN28T/) and [the matrices of graphs](/JFWP2SBCF0/). Add [linear recurrences](/K00NJY6C33/) and [PageRank](/9ZPQYZ5NDP/) if you want more on eigenvalues, and [image compression by the SVD](/9QB82PPEMV/) if you have read the chapter on the singular value decomposition.

The long entry on applications of linear systems is a set of four separate models; read one of them and skip the rest. The signal-processing entry assumes some comfort with complex numbers for the Fourier part, and its JPEG section can be left out. The Lights Out entry needs only row reduction over $\mathbb F_2$ and is a good place to see that elimination works over any [field](/0ZXZ82FTX2/).

## Before you start

The first group needs [Gaussian elimination](/0JVJ2WCXZH/) from [systems of linear equations and row reduction](/DXSXFVDMXQ/), and [least squares](/0BYTQ4X1HC/) with the [normal equations](/4D7MRG4D91/) from [orthogonal complements, projections and least squares](/8GQVME4SZZ/). The second group rests on [diagonalization, triangularization and invariant subspaces](/Z6S6PWMJPH/), with [powers of a diagonalizable matrix](/0TNR9BQ871/) and the [matrix exponential](/020M04FN1H/). The third group uses rotations and reflections from [isometries and the orthogonal and unitary groups](/AZS5BPF5H3/), and the SVD and the [Eckart-Young-Mirsky theorem](/JJT6GC055J/) from [positive definite matrices and the singular value decomposition](/SS4EVPKT3A/). The Lights Out entry needs only row reduction, the [rank](/0ZC9YTXZRY/) and the [rank-nullity theorem](/0W4FSW1TVB/); the graph entry also uses matrix powers and, at its end, the eigenvalues of the Laplacian.
