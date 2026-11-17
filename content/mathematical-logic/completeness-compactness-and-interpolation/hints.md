1. In the domain $\set{0, 1}$ with $R = \set{(0,1), (1,0)}$, every element has an $R$-successor, but no $y$ has $R(y,y)$. By soundness, the sentence is not derivable in the Hilbert calculus.

3. (a) Yes: $\sigma \vee \tau$ abbreviates $\neg\sigma \to \tau$, and if $\sigma \notin \Delta$ then $\neg\sigma \in \Delta$, so $\tau \in \Delta$ by modus ponens and deductive closure. (b) Yes. (c) Yes, because $\neg\sigma \in \Delta$. (d) No: in a language with no constant symbols at all, a maximal consistent set containing $\exists x\, P(x)$ has no instances $P(c)$. Witnesses come from the Henkin construction, not from Lindenbaum's lemma.

4. (a) At most $\aleph_0$ elements. (b) At most $\aleph_1$. Yes: the model is a quotient of the closed terms by provable equality, so for $\Gamma = \set{\forall x\, \forall y\, (x = y)}$ it has one element.

6. (a) No finite subset containing $\lambda_2$ has a model, so neither does the whole set. (b) Yes and yes: any infinite set with distinct values for the $c_i$. (c) Yes and yes: a one-element structure. (d) Yes and yes: an infinite set with $P$ empty.

8. $Q(c)$. Its symbols $Q$ and $c$ occur on both sides, the left side implies it, and it implies the right side.

12. $\Delta$ is closed under $\vdash$. Reflexivity, symmetry and transitivity of $=$ are derivable for variables, and the generalization theorem with axiom group 2 instantiates them with closed terms. For the last claim, instantiate the generalized group 6 axiom $\forall x\, \forall y\, (x = y \to (P(x) \to P(y)))$ with $s$ and $t$ and apply modus ponens twice.

14. Take the graph axioms and, for each odd $k$, a sentence saying that there are no $k$ distinct vertices forming a cycle. A single sentence $\sigma$ would follow from finitely many of these, say those with $k \le 2n + 1$, by compactness. The cycle of length $2n + 3$ satisfies them, so it satisfies $\sigma$, but it is not bipartite.

16. Suppose $\Phi$ axiomatizes the class. Add constants $c, d_0, d_1, \ldots$ and the sentences $E(c, d_i)$ and $d_i \neq d_j$ for $i < j$. A finite star satisfies each finite subset together with $\Phi$; compactness gives a model of $\Phi$ in which $c$ has infinite degree.

18. Given a sentence, there are finitely many ways to read it as a conjunction of $k$ copies of one sentence $\tau$. For each, list $\sigma_0, \ldots, \sigma_{k-1}$ and check whether $\sigma_{k-1} = \tau$. Each sentence of $A$ is equivalent to a sentence of $T$ and conversely, so they have the same theorems.

19. With $\psi(x) = \neg P(x) \vee P(f(f(x)))$, the disjunction $\psi(c) \vee \psi(f(f(c)))$ contains $P(f(f(c)))$ and $\neg P(f(f(c)))$, so it is a tautology. One instance $\psi(t)$ has two different atoms $P(t)$ and $P(f(f(t)))$, and the valuation that makes the first true and the second false falsifies it.

21. Let $\Gamma = T \cup \set{\exists x\, \forall y\, (x = y \vee x < y)}$ and $\Sigma = T \cup \set{\neg \exists x\, \forall y\, (x = y \vee x < y)}$. Both are consistent ($\N$ and $\Z$ are models), and their union is not.

22. Use the abelian group axioms and $\forall x\, \exists y\, (ny = x)$ for each $n \ge 1$. A single sentence would follow from the axioms with $n \le N$ for some $N$. The group $\Z[1/N!]$ of rationals whose denominators divide a power of $N!$ satisfies these, but $1$ has no $p$-th part in it for a prime $p > N$.

23. Every ground instance is $c = c$, which is an atomic sentence and so a propositional variable; no disjunction of copies of it is a tautology. With equality, the disjunction must be a tautological consequence of finitely many ground instances of the equality axioms, here of $c = c$ itself.

24. Let $P'$ be a new symbol. Monotonicity gives $\varphi(P) \wedge \forall x\, (P(x) \to P'(x)) \models \varphi(P')$. A Lyndon interpolant $\theta(P')$ has $P'$ only positively, since $P'$ occurs only positively on the left. Replacing $P'$ by $P$ gives $\varphi(P) \models \theta(P)$ and $\theta(P) \models \varphi(P)$.

25. From Robinson to Craig: if $\varphi \models \psi$, then $\set{\varphi}$ and $\set{\neg\psi}$ have no joint model, so some $\theta$ of the common language separates them, and $\theta$ is an interpolant. From Craig to Robinson: if $\Gamma \cup \Sigma$ has no model, compactness gives finite conjunctions $\gamma$ of $\Gamma$ and $\delta$ of $\Sigma$ with $\gamma \models \neg\delta$, and an interpolant of these separates $\Gamma$ from $\Sigma$. Only the second direction uses compactness.

26. A finite nonempty linear order has a greatest element, so the theory has only infinite models. If a sentence $\sigma$ were undecided, the theory with $\sigma$ and the theory with $\neg\sigma$ would both have countable models, by the downward [Löwenheim–Skolem theorem](/484M0TZ1S7/); these are isomorphic by Cantor's theorem, which is impossible. The theory has finitely many axioms and is complete, so it is decidable.
