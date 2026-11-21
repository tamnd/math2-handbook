1. (a) $\mathsf{WKL}_0$; (b) $\mathsf{ACA}_0$; (c) $\mathsf{ATR}_0$; (d) $\Pi^1_1\text{-}\mathsf{CA}_0$; (e) $\mathsf{RCA}_0$ proves it; (f) $\mathsf{ACA}_0$; (g) $\mathsf{ACA}_0$; (h) $\mathsf{WKL}_0$.

3. (a) and (c) are Turing ideals. The low sets are not closed under join, since $\emptyset'$ is the join of two low sets. The c.e. sets are not closed downwards, since the complement of the halting set is computable from it. The finite sets miss the infinite computable sets.

5. (a) True. (b) False, by Seetapun and Slaman. (c) False, by Liu. (d) False: $\mathsf{WKL}_0$ has an $\omega$-model of low sets, and Jockusch built a computable colouring with no $\Delta^0_2$ homogeneous set. (e) True.

7. $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$: $\omega^\omega$ and $\mathrm{I}\Sigma_1$. $\mathsf{ACA}_0$: $\varepsilon_0$ and PA. $\mathsf{ATR}_0$: $\Gamma_0$, and it proves the consistency of PA. $\Pi^1_1\text{-}\mathsf{CA}_0$: $\psi_0(\Omega_\omega)$.

9. Keep a string $\sigma$ at length $s$ unless $\varphi_{e, s}(e)$ converges to $i \in \set{0, 1}$ with $\sigma(e) = i$, for some $e < \abs\sigma$. A path is a set that separates the two c.e. sets, and a computable separating set $\varphi_e$ would give a contradiction at $e$.

10. By the equivalence of $\mathsf{ACA}_0$ with the [existence of ranges of injections](/3MQ39PRCYJ/), it suffices to decide $k \in \mathrm{ran}(f)$. If $L$ is the limit and $L - a_n < 2^{-k}$, then $f(m) = k$ for no $m > n$, so $k \in \mathrm{ran}(f)$ if and only if $k \in \set{f(0), \dots, f(n)}$.

12. The removed strings form an open set of measure at most $\sum_e 2^{-(e + 3)} = 1/4$. A computable path $\varphi_e$ extends $\varphi_e \restriction (e + 3)$ and is removed.

14. $\mathsf{WKL}_0$ is $\Pi^0_2$-conservative over PRA and $\mathrm{Con}(\mathsf{PRA})$ is $\Pi^0_1$. A proof in $\mathsf{WKL}_0$ would give one in PRA, against the second incompleteness theorem.

16. The tree of finite binary strings that code an assignment of truth values to the first sentences, with no proof of inconsistency below the length of the string, is computable and infinite. A path computes a completion.

17. For one direction, build the tree of strings $\sigma$ that respect the witnesses of $\varphi_0$ and $\varphi_1$ found below $\abs\sigma$; a path separates. For the other, separate "$\sigma 0$ dies before $\sigma 1$" from "$\sigma 1$ dies before $\sigma 0$", and follow the separating set from the root.

18. Every Turing ideal contains the computable sets. For a noncomputable $Z$, iterate the cone-avoiding basis theorem: each infinite tree computable from the current set has a path that does not compute $Z$ together with it. The union of the resulting ideals is an $\omega$-model of $\mathsf{WKL}_0$ without $Z$.

19. Let $R_x = \set{y : c(x, y) = 1}$ and take an infinite set $Y$ cohesive for $(R_x)$. Then $c$ restricted to pairs from $Y$ is stable. Apply $\mathsf{SRT}^2_2$ to the colouring transported along the increasing enumeration of $Y$.

20. A formula with set parameters from $\mathrm{Def}(M)$ becomes a first-order formula over $M$ when each parameter is replaced by its definition. So arithmetical comprehension and set induction hold. Every model of PA expands to a model of $\mathsf{ACA}_0$, and completeness gives conservation.
