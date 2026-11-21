1. ◦ Let $W = \set{1, 2, 3, 4}$, $R = \set{(1,2), (1,3), (2,4), (3,4), (4,3)}$ and $V(p) = \set{2, 3}$. Find the set of worlds of this [Kripke model](/NGHWZ9Y7ZV/) at which each of $\square p$, $\lozenge p$, $\square\lozenge p$ and $\lozenge\square p$ is true. Is $\square\lozenge p \to \lozenge\square p$ true in the model? Is it valid on the frame?

2. ◦ Which of the following sets of formulas are modal logics, and which of those are [normal](/D1TJYZZDCY/)? (a) The set of all formulas. (b) The set of substitution instances of propositional tautologies. (c) The set of formulas valid on the frame with one world and empty relation. (d) The set of tautologies together with the single formula $\square p$.

3. ◦ On $W = \set{1, 2, 3}$ take $R_1 = \set{(1,2), (2,3), (3,3)}$, $R_2 = \set{(1,1), (2,2), (3,3), (1,2), (2,1)}$ and $R_3 = \set{(1,2), (1,3), (2,2), (2,3), (3,2), (3,3)}$. For each frame, decide which of the [axioms](/FDFQFWPM4X/) $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$ are valid on it.

4. ◦ Find a frame for [$\mathsf{K4}$](/XVYMEZKH7R/) with as few worlds as possible on which $\square\square p \to \square p$ fails, and show that no smaller frame will do.

5. ◦ Which of these are theorems of $\mathsf{K}$? Give a derivation sketch or a countermodel for each. (a) $\lozenge(p \vee q) \to \lozenge p \vee \lozenge q$. (b) $\lozenge p \wedge \lozenge q \to \lozenge(p \wedge q)$. (c) $\square p \wedge \lozenge q \to \lozenge(p \wedge q)$. (d) $\square\lozenge\top$. (e) $\square(p \to q) \to (\lozenge p \to \lozenge q)$.

6. ◦ Let $M$ be the model on $\N$ with $n R m$ iff $m = n + 1$ and $V(p) = \set{n : 3 \text{ divides } n}$, and let $\Sigma = \set{p, \lozenge p, \lozenge\lozenge p}$. Find the classes of worlds that agree on $\Sigma$ and the smallest [filtration](/6ZZSHAKG5F/) of $M$ through $\Sigma$. Compare its size with the bound $2^{\abs{\Sigma}}$.

7. ◦ Write the [standard translation](/YW6YGBMVQY/) $\mathrm{ST}_x$ of $\lozenge(p \wedge \square q)$ and of $\square p \to \lozenge p$, using only the variables $x$ and $y$.

8. ◦ On $W = \set{1, 2, 3}$ let $N(w) = \set{X \subseteq W : X \cap \set{1, 2} \neq \emptyset}$ for every $w$. Which of the conditions (m), (c) and (n) of [neighbourhood semantics](/CN7HK9K1B6/) hold? Is the frame augmented? Answer the same questions for $N'(w) = \set{X \subseteq W : 1 \in X}$, and find a Kripke frame equivalent to the second.

9. ◦ Reduce $\lozenge\square\lozenge\square\lozenge p$ to a shortest equivalent modality in [$\mathsf{S4}$](/N60RVXSA5W/) and in [$\mathsf{S5}$](/VC3A2VWXND/). Give a two-world $\mathsf{S4}$-model showing that the $\mathsf{S4}$ answer is not equivalent to $\lozenge p$.

10. • Show that $\mathsf{D} = \mathsf{K} + \lozenge\top$: the axiom $\square p \to \lozenge p$ and the formula $\lozenge\top$ derive each other over $\mathsf{K}$.

11. • Prove that $\mathrm{D}$ is valid on a frame if and only if the frame is serial, and that $\mathrm{5}$ is valid if and only if the frame is Euclidean.

12. • Show that $\lozenge p \to \square p$ is valid on a frame if and only if every world has at most one successor.

13. • Show that $\square(\square p \to p)$ is valid on a frame if and only if $w R v$ implies $v R v$. Deduce that it is a theorem of $\mathsf{T}$, and show that it is not a theorem of $\mathsf{K4}$.

14. • Show that a symmetric transitive relation is Euclidean. Use the [canonical model](/TVE4F04KME/) to deduce that $\mathrm{5}$ is a theorem of $\mathsf{KB4}$, and give a frame showing that $\mathrm{B}$ is not a theorem of $\mathsf{K45}$.

15. • Let $\Lambda$ be a normal logic with canonical relation $R^\Lambda$. Prove that $R^\Lambda$ is transitive if $\mathrm{4} \in \Lambda$ and symmetric if $\mathrm{B} \in \Lambda$.

16. • Let $\Lambda = \mathsf{K} + (\square p \leftrightarrow p)$. Show that the canonical relation of $\Lambda$ is the identity, and deduce that $\Lambda$ is the logic of the frame with one reflexive world.

17. • Show that every filtration of a serial model is serial and that the smallest filtration of a symmetric model is symmetric. Give a symmetric model and a set $\Sigma$ for which the largest filtration is not symmetric.

18. • Prove that every neighbourhood frame on a finite set that satisfies (m), (c) and (n) is augmented, and so is equivalent to a Kripke frame.

19. • In [multimodal logic](/ERG3KAQWYF/) with boxes $\square_1$ and $\square_2$, show that $\square_1\square_2 p \to \square_2\square_1 p$ is valid on a frame if and only if, whenever $w R_2 v R_1 u$, there is $v'$ with $w R_1 v' R_2 u$.

20. • Write the second-order sentence that expresses the validity of $\square p \to \square\square p$ on a frame, and show directly that it is equivalent to transitivity.

21. • Translate intuitionistic formulas into the modal language by $t(p) = \square p$, $t(\varphi \vee \psi) = t(\varphi) \vee t(\psi)$ and $t(\neg\varphi) = \square\neg t(\varphi)$. Show that $t(p \vee \neg p)$ is not a theorem of $\mathsf{S4}$.

22. • Show that the formulas $\square^n p$, $n \geq 0$, are pairwise non-equivalent in $\mathsf{T}$, so that $\mathsf{T}$ has infinitely many distinct modalities.

23. ★ Show that $\mathsf{KT5}$ proves $\mathrm{B}$ and $\mathrm{4}$, and that $\mathsf{KB4}$ proves $\mathrm{5}$, by derivations in the [Hilbert system](/1MGMQX43B8/), not by frames. Deduce that $\mathsf{KT5} = \mathsf{KTB4}$, and show that a reflexive Euclidean relation is an equivalence relation.

24. ★ For each $n$, give a formula $\varphi_n$ of length polynomial in $n$ that is satisfiable in $\mathsf{K}$, but only in models with at least $2^n$ worlds. This is the first step of [Ladner's theorem](/1P2B0C7CQ4/).

25. ★ Let $\varphi$ have $m$ subformulas of the form $\square\psi$. Show that if $\varphi$ is $\mathsf{S5}$-satisfiable, it is true at a world of a universal model with at most $m + 1$ worlds. Deduce that $\mathsf{S5}$-satisfiability is in NP.

26. ★ Prove that $\mathsf{K4}$ has the [finite model property](/3NT8RCA6HE/): define the transitive filtration of a transitive model and prove that it is a filtration and is transitive.

27. ★ Show that $\mathsf{S5}$ is not the logic of any single finite frame: for each $n$, find a formula valid on every frame with at most $n$ worlds and not a theorem of $\mathsf{S5}$. Show that $\mathsf{S5}$ is nevertheless the logic of the class of finite universal frames.
