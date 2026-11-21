## What to remember

- **[GL](/WJK0YA4GP2/)** is the normal modal logic K plus Löb's axiom $\square(\square p \to p) \to \square p$. [Löb's axiom](/QQ6PZFGGB3/) implies axiom 4, $\square p \to \square\square p$, and it is valid on a frame exactly when the frame is transitive and has no infinite chain $w_0 R w_1 R w_2 \cdots$. Axiom T, $\square p \to p$, is not a theorem.
- **[Kripke completeness](/1DMFNR7FZT/):** $\mathsf{GL}$ proves exactly the formulas valid on all finite transitive irreflexive frames. So $\mathsf{GL}$ is decidable, and its theorems can be refuted by drawing small finite trees.
- **[Solovay's theorem](/1ZRWVDYPX0/):** $\mathsf{GL} \vdash A$ if and only if $\mathsf{PA}$ proves every arithmetical realization of $A$. The logic $\mathsf{GLS}$, with all theorems of $\mathsf{GL}$, all instances of $\square A \to A$ and modus ponens only, gives the realizations that are all true.
- **[Fixed points](/TDDX1NHG8D/):** if $p$ occurs in $A(p)$ only inside boxes, there is a formula $D$ without $p$ with $\mathsf{GL} \vdash D \leftrightarrow A(D)$, and any two fixed points are provably equivalent. The fixed point of $p \leftrightarrow \neg\square p$ is $\neg\square\bot$, so all Gödel sentences of PA are equivalent to $\mathrm{Con}(\mathsf{PA})$.
- **Letter-free formulas** are $\mathsf{GL}$-equivalent to Boolean combinations of the formulas $\square^n\bot$. At a world of depth $d$ in a finite frame, $\square^n\bot$ is true exactly when $d < n$.
- **[Grz](/2Q8E4GQF3B/)** is S4 plus $\square(\square(p \to \square p) \to p) \to p$. It is the logic of finite partial orders, and it is the logic of "true and provable": the translation $(\square A)^t = A^t \wedge \square A^t$ embeds it into $\mathsf{GL}$.
- **[GLP](/3EDRQJJHMT/)** has boxes $[n]$ for $n$-provability, with $[m]A \to [n]A$ for $m \le n$ and $\langle m \rangle A \to [n]\langle m \rangle A$ for $m < n$. It is arithmetically complete but has no complete class of Kripke frames, and its closed fragment gives the worms, ordered in type $\varepsilon_0$.
- **[Magari algebras](/PHWAN904PT/)** are Boolean algebras with $\square 1 = 1$, $\square(x \wedge y) = \square x \wedge \square y$ and $\square(\square x \to x) = \square x$. The Lindenbaum algebra of PA is one, and $\mathsf{GL}$ is complete for this class.
- **[Interpretability logic](/BGKZTSQN3W/):** $\mathsf{IL}$ is $\mathsf{GL}$ plus J1 to J5 for $\rhd$; it is sound and complete for Veltman frames. $\mathsf{ILM}$ is the interpretability logic of PA, and $\mathsf{ILP}$ that of finitely axiomatized theories such as GB. With quantifiers, the [provability logic](/5K9J8R8SCP/) of PA is $\Pi^0_2$-complete.

## Logics, frames and arithmetic

| Logic | Kripke-style semantics | Arithmetical reading |
|---|---|---|
| $\mathsf{GL}$ | finite transitive irreflexive frames | provability in PA |
| $\mathsf{GLS}$ | none; reduced to $\mathsf{GL}$ by adding $\square B \to B$ for the boxed subformulas | truth of all realizations |
| $\mathsf{Grz}$ | finite partial orders | "true and provable" in PA |
| $\mathsf{GLP}$ | none complete | $n$-provability in PA |
| $\mathsf{ILM}$ | Veltman frames with $u S_w v R z \Rightarrow u R z$ | interpretability over PA |
| $\mathsf{ILP}$ | Veltman frames with $w R w' R u S_w v \Rightarrow u S_{w'} v$ | interpretability over GB |

: The main propositional logics of the chapter, with their frames and the arithmetical meaning of the box or of $\rhd$.

## Common errors

- **Reading $\square A$ as "A is true".** In $\mathsf{GL}$, $\square A \to A$ fails; the theorem $\square A \to A$ of $\mathsf{GLS}$ holds only at the actual world, and $\mathsf{GLS}$ is not closed under necessitation.
- **Using reflexive or infinite chains as $\mathsf{GL}$ frames.** A reflexive world, a cycle, or the frame $(\N, <)$ all violate Löb's axiom. Only frames with no infinite ascending chain work.
- **Confusing the fixed point with the formula.** The fixed point of $p \leftrightarrow \square p$ is $\top$, not $p$, and that of $p \leftrightarrow \Diamond p$ is $\bot$. The theorem needs $p$ to occur only under boxes.
- **Looking for Kripke frames for GLP.** In every frame that validates the axioms of $\mathsf{GLP}$, the relation for $[1]$ is empty. Such frames validate $[1]\bot$, which $\mathsf{GLP}$ does not prove, so no class of frames is complete for $\mathsf{GLP}$.
- **Taking $p \rhd q$ to mean $\square(p \to q)$.** J1 gives only one direction. A Veltman model can make $p \rhd q$ true while $\square(p \to q)$ is false, and $\top \rhd \Diamond\top$ fails because PA does not interpret $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
- **Expecting quantified provability logic to be like $\mathsf{GL}$.** With quantifiers, the set of laws is not even recursively enumerable.
