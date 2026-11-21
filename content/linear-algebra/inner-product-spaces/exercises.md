1. ◦ Which of these formulas are [inner products](/0NB0AWGJBW/) on $\R^2$? (a) $x_1 y_1 + 3x_2 y_2$. (b) $x_1 y_1 - x_2 y_2$. (c) $x_1 y_2 + x_2 y_1$. (d) $2x_1 y_1 + x_1 y_2 + x_2 y_1 + x_2 y_2$. For each one that is not, name an axiom that fails and a vector that shows it.

2. ◦ In $\C^2$ with the [standard inner product](/TFZ8DYVJ1J/), let $x = (2, 1 + i)$ and $y = (1 + i, i)$. Compute $\ip{x}{y}$, $\ip{y}{x}$, $\norm{x}$, $\norm{y}$, $\ip{ix}{y}$ and $\ip{x}{iy}$.

3. ◦ For the taxicab norm $\abs{x_1} + \abs{x_2}$ on $\R^2$, compute both sides of the [parallelogram law](/026HPGYGS4/) for $x = (1, 2)$ and $y = (2, -1)$. What do you conclude?

4. ◦ On the real polynomials of degree at most $2$ with $\ip{p}{q} = \int_0^1 p(t) q(t)\, dt$, compute $\ip{1}{t}$, $\norm{1}$, $\norm{t}$ and $\norm{1 + t}$. Check the [Cauchy-Schwarz inequality](/0RFWW56Y22/) and the [triangle inequality](/SRN4T2G6AM/) for $1$ and $t$.

5. ◦ In $\C^2$, let $x = (1, i)$ and $y = (i, 0)$. Show that $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ but $x$ and $y$ are not [orthogonal](/0Y2X7P2WB7/). Then compute $\norm{x + iy}^2$, and explain how it detects the failure.

