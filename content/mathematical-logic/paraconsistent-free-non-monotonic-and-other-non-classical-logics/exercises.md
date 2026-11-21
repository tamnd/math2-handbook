1. ◦ A logic is paraconsistent when $A, \neg A \vDash B$ fails for some $A$ and $B$, and paracomplete when $\vDash A \lor \neg A$ fails for some $A$. For each of [K3](/SZHA10A9X7/), [LP](/BXJZG67PX3/), [FDE](/KXTP4P3GHT/), [intuitionistic logic](/Q11N8X99FK/) and [discussive logic](/489SFB5NX2/) $D_2$, say whether it is paraconsistent and whether it is paracomplete.

2. ◦ The Lewis argument for [explosion](/TTKZGJEEK7/) goes from $A$ to $A \lor B$ by disjunction introduction, and then from $A \lor B$ and $\neg A$ to $B$ by disjunctive syllogism. For each of K3, LP and $D_2$, say which of the two steps is not valid, if any.

3. ◦ Let $v(p) = \mathsf{B}$, the middle value, and use the strong Kleene tables with $A \supset B := \neg A \lor B$. Compute $v(p \supset p)$ and $v(\neg(p \land \neg p))$. Is either value designated in K3? In LP? What does this show about $p \supset p$ in K3?

4. ◦ Let $v(p) = \mathsf{T}$ and let $v(q)$ be undefined. Compute the values of $p \lor q$, $p \land q$ and $\neg p \lor q$ under the strong Kleene tables and under the [weak Kleene](/BCK5QXQXA6/) tables. Then do the same with $v(p) = \mathsf{F}$.

5. ◦ Which of the following are theorems of positive [free logic](/Y0CNMRXHVJ/)? (a) $\forall x\, Px \to Pt$; (b) $\forall x\, Px \to (E!t \to Pt)$; (c) $Pt \to \exists x\, Px$; (d) $t = t$; (e) $E!t \to \exists x\, (x = t)$.

6. ◦ Read $b$ as "bird", $f$ as "flies", $w$ as "has wings", $s$ as "swims" and $g$ as "penguin". Name the rule used in each step, and say whether it belongs to [system $\mathbf{P}$](/G4QC9MKFAG/). (a) From $b \mathrel{|\!\sim} f$ and $b \mathrel{|\!\sim} w$ infer $b \land w \mathrel{|\!\sim} f$. (b) From $b \mathrel{|\!\sim} f$ infer $b \mathrel{|\!\sim} f \lor s$. (c) From $b \mathrel{|\!\sim} f$ infer $b \land g \mathrel{|\!\sim} f$.

7. ◦ In the lattice of subspaces of $\R^3$, let $a$ be the $x$-axis and $b$ the $xy$-plane, so $a \leq b$. Compute $a^\perp$, $a^\perp \wedge b$ and $a \vee (a^\perp \wedge b)$, and check that the [orthomodular law](/6FPKEFX0X4/) holds for this pair.

8. ◦ In [Montague grammar](/FT512R206H/), "John" lifts to $\lambda P\, P(\mathbf{john})$, "a" translates to $\lambda P \lambda Q\, \exists y\, (P(y) \land Q(y))$, and a transitive verb $\tau$ with a noun phrase $\eta$ gives the verb phrase $\lambda x\, \eta'(\lambda y\, \tau'(x, y))$. Translate "John loves a woman" step by step, and reduce the result to a first-order formula.

9. ◦ In [computability logic](/C7CV0XMSTT/), let $h(x)$ be the halting predicate. Which of these problems are computable? (a) $\sqcap x \sqcup y\, (y = x^2)$; (b) $\sqcup y \sqcap x\, (x = y)$; (c) $\sqcap x \sqcup y\, (h(x) \leftrightarrow y = 1)$; (d) $\sqcap x\, \exists y\, (h(x) \leftrightarrow y = 1)$.

10. • Show that $p \land \neg p \vDash q \lor \neg q$ holds in LP and holds in K3. Then give a four-valued valuation that shows it fails in FDE. What does this say about FDE consequence compared with the inferences that are valid in both LP and K3?

11. • Show that $((p \supset q) \land p) \supset q$ is an LP tautology, using the [theorem on LP tautologies](/DHRMY6TC52/). Compute its value when $v(p) = \mathsf{B}$ and $v(q) = \mathsf{F}$. Explain why this tautology does not make modus ponens a valid rule of LP.

