## What to remember

- **Explosion and the Lewis argument:** a consequence relation with disjunction introduction, [disjunctive syllogism](/6EFJF9NAYX/) and transitivity satisfies $\set{A, \neg A} \vdash B$. A paraconsistent logic must drop one of the three rules, and most drop disjunctive syllogism. [Dialetheism](/3P0FM0AQF3/), the view that some contradictions are true, is a separate claim.
- **LP and K3** share the strong Kleene tables on $\mathsf{T}, \mathsf{B}, \mathsf{F}$. LP designates $\mathsf{T}$ and $\mathsf{B}$, and K3 designates only $\mathsf{T}$. The LP tautologies are exactly the classical ones, K3 has none, and $\gamma \vDash_{\mathrm{LP}} \varphi$ if and only if $\neg\varphi \vDash_{\mathrm{K3}} \neg\gamma$. In LP, modus ponens for $\supset$ and disjunctive syllogism fail.
- **Da Costa's $C_1$** keeps positive classical logic, excluded middle and $\neg\neg A \to A$, but not $\neg(A \land \neg A)$. With $A^\circ := \neg(A \land \neg A)$, gentle explosion $A^\circ, A, \neg A \vdash B$ holds. Adding $A^\circ$ for every $A$ gives classical logic.
- **Discussive logic $D_2$:** $\Gamma \vDash_{D_2} B$ when $\set{\Diamond\gamma : \gamma \in \Gamma} \vDash_{\mathsf{S5}} \Diamond B$. So $A, \neg A \nvDash_{D_2} A \land \neg A$, while every classical inference from a single premise stays valid.
- **Free logic** restricts specification to $\forall x\, A \to (E!t \to A[t/x])$, and existential generalization to $A[t/x] \land E!t \to \exists x\, A$. Allowing an empty domain is a different change, called inclusive logic.
- **Connexive logic** proves Aristotle's theses $\sim(\sim A \to A)$ and $\sim(A \to \sim A)$, and Boethius' theses $(A \to B) \to \sim(A \to \sim B)$ and $(A \to \sim B) \to \sim(A \to B)$. Classical logic is Post-complete, so a non-trivial connexive logic in the classical language must lose some classical theorems.
- **Default logic:** an extension of $(W, D)$ is a set $E$ with $E = \Gamma_{(W,D)}(E)$. A theory can have no extension, one or several, and every normal theory has at least one. Skeptical consequence uses all extensions, credulous consequence some.
- **System $\mathbf{P}$** has Reflexivity, Left Logical Equivalence, Right Weakening, Cut, Or and Cautious Monotony. It is sound and complete for preferential models, where $\alpha \mathrel{|\!\sim} \beta$ means that $\beta$ holds in the most normal $\alpha$-states. Rational relations correspond to ranked models.
- **Beyond these**, the closed subspaces of a Hilbert space form an orthomodular lattice that is not distributive when $\dim H \geq 2$. In computability logic, $P \vee \neg P$ is valid but $P \sqcup \neg P$ is not, because the choice disjunction requires the machine to commit to one side.

## Some logics compared

| Logic | $A, \neg A \vDash B$ | $\vDash A \lor \neg A$ | $A \lor B, \neg A \vDash B$ | $A, B \vDash A \land B$ | Semantics |
|---|---|---|---|---|---|
| Classical | yes | yes | yes | yes | two values |
| [Intuitionistic](/Q11N8X99FK/) | yes | no | yes | yes | Kripke models |
| [K3](/SZHA10A9X7/) | yes | no | yes | yes | three values, $\mathsf{T}$ designated |
| [LP](/BXJZG67PX3/) | no | yes | no | yes | three values, $\mathsf{T}$ and $\mathsf{B}$ designated |
| [FDE](/KXTP4P3GHT/) | no | no | no | yes | four values, $\mathsf{T}$ and $\mathsf{B}$ designated |
| [$C_1$](/KN2VBRQB3Q/) | no | yes | no | yes | bivaluations; no finite characteristic matrix |
| [$D_2$](/489SFB5NX2/) | no | yes | no | no | translation $A \mapsto \Diamond A$ into S5 |

: Seven propositional logics and four classical laws. A logic with disjunction introduction and transitivity that keeps explosion can keep disjunctive syllogism, but a logic that drops explosion must also drop disjunctive syllogism. Only $D_2$ also gives up adjunction.

## Common errors

- **Reading "non-classical" as "weaker".** Extensions such as modal logics prove more than classical logic, and connexive logics prove formulas that classical logic does not prove.
- **Deciding paraconsistency from the tables alone.** LP and K3 have the same tables, and only the choice of designated values makes LP paraconsistent and K3 explosive.
- **Confusing a theorem with a rule.** In LP the formula $(p \land (p \supset q)) \supset q$ is a tautology, but the rule from $p$ and $p \supset q$ to $q$ fails.
- **Testing a default against the facts only.** The justification of a default is checked against the final extension $E$, not against $W$.
- **Treating $\mathrel{|\!\sim}$ as monotonic.** System $\mathbf{P}$ has Cautious Monotony only: from $\alpha \mathrel{|\!\sim} \beta$ and $\alpha \mathrel{|\!\sim} \gamma$ it gives $\alpha \land \beta \mathrel{|\!\sim} \gamma$, but $\alpha \mathrel{|\!\sim} \gamma$ alone does not give $\alpha \land \beta \mathrel{|\!\sim} \gamma$.
- **Joining two axiom systems and expecting a conservative result.** Two implications that both satisfy the deduction theorem collapse into one. This is how fibring intuitionistic and classical logic gives Peirce's law for the intuitionistic implication.
