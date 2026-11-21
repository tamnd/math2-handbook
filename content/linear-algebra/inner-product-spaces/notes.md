## History

The inner product began as the dot product of three-dimensional vectors. Hermann Grassmann used the name "inner product" in his calculus of extension in the middle of the nineteenth century, and in the 1880s Josiah Willard Gibbs and Oliver Heaviside made the scalar product of two vectors a standard tool of physics. The inequalities came earlier, as facts about sums and integrals. Augustin-Louis Cauchy proved the inequality for finite sums in his *Cours d'analyse* of 1821. Viktor Bunyakovsky gave the version for integrals in 1859, and Hermann Amandus Schwarz found it again later in the century in his work on minimal surfaces.

The orthonormal expansions of this chapter grew out of Fourier series. Marc-Antoine Parseval stated his identity for series in a memoir of 1799, and Friedrich Bessel derived a special case of his inequality in 1828. Jørgen Pedersen Gram orthogonalized a family of functions in 1883, in a paper on series expansions by the method of least squares, and Erhard Schmidt gave the recursive process in its modern form in 1907, in his work on integral equations. The method was known still earlier: Laplace used it, although not in the language of vectors.

Abstract spaces with an inner product came from the theory of integral equations. David Hilbert's papers of 1904 to 1910 worked with square-summable sequences, and in 1907 Frigyes Riesz and Maurice Fréchet showed independently that the continuous linear forms on the space of square-integrable functions are exactly the maps $f \mapsto \ip{f}{g}$. John von Neumann set out the axioms of an abstract Hilbert space in the late 1920s, for the mathematics of quantum mechanics. In 1935 Pascual Jordan and von Neumann proved that a norm comes from an inner product exactly when it satisfies the parallelogram law.

Two conventions for complex inner products are still in use. Most mathematics books, and this chapter, take the inner product linear in the first slot. Physicists follow Dirac's bra-ket notation, in which $\langle x \mid y \rangle$ is linear in the second slot, and Mathlib does the same. The two inner products are complex conjugates of each other, so every formula has a twin in which the conjugates sit on the other factor.

## Further reading

- Sheldon Axler, *Linear Algebra Done Right*, fourth edition (2024). Chapter 6 covers inner products, norms, orthonormal bases, the Gram-Schmidt process and the Riesz representation theorem, with the same convention as this chapter; it is the source the entries follow.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces*, second edition (1958). A short, coordinate-free treatment of inner product spaces that points toward Hilbert space.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra*, second edition (1971). Its chapter on inner product spaces gives careful proofs over $\R$ and $\C$, including the existence of orthonormal bases and the representation of linear forms.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997). The lectures on QR factorization explain the classical and modified Gram-Schmidt processes and why the modified one behaves better in floating point.
- Erwin Kreyszig, *Introductory Functional Analysis with Applications* (1978). For the step from finite dimension to Hilbert space: orthonormal sequences, Bessel's inequality, Parseval's identity and the Riesz theorem in infinite dimension.
