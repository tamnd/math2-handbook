## What to remember

- **Tense frames.** In [temporal logic](/8XB117FKKV/), $\mathbf{G}p \to \mathbf{G}\mathbf{G}p$ is valid on a frame exactly when the order is transitive, $\mathbf{G}p \to \mathbf{F}p$ exactly when every point has a later point, and $\mathbf{F}p \to \mathbf{F}\mathbf{F}p$ exactly when the order is dense. The minimal tense logic $\mathrm{K_t}$ adds $p \to \mathbf{G}\mathbf{P}p$ and $p \to \mathbf{H}\mathbf{F}p$, which make the past the converse of the future.
- **Linear time.** [LTL](/RMJ56ZPA63/) is read on infinite words indexed by $\N$, with a reflexive until that satisfies $\varphi\,\mathbf{U}\,\psi \equiv \psi \vee (\varphi \wedge \mathbf{X}(\varphi\,\mathbf{U}\,\psi))$. Satisfiability and model checking are PSPACE-complete, and model checking takes time $\abs{M} \cdot 2^{O(\abs{\varphi})}$, through a Büchi automaton with $2^{O(\abs{\varphi})}$ states.
- **Branching time.** In [CTL](/F6JA5C5BJX/) every temporal operator is preceded by a path quantifier. $\mathbf{EG}$ is a greatest and $\mathbf{EU}$ a least fixed point, and model checking takes time $O(\abs{M} \cdot \abs{\varphi})$. [CTL*](/Y4XZ94GRXV/) allows free nesting and contains both LTL and CTL; $\mathbf{E}\,\mathbf{GF}p$ is a CTL* formula that is not expressible in CTL.
- **Knowledge.** In [epistemic logic](/EA34W4ERRE/), $\mathrm{T}$, $4$ and $5$ correspond to reflexive, transitive and Euclidean relations, and knowledge is usually $\mathrm{S5}$. [Common knowledge](/7BCMKF2P7X/) $C_G\varphi$ holds at $w$ when $\varphi$ holds at every world reachable from $w$ in one or more steps of the agents' relations. It satisfies the fixed point axiom $C_G\varphi \leftrightarrow E_G(\varphi \wedge C_G\varphi)$ and the induction rule: from $\psi \to E_G(\varphi \wedge \psi)$ infer $\psi \to C_G\varphi$.
- **Belief and announcements.** [Belief](/RTP4HTZYK3/) is $\mathrm{KD45}$: consistent and introspective, but not factive. A [public announcement](/9465T2PWZT/) of $\varphi$ deletes the worlds where $\varphi$ is false, and reduction axioms such as $[!\varphi]K_a\psi \leftrightarrow (\varphi \to K_a[!\varphi]\psi)$ translate announcement logic back into epistemic logic.
- **Obligation and conditionals.** Standard [deontic logic](/7B74J6J5JV/) is $\mathrm{KD}$, complete for serial frames, with $\mathbf{P}\varphi = \neg\mathbf{O}\neg\varphi$; it proves neither $\mathbf{O}p \to p$ nor $\mathbf{O}(\mathbf{O}p \to p)$. A [counterfactual](/ZGYG7WN7EC/) $\varphi > \psi$ is true at $w$ when no sphere around $w$ contains a $\varphi$-world, or some sphere contains one and $\varphi \to \psi$ holds throughout it. Strengthening the antecedent, transitivity and contraposition fail.
- **Explicit evidence.** The logic of proofs $\mathsf{LP}$ of [justification logic](/5HKWCXEFG1/) has application, sum, factivity and the checker $t{:}\varphi \to {!t}{:}(t{:}\varphi)$. Its forgetful projection, which replaces every term by a box, is exactly $\mathrm{S4}$: this is the realization theorem.
- **Belief change.** [AGM revision](/Y05YQN7HGQ/) satisfies eight postulates and is linked to contraction by the Levi identity $K * \varphi = (K \div \neg\varphi) + \varphi$ and the Harper identity $K \div \varphi = K \cap (K * \neg\varphi)$. By [Gärdenfors's theorem](/WMZ1QP7KQY/), no non-trivial belief revision system satisfies the Ramsey test together with preservation.

## Logics and their decision problems

| Logic | Models | Satisfiability |
|---|---|---|
| [LTL](/RMJ56ZPA63/) | infinite words over $\N$ | PSPACE-complete |
| [CTL](/F6JA5C5BJX/) | total transition systems | EXPTIME-complete |
| [CTL*](/Y4XZ94GRXV/) | total transition systems | 2EXPTIME-complete |
| [HS](/991B5RR6X4/) | intervals of a linear order | undecidable over any class with an infinite ascending or descending sequence |
| [$\mathrm{S5}_n$](/EA34W4ERRE/) | $n$ equivalence relations | NP-complete for $n = 1$, PSPACE-complete for $n \ge 2$ |
| $\mathrm{S5}_n$ with [common knowledge](/7BCMKF2P7X/) | $n \ge 2$ equivalence relations | EXPTIME-complete |
| [$\mathrm{KD45}_n$](/RTP4HTZYK3/) | serial, transitive, Euclidean relations | NP-complete for $n = 1$, PSPACE-complete for $n \ge 2$ |
| [SDL](/7B74J6J5JV/), that is $\mathrm{KD}$ | serial frames | PSPACE-complete |
| [$\mathcal{ALC}$](/TXQ80B8ZSA/) | interpretations of concept and role names | PSPACE-complete; EXPTIME-complete with a general TBox |

: Satisfiability of the main logics of the chapter. One agent of knowledge or belief costs no more than propositional logic; a second agent brings PSPACE, and fixed points such as common knowledge or a general TBox bring EXPTIME.

## Common errors

- **Reading a CTL formula as a property of one path.** $\mathbf{AF}\,\mathbf{AG}\,p$ is strictly stronger than $\mathbf{A}\,\mathbf{FG}\,p$: on every path $p$ eventually holds forever, but the point from which it holds may depend on the path.
- **Confusing the two untils.** LTL counts the present position in $\varphi\,\mathbf{U}\,\psi$. The until of Prior's tense logic and of Kamp's theorem is strict, so that $\mathbf{X}\varphi = \bot\,\mathbf{U}\,\varphi$ over $\Z$.
- **Treating everyone-knows as common knowledge.** $E_G^n\varphi$ for a fixed $n$ does not imply $C_G\varphi$. With $k$ muddy children, "someone is muddy" holds as $E_G^{k-1}$ before the father speaks, and his announcement is needed all the same.
- **Assuming announced truths stay true.** $[!\varphi]\varphi$ fails for the Moore sentence $p \wedge \neg K_a p$: after it is announced, $a$ knows $p$.
- **Expecting monotone behaviour where the reading is not monotone.** A counterfactual is not a strict conditional, and the deliberative stit is not a normal modality: $[i\ \mathsf{dstit}](p \vee \neg p)$ is always false.
