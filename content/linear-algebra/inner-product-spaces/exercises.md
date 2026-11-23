1. ◦ Decide which of the following is an inner product on $\R^2$, and for the one that is, find the length of $(1, 1)$.

$$\text{(a)}\ \langle x, y\rangle = 3x_1y_1 - x_1y_2 - x_2y_1 + x_2y_2, \qquad \text{(b)}\ \langle x, y\rangle = x_1y_1 + 2x_1y_2 + 2x_2y_1 + x_2y_2.$$

2. ◦ In $\C^2$ with the standard inner product $\langle z, w\rangle = z_1\overline{w_1} + z_2\overline{w_2}$, let $x = (2, 1 - i)$ and $y = (i, 3)$. Compute $\langle x, y\rangle$, $\langle y, x\rangle$, $\norm{x}$ and $\norm{y}$, and check the Cauchy-Schwarz inequality for this pair.

3. ◦ On the space of real polynomials of degree at most $2$, let $\langle p, q\rangle = p(-1)q(-1) + p(0)q(0) + p(1)q(1)$. Show that this is an inner product, and compute $\langle t, t^2\rangle$, $\langle 1, t^2\rangle$, $\norm{1}$ and $\norm{t^2}$.

4. ◦ In $\R^3$ with the dot product, let $x = (1, -2, 2)$ and $y = (4, 0, 3)$. Compute $\langle x, y\rangle$, $\norm{x}$, $\norm{y}$ and $\norm{x + y}$, check the Cauchy-Schwarz and triangle inequalities, and find the cosine of the angle between $x$ and $y$.

5. ◦ In a real inner product space, $\norm{x} = 3$, $\norm{y} = 4$ and $\norm{x + y} = 6$. Find $\langle x, y\rangle$ and $\norm{x - y}$.

6. ◦ In a complex inner product space, two vectors satisfy $\norm{x + y}^2 = 10$, $\norm{x - y}^2 = 2$, $\norm{x + iy}^2 = 8$ and $\norm{x - iy}^2 = 4$. Find $\langle x, y\rangle$, $\langle y, x\rangle$ and $\norm{x}^2 + \norm{y}^2$.

7. ◦ Find all vectors of $\R^3$ that are orthogonal, for the dot product, to both $(1, -1, 2)$ and $(2, 1, 0)$.

8. ◦ Check that the vectors $e_1 = \frac17(2, 3, 6)$, $e_2 = \frac17(3, -6, 2)$ and $e_3 = \frac17(6, 2, -3)$ form an orthonormal basis of $\R^3$ with the dot product. Write $v = (7, 0, 7)$ in this basis without solving a linear system, and check that the squared coordinates add up to $\norm{v}^2$.

9. ◦ Which of these matrices is the Gram matrix of two vectors in some inner product space? Give a reason for each.

$$A = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 1 + i \\ 1 + i & 3 \end{pmatrix}, \qquad C = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}.$$

10. • Find all real numbers $t$ for which $\langle x, y\rangle = x^{\mathsf T} G y$ is an inner product on $\R^3$, where

$$G = \begin{pmatrix} 1 & t & 0 \\ t & 1 & t \\ 0 & t & 1 \end{pmatrix}.$$

11. • A student writes: "In an inner product space, $\norm{x + y} = \norm{x} + \norm{y}$ holds if and only if $x$ and $y$ are linearly dependent." Give a counterexample in $\R^2$, state the correct condition, and prove the direction of it that the counterexample breaks.

12. • Prove that in a real inner product space, $\norm{x} = \norm{y}$ implies that $x + y$ and $x - y$ are orthogonal. Then show that this fails in $\C^2$ with the standard inner product, using $x = (1, 1)$ and $y = (i, 1)$.

13. • In $\R^4$ with the dot product, let $e_1 = \frac12(1, 1, 1, 1)$, $e_2 = \frac12(1, -1, 1, -1)$ and $x = (4, 0, 2, 2)$. Compute both sides of Bessel's inequality for $x$ and the family $e_1, e_2$, and find the distance from $x$ to the span of $e_1, e_2$.

14. • Apply the Gram-Schmidt process, with the dot product, to $v_1 = (1, 1, 1, 1)$ and $v_2 = (0, 1, 3, 4)$ in $\R^4$.

15. • On $\R^3$, take the inner product $\langle x, y\rangle = x_1y_1 + 2x_2y_2 + 3x_3y_3$. Apply the Gram-Schmidt process to $(1, 1, 1)$, $(0, 1, 1)$, $(0, 0, 1)$, and check the result.

16. • In $\C^2$ with the standard inner product, a student applies Gram-Schmidt to $v_1 = (2, i)$ and $v_2 = (1, 1)$ and writes

$$u_2 = v_2 - \frac{\langle v_1, v_2\rangle}{\langle v_1, v_1\rangle}\, v_1.$$

Compute the student's $u_2$, show that it is not orthogonal to $v_1$, find the error, and give the correct $u_2$ and its length.

17. • In $\R^4$ with the dot product, extend the orthonormal family $\frac12(1, 1, 1, 1)$, $\frac12(1, 1, -1, -1)$ to an orthonormal basis. Show that the last two vectors of every such extension span the same plane, and describe that plane.

18. • Let $x = (1, 2, 2)$ and $y = (2, 0, 1)$ in $\R^3$ with the dot product. Compute the Gram matrix of $x, y$ and its determinant, and compare with the squared length of the cross product $x \times y$.

19. • On the space of real polynomials of degree at most $2$ with the inner product of Exercise 3, find the polynomials $u$ and $w$ with $p(1) = \langle p, u\rangle$ and $p'(0) = \langle p, w\rangle$ for every $p$.

20. • On $\R^2$ with the inner product (a) of Exercise 1, find the vector $u$ with $x_1 + x_2 = \langle x, u\rangle$ for all $x$. Explain why the answer is not $(1, 1)$.

21. ★ For $1 \le p < \infty$, let $\norm{x}_p = (\abs{x_1}^p + \abs{x_2}^p)^{1/p}$ on $\R^2$. Find all $p$ for which $\norm{\cdot}_p$ is induced by an inner product.

22. ★ Let $V$ and $W$ be real inner product spaces, and let $T \colon V \to W$ be a map, not assumed linear, with $T(0) = 0$ and $\norm{T x - T y} = \norm{x - y}$ for all $x, y$. Prove that $\langle T x, T y\rangle = \langle x, y\rangle$ for all $x, y$, and then that $T$ is linear.

23. ★ Let $T$ be a linear map from an inner product space $V$ to itself with $\langle T x, x\rangle = 0$ for every $x \in V$. Show that $T = 0$ if $V$ is complex, and give a nonzero example with $V = \R^2$ and the dot product.

24. ★ Let $v_1, \dots, v_k$ be vectors in an inner product space, with Gram matrix $G$. Prove that $\det G \le \norm{v_1}^2 \cdots \norm{v_k}^2$, and find exactly when equality holds.

25. ★ Prove that for every inner product on $\R^n$ there is an invertible $n \times n$ matrix $P$ with $\langle x, y\rangle = (Px) \cdot (Py)$ for all $x, y$. Find one such $P$ for the inner product (a) of Exercise 1.