6. ◦ Check that $\frac{1}{\sqrt3}(1, 1, 1)$, $\frac{1}{\sqrt2}(1, -1, 0)$ and $\frac{1}{\sqrt6}(1, 1, -2)$ form an [orthonormal basis](/0S9GGTR0EX/) of $\R^3$. Find the coordinates of $v = (1, 2, 3)$ in it with the [coordinate formula](/09DZ8CD1AK/), and check [Parseval's identity](/047RFCNVSK/) for $v$.

7. ◦ In $\R^3$ let $e_1 = (1, 0, 0)$, $e_2 = \frac{1}{\sqrt2}(0, 1, 1)$ and $x = (1, 2, 3)$. Compute both sides of [Bessel's inequality](/0RBT5PB74K/), the vector $x - \ip{x}{e_1} e_1 - \ip{x}{e_2} e_2$, and its squared norm. How are the three numbers related?

8. ◦ Which of these matrices are [Gram matrices](/00SPJSDT3Z/) of some family of vectors? (a) $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. (b) $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$. (c) $\begin{pmatrix} 1 & 1 + i \\ 1 - i & 3 \end{pmatrix}$. (d) $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.

9. ◦ A student runs the [Gram-Schmidt process](/0VT6P0GNQR/) in $\C^2$ on $v_1 = (i, 1)$, $v_2 = (1, 0)$ and writes $u_2 = v_2 - \frac{\ip{u_1}{v_2}}{\ip{u_1}{u_1}} u_1 = \left(\frac32, -\frac{i}{2}\right)$. Find the error, give the correct $u_2$, and check that it is orthogonal to $u_1$ while the student's vector is not.

10. ◦ On $\C^2$ with the standard inner product, find the vector $u$ with $f(z) = \ip{z}{u}$ for the linear form $f(z) = (1 + i) z_1 + 2 z_2$. Then find the vector that represents $if$, and compare it with $iu$, as in the [Riesz representation theorem](/04GYPXDXNH/).

11. • Show that $\ip{x}{y} = x_1 y_1 - x_1 y_2 - x_2 y_1 + 3 x_2 y_2$ is an inner product on $\R^2$. Then find an orthonormal basis for it whose first vector is $(1, 0)$.

12. • (a) Compute $\ip{x}{y}$ for $x = (1, i)$ and $y = (1, 1)$ in $\C^2$ from the four norms in the complex [polarization identity](/05FKHRT0B4/), and check the result directly. (b) Let $A$ be a real $2 \times 2$ matrix with $\norm{Ae_1} = \norm{Ae_2} = 1$ and $\norm{A(e_1 + e_2)} = \sqrt2$. Show that $A$ is orthogonal. (c) Show that (b) fails for complex matrices: give a complex $2 \times 2$ matrix with the same three norms that is not unitary.

13. • Use the Cauchy-Schwarz inequality to show: (a) $(a + 2b + 3c)^2 \le 14(a^2 + b^2 + c^2)$ for real $a, b, c$; (b) $(x_1 + \dots + x_n)\left(\frac{1}{x_1} + \dots + \frac{1}{x_n}\right) \ge n^2$ for positive reals $x_i$. When does equality hold in each?

14. • Show that $\norm{x + y}\,\norm{x - y} \le \norm{x}^2 + \norm{y}^2$ in every inner product space. When does equality hold?

15. • Let $x, y$ be vectors of a real inner product space with $\norm{x} = \norm{y}$. Show that $x + y \perp x - y$ (the diagonals of a rhombus are perpendicular). Over $\C$, show that $\ip{x + y}{x - y} = 2i \operatorname{Im}\ip{y}{x}$ when $\norm{x} = \norm{y}$, and give an example where the diagonals are not orthogonal.

16. • Show that the $p$-norm $(\abs{x_1}^p + \abs{x_2}^p)^{1/p}$ on $\R^2$, for $1 \le p < \infty$, satisfies the parallelogram law only for $p = 2$. Which of these norms come from an inner product? Answer the same question for the maximum norm.

17. • On the real polynomials of degree at most $2$, let $\ip{p}{q} = p(0)q(0) + p(1)q(1) + p(2)q(2)$. Show that this is an inner product, and that the same formula is not an inner product on the polynomials of degree at most $3$. Apply the Gram-Schmidt process to $1, t, t^2$.

18. • Apply the Gram-Schmidt process in $\C^3$ to $v_1 = (1, i, 0)$ and $v_2 = (1, 1, 1)$. Check that the result is orthonormal.

19. • Find an orthonormal basis of $\R^3$ whose first vector is $\frac17(2, 3, 6)$, as the [existence theorem](/0Y85GYEGSF/) promises. Give the coordinates of $(1, 0, 0)$ in your basis.

20. • Use Gram determinants to compute (a) the area of the triangle in $\R^3$ with vertices $0$, $(1, 2, 3)$ and $(3, 2, 1)$, and (b) the $3$-dimensional volume of the parallelepiped in $\R^4$ spanned by $(1, 1, 0, 0)$, $(0, 1, 1, 0)$ and $(0, 0, 1, 1)$. Check (a) with the [cross product](/0N5N15HWZ7/).

21. • Let $A$ be a real $m \times n$ matrix. Show that $\ip{x}{y} = (Ax) \cdot (Ay)$ is an inner product on $\R^n$ if and only if the columns of $A$ are independent. Show also that the Gram matrix $A^{\mathsf T} A$ of the columns has the same kernel, and so the same rank, as $A$.

22. • On the real polynomials of degree at most $2$ with $\ip{p}{q} = \int_0^1 p(t) q(t)\, dt$, find the polynomial $u$ with $p(0) = \ip{p}{u}$ for every $p$. Why does the same form have no representative on the space of all real polynomials?

23. • On the real $n \times n$ matrices, let $\ip{A}{B} = \tr(B^{\mathsf T} A)$. Show that every symmetric matrix is orthogonal to every skew-symmetric matrix. Conclude that the space of all real $n \times n$ matrices is the direct sum of the symmetric and the skew-symmetric matrices.

24. ★ Prove Lagrange's identity $\left(\sum_k a_k^2\right)\left(\sum_k b_k^2\right) - \left(\sum_k a_k b_k\right)^2 = \sum_{j < k} (a_j b_k - a_k b_j)^2$ for real numbers, and use it to prove the Cauchy-Schwarz inequality for the dot product on $\R^n$, with its equality case.

25. ★ Let $\norm{\cdot}$ be a norm on a real vector space that satisfies the parallelogram law, and put $\ip{x}{y} = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right)$. Prove that this is an inner product whose norm is $\norm{\cdot}$. Prove symmetry and $\ip{x}{x} = \norm{x}^2$ first, then additivity in the first slot, then $\ip{qx}{y} = q\ip{x}{y}$ for rational $q$, and finish with continuity. This is the real case of the [Jordan-von Neumann theorem](/46WGVM5VS6/).

26. ★ Prove Hadamard's inequality: for vectors $v_1, \dots, v_k$ in an inner product space, $\det G(v_1, \dots, v_k) \le \norm{v_1}^2 \cdots \norm{v_k}^2$, with equality exactly when the family is orthogonal or contains $0$. Deduce that $\abs{\det A}$ is at most the product of the lengths of the columns of a square real matrix $A$.

27. ★ Let $M = \begin{pmatrix} a & b \\ \overline{b} & d \end{pmatrix}$ with $a, d$ real and $b \in \C$, and put $h(x, y) = y^* M x$ on $\C^2$. Show that $h$ is an inner product if and only if $a > 0$ and $ad - \abs{b}^2 > 0$.

28. ★ Let $V$ be a finite-dimensional inner product space, and for $f \in V^*$ let $u_f$ be its Riesz representative. Show that $\ip{f}{g} = \ip{u_g}{u_f}$ is an inner product on $V^*$, that $\max_{\norm{v} = 1} \abs{f(v)} = \norm{u_f}$, and that the dual basis of an orthonormal basis of $V$ is an orthonormal basis of $V^*$.
