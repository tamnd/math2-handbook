1. ◦ Show that $\forall x\, \exists y\, R(x,y) \to \exists y\, R(y,y)$ is not valid. What does the [soundness theorem](/AVD7T7J063/) then tell you about it?

2. ◦ Use soundness to show that the axioms of the [theory of groups](/RX9MB386C5/) derive neither $\exists x\, \neg(x = e)$ nor its negation.

3. ◦ Let $\Delta$ be a maximal consistent set of sentences, as in [Lindenbaum's lemma](/SC0BSJ3GT6/). Which of these statements hold for every such $\Delta$? (a) If $\sigma \vee \tau \in \Delta$, then $\sigma \in \Delta$ or $\tau \in \Delta$. (b) If $\Delta \vdash \sigma$, then $\sigma \in \Delta$. (c) If $\sigma \notin \Delta$, then $\Delta \cup \{\sigma\}$ is inconsistent. (d) If $\exists x\, \varphi \in \Delta$, then $\varphi(c) \in \Delta$ for some constant $c$.

4. ◦ What bound on the size of the model does the [Henkin construction](/RY8KRKR097/) give when $L$ has (a) three symbols, (b) $\aleph_1$ constant symbols? Can the model it builds be smaller than the bound? Give an example.

5. ◦ Write the sentence $\lambda_3$, which is true exactly in the structures with at least three elements. Then give a set of sentences whose models are exactly the infinite structures.

6. ◦ For each set, say whether every finite subset has a model and whether the whole set has one. (a) $\set{\lambda_n : n \ge 2} \cup \set{\forall x\, \forall y\, (x = y)}$. (b) $\set{c_i \neq c_j : i < j}$, with constants $c_0, c_1, \ldots$. (c) $\set{\neg \lambda_n : n \ge 2}$. (d) $\set{\lambda_n : n \ge 2} \cup \set{\forall x\, \forall y\, (P(x) \to P(y))}$, with $P$ unary.

7. ◦ Let $T$ be a complete, consistent, [recursively axiomatizable theory](/3ANXZC3BEG/) in a countable language. Describe an algorithm that decides, for each sentence $\sigma$, whether $T \vdash \sigma$. Where does the algorithm use completeness, and where consistency?

8. ◦ Find an interpolant, in the sense of the [Craig interpolation theorem](/E2CBFNAVZY/), for $\forall x\, (P(x) \to Q(x)) \wedge P(c) \models Q(c) \vee R(c)$.

9. ◦ In each sentence, which sense of "complete" is meant? (a) "First-order logic is complete." (b) "The theory of dense linear orders without endpoints is complete." (c) "Peano arithmetic is incomplete." State both definitions.

10. • Use soundness to show $\forall x\, (P(x) \vee Q(x)) \nvdash \forall x\, P(x) \vee \forall x\, Q(x)$.

11. • Show that the union of a chain of consistent sets of sentences is consistent. Where does the proof of Lindenbaum's lemma by Zorn's lemma use this?

12. • Let $\Delta$ be a maximal consistent set of sentences in Enderton's calculus, and for closed terms put $s \sim t$ when $(s = t) \in \Delta$. Show that $\sim$ is an equivalence relation and that $P(s) \in \Delta$ and $s \sim t$ imply $P(t) \in \Delta$.

13. • Let $\sigma$ be a sentence in the language of rings that is true in every field of characteristic $0$. Use the [compactness theorem](/1NR3HAWG9D/) to show that there is an $N$ such that $\sigma$ is true in every field of characteristic $p$ for every prime $p > N$.

14. • A graph is bipartite exactly when it has no cycle of odd length. Show that the class of bipartite graphs is elementary, but that no single sentence axiomatizes it.

15. • Show that the class of Archimedean ordered fields is not elementary. Follow the plan of the [applications of first-order compactness](/PES0S9XQZ5/).

16. • Show that no set of first-order sentences in the language $\set{E}$ of graphs has as its models exactly the graphs in which every vertex has finite degree.

17. • Show that $\operatorname{Th}(\N, 0, 1, +, \cdot, <)$ has a model with an element $a \neq 0$ that is divisible by every standard positive integer $n$.

18. • Let $\sigma_0, \sigma_1, \sigma_2, \ldots$ be a computable list of the sentences of a theory $T$. Let $A$ consist of the sentences $\sigma_n \wedge \sigma_n \wedge \cdots \wedge \sigma_n$ with $n + 1$ conjuncts. Show that $A$ is decidable and has the same theorems as $T$, as in [Craig's theorem on axiomatizability](/6AN62NQ8AN/).

19. • Find a Herbrand disjunction, as in [Herbrand's theorem](/VZ21F10WRS/), for the valid sentence $\exists x\, (\neg P(x) \vee P(f(f(x))))$ in a language with one constant $c$. Show that no single ground instance is a tautology.

20. • Find a Craig interpolant for $\forall x\, (P(x) \to Q(x)) \wedge P(c) \models \exists x\, Q(x)$. Why is $Q(c)$ not one? Is your interpolant also a Lyndon interpolant?

21. • Show that [Robinson's joint consistency theorem](/R6AN38DNBD/) in its classical form needs $T$ to be complete. Take $L_0 = \set{<}$ and $T$ the theory of linear orders.

22. ★ An abelian group is divisible when for every $x$ and every $n \ge 1$ there is $y$ with $ny = x$. Show that the divisible abelian groups form an elementary class that is not axiomatized by any single sentence.

23. ★ The sentence $\exists x\, (x = x)$ is valid. Show that no disjunction of its ground instances is a tautology, so Herbrand's theorem fails with equality as stated. How must the theorem be changed to cover languages with equality?

24. ★ A sentence $\varphi$ is monotone in the unary relation symbol $P$ when, for every structure $\mathcal{M}$ and every $P' \supseteq P^{\mathcal{M}}$, $\mathcal{M} \models \varphi$ implies $(\mathcal{M}, P') \models \varphi$. Use the [Lyndon interpolation theorem](/BRDT1BT7WW/) to show that such a $\varphi$ is equivalent to a sentence in which $P$ occurs only positively.

25. ★ Show that Craig's interpolation theorem and the separation form of Robinson's joint consistency theorem imply each other. Say where you use compactness.

26. ★ Show that the theory of [dense linear orders without endpoints](/2W4S2H4VYA/) is complete and decidable. You may use Cantor's theorem that any two countable models are isomorphic.