12. • [Da Costa's](/KN2VBRQB3Q/) $C_1$ contains positive classical logic, so $A \vdash A \lor B$ holds in it. (a) Show that disjunctive syllogism $A \lor B, \neg A \vdash B$ cannot hold in $C_1$ for all $A$ and $B$. (b) Show that $A^\circ, A \lor B, \neg A \vdash B$ does hold, using gentle explosion and proof by cases.

13. • Recall that $\Gamma \vDash_{D_2} B$ when $\set{\Diamond\gamma : \gamma \in \Gamma} \vDash_{\mathsf{S5}} \Diamond B$. Give an S5 model that shows $p, \neg p \lor q \nvDash_{D_2} q$. Then show that $p \land (\neg p \lor q) \vDash_{D_2} q$.

14. • Use the [adaptive logic](/X8RW5F4261/) with lower limit CLuN, abnormalities $A \land \neg A$ and the reliability strategy. Let $\Gamma = \set{p, \neg p, \neg p \lor q, r, \neg r \lor s}$. Find the minimal Dab-consequences of $\Gamma$, and decide whether $q$ and $s$ are finally derivable.

15. • Give a dual-domain model of positive free logic in which $Pt \to \exists x\, Px$ is false. Then show that $Pt \to \exists x\, Px$ is valid in negative free logic.

16. • Show that the [multiple-conclusion](/3AJTDAP93H/) LP sequent $p, \neg p \lor q \vDash q, \, p \land \neg p$ is valid, although $p, \neg p \lor q \vDash q$ is not. Read the result as a statement about disjunctive syllogism.

17. • Read $\sim$ as classical negation and $\to$ as the material conditional. Show directly that adding Aristotle's thesis $\sim(\sim A \to A)$ as an axiom schema to classical propositional logic makes every formula provable. What does this say about [connexive logic](/NQFYY76BSM/)?

18. • Find all [extensions](/44Z7CFSJAE/) of the [default theory](/K4AYFFKY2D/) with $W = \emptyset$ and $D = \set{\frac{\top : p}{q}, \frac{\top : \neg q}{r}}$. Check each candidate set of generating defaults.

19. • Find all extensions of the default theory with $W = \set{p \lor q}$ and $D = \set{\frac{\top : \neg p}{\neg p}, \frac{\top : \neg q}{\neg q}}$. Is $\neg(p \land q)$ a skeptical consequence? Is $p$ a skeptical or a credulous consequence?

20. • A ranked [preferential model](/7J659YV5WA/) has three states: $c$ with $\neg b, \neg f$; $a$ with $b, f$; and $d$ with $b, \neg f$. The order is $c \prec a \prec d$ (so also $c \prec d$). Decide $\top \mathrel{|\!\sim} \neg f$, $b \mathrel{|\!\sim} f$ and $b \mathrel{|\!\sim} \neg f$. Which rule of classical consequence fails here?

21. • In the fusion $\mathsf{K} \otimes \mathsf{T}$ of [combining logics](/HP1N0MBTDJ/), $\Box_1$ obeys $\mathsf{K}$ and $\Box_2$ obeys $\mathsf{T}$, with no interaction axioms. For each formula, give a derivation or a Kripke countermodel: (a) $\Box_2 \Box_1 p \to \Box_1 p$; (b) $\Box_1 \Box_2 p \to \Box_2 p$; (c) $\Box_1 \Box_2 p \to \Box_1 p$.

22. • Write the two Montague readings of "A man loves every woman", one with "a man" taking wide scope and one with "every woman" taking wide scope. Show that one reading entails the other, and give a finite model in which the weaker reading is true and the stronger one false.

23. ★ On $\set{\mathsf{T}, \mathsf{B}, \mathsf{F}}$, put $x \sqsubseteq y$ when $x = y$ or $y = \mathsf{B}$. Prove by induction on formulas in $\neg, \land, \lor$ that if $v(p) \sqsubseteq w(p)$ for every atom $p$, then $v(\varphi) \sqsubseteq w(\varphi)$ under the strong Kleene tables. Deduce that every classical tautology is an LP tautology.

24. ★ In the adaptive logic of Exercise 14, let $\Gamma = \set{\neg p, \neg q, p \lor q, p \lor r, q \lor r}$. Show that $r$ is a consequence under the minimal abnormality strategy but not under the reliability strategy.

25. ★ Prove that a default theory $(W, D)$ has an inconsistent extension if and only if $W$ is inconsistent.

26. ★ Prove that Cautious Monotony holds in every finite preferential model: if $\alpha \mathrel{|\!\sim} \beta$ and $\alpha \mathrel{|\!\sim} \gamma$, then $\alpha \land \beta \mathrel{|\!\sim} \gamma$.

27. ★ Show that there is no map $h$ from the lattice of subspaces of $\R^3$ to $\set{0, 1}$ with $h(0) = 0$, $h(\R^3) = 1$, $h(M \wedge N) = \min(h(M), h(N))$ and $h(M \vee N) = \max(h(M), h(N))$. Use lines inside one plane, and then two planes.
